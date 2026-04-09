---
title: "ArgoCD 운영 흐름 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/338e313f58b981f4a6d8d696ab620029__ArgoCD 운영 흐름 가이드
notion_id: 338e313f58b981f4a6d8d696ab620029
notion_url: https://www.notion.so/338e313f58b981f4a6d8d696ab620029
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
# ArgoCD 운영 흐름 가이드

이 문서는 ArgoCD를 운영 관점에서 어떻게 읽어야 하는지 설명하는 가이드다.

## ArgoCD의 역할

ArgoCD는 GitOps 선언을 읽고, 클러스터의 실제 상태를 원하는 상태로 수렴시키는 컨트롤러다.

운영자는 ArgoCD를 통해 아래를 본다.

- 어떤 애플리케이션이 관리 대상인지
- 원하는 상태와 실제 상태가 일치하는지
- 수렴이 실패했는지
- 리소스 health가 정상인지

## 초보자가 먼저 보는 화면 개념

| 항목 | 운영에서 보는 의미 |
| --- | --- |
| `Application` | 동기화 단위다. 서비스 하나이거나 인프라 묶음일 수 있다. |
| `Sync Status` | Git 기준과 live 기준이 같은지 |
| `Health Status` | 리소스가 정상적으로 떠 있는지 |
| `Source` | 어떤 레포 경로를 기준으로 삼는지 |
| `Destination` | 어느 클러스터와 namespace에 적용되는지 |

## 가장 중요한 판단 원칙

`OutOfSync` 하나만 보고 곧바로 장애라고 단정하지 않는다.

운영에서는 항상 아래 둘을 같이 본다.

1. `Sync Status`
2. `Health Status`

예를 들어 `OutOfSync` 여도 앱이 정상 동작 중일 수 있고, 반대로 `Synced` 여도 리소스 health가 깨져 있을 수 있다.

## Application을 추적하는 기본 흐름

1. 어떤 서비스나 인프라 묶음이 문제인지 찾는다.
2. 해당 `Application` 이 어떤 namespace를 관리하는지 본다.
3. `source.path` 가 어느 overlay 또는 manifest 경로를 가리키는지 본다.
4. health가 깨진 구체 리소스를 내려가서 본다.
5. 필요하면 Kubernetes 리소스와 로그로 내려간다.

즉 ArgoCD는 최종 원인 그 자체보다, `어느 선언과 어느 리소스가 어긋났는지`를 찾는 출발점에 가깝다.

## ArgoCD와 Kubernetes의 역할 차이

- ArgoCD는 `무엇을 적용해야 하는가`를 본다.
- Kubernetes는 `실제로 무엇이 떠 있는가`를 본다.

둘을 같이 봐야 운영 판단이 맞아진다.

## 이 문서 다음에 무엇을 읽는가

- 변경 기준이 궁금하면 `GitOps 운영 모델 가이드`
- 바닥 리소스 구조가 약하면 `Kubernetes 기본 구조 가이드`
- 실제 절차는 `Manual` 의 배포 확인, sync 확인, 롤백 문서를 본다.
