# atlas

`do4ai/atlas`는 Atlas 문서 내용과 마크다운 베이스라인만 관리하는 콘텐츠 저장소다.

- 배포 도메인: `atlas.do4ai.com`
- 인프라와 운영: 별도 GitOps 저장소에서 담당
- 이 저장소의 책임: `vault/` 아래 마크다운 문서와 내보낸 콘텐츠 베이스라인 유지
- 기본 UX 방향: Notion에 가까운 넓은 문서 편집 화면, 템플릿, slash snippets 제공

## 갱신 방식

현재 이 vault는 `do4ai/notion` 저장소의 `scripts/notion_obsidian_export.py`로 생성된다.

```bash
python3 scripts/notion_obsidian_export.py seed-repo --repo-dir ../atlas
```

GitOps와 런타임 마이그레이션 작업은 이 저장소를 기준 콘텐츠 베이스라인으로 사용한다.
