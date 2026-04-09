---
title: "Kubernetes 기본 구조 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/338e313f58b9818d93b4df013bf48769__Kubernetes 기본 구조 가이드
notion_id: 338e313f58b9818d93b4df013bf48769
notion_url: https://www.notion.so/338e313f58b9818d93b4df013bf48769
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
# Kubernetes 기본 구조 가이드

이 문서는 연구실 운영 문서를 읽기 전에 알아야 하는 Kubernetes의 기본 추상화를 정리한 가이드다.

## 언제 읽는가

- `kubectl get` 출력이 무엇을 뜻하는지 헷갈릴 때
- ArgoCD 화면에서 보이는 리소스 종류가 감이 안 올 때
- 서비스 장애를 볼 때 `pod`, `deployment`, `service`, `ingress`의 관계가 잘 안 잡힐 때

## 먼저 잡아야 하는 구조

Kubernetes는 애플리케이션을 한 번에 직접 실행하는 도구가 아니라, 원하는 상태를 선언하고 그 상태로 수렴시키는 플랫폼이다.

초보자는 아래 관계만 먼저 잡으면 된다.

1. `namespace` 는 리소스를 나누는 운영 단위다.
2. `deployment` 는 stateless 앱의 원하는 복제 상태를 관리한다.
3. `statefulset` 은 데이터가 붙는 워크로드를 안정적으로 관리한다.
4. `service` 는 워크로드를 고정된 네트워크 이름으로 노출한다.
5. `ingress` 는 외부 HTTP 요청을 service로 연결한다.

## 운영에서 자주 보는 리소스

| 리소스 | 의미 | 언제 먼저 보나 |
| --- | --- | --- |
| `pod` | 실제로 뜬 실행 단위 | 앱이 죽었는지 볼 때 |
| `deployment` | 앱 replica를 관리하는 상위 리소스 | 원하는 수와 실제 수가 맞는지 볼 때 |
| `statefulset` | 데이터가 있는 워크로드의 안정적 단위 | DB나 저장소가 붙은 앱을 볼 때 |
| `service` | 내부 고정 네트워크 진입점 | 앱은 떴는데 연결이 안 될 때 |
| `ingress` | 외부 도메인과 HTTP 라우팅 | 도메인 접근이 안 될 때 |
| `secret` | 민감한 설정 값 | 앱이 환경 변수나 인증 값 없이 뜰 때 |
| `configmap` | 비밀이 아닌 설정 값 | 앱 설정이 어긋났을 때 |

## 문제를 볼 때의 기본 순서

앱이 안 뜬다고 바로 코드부터 보지 않는다.

1. `namespace` 가 맞는지 본다.
2. `deployment` 또는 `statefulset` 이 원하는 개수로 뜨는지 본다.
3. `pod` 가 `Running` 또는 `Ready` 인지 본다.
4. `service` 가 올바른 포트를 바라보는지 본다.
5. `ingress` 가 올바른 host/path를 service로 연결하는지 본다.
6. 그 다음에 `secret`, `configmap`, 로그를 본다.

## 연구실 운영 문서를 읽을 때 연결되는 개념

- `k3s` 는 Kubernetes 배포판이다.
- `GitOps` 는 Kubernetes 리소스를 레포 기준으로 운영하는 방식이다.
- `ArgoCD` 는 GitOps 선언을 읽어 클러스터를 수렴시키는 컨트롤러다.
- `Infisical` 은 시크릿의 원천 저장소고, Kubernetes에는 그 결과가 `Secret` 형태로 들어온다.

즉 Kubernetes는 바닥 플랫폼이고, 나머지 도구는 이 플랫폼 위에서 운영 모델을 구성한다고 보면 된다.
