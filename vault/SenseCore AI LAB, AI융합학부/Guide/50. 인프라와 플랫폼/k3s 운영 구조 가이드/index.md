---
title: "k3s 운영 구조 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/338e313f58b9817bbfd3ecb17862cbd8__k3s 운영 구조 가이드
notion_id: 338e313f58b9817bbfd3ecb17862cbd8
notion_url: https://www.notion.so/338e313f58b9817bbfd3ecb17862cbd8
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
# k3s 운영 구조 가이드

이 문서는 연구실이 운영 클러스터를 어떤 단위로 바라보는지 설명하는 가이드다.

## 왜 k3s를 쓰는가

k3s는 Kubernetes를 더 가볍게 운영할 수 있게 정리한 배포판이다.

연구실 운영 관점에서는 아래 이유가 중요하다.

- 단일 서버 또는 소규모 노드 환경에 맞게 단순하게 운영할 수 있다.
- 표준 Kubernetes 리소스와 도구를 그대로 활용할 수 있다.
- 실험 환경과 운영 환경의 구조를 크게 다르게 가져가지 않아도 된다.

즉 `가볍지만 Kubernetes와 단절되지 않는 선택`으로 보는 것이 맞다.

## 운영 단위는 어떻게 나뉘는가

초보자는 k3s 자체의 내부 구현보다 운영 단위를 먼저 보면 된다.

1. 서버 또는 노드
2. k3s 클러스터
3. namespace
4. 공통 인프라
5. 서비스별 워크로드

이 문서 집합에서는 특히 아래 두 층을 구분하는 것이 중요하다.

- 공통 인프라: ingress, 시크릿 주입, 관측성, 배포 컨트롤러
- 서비스 워크로드: `do4i`, `palcar`, `papersens` 같은 개별 앱

## 초보자가 헷갈리기 쉬운 포인트

| 헷갈리는 것 | 실제로는 |
| --- | --- |
| `서버` 와 `클러스터` | 같은 물리 환경을 말하더라도 관점이 다르다. 서버는 머신, 클러스터는 Kubernetes 운영 면이다. |
| `k3s` 와 `Kubernetes` | k3s는 Kubernetes를 운영하기 쉽게 묶은 배포판이다. |
| `클러스터 장애` 와 `앱 장애` | 노드, ingress, DNS, 시크릿 문제는 클러스터 쪽이고, replica 부족이나 앱 에러는 워크로드 쪽이다. |

## k3s 위에서 같이 보는 운영 도구

- `GitOps`: 레포 기준으로 원하는 상태를 관리한다.
- `ArgoCD`: GitOps 선언을 읽어 실제 클러스터를 수렴시킨다.
- `Infisical`: 시크릿 원천을 관리한다.
- `Observability` 스택: 메트릭, 로그, 트레이스를 통해 상태를 읽는다.

즉 k3s는 단독으로 이해하기보다, 운영 도구들이 붙는 바닥 플랫폼으로 이해하는 편이 맞다.

## 이 문서 다음에 무엇을 읽는가

- 리소스 개념이 약하면 `Kubernetes 기본 구조 가이드`
- 배포 흐름이 궁금하면 `GitOps 운영 모델 가이드`
- 동기화와 수렴 판단이 궁금하면 `ArgoCD 운영 흐름 가이드`
