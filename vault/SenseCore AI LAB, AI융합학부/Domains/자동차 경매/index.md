---
title: "자동차 경매"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980468a30cf0017202035__자동차 경매
notion_id: 31fe313f58b980468a30cf0017202035
notion_url: https://www.notion.so/31fe313f58b980468a30cf0017202035
parent_notion_id: 32be313f58b9803bb9adf68c0393a0f6
---
## 도메인 한 줄 정의

PALCAR의 자동차 경매 도메인은 판매자가 차량을 출품하고 승인된 딜러만 입찰하며, 낙찰 이후 검차, 감가, 인도, 송금, 정산까지 거래를 끝까지 닫는 딜러 승인형 중고차 경매 도메인이다.

## 왜 이 도메인을 따로 보나

- 단순 매물 게시판이 아니라 `승인된 시장`과 `거래 운영`을 동시에 가진다.
- 낙찰이 끝이 아니라 후속 거래 운영이 핵심 가치다.
- 판매자, 딜러, 운영자 사이의 권한 차이가 비즈니스 규칙을 만든다.

## 하위 문서

- 도메인 스토리텔링: 핵심 happy path와 전환점
- 바운디드 컨텍스트: 책임 경계와 분리 이유
- UL: 팀이 공통으로 써야 하는 핵심 용어
- 컨텍스트 맵: upstream, downstream, 번역 책임

## 설계 메모

- PALCAR의 첫 번째 코어는 `딜러 승인형 경매 시장`이다.
- 두 번째 코어는 `낙찰 이후 거래 운영`이다.
- 그래서 `Auction & Award`와 `Trade Fulfillment`를 분리해서 보는 것이 맞다.

## 핵심 판단

- PALCAR의 거래 완료 조건은 `낙찰`이 아니라 `검차, 감가 조정, 인도, 송금, 정산 완료`까지 닫힌 상태다.
- 그래서 경매 규칙과 낙찰 후 운영 규칙을 한 컨텍스트에 섞지 않는다.
- `Settlement Ledger`는 거래를 소유하는 컨텍스트가 아니라 거래 결과를 금융 관점으로 확정하는 supporting 컨텍스트다.

## 확인 소스

- `palcar/README.md`
- `palcar/sdd/02_plan/01_architecture/architecture.md`
- `palcar/sdd/01_planning/01_feature/vehicles_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/bidding_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/trades_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/settlement_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/dealers_feature_spec.md`
- `palcar/scripts/e2e/dev_full_api_e2e.sh`

---

[도메인 스토리텔링](도메인 스토리텔링/index.md)
[바운디드 컨텍스트](바운디드 컨텍스트/index.md)
[UL](UL/index.md)
[컨텍스트 맵](컨텍스트 맵/index.md)
