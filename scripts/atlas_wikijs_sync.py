#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib import error, parse, request


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_VAULT_ROOT = REPO_ROOT / "vault"
DEFAULT_BASE_URL = "http://127.0.0.1:3000"
DEFAULT_SITE_URL = "https://atlas.do4ai.com"
DEFAULT_LOCALE = "en"
SYNC_TAG = "atlas-sync"
STATE_VERSION = 1


class WikiSyncError(RuntimeError):
    pass


@dataclass(frozen=True)
class PageSpec:
    source_path: Path
    rel_path: str
    wiki_path: str
    title: str
    description: str
    content: str
    digest: str


def debug(enabled: bool, message: str) -> None:
    if enabled:
        print(message, file=sys.stderr)


def http_request(
    url: str,
    *,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    data: Optional[object] = None,
    timeout: int = 30,
) -> Tuple[int, str]:
    req_headers = dict(headers or {})
    body: Optional[bytes] = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req_headers.setdefault("Content-Type", "application/json")
    req = request.Request(url, method=method, headers=req_headers, data=body)
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        return exc.code, payload


def wait_for_http(base_url: str, *, timeout_seconds: int, verbose: bool) -> None:
    deadline = time.time() + timeout_seconds
    root_url = base_url.rstrip("/") + "/"
    while time.time() < deadline:
        try:
            status, _ = http_request(root_url, timeout=10)
            if status < 500:
                return
        except Exception:
            pass
        debug(verbose, "waiting for Wiki.js HTTP endpoint")
        time.sleep(3)
    raise WikiSyncError(f"Wiki.js did not become reachable within {timeout_seconds}s")


def graphql(
    base_url: str,
    query: str,
    variables: Dict[str, object],
    *,
    token: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, object]:
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    status, payload = http_request(
        base_url.rstrip("/") + "/graphql",
        method="POST",
        headers=headers,
        data={"query": query, "variables": variables},
        timeout=timeout,
    )
    if status >= 400:
        raise WikiSyncError(f"GraphQL request failed with HTTP {status}: {payload[:500]}")
    parsed = json.loads(payload)
    if parsed.get("errors"):
        raise WikiSyncError(f"GraphQL returned errors: {json.dumps(parsed['errors'], ensure_ascii=False)}")
    return parsed["data"]


def login(base_url: str, username: str, password: str) -> str:
    data = graphql(
        base_url,
        """
        mutation Login($username: String!, $password: String!, $strategy: String!) {
          authentication {
            login(username: $username, password: $password, strategy: $strategy) {
              responseResult {
                succeeded
                slug
                message
              }
              jwt
            }
          }
        }
        """,
        {"username": username, "password": password, "strategy": "local"},
        timeout=30,
    )
    result = data["authentication"]["login"]
    response = result["responseResult"]
    if not response["succeeded"] or not result.get("jwt"):
        message = response.get("message") or response.get("slug") or "login failed"
        raise WikiSyncError(message)
    return result["jwt"]


def ensure_setup(
    *,
    base_url: str,
    site_url: str,
    admin_email: str,
    admin_password: str,
    timeout_seconds: int,
    verbose: bool,
) -> None:
    wait_for_http(base_url, timeout_seconds=timeout_seconds, verbose=verbose)
    try:
        login(base_url, admin_email, admin_password)
        debug(verbose, "Wiki.js is already initialized")
        return
    except WikiSyncError:
        pass

    status, body = http_request(base_url.rstrip("/") + "/", timeout=20)
    if status >= 400:
        raise WikiSyncError(f"unable to read Wiki.js root page during setup check: HTTP {status}")
    looks_like_setup = (
        "finalize" in body.lower()
        or "<title>setup" in body.lower()
        or "set up your wiki" in body.lower()
    )
    if not looks_like_setup:
        raise WikiSyncError("Wiki.js is reachable but not in setup mode, and admin login failed")

    debug(verbose, "finalizing Wiki.js setup")
    status, payload = http_request(
        base_url.rstrip("/") + "/finalize",
        method="POST",
        data={
            "siteUrl": site_url,
            "telemetry": False,
            "adminEmail": admin_email,
            "adminPassword": admin_password,
        },
        timeout=60,
    )
    if status >= 400:
        raise WikiSyncError(f"Wiki.js setup finalize failed with HTTP {status}: {payload[:500]}")

    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            wait_for_http(base_url, timeout_seconds=30, verbose=verbose)
            login(base_url, admin_email, admin_password)
            debug(verbose, "Wiki.js setup completed")
            return
        except Exception:
            time.sleep(5)
    raise WikiSyncError("Wiki.js setup finalize returned, but admin login never became available")


