---
title: "Domains"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains
notion_id: 32be313f58b9803bb9adf68c0393a0f6
notion_url: https://www.notion.so/32be313f58b9803bb9adf68c0393a0f6
parent_notion_id: 31ee313f58b980d68c5ad8ed9d5aeff8
---
도메인 문서는 화면 목록이 아니라 비즈니스 경계를 정하는 문서여야 한다.

이 섹션은 아래 5개 질문에 답하는 고정 체계를 사용한다.

1. 이 솔루션이 실제로 해결하는 거래 또는 업무는 무엇인가.
2. 80% 핵심 시나리오에서 누가 무엇을 시작하고, 무엇이 완료 조건인가.
3. 어떤 책임을 하나의 바운디드 컨텍스트로 묶어야 하는가.
4. 팀이 코드, 문서, 대화에서 같은 뜻으로 써야 하는 UL은 무엇인가.
5. 컨텍스트 사이의 upstream, downstream, 번역 책임은 어디에 있는가.

이 체계는 Eric Evans의 DDD Reference와 DDD Crew의 Starter Modelling Process를 참고해, 설명보다 경계와 언어를 먼저 고정하는 방식으로 정리했다.

- https://www.domainlanguage.com/ddd/reference/
- https://ddd-crew.github.io/ddd-starter-modelling-process/
- https://domainstorytelling.org/quick-start-guide/

현재 관리 대상 솔루션은 아래 3개다.

- 자동차 경매: PALCAR의 딜러 승인형 중고차 경매 및 거래 운영 도메인
- 에이전트 플랫폼: PASSV의 에이전트 제작, 유통, 과금, 상담 실행 도메인
- 논문 검사 솔루션: PaperSens의 논문 점검, 심사 보조, 근거 추출 도메인

각 솔루션 문서는 같은 순서를 유지한다.

1. 도메인 한 줄 정의
2. 도메인 스토리텔링
3. 바운디드 컨텍스트
4. UL
5. 컨텍스트 맵

도메인 문서 작성 프로세스는 아래처럼 고정한다.

1. `Align`: 제품이 실제로 만드는 거래 완료 조건과 1차 사용자 집단을 고정한다.
2. `Discover`: Domain Storytelling 방식으로 현재 기준 `as-is` 80% 시나리오를 먼저 적고, 예외는 annotation처럼 분리한다.
3. `Decompose`: 시나리오에서 책임이 갈라지는 지점을 기준으로 core, supporting, generic 컨텍스트를 나눈다.
4. `Connect`: upstream, downstream, 번역 책임을 현재 구조와 목표 구조 두 관점에서 검토한다.
5. `Define`: UL, 금지할 동의어, 남은 질문, 추가 증거 수집 포인트를 명시한다.

즉 현재 4개 하위 문서는 단순 설명 페이지가 아니라 아래 역할을 가진다.

- 도메인 스토리텔링: actor, trigger, work object, happy path, 주요 variation의 기준 페이지
- 바운디드 컨텍스트: 책임 경계, 분리 이유, core/supporting/generic 분류 결정 페이지
- UL: 팀이 써야 할 표준 용어와 금지할 혼용어를 정리하는 계약 페이지
- 컨텍스트 맵: 현재 상호작용과 목표 상호작용을 비교하는 페이지

이 섹션의 작성 기준은 아래 4개다.

- 각 도메인의 `as-is`와 `to-be`를 구분해서 적을 것
- 하위 문서마다 증거 소스가 된 로컬 레포 경로를 남길 것
- UL에 alias, 금지어, 혼동하기 쉬운 표현을 더 넣을 것
- 컨텍스트 맵에 관계 이름만이 아니라 번역 책임과 변경 비용을 적을 것

실무 원칙은 단순하다.

- 스토리텔링은 80% happy path를 먼저 적는다.
- 바운디드 컨텍스트는 화면이 아니라 트랜잭션 경계와 책임 변화 기준으로 자른다.
- UL은 사전이 아니라 오해를 줄이는 계약으로 적는다.
- 컨텍스트 맵은 API 목록이 아니라 영향 방향과 번역 책임을 적는다.

---

[Domain Template](Domain Template/index.md)
[에이전트 플랫폼](에이전트 플랫폼/index.md)
[자동차 경매](자동차 경매/index.md)
[OAuth 2.0](OAuth 2.0/index.md)
[논문 검사 솔루션](논문 검사 솔루션/index.md)
