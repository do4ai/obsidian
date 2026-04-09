---
title: "70. 서비스별 운영 작업"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98181a506fee4b158ad5a__70. 서비스별 운영 작업
notion_id: 330e313f58b98181a506fee4b158ad5a
notion_url: https://www.notion.so/330e313f58b98181a506fee4b158ad5a
parent_notion_id: 330e313f58b98098b619f0e3ef2d0fa0
---
# 70. 서비스별 운영 작업

이 섹션은 각 서비스별 배포 확인, 점검, 운영 변경, 1차 대응 절차를 정리한다.

서비스별 차이가 큰 항목은 공통 절차와 분리해서 개별 매뉴얼로 관리한다.

현재 운영 기준으로 먼저 볼 문서는 아래다.

- `서비스 배포 이상 1차 대응 절차`: `ArgoCD`, namespace live 상태, 앱 로그를 이용한 공통 초기 대응 절차
- `do4i 배포 이상 대응 절차`: `api`, `mysql`, `api-ingress` 중심의 상세 확인 절차
- `palcar 배포 이상 대응 절차`: `api`, `mysql`, `/api`, `/health` 경로 중심의 상세 확인 절차
- `papersens 배포 이상 대응 절차`: `papersens` deployment 와 ingress 중심의 상세 확인 절차

권장 순서는 아래와 같다.

1. 공통 문서인 `서비스 배포 이상 1차 대응 절차`로 범위를 먼저 좁힌다.
2. 그 다음 대상 서비스의 상세 문서로 내려가 리소스, 로그, 검증 포인트를 서비스 기준으로 확인한다.