def load_state(state_file: Path) -> Dict[str, object]:
    if not state_file.exists():
        return {"version": STATE_VERSION, "pages": {}}
    try:
        parsed = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception:
        return {"version": STATE_VERSION, "pages": {}}
    if parsed.get("version") != STATE_VERSION:
        return {"version": STATE_VERSION, "pages": {}}
    pages = parsed.get("pages")
    if not isinstance(pages, dict):
        return {"version": STATE_VERSION, "pages": {}}
    return {"version": STATE_VERSION, "pages": pages}


def save_state(state_file: Path, pages: Dict[str, str]) -> None:
    state_file.parent.mkdir(parents=True, exist_ok=True)
    tmp_file = state_file.with_suffix(state_file.suffix + ".tmp")
    tmp_file.write_text(
        json.dumps({"version": STATE_VERSION, "pages": pages}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    tmp_file.replace(state_file)


def iter_content_files(vault_root: Path) -> List[Path]:
    results: List[Path] = []
    for path in sorted(vault_root.rglob("*.md")):
        rel = path.relative_to(vault_root)
        rel_posix = rel.as_posix()
        if rel_posix == "CONFIG.md":
            continue
        if rel_posix.startswith("Library/"):
            continue
        results.append(path)
    return results


def split_frontmatter(raw: str) -> Tuple[Dict[str, str], str]:
    text = raw.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return {}, text
    front_raw = text[4:end]
    body = text[end + len(marker) :]
    metadata: Dict[str, str] = {}
    for line in front_raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            value = value[1:-1]
        metadata[key] = value
    return metadata, body


def strip_markdown(md: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", md)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_>#-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def derive_title(metadata: Dict[str, str], body: str, fallback: str) -> str:
    title = metadata.get("title", "").strip()
    if title:
        return title
    match = re.search(r"^\s*#\s+(.+?)\s*$", body, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def derive_description(body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue
        description = strip_markdown(stripped)
        if description:
            return description[:240]
    return ""


def slugify_segment(segment: str) -> str:
    normalized = unicodedata.normalize("NFKC", segment).strip().lower()
    pieces: List[str] = []
    prev_dash = False
    for ch in normalized:
        if ch.isalnum():
            pieces.append(ch)
            prev_dash = False
            continue
        if ch in {"-", "_"}:
            if not prev_dash:
                pieces.append("-")
                prev_dash = True
            continue
        if not prev_dash:
            pieces.append("-")
            prev_dash = True
    slug = "".join(pieces).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug or "page"


def logical_segments(rel_path: str) -> List[str]:
    rel = Path(rel_path)
    if rel_path == "index.md":
        return ["home"]
    if rel.name == "index.md":
        parts = list(rel.parent.parts)
    else:
        parts = list(rel.parent.parts) + [rel.stem]
    return [slugify_segment(part) for part in parts if part not in {"", "."}]


def build_path_map(rel_paths: Sequence[str]) -> Dict[str, str]:
    proposals: Dict[str, List[str]] = {rel_path: logical_segments(rel_path) for rel_path in rel_paths}
    collisions: Dict[str, List[str]] = {}
    for rel_path, segments in proposals.items():
        collisions.setdefault("/".join(segments), []).append(rel_path)

    resolved: Dict[str, List[str]] = {}
    for path_key, rel_group in collisions.items():
        if len(rel_group) == 1:
            rel_path = rel_group[0]
            resolved[rel_path] = proposals[rel_path]
            continue
        for rel_path in sorted(rel_group):
            segments = list(proposals[rel_path])
            suffix = hashlib.sha1(rel_path.encode("utf-8")).hexdigest()[:8]
            segments[-1] = f"{segments[-1]}-{suffix}"
            resolved[rel_path] = segments

    return {rel_path: "/".join(segments) for rel_path, segments in resolved.items()}


def split_code_fences(text: str) -> List[Tuple[bool, str]]:
    parts: List[Tuple[bool, str]] = []
    cursor = 0
    for match in re.finditer(r"```.*?```", text, flags=re.DOTALL):
        if match.start() > cursor:
            parts.append((False, text[cursor : match.start()]))
        parts.append((True, match.group(0)))
        cursor = match.end()
    if cursor < len(text):
        parts.append((False, text[cursor:]))
    return parts


def normalize_relative_target(current_file: Path, target: str, vault_root: Path) -> Optional[str]:
    raw_target = target.strip()
    if not raw_target:
        return None
    if raw_target.startswith("<") and raw_target.endswith(">"):
        raw_target = raw_target[1:-1]
    if raw_target.startswith(("#", "/", "mailto:", "http://", "https://")):
        return None

    path_part, fragment = raw_target, ""
    if "#" in raw_target:
        path_part, fragment = raw_target.split("#", 1)
        fragment = "#" + fragment

    resolved = (current_file.parent / parse.unquote(path_part)).resolve()
    candidates = [resolved]
    if resolved.is_dir():
        candidates.insert(0, resolved / "index.md")
    if resolved.suffix == "":
        candidates.append(resolved.with_suffix(".md"))
        candidates.append(resolved / "index.md")

    for candidate in candidates:
        if not candidate.exists() or not candidate.is_file():
            continue
        try:
            rel = candidate.relative_to(vault_root).as_posix()
        except ValueError:
            continue
        return rel + fragment
    return None


def rewrite_links(body: str, current_file: Path, vault_root: Path, wiki_paths: Dict[str, str]) -> str:
    def rewrite_target(target: str) -> str:
        normalized = normalize_relative_target(current_file, target, vault_root)
        if not normalized:
            return target
        rel_path = normalized
        fragment = ""
        if "#" in normalized:
            rel_path, fragment = normalized.split("#", 1)
            fragment = "#" + fragment
        wiki_path = wiki_paths.get(rel_path)
        if not wiki_path:
            return target
        return f"/{wiki_path}{fragment}"

    def rewrite_segment(segment: str) -> str:
        out: List[str] = []
        idx = 0
        length = len(segment)
        while idx < length:
            if segment[idx] == "[" and (idx == 0 or segment[idx - 1] != "!"):
                label_end = find_matching(segment, idx, "[", "]")
                if label_end != -1 and label_end + 1 < length and segment[label_end + 1] == "(":
                    target_end = find_link_target_end(segment, label_end + 2)
                    if target_end != -1:
                        label = segment[idx + 1 : label_end]
                        target = segment[label_end + 2 : target_end]
                        out.append(f"[{label}]({rewrite_target(target)})")
                        idx = target_end + 1
                        continue
            out.append(segment[idx])
            idx += 1
        return "".join(out)

    rebuilt: List[str] = []
    for is_code, segment in split_code_fences(body):
        rebuilt.append(segment if is_code else rewrite_segment(segment))
    return "".join(rebuilt)


def find_matching(text: str, start: int, open_char: str, close_char: str) -> int:
    depth = 0
    for idx in range(start, len(text)):
        ch = text[idx]
        if ch == "\\":
            continue
        if ch == open_char:
            depth += 1
        elif ch == close_char:
            depth -= 1
            if depth == 0:
                return idx
    return -1


def find_link_target_end(text: str, start: int) -> int:
    depth = 1
    idx = start
    while idx < len(text):
        ch = text[idx]
        if ch == "\\":
            idx += 2
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return idx
        idx += 1
    return -1


def build_page_specs(vault_root: Path) -> List[PageSpec]:
    vault_root = vault_root.resolve()
    files = iter_content_files(vault_root)
    rel_paths = [path.relative_to(vault_root).as_posix() for path in files]
    wiki_paths = build_path_map(rel_paths)
    pages: List[PageSpec] = []

    for path in files:
        rel_path = path.relative_to(vault_root).as_posix()
        raw = path.read_text(encoding="utf-8-sig")
        metadata, body = split_frontmatter(raw)
        title = derive_title(metadata, body, path.stem if path.name != "index.md" else path.parent.name or "Home")
        body = rewrite_links(body, path, vault_root, wiki_paths).strip()
        if not body:
            body = f"# {title}\n"
        description = derive_description(body)
        digest = hashlib.sha256(
            json.dumps(
                {
                    "wiki_path": wiki_paths[rel_path],
                    "title": title,
                    "description": description,
                    "content": body,
                },
                ensure_ascii=False,
                sort_keys=True,
            ).encode("utf-8")
        ).hexdigest()
        pages.append(
            PageSpec(
                source_path=path,
                rel_path=rel_path,
                wiki_path=wiki_paths[rel_path],
                title=title,
                description=description,
                content=body,
                digest=digest,
            )
        )

    pages.sort(key=lambda page: (page.wiki_path.count("/"), page.wiki_path))
    return pages


def list_remote_pages(base_url: str, token: str, locale: str) -> List[Dict[str, object]]:
    data = graphql(
        base_url,
        """
        query Pages($locale: String!, $limit: Int!, $tags: [String!]) {
          pages {
            list(locale: $locale, limit: $limit, orderBy: PATH, orderByDirection: ASC, tags: $tags) {
              id
              path
              title
              tags
            }
          }
        }
        """,
        {"locale": locale, "limit": 5000, "tags": []},
        token=token,
    )
    return data["pages"]["list"]


def create_page(base_url: str, token: str, page: PageSpec, locale: str) -> None:
    data = graphql(
        base_url,
        """
        mutation CreatePage(
          $content: String!,
          $description: String!,
          $editor: String!,
          $isPublished: Boolean!,
          $isPrivate: Boolean!,
          $locale: String!,
          $path: String!,
          $tags: [String]!,
          $title: String!
        ) {
          pages {
            create(
              content: $content,
              description: $description,
              editor: $editor,
              isPublished: $isPublished,
              isPrivate: $isPrivate,
              locale: $locale,
              path: $path,
              tags: $tags,
              title: $title
            ) {
              responseResult {
                succeeded
                slug
                message
              }
              page {
                id
                path
              }
            }
          }
        }
        """,
        {
            "content": page.content,
            "description": page.description,
            "editor": "markdown",
            "isPublished": True,
            "isPrivate": False,
            "locale": locale,
            "path": page.wiki_path,
            "tags": [SYNC_TAG],
            "title": page.title,
        },
        token=token,
        timeout=120,
    )
    response = data["pages"]["create"]["responseResult"]
    if not response["succeeded"]:
        raise WikiSyncError(response.get("message") or response.get("slug") or f"failed to create {page.wiki_path}")


def update_page(base_url: str, token: str, page_id: int, page: PageSpec, locale: str) -> None:
    data = graphql(
        base_url,
        """
        mutation UpdatePage(
          $id: Int!,
          $content: String!,
          $description: String!,
          $isPublished: Boolean!,
          $isPrivate: Boolean!,
          $locale: String!,
          $path: String!,
          $tags: [String]!,
          $title: String!
        ) {
          pages {
            update(
              id: $id,
              content: $content,
              description: $description,
              isPublished: $isPublished,
              isPrivate: $isPrivate,
              locale: $locale,
              path: $path,
              tags: $tags,
              title: $title
            ) {
              responseResult {
                succeeded
                slug
                message
              }
              page {
                id
                path
              }
            }
          }
        }
        """,
        {
            "id": int(page_id),
            "content": page.content,
            "description": page.description,
            "isPublished": True,
            "isPrivate": False,
            "locale": locale,
            "path": page.wiki_path,
            "tags": [SYNC_TAG],
            "title": page.title,
        },
        token=token,
        timeout=120,
    )
    response = data["pages"]["update"]["responseResult"]
    if not response["succeeded"]:
        raise WikiSyncError(response.get("message") or response.get("slug") or f"failed to update {page.wiki_path}")


def delete_page(base_url: str, token: str, page_id: int, page_path: str) -> None:
    data = graphql(
        base_url,
        """
        mutation DeletePage($id: Int!) {
          pages {
            delete(id: $id) {
              responseResult {
                succeeded
                slug
                message
              }
            }
          }
        }
        """,
        {"id": int(page_id)},
        token=token,
        timeout=60,
    )
    response = data["pages"]["delete"]["responseResult"]
    if not response["succeeded"]:
        raise WikiSyncError(response.get("message") or response.get("slug") or f"failed to delete {page_path}")


def sync_pages(
    *,
    base_url: str,
    admin_email: str,
    admin_password: str,
    locale: str,
    vault_root: Path,
    state_file: Optional[Path],
    dry_run: bool,
    verbose: bool,
) -> None:
    pages = build_page_specs(vault_root)
    print(f"prepared {len(pages)} pages from {vault_root}")

    if dry_run:
        for page in pages[:20]:
            print(f"{page.rel_path} -> /{page.wiki_path}")
        if len(pages) > 20:
            print(f"... truncated {len(pages) - 20} additional pages")
        return

    token = login(base_url, admin_email, admin_password)
    remote_pages = list_remote_pages(base_url, token, locale)
    remote_by_path = {page["path"]: page for page in remote_pages}
    atlas_remote = {
        page["path"]: page
        for page in remote_pages
        if isinstance(page.get("tags"), list) and SYNC_TAG in page["tags"]
    }
    state = load_state(state_file) if state_file else {"version": STATE_VERSION, "pages": {}}
    state_pages: Dict[str, str] = dict(state.get("pages", {}))

    created = 0
    updated = 0
    skipped = 0

    next_state: Dict[str, str] = {}

    for page in pages:
        remote = remote_by_path.get(page.wiki_path)
        needs_update = True
        if remote and state_pages.get(page.rel_path) == page.digest:
            remote_tags = remote.get("tags") or []
            if SYNC_TAG in remote_tags:
                needs_update = False

        if remote is None:
            print(f"create /{page.wiki_path}")
            create_page(base_url, token, page, locale)
            created += 1
        elif needs_update:
            print(f"update /{page.wiki_path}")
            update_page(base_url, token, int(remote["id"]), page, locale)
            updated += 1
        else:
            skipped += 1
        next_state[page.rel_path] = page.digest

    desired_paths = {page.wiki_path for page in pages}
    deleted = 0
    for page_path, remote in atlas_remote.items():
        if page_path in desired_paths:
            continue
        print(f"delete /{page_path}")
        delete_page(base_url, token, int(remote["id"]), page_path)
        deleted += 1

    if state_file:
        save_state(state_file, next_state)

    print(
        f"sync complete: created={created} updated={updated} deleted={deleted} skipped={skipped} total={len(pages)}"
    )


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync Atlas markdown content into Wiki.js")
    subparsers = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--base-url", default=os.environ.get("WIKIJS_BASE_URL", DEFAULT_BASE_URL))
    common.add_argument("--site-url", default=os.environ.get("WIKIJS_SITE_URL", DEFAULT_SITE_URL))
    common.add_argument("--admin-email", default=os.environ.get("WIKIJS_ADMIN_EMAIL", "atlas-admin@do4ai.com"))
    common.add_argument("--admin-password", default=os.environ.get("WIKIJS_ADMIN_PASSWORD"))
    common.add_argument("--locale", default=os.environ.get("WIKIJS_LOCALE", DEFAULT_LOCALE))
    common.add_argument("--vault-root", type=Path, default=Path(os.environ.get("ATLAS_VAULT_ROOT", str(DEFAULT_VAULT_ROOT))))
    common.add_argument("--verbose", action="store_true")

    setup_parser = subparsers.add_parser("ensure-setup", parents=[common])
    setup_parser.add_argument("--timeout-seconds", type=int, default=300)

    sync_parser = subparsers.add_parser("sync", parents=[common])
    sync_parser.add_argument("--state-file", type=Path, default=Path(os.environ.get("ATLAS_WIKIJS_STATE_FILE", "/workspace/state/atlas-wikijs-sync.json")))
    sync_parser.add_argument("--dry-run", action="store_true")

    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    if not args.admin_password and not getattr(args, "dry_run", False):
        raise WikiSyncError("--admin-password or WIKIJS_ADMIN_PASSWORD is required")

    if args.command == "ensure-setup":
        ensure_setup(
            base_url=args.base_url,
            site_url=args.site_url,
            admin_email=args.admin_email,
            admin_password=args.admin_password,
            timeout_seconds=args.timeout_seconds,
            verbose=args.verbose,
        )
        return 0

    if args.command == "sync":
        sync_pages(
            base_url=args.base_url,
            admin_email=args.admin_email,
            admin_password=args.admin_password,
            locale=args.locale,
            vault_root=args.vault_root,
            state_file=args.state_file,
            dry_run=args.dry_run,
            verbose=args.verbose,
        )
        return 0

    raise WikiSyncError(f"unsupported command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except WikiSyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
