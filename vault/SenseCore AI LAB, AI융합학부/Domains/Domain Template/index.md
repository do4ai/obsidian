---
title: "Domain Template"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980168893e49708057b73__Domain Template
notion_id: 31fe313f58b980168893e49708057b73
notion_url: https://www.notion.so/31fe313f58b980168893e49708057b73
parent_notion_id: 32be313f58b9803bb9adf68c0393a0f6
---
이 페이지는 도메인 문서를 쓸 때 모든 솔루션이 같은 형식을 따르도록 만드는 정본 템플릿이다.

도메인 문서는 화면 목록이 아니라 비즈니스 경계와 언어를 고정하는 문서여야 한다.

따라서 작성 순서는 아래처럼 고정한다.

1. 도메인 한 줄 정의: 이 솔루션이 실제로 닫는 거래 또는 업무를 한 문장으로 고정한다.
2. 도메인 스토리텔링: 현재 기준 `as-is` 80% happy path를 actor와 work object 기준으로 적는다.
3. 바운디드 컨텍스트: 책임이 갈라지는 지점을 기준으로 core, supporting, generic을 나눈다.
4. UL: 팀이 반드시 같은 뜻으로 써야 하는 용어와 금지할 혼용어를 적는다.
5. 컨텍스트 맵: upstream, downstream, 번역 책임, 변경 비용을 적는다.

문서 작성 원칙은 아래와 같다.

- `as-is`와 `to-be`를 섞지 않는다.
- 화면 이름보다 거래 완료 조건과 책임 전이를 먼저 적는다.
- UL은 사전이 아니라 팀 계약으로 쓴다.
- 컨텍스트 맵에는 관계 이름만이 아니라 번역 책임을 적는다.
- 각 하위 문서에는 확인 소스를 남긴다.

이 템플릿의 하위 문서는 실제 작성 형식을 그대로 보여준다.

## 하위 문서 구성

- 도메인 스토리텔링: actor, trigger, work object, happy path, variation을 적는다.
- 바운디드 컨텍스트: core, supporting, generic 분류와 경계 이유를 적는다.
- UL: 팀이 반드시 같은 뜻으로 써야 할 용어와 금지 표현을 적는다.
- 컨텍스트 맵: upstream, downstream, 번역 책임, 변경 비용을 적는다.

---
