---
title: "컨텍스트 맵"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b98033b03cdb4016dd7830__에이전트 플랫폼/children/330e313f58b981cba3cdecc6ce6194b6__컨텍스트 맵
notion_id: 330e313f58b981cba3cdecc6ce6194b6
notion_url: https://www.notion.so/330e313f58b981cba3cdecc6ce6194b6
parent_notion_id: 31fe313f58b98033b03cdb4016dd7830
---
## 이 페이지의 목적

이 페이지는 do4i의 platform core와 mobile facade가 어떤 관계로 이어지는지 보여주는 전략 설계 페이지다.

| Upstream | Downstream | 관계 | 번역 책임 | 변경 비용 메모 |
| --- | --- | --- | --- | --- |
| Identity & Access | User Account & Preferences | Shared Kernel | 프로필 쪽이 기본 식별자를 그대로 사용한다. | auth 표현이 바뀌면 profile과 onboarding이 함께 수정된다. |
| Organization Workspace | Agent Catalog & Entitlement | Customer/Supplier | catalog가 조직 소유 agent와 membership 기반 접근을 해석한다. | 조직 모델 변경이 entitlement 규칙에 직접 영향을 준다. |
| Agent Catalog & Entitlement | Agent Builder | Customer/Supplier | builder가 agent 소유권과 공개 범위를 받아 시나리오 수명주기를 붙인다. | product schema 변경이 builder 발행 규칙을 흔든다. |
| Agent Builder | Chat Conversation | Published Language | 발행된 scenario를 runtime 설정 언어로 변환한다. | publishing rule 변경이 session 시작 흐름을 깨기 쉽다. |
| Agent Catalog & Entitlement | Billing & Metering | Conformist | billing이 권한 획득 결과를 과금 artifact로 해석한다. | purchase와 wallet 규칙이 섞이면 변경 비용이 급격히 커진다. |
| Chat Conversation | Voice & Avatar Interaction | Shared Kernel | turn, session 일부 언어를 공유한다. | modality 확장 시 shared kernel 침식 위험이 있다. |
| Agent Catalog & Entitlement | IN Workspace Facade | Anti-Corruption Layer | mobile `IN`이 catalog를 상담 카드와 기본 agent resolve로 번역한다. | mobile experience 변경이 core 상품 모델을 건드리지 않게 해야 한다. |
| Organization Workspace | IN Workspace Facade | Customer/Supplier | mobile이 조직 소속과 읽기 모델을 사용한다. | organization summary가 흔들리면 `IN` 홈 구성도 함께 흔들린다. |
| Support Inbox | IN Workspace Facade | Published Language | 문의, 알림 집계를 모바일 표면에 노출한다. | 지원 메시지 포맷 변경 시 mobile surface만 조정하면 된다. |
| Seller Governance | Agent Catalog & Entitlement | Governance | seller 승인 상태가 publish 허용 여부를 제한한다. | seller 승인 규칙이 바뀌면 publish 운영도 같이 바뀐다. |

## 현재 해석

- do4i의 core는 `Agent Catalog & Entitlement`, `Agent Builder`, `Conversation Runtime`, `Billing & Metering`의 조합이다.
- mobile `IN`은 새로운 코어보다 여러 컨텍스트의 읽기 모델과 orchestration을 얹은 facade에 가깝다.

## 확인 소스

- `do4i/server/README.md`
- `do4i/server/api/http/products.py`
- `do4i/server/api/http/support.py`
- `do4i/client/mobile/src/flow/InFlowProvider.tsx`
