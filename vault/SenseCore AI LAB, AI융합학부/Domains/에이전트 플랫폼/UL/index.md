---
title: "UL"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b98033b03cdb4016dd7830__에이전트 플랫폼/children/330e313f58b98122b3c0f8a0603b4d19__UL
notion_id: 330e313f58b98122b3c0f8a0603b4d19
notion_url: https://www.notion.so/330e313f58b98122b3c0f8a0603b4d19
parent_notion_id: 31fe313f58b98033b03cdb4016dd7830
---
## 이 페이지의 목적

이 페이지는 do4i에서 상품, 권한, 실행, 과금 언어가 섞이지 않도록 막는 UL 페이지다.

| 용어 | 정의 | 사용하는 문맥 | 금지 또는 주의 표현 |
| --- | --- | --- | --- |
| User | do4i의 기본 계정 | auth, profile, membership | seller, buyer를 별도 루트 엔티티처럼 부르지 않는다. |
| AuthIdentity | 외부 로그인 제공자와 연결된 식별자 | identity | Google 계정 그 자체와 혼용하지 않는다. |
| PhoneAuthSession | 가입 완료 전 휴대폰 인증 상태 | identity | 완성된 회원 계정과 혼용하지 않는다. |
| Organization | 멤버, 권한, 초대 구조를 가진 workspace | organizations | 단순 그룹 또는 채팅방처럼 부르지 않는다. |
| InviteCode | 조직 입장 진입 수단 | organizations | membership 자체와 혼용하지 않는다. |
| Agent | 카탈로그에서 발견되고 실행되는 AI 상품 단위 | products, runtime | 모델 endpoint나 scenario 파일과 같은 뜻으로 쓰지 않는다. |
| Purchase | 접근 권한 획득 기록 | catalog, billing | 결제 영수증 전체와 같은 뜻으로 쓰지 않는다. |
| Entitlement | 사용자가 agent를 실행할 수 있는 권한 상태 | catalog, organizations | purchase와 항상 1:1이라고 가정하지 않는다. |
| ChatbotScenario | agent의 대화 정의와 발행 단위 | builder | runtime message history와 혼용하지 않는다. |
| ChatSession | 텍스트 대화 세션 | runtime | scenario와 같은 뜻으로 쓰지 않는다. |
| VoiceSession | 음성 대화 세션 | runtime | 단순 채팅 옵션 정도로 축소하지 않는다. |
| AvatarSession | 아바타 실시간 세션 | runtime | voice session과 완전히 같은 것으로 보지 않는다. |
| Wallet | 사용량 기반 과금의 잔액 기준 | billing | entitlement나 subscription과 같은 뜻으로 쓰지 않는다. |
| UsageRecord | 사용량 집계 이벤트 | billing | purchase history와 혼용하지 않는다. |
| SellerApplication | 판매자 권한 신청 | governance | seller profile 수정과 구분한다. |
| GuideArticle | 운영 가능한 가이드 문서 | guides | 마케팅 카피와 구분한다. |
| IN Workspace | 모바일 상담 표면에서 보이는 서비스 카드, 대시보드, 기본 상담 진입점 묶음 | mobile facade | 독립 코어 도메인처럼 과도하게 모델링하지 않는다. |

## 용어 운영 원칙

- builder 언어와 runtime 언어를 분리한다.
- catalog, entitlement, billing은 같은 사용자 행동을 다뤄도 서로 다른 artifact를 가진다.
- mobile `IN`은 경험 이름일 수 있어도 도메인 이름은 facade 기준으로 잡는다.

## 확인 소스

- `do4i/server/api/http/products.py`
- `do4i/server/api/http/guides.py`
- `do4i/server/tests/e2e/test_platform_billing_flow.py`
