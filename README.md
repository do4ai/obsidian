# wiki

`do4ai/wiki`는 Wiki 문서 원본을 관리하는 마크다운 저장소다.

- 배포 도메인: `wiki.do4ai.com`
- 인프라와 운영: 별도 GitOps 저장소에서 담당
- 이 저장소의 책임: `vault/` 아래 마크다운 문서와 Wiki.js 동기화 스크립트 유지
- 배포 런타임: GitOps 저장소에서 `vault/`를 Wiki.js 인스턴스로 동기화

## 갱신 방식

현재 이 vault는 `do4ai/notion` 저장소의 `scripts/notion_obsidian_export.py`로 생성된다.

```bash
python3 scripts/notion_obsidian_export.py seed-repo --repo-dir ../wiki
```

GitOps 저장소는 이 저장소를 주기적으로 pull 한 뒤 `scripts/wiki_wikijs_sync.py`로 Wiki.js에 반영한다.

## Wiki.js 동기화

로컬에서 경로 매핑과 링크 재작성을 점검하려면 dry-run을 사용한다.

```bash
python3 scripts/wiki_wikijs_sync.py sync --dry-run
```

실제 운영 배포에서는 같은 스크립트가 두 단계를 담당한다.

- `ensure-setup`: 빈 Wiki.js 인스턴스를 자동 초기화
- `sync`: `vault/` 문서를 Wiki.js page path로 변환하고 create, update, delete 반영

동기화 대상은 `vault/` 전체이며, 다음 경로는 제외한다.

- `vault/CONFIG.md`
- `vault/Library/`
