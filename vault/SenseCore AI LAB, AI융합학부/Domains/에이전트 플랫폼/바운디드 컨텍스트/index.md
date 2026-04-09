---
title: "바운디드 컨텍스트"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b98033b03cdb4016dd7830__에이전트 플랫폼/children/330e313f58b9818fbda9c667e825f89b__바운디드 컨텍스트
notion_id: 330e313f58b9818fbda9c667e825f89b
notion_url: https://www.notion.so/330e313f58b9818fbda9c667e825f89b
parent_notion_id: 31fe313f58b98033b03cdb4016dd7830
---
## 이 페이지의 목적

이 페이지는 do4i의 상품화, 실행, 과금, 모바일 facade 경계를 분리하는 페이지다.

| 컨텍스트 | 분류 | 핵심 책임 | 대표 개념 |
| --- | --- | --- | --- |
| Identity & Access | Generic | 인증, 세션, OAuth 연동, 휴대폰 인증, 가입 continuation | AuthIdentity, PhoneAuthSession, MobileSignupProfile |
| User Account & Preferences | Supporting | 프로필, 알림/마케팅 설정, 기본 언어/모드, seller 상태 | User, UserSetting |
| Organization Workspace | Core | 조직 생성, 멤버십, 초대 코드, 참여 요청 승인 | Organization, InviteCode, OrganizationJoinRequest |
| Agent Catalog & Entitlement | Core | 카테고리, Agent, 공개/비공개 노출, 구매 기반 접근 권한 | Category, Agent, Purchase |
| Agent Builder | Core | 시나리오 작성, 버전, 발행, 수정 | ChatbotScenario |
| Chat Conversation | Core | 텍스트 대화 세션, 메시지, 첨부 파일, 대화 기록 | ChatSession, ChatMessage, UploadedFile |
| Voice & Avatar Interaction | Core | 음성 세션, 아바타 세션, 실시간 대화 변형 | VoiceSession, AvatarSession |
| Billing & Metering | Core | 결제수단, 구독, 월렛, 토큰 사용량, 과금 기록 | Payment, Subscription, Wallet, UsageRecord |
| Survey Evaluation | Supporting | 설문 정의, 응답, 리포트 생성 | Survey, SurveyResponse, EvaluationReport |
| Assessment Evaluation | Supporting | 평가 정의, 세션, 채점 및 결과 산출 | Assessment, AssessmentSession, AssessmentAnswer |
| Seller Governance | Supporting | 판매자 신청, 승인, 운영 요약 | SellerApplication |
| Guide Content | Supporting | 가이드 카테고리와 문서 발행 | GuideCategory, GuideArticle |
| Support Inbox | Supporting | 문의 접수, 답변, 알림 | SupportInquiry, Notification |
| IN Workspace Facade | Supporting | 모바일 대시보드, 서비스 카드, 기본 상담 에이전트 resolve | InDashboardResponse, InServicesResponse |

## 경계를 이렇게 자르는 이유

- `Agent Catalog & Entitlement`와 `Billing & Metering`를 분리해야 구매 권한과 실제 결제 artifact가 뒤섞이지 않는다.
- `Agent Builder`는 시나리오 수명주기와 출판 규칙을 가지므로 runtime chat과 분리하는 편이 더 안정적이다.
- `IN Workspace Facade`는 자체 상품 규칙을 소유하지 않고 여러 컨텍스트의 읽기 모델을 조합한다.

## 번역 또는 조정이 필요한 경계

- `Agent Builder -> Chat Conversation`에서는 발행된 scenario가 runtime 설정으로 번역된다.
- `Agent Catalog & Entitlement -> Billing & Metering`에서는 권한 획득과 비용 집계가 분리된 언어로 관리된다.
- `Organization Workspace`와 `Agent Catalog & Entitlement`의 조합이 `IN Workspace Facade`에서 모바일 상담 카드로 재구성된다.

## 확인 소스

- `do4i/README.md`
- `do4i/server/README.md`
- `do4i/server/api/http/products.py`
- `do4i/server/api/http/support.py`
- `do4i/server/api/http/assessments.py`
- `do4i/client/mobile/src/flow/InFlowProvider.tsx`
