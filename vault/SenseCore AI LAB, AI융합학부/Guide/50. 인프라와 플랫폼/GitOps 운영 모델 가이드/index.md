---
title: "GitOps 운영 모델 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/338e313f58b981008b6bcee9a4b3333e__GitOps 운영 모델 가이드
notion_id: 338e313f58b981008b6bcee9a4b3333e
notion_url: https://www.notion.so/338e313f58b981008b6bcee9a4b3333e
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
# GitOps 운영 모델 가이드

이 문서는 연구실 운영 환경이 왜 GitOps 방식으로 관리되는지 설명하는 가이드다.

## GitOps를 한 문장으로 보면

운영 상태를 사람 손으로 직접 고치는 대신, 레포에 선언한 원하는 상태를 기준으로 클러스터를 수렴시키는 운영 방식이다.

핵심은 아래 두 문장이다.

1. 변경의 기준은 레포다.
2. 클러스터는 그 기준 상태로 계속 맞춰진다.

## 왜 이 방식이 중요한가

- 어떤 변경이 있었는지 추적하기 쉽다.
- 사람마다 다른 수동 조작을 줄일 수 있다.
- 운영 상태를 레포 diff와 연결해 설명할 수 있다.
- 배포와 인프라 변경을 같은 모델로 볼 수 있다.

## 운영에서 보는 기본 흐름

1. 운영자가 레포를 수정한다.
2. 변경이 검토되고 반영된다.
3. GitOps 컨트롤러가 변경을 읽는다.
4. 클러스터 리소스가 선언 상태로 수렴한다.
5. 운영자는 수렴 결과를 확인한다.

여기서 중요한 점은 `배포`가 곧 `서버 접속 후 수동 적용`을 뜻하지 않는다는 것이다.

## GitOps에서 자주 쓰는 판단 기준

| 기준 | 의미 |
| --- | --- |
| `desired state` | 레포에 선언된 목표 상태 |
| `live state` | 현재 클러스터에 실제로 존재하는 상태 |
| `drift` | 목표 상태와 실제 상태가 어긋난 경우 |
| `reconcile` | 어긋난 상태를 다시 맞추는 과정 |

즉 운영자는 개별 pod를 손으로 만지기보다 `무엇이 drift 되었고 왜 수렴하지 않는가`를 본다.

## 초보자가 자주 놓치는 점

- GitOps는 자동화된 `kubectl apply` 정도로만 보면 부족하다.
- 핵심은 `변경 기준`, `수렴`, `검증`을 한 모델로 묶는 데 있다.
- live에서 급히 수정한 값은 일시적으로 문제를 덮을 수 있지만, 레포와 어긋나면 다시 뒤집히거나 drift로 남는다.

## 연구실 문서에서 연결되는 도구

- `ArgoCD` 는 GitOps 컨트롤러다.
- `kustomize` 또는 manifest 구조는 환경별 선언을 정리하는 수단이다.
- `Manual` 에서는 GitOps 변경 적용, 확인, 롤백 절차를 다룬다.
