---
title: "에이전트 플랫폼"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b98033b03cdb4016dd7830__에이전트 플랫폼
notion_id: 31fe313f58b98033b03cdb4016dd7830
notion_url: https://www.notion.so/31fe313f58b98033b03cdb4016dd7830
parent_notion_id: 32be313f58b9803bb9adf68c0393a0f6
---
## 도메인 한 줄 정의

PASSV의 에이전트 플랫폼 도메인은 에이전트를 제작하고 카탈로그에 배포하며, 구매 또는 조직 권한을 통해 접근한 사용자가 텍스트, 음성, 아바타, 모바일 상담 표면에서 실행하도록 운영하는 다중 표면 AI 플랫폼 도메인이다.

## 왜 이 도메인을 따로 보나

- 채팅 기능 하나가 아니라 `상품화`, `접근 권한`, `실행`, `과금`, `운영`이 함께 움직인다.
- seller, buyer, organization, admin의 역할 차이가 명확한 플랫폼이다.
- mobile `IN`은 별도 코어가 아니라 platform core를 상담 중심으로 재구성한 facade다.

## 하위 문서

- 도메인 스토리텔링: 계정 생성부터 agent 실행까지의 핵심 흐름
- 바운디드 컨텍스트: platform core와 supporting context의 경계
- UL: 제품, 권한, 실행, 과금 언어 계약
- 컨텍스트 맵: catalog, builder, runtime, billing, `IN`의 연결 방식

## 설계 메모

- PASSV의 코어는 `에이전트 제작`이 아니라 `에이전트 상품화와 실행` 전체다.
- `IN`은 독립 코어보다 projection/facade로 보는 편이 실제 코드와 맞다.
- 그래서 `Agent Catalog`, `Agent Builder`, `Conversation Runtime`, `Billing`을 섞지 않는 것이 중요하다.

## 핵심 판단

- do4i의 핵심은 `에이전트를 만들고 판매하고 실행하고 과금하는 플랫폼 전체`다.
- `Purchase`, `Entitlement`, `UsageRecord`는 같은 사용자 여정에 있어도 서로 다른 artifact이므로 언어를 분리한다.
- mobile `IN`은 독립 코어가 아니라 platform core를 상담 중심으로 노출하는 facade로 본다.

## 확인 소스

- `do4i/README.md`
- `do4i/server/api/http/products.py`
- `do4i/server/api/http/guides.py`
- `do4i/server/api/http/support.py`
- `do4i/server/api/http/assessments.py`
- `do4i/server/scripts/seed_guides.py`
- `do4i/client/agents/src/pages/Organization.tsx`
- `do4i/client/agents/src/pages/GuidePage.tsx`
- `do4i/client/mobile/src/flow/InFlowProvider.tsx`
- `do4i/server/tests/e2e/test_platform_billing_flow.py`

---

[도메인 스토리텔링](도메인 스토리텔링/index.md)
[바운디드 컨텍스트](바운디드 컨텍스트/index.md)
[UL](UL/index.md)
[컨텍스트 맵](컨텍스트 맵/index.md)
