---
title: "k3s GitOps 운영 클러스터 초보자 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/330e313f58b98144ac78c9476ef7246c__k3s GitOps 운영 클러스터 초보자 가이드
notion_id: 330e313f58b98144ac78c9476ef7246c
notion_url: https://www.notion.so/330e313f58b98144ac78c9476ef7246c
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
이 문서는 연구실 운영 클러스터에 처음 들어오는 사람이 `k3s`, 쿠버네티스 리소스, GitOps 배포 흐름이 어떻게 연결되는지 빠르게 잡기 위한 입문 가이드다.

<callout color="yellow_bg">
운영용 비밀번호, 시크릿 값, 개인 접속 정보는 이 문서에 적지 않는다. 민감한 값은 별도 보안 채널에서 관리하고, 여기에는 구조와 확인 관점만 남긴다.
</callout>

# 먼저 잡을 그림

1. 연구실 서비스는 `k3s` 기반 쿠버네티스 클러스터 위에서 동작한다.
2. 클러스터 상태는 `namespace`, `deployment`, `service`, `ingress`, `secret` 같은 쿠버네티스 리소스로 표현된다.
3. 실제 반영 기준은 `gitops` 레포이고, `ArgoCD`가 그 레포를 읽어 클러스터를 원하는 상태로 수렴시킨다.
4. 인프라 계층은 ingress, 모니터링, 시크릿 관리, 관측성을 먼저 올리고, 그 위에 서비스가 각 namespace에서 동작한다.

즉 초보자가 먼저 잡아야 하는 순서는 `클러스터 구조 -> GitOps 반영 단위 -> 인프라 계층 -> 서비스 계층`이다.

## 이 문서의 역할

이 문서는 입문자가 아래 질문에 답할 수 있게 만드는 것이 목적이다.

- `k3s`와 쿠버네티스는 이 운영 환경에서 어떤 관계인가
- `ArgoCD app`, `namespace`, `overlay`, `base`는 각각 무엇을 뜻하는가
- 문제가 생겼을 때 앱 코드보다 먼저 어느 계층을 봐야 하는가
- 서비스 하나가 GitOps 레포에서 어디에 매핑되는가

실제 접속, 명령 실행, 배포 확인, 되돌리기 같은 절차는 `Manual`에서 관리한다.

## 운영 구조를 이해할 때 보는 단위

### 클러스터

- 운영 환경 전체를 담는 실행 기반이다.
- 노드, 네트워크, 스토리지, 시스템 namespace 같은 공통 기반이 여기 포함된다.

### GitOps

- 원하는 운영 상태를 레포로 선언하는 방식이다.
- 누가 무엇을 배포할지보다, 레포에 정의된 상태가 무엇인지가 기준이 된다.

### ArgoCD 애플리케이션

- GitOps 동기화 단위다.
- 인프라 하나 또는 서비스 하나가 보통 하나 이상의 `ArgoCD app`으로 관리된다.

### Namespace

- 쿠버네티스 리소스가 실제로 모여 있는 실행 단위다.
- 운영 중에는 서비스별 또는 인프라 성격별로 namespace를 나눠서 본다.

### Overlay

- 환경별 최종 조합이다.
- 운영 환경은 보통 `overlays/prod` 같은 위치가 최종 반영 기준이 된다.

## 초보자가 자주 헷갈리는 포인트

| 헷갈리는 것 | 실제 의미 |
| --- | --- |
| `ArgoCD app 이름` | GitOps 동기화 단위다 |
| `namespace 이름` | 쿠버네티스 리소스가 실제로 실행되는 위치다 |
| `overlay` | 환경별 최종 조합이다 |
| `base` | 환경 공통 리소스다 |
| `OutOfSync` | Git 기준과 live 리소스가 다르다는 뜻이지 즉시 장애라는 뜻은 아니다 |
| `Degraded` | 현재 live 상태가 기대한 상태로 수렴하지 않았다는 신호다 |

## 인프라 계층을 보는 순서

앱 문제가 보여도 초보자는 바로 애플리케이션 코드부터 보지 않는 편이 좋다.

먼저 아래 순서로 구조를 본다.

1. ingress가 외부 요청을 정상적으로 받는가
2. service가 올바른 backend를 가리키는가
3. deployment 또는 statefulset이 정상적으로 떠 있는가
4. secret, config 같은 실행 의존성이 들어와 있는가
5. 그 다음에 앱 로그와 서비스 내부 동작을 본다

이 순서가 중요한 이유는, 많은 장애가 애플리케이션 코드보다 배포 계층이나 실행 의존성 계층에서 먼저 드러나기 때문이다.

## GitOps 레포는 왜 보나

GitOps 레포는 현재 운영이 어떤 상태로 선언돼 있는지 확인하는 기준이다.

초보자가 레포를 볼 때는 아래 수준만 먼저 이해하면 충분하다.

| 경로 축 | 의미 |
| --- | --- |
| `terraform/cluster` | 클러스터 생성과 초기 bootstrap 관점 |
| `k8s/bootstrap/argocd` | ArgoCD가 어디서 시작되는지 보는 관점 |
| `k8s/clusters/...` | 특정 클러스터에 어떤 애플리케이션을 올릴지 보는 관점 |
| `k8s/infra/...` | ingress, monitoring, infisical, observability 같은 공통 인프라 관점 |
| `k8s/apps/...` | 서비스별 매니페스트와 overlay 관점 |

즉 서비스 하나를 이해하려면 보통 `clusters`에서 app을 찾고, 거기서 `apps/.../overlays/...`로 내려가는 흐름을 따르면 된다.

## 서비스 계층은 어떻게 이어지나

서비스는 보통 아래 단위로 이해하면 된다.

- GitOps에서 하나의 서비스 애플리케이션이 정의된다.
- 그 애플리케이션은 특정 namespace로 배포된다.
- namespace 안에는 deployment, service, ingress, secret 같은 리소스가 모인다.
- 사용자는 ingress를 통해 서비스에 들어오고, 운영자는 ArgoCD와 관측 도구를 통해 상태를 본다.

따라서 `서비스 이름 -> ArgoCD app -> namespace -> overlay` 순서로 관계를 잡아두면 이후 문서를 읽기 쉬워진다.

## 인프라 스택은 어디까지 알고 시작하면 되나

초보자 기준 최소한 아래 정도의 역할 구분은 알고 시작하면 된다.

| 스택 | 왜 필요한가 |
| --- | --- |
| ingress-nginx | 외부 HTTP 요청을 클러스터 서비스로 보낸다 |
| monitoring | 메트릭과 대시보드를 본다 |
| infisical | 운영 시크릿을 중앙에서 관리한다 |
| infisical-operator | 시크릿을 쿠버네티스 실행 환경으로 전달한다 |
| observability | 로그와 트레이스를 수집하고 조회한다 |

각 스택의 세부 구조와 운영 관점은 해당 가이드 문서에서 따로 읽는 편이 좋다.

## 이 문서를 읽은 뒤 다음으로 볼 것

입문자는 보통 아래 순서로 이어서 보면 된다.

1. `k3s`와 쿠버네티스의 관계를 먼저 이해한다.
2. `GitOps`와 `ArgoCD`가 어떤 단위로 상태를 맞추는지 본다.
3. `Infisical`, `Monitoring`, `Observability`처럼 공통 인프라 역할을 본다.
4. 마지막으로 서비스별 가이드와 운영 매뉴얼로 내려간다.

즉 이 문서는 "지도를 펴는 문서"이고, 실제 작업 문서는 별도 가이드와 매뉴얼에서 이어진다.
