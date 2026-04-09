---
title: "도메인 스토리텔링"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b98033b03cdb4016dd7830__에이전트 플랫폼/children/330e313f58b98155aa9af734bab3f161__도메인 스토리텔링
notion_id: 330e313f58b98155aa9af734bab3f161
notion_url: https://www.notion.so/330e313f58b98155aa9af734bab3f161
parent_notion_id: 31fe313f58b98033b03cdb4016dd7830
---
## 이 페이지의 목적

이 페이지는 do4i의 플랫폼 핵심 흐름을 계정, 상품화, 실행, 과금 기준으로 고정하는 페이지다.

## 핵심 액터

- 사용자: buyer, seller, organization member, admin 역할을 가질 수 있는 기본 계정이다.
- seller 또는 organization owner: agent를 만들고 공개 또는 조직 전용으로 운영한다.
- platform runtime: chat, voice, avatar, mobile `IN` 표면에서 agent를 실행한다.

## 핵심 work object

- Agent: 카탈로그에서 발견되고 실행되는 AI 상품 단위다.
- ChatbotScenario: agent의 대화 정의와 발행 단위다.
- Entitlement: 구매 또는 조직 권한을 통해 agent에 접근할 수 있게 하는 권한 상태다.
- Session: chat, voice, avatar 실행 중 생성되는 대화 세션이다.

## 80% 핵심 시나리오

1. 게스트는 이메일, Google, Kakao, 휴대폰 인증 중 하나로 계정을 만든다.
2. 사용자는 판매자 신청을 통해 seller가 되거나, 조직에 참여해 organization member가 된다.
3. seller 또는 organization owner는 workspace 안에서 agent를 생성하고 카테고리, 공개 여부, 가격 정책을 정한다.
4. seller는 agent에 연결된 scenario를 편집하고 발행 상태를 관리한다.
5. 사용자는 landing, catalog, mobile `IN` 서비스 카드에서 agent를 발견한다.
6. 사용자는 구매 또는 조직 권한으로 entitlement를 얻고 chat, voice, avatar 세션 중 하나를 시작한다.
7. 사용량과 결제 정보는 wallet, subscription, payment, usage record 같은 artifact로 집계된다.
8. 후속으로 survey, assessment, guide, support inquiry 같은 supporting 흐름이 이어진다.

## 주요 variation

- 조직 전용 agent는 catalog 공개 없이 entitlement가 조직 membership에서 결정될 수 있다.
- mobile `IN`은 별도 상품군처럼 보이지만 실제로는 기존 platform capability를 상담 표면으로 재구성한다.
- 일부 사용자는 구매보다 wallet 사용량 기반으로 agent를 소비한다.

## 경계 판단 포인트

- 상품화와 실행은 같은 agent를 다루더라도 서로 다른 수명주기를 가진다.
- entitlement와 billing artifact를 같은 모델에 넣으면 구매 권한과 비용 집계가 섞인다.
- `IN`은 독립 코어보다 facade/read model로 보는 편이 현재 구조에 더 맞다.

## 확인 소스

- `do4i/README.md`
- `do4i/server/README.md`
- `do4i/server/api/http/products.py`
- `do4i/server/api/http/guides.py`
- `do4i/client/agents/src/pages/Organization.tsx`
- `do4i/client/mobile/src/flow/InFlowProvider.tsx`
