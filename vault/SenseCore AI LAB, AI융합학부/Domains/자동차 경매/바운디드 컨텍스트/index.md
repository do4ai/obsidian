---
title: "바운디드 컨텍스트"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980468a30cf0017202035__자동차 경매/children/330e313f58b9810c8326d8e545ec2666__바운디드 컨텍스트
notion_id: 330e313f58b9810c8326d8e545ec2666
notion_url: https://www.notion.so/330e313f58b9810c8326d8e545ec2666
parent_notion_id: 31fe313f58b980468a30cf0017202035
---
## 이 페이지의 목적

이 페이지는 PALCAR의 경쟁우위가 걸린 책임과 supporting 책임을 분리하는 페이지다.

| 컨텍스트 | 분류 | 핵심 책임 | 대표 개념 |
| --- | --- | --- | --- |
| Identity & Access | Generic | 로그인, 세션, 비밀번호 재설정, 역할 게이트 | Seller Account, Dealer Account, Admin Account |
| Dealer Onboarding & Approval | Core | 딜러 서류 접수, 심사, 승인/반려, 시장 진입 자격 부여 | Dealer Application, Dealer Document, Approval |
| Vehicle Intake & Listing | Core | 판매자 차량 등록, 매물 정보 관리, 경매 기본 조건 설정 | Vehicle, Listing, Reserve Price |
| Auction & Award | Core | 입찰 등록/수정/취소, 최고가 경쟁, 판매자 마감, 낙찰/유찰 결정 | Bid, Winning Dealer, Winning Price |
| Trade Fulfillment | Core | 검차, 감가 협상, 인도, 송금 확인, 거래 단계 전이 | Inspection, Depreciation Proposal, Delivery Schedule, Remittance |
| Settlement Ledger | Supporting | 정산 계좌, 정산 결과 조회, 지급 완료 기록 | Settlement Account, Settlement Record |
| Support Content & Inbox | Supporting | 공지, FAQ, 문의, 알림, 운영 답변 | Notice, FAQ, Inquiry, Notification |
| Admin Operations | Supporting | 관리자 계정, 권한 그룹, 감사 로그, 블랙리스트, 운영 추적 | Admin Role, Audit Log, Blacklist |
| Account Settings | Supporting | 프로필, 보안 설정, 환경설정, 회원 탈퇴 | Profile, Security Setting, Withdrawal |

## 경계를 이렇게 자르는 이유

- `Auction & Award`와 `Trade Fulfillment`를 분리해야 낙찰 전 경쟁 규칙과 낙찰 후 운영 규칙이 섞이지 않는다.
- `Dealer Onboarding & Approval`을 `Identity`에 섞으면 딜러 심사 규칙이 일반 로그인 규칙을 오염시킨다.
- `Settlement Ledger`는 거래 단계 전이를 소유하지 않고, 완료된 거래 결과를 금융 관점으로 확정한다.

## 번역 또는 조정이 필요한 경계

- `Vehicle Intake & Listing -> Auction & Award`에서는 차량 원본 정보가 경매 상품 표현으로 번역된다.
- `Auction & Award -> Trade Fulfillment`에서는 낙찰 이벤트가 거래 워크플로우 생성으로 번역된다.
- `Trade Fulfillment -> Settlement Ledger`에서는 운영 단계 결과가 지급 완료 관점 레코드로 요약된다.

## 확인 소스

- `palcar/README.md`
- `palcar/sdd/02_plan/01_architecture/architecture.md`
- `palcar/sdd/01_planning/01_feature/dealers_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/trades_feature_spec.md`
