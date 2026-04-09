---
title: "UL"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980468a30cf0017202035__자동차 경매/children/330e313f58b98132bb20eaca3689151f__UL
notion_id: 330e313f58b98132bb20eaca3689151f
notion_url: https://www.notion.so/330e313f58b98132bb20eaca3689151f
parent_notion_id: 31fe313f58b980468a30cf0017202035
---
## 이 페이지의 목적

이 페이지는 PALCAR 팀이 거래 운영을 같은 뜻으로 말하게 만드는 언어 계약 페이지다.

| 용어 | 정의 | 사용하는 문맥 | 금지 또는 주의 표현 |
| --- | --- | --- | --- |
| Seller | 차량을 출품하는 판매자 | listing 등록, 경매 마감, 거래 수락 | 딜러와 같은 사용자 계정이라는 이유로 Buyer처럼 부르지 않는다. |
| Dealer | 승인 후 입찰 가능한 매수자 | 입찰, 감가 제안, 송금 제출 | 승인 전 신청자를 Dealer라고 부르지 않는다. |
| Dealer Approval | 딜러 시장 진입 자격 부여 | dealers context | 단순 회원가입 완료와 혼용하지 않는다. |
| Vehicle Listing | 경매 가능한 차량 출품 단위 | vehicles, bidding | 차량 원본 정보 전체와 같은 뜻으로 쓰지 않는다. |
| Reserve Price | 판매자가 수용 가능한 최소 가격 | listing, award 판단 | 시작가와 같은 뜻으로 쓰지 않는다. |
| Minimum Bid Increment | 최소 입찰 증가 단위 | bidding validation | UI 안내값 정도로 축소하지 않는다. |
| Bid | 현재 유효한 입찰 | bidding | 제안가, 희망가와 혼용하지 않는다. |
| Winning Dealer | 낙찰된 딜러 | award 이후 trade 시작 | 최고가 제출자와 자동 동의어로 쓰지 않는다. |
| Winning Price | 낙찰 시점 가격 | award | 최종 정산 금액과 같은 뜻으로 쓰지 않는다. |
| Inspection | 운영 주도 검차 단계 | trades | 차량 조회, 차량 등록과 혼용하지 않는다. |
| Depreciation Proposal | 검차 이후 가격 재협상 제안 | trades | 단순 할인 요청으로 부르지 않는다. |
| Agreed Price | 감가 반영 후 합의된 거래 금액 | trades, settlement | Winning Price와 혼용하지 않는다. |
| Remittance | 딜러 송금 제출 및 운영 확인 상태 | trades | 정산 완료와 같은 뜻으로 쓰지 않는다. |
| Settlement | 판매자 지급 완료 | settlement | 송금 제출, 거래 완료와 구분한다. |

## 용어 운영 원칙

- 낙찰 이전 언어와 낙찰 이후 언어를 섞지 않는다.
- UI 문구가 다르더라도 코드와 문서의 정본 용어는 위 표를 따른다.
- 감가, 송금, 정산은 모두 거래 후속 운영 용어로 분리한다.

## 확인 소스

- `palcar/README.md`
- `palcar/sdd/01_planning/01_feature/bidding_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/trades_feature_spec.md`
