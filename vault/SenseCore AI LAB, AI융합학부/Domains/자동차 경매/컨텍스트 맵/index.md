---
title: "컨텍스트 맵"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980468a30cf0017202035__자동차 경매/children/330e313f58b98126ac1edc4f114b1de4__컨텍스트 맵
notion_id: 330e313f58b98126ac1edc4f114b1de4
notion_url: https://www.notion.so/330e313f58b98126ac1edc4f114b1de4
parent_notion_id: 31fe313f58b980468a30cf0017202035
---
## 이 페이지의 목적

이 페이지는 PALCAR의 시장, 거래, 정산 경계가 어떻게 이어지는지 보여주는 전략 설계 페이지다.

| Upstream | Downstream | 관계 | 번역 책임 | 변경 비용 메모 |
| --- | --- | --- | --- | --- |
| Identity & Access | Dealer Onboarding & Approval | Customer/Supplier | 딜러 심사 쪽이 계정 정보를 business gate로 해석한다. | 계정 모델이 바뀌면 승인 규칙도 함께 흔들린다. |
| Dealer Onboarding & Approval | Auction & Award | Customer/Supplier | 경매 쪽이 승인 상태를 입찰 가능 여부로 번역한다. | 승인 상태 표현이 바뀌면 입찰 권한 검증이 깨질 수 있다. |
| Vehicle Intake & Listing | Auction & Award | Customer/Supplier | listing이 경매 상품 표현을 제공한다. | listing 필드가 흔들리면 필터/정렬/마감 규칙도 영향받는다. |
| Auction & Award | Trade Fulfillment | Open Host Service | 낙찰 이벤트를 거래 시작 이벤트로 번역한다. | 이 경계가 가장 중요하며 award 모델 변경 시 거래 생성이 깨진다. |
| Trade Fulfillment | Settlement Ledger | Published Language | 거래 운영 결과를 지급 완료용 언어로 요약한다. | 지급 규칙 변경 시 read model과 ledger 모두 손봐야 한다. |
| Support Content & Inbox | Seller/Dealer surface | Supporting | 표면 쪽이 운영 콘텐츠를 UI 흐름으로 반영한다. | 핵심 경매 모델 변경과는 결합이 약하다. |
| Admin Operations | 전체 컨텍스트 | Governance | 운영자가 단계 확정을 하되 각 컨텍스트의 핵심 규칙은 그대로 둔다. | 운영 화면 요구가 코어 모델을 침식시키지 않게 주의해야 한다. |

## 현재 해석

- PALCAR의 핵심 경계는 `입찰 경쟁`과 `낙찰 후 거래 운영`을 나누는 지점이다.
- `Settlement Ledger`는 거래 규칙을 소유하지 않고 financial close 관점으로 결과를 확정한다.

## 확인 소스

- `palcar/README.md`
- `palcar/sdd/02_plan/01_architecture/architecture.md`
- `palcar/sdd/01_planning/01_feature/trades_feature_spec.md`
