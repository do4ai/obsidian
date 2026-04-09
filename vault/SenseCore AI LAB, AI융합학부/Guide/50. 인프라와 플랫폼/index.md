---
title: "50. 인프라와 플랫폼"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼
notion_id: 330e313f58b981a0b738ed69daa8f3a0
notion_url: https://www.notion.so/330e313f58b981a0b738ed69daa8f3a0
parent_notion_id: 330e313f58b9802b9cedda8dcbc5d112
---
# 50. 인프라와 플랫폼

이 섹션은 SCAI LAB 연구실의 서버, 클러스터, 배포 플랫폼, 운영 도구를 이해하기 위한 가이드다.

운영 환경을 처음 접하는 구성원은 아래 순서로 읽는 것을 권장한다.

[k3s GitOps 운영 클러스터 초보자 가이드](k3s GitOps 운영 클러스터 초보자 가이드/index.md)

그 다음에는 아래 개념 가이드를 주제별로 읽으면 전체 구조가 더 안정적으로 잡힌다.

| 문서 | 초점 |
| --- | --- |
| `Kubernetes 기본 구조 가이드` | namespace, deployment, service, ingress 같은 기본 추상화 |
| `k3s 운영 구조 가이드` | 연구실이 왜 k3s를 쓰고 어떤 운영 단위로 보는지 |
| `GitOps 운영 모델 가이드` | 레포 변경이 어떻게 운영 상태로 수렴하는지 |
| `ArgoCD 운영 흐름 가이드` | Application, sync, health를 어떻게 읽는지 |
| `Infisical 시크릿 관리 가이드` | 운영 시크릿이 어떻게 저장되고 주입되는지 |
| `Observability 운영 가이드` | 메트릭, 로그, 트레이스를 어떤 순서로 보는지 |

이 섹션의 원칙은 아래와 같다.

- 이곳은 개념과 구조를 설명한다.
- 날짜별 상태, 특정 장애 기록, 일회성 운영 메모는 별도 운영 문서에서 다룬다.
- 실제 변경 절차와 검증, 롤백은 `Manual`에서 다룬다.
