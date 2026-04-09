---
title: "도메인 스토리텔링"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/31fe313f58b980468a30cf0017202035__자동차 경매/children/330e313f58b981cab445ea320d15420f__도메인 스토리텔링
notion_id: 330e313f58b981cab445ea320d15420f
notion_url: https://www.notion.so/330e313f58b981cab445ea320d15420f
parent_notion_id: 31fe313f58b980468a30cf0017202035
---
## 이 페이지의 목적

이 페이지는 PALCAR의 `as-is` 거래 흐름을 판매자, 딜러, 운영자 기준으로 고정하는 페이지다.

## 핵심 액터

- 판매자: 차량을 출품하고 경매 종료와 거래 수락을 결정한다.
- 딜러: 승인 후 시장에 진입해 입찰하고 낙찰 후 거래를 진행한다.
- 관리자: 딜러 승인, 검차, 송금 확인 같은 운영 단계를 확정한다.

## 핵심 work object

- Vehicle Listing: 출품된 차량과 경매 조건을 담는 판매 단위다.
- Bid: 딜러가 제출하는 유효 입찰이다.
- Trade Workflow: 낙찰 이후 검차, 감가, 인도, 송금, 정산 상태를 가진 거래 객체다.

## 80% 핵심 시나리오

1. 공개 사용자는 판매자 또는 딜러 계정으로 가입한다.
2. 딜러는 사업자 증빙과 딜러 서류를 제출하고 승인 전까지 경매에 참여하지 못한다.
3. 판매자는 차량을 등록하면서 희망가, 최소 입찰 단위, 종료 시각 같은 경매 조건을 정한다.
4. 승인된 딜러는 활성 매물을 조회하고 입찰을 생성, 수정, 취소한다.
5. 판매자는 마감 시점에 경매를 닫고 유찰 또는 낙찰을 확정한다.
6. 낙찰이 생기면 거래는 검차 단계로 넘어가고 관리자가 검차 일정을 제안하고 완료를 기록한다.
7. 딜러는 감가를 제안하고 판매자는 재협의 또는 승인을 통해 최종 거래 금액을 확정한다.
8. 이후 인도 일정, 양측 인도 확인, 딜러 송금 제출, 관리자 송금 확인, 판매자 정산 완료 순서로 거래를 닫는다.

## 주요 variation

- 활성 입찰이 없거나 희망가 미달이면 유찰로 종료된다.
- 검차 이후 감가가 없을 수도 있고, 감가 재협의가 여러 차례 반복될 수도 있다.
- 관리자 강제 종료는 정상 거래 흐름을 끊는 별도 운영 경로다.

## 경계 판단 포인트

- 딜러 승인 이전과 이후는 같은 사용자라도 완전히 다른 시장 권한을 가진다.
- 낙찰 전 경쟁 규칙과 낙찰 후 거래 운영 규칙은 분리해서 봐야 한다.
- 정산 완료는 단순 조회가 아니라 거래를 financial close로 닫는 운영 단계다.

## 확인 소스

- `palcar/README.md`
- `palcar/sdd/02_plan/01_architecture/architecture.md`
- `palcar/sdd/01_planning/01_feature/bidding_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/trades_feature_spec.md`
- `palcar/sdd/01_planning/01_feature/settlement_feature_spec.md`
