# obsidian

`do4ai/obsidian`는 문서 내용만 관리하는 옵시디언 vault 저장소다.

- 배포 도메인: `obsidian.do4ai.com`
- 인프라와 운영: 별도 GitOps 저장소에서 담당
- 이 저장소의 책임: `vault/` 아래 마크다운 문서와 첨부 없이도 읽을 수 있는 구조 유지

## 갱신 방식

현재 이 vault는 `do4ai/notion` 저장소의 `scripts/notion_obsidian_export.py`로 생성된다.

```bash
python3 scripts/notion_obsidian_export.py seed-repo --repo-dir ../obsidian
```

GitOps 저장소는 이 저장소를 읽어 `obsidian.do4ai.com`에 배포한다.
