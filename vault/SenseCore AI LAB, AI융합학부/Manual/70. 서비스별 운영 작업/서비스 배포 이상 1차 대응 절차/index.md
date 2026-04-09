---
title: "서비스 배포 이상 1차 대응 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98181a506fee4b158ad5a__70. 서비스별 운영 작업/children/338e313f58b9816f87cee5b8285862b0__서비스 배포 이상 1차 대응 절차
notion_id: 338e313f58b9816f87cee5b8285862b0
notion_url: https://www.notion.so/338e313f58b9816f87cee5b8285862b0
parent_notion_id: 330e313f58b98181a506fee4b158ad5a
---
# 서비스 배포 이상 1차 대응 절차

## 문서 목적

이 문서는 `do4i`, `palcar`, `papersens` 같은 운영 서비스가 배포 후 정상 수렴하지 않을 때 공통으로 따르는 1차 대응 절차를 정리한다.

서비스별 상세 차이는 따로 보강할 수 있지만, 초기 대응 흐름은 공통으로 유지하는 편이 빠르고 안전하다.

## 준비물

- 장애가 난 서비스명
- 대상 namespace
- 최근 배포 시각 또는 최근 변경 커밋
- 확인 가능한 health endpoint 또는 대표 URL

## 절차

### 1. 서비스 범위를 먼저 고정한다

1. 장애가 난 서비스가 하나인지 여러 개인지 구분한다.
2. namespace를 고정한다.
3. 최근 배포가 있었는지 확인한다.

여기서 범위를 못 좁히면 클러스터 전체 문제와 서비스 단일 문제를 혼동하기 쉽다.

### 2. ArgoCD 상태를 본다

```bash
sudo kubectl get applications -A
```

확인할 것은 아래다.

- 대상 서비스 `Application` 이 보이는가
- `OutOfSync` 인가
- `Degraded` 인가
- sync 이후 수렴이 멈췄는가

### 3. namespace live 상태를 본다

```bash
sudo kubectl get deploy,sts,svc,ing -n <namespace>
sudo kubectl get pods -n <namespace>
```

먼저 아래를 확인한다.

1. deployment/statefulset 이 존재하는가
2. available replica 가 부족한가
3. pod가 `CrashLoopBackOff`, `ImagePullBackOff`, `Pending` 인가
4. ingress 와 service 가 끊기지 않았는가

### 4. 앱 로그를 확인한다

```bash
sudo kubectl logs deploy/<deploy-name> -n <namespace> --tail=100
```

로그에서 먼저 찾는 것은 아래다.

- 환경 변수 또는 secret 누락
- DB 연결 실패
- 외부 API 인증 실패
- migration 또는 startup 실패

### 5. 변경 유형별로 원인을 좁힌다

아래 기준으로 빠르게 분류한다.

- `ImagePullBackOff`: 이미지 태그 또는 registry 접근 문제
- `CrashLoopBackOff`: 앱 시작 설정, secret, 코드 오류 문제
- ingress 이상: 도메인, path, service backend 문제
- `OutOfSync` 만 있고 앱은 정상: 즉시 장애인지 아닌지 구분 필요

## 검증 기준

- 서비스 pod가 최소 정상 기동 상태로 수렴하는가
- 대표 URL 또는 health endpoint가 응답하는가
- 로그에 반복 치명 오류가 남지 않는가
- 동일 namespace의 다른 핵심 리소스가 함께 망가지지 않았는가

## 롤백 또는 중단 기준

아래 중 하나면 롤백을 우선 검토한다.

- 기동 자체가 되지 않는다
- 대표 기능이 응답하지 않는다
- 새 변경이 원인이라는 근거가 명확하다

바로 롤백하면 안 되는 경우도 있다.

- 장애 원인이 외부 의존성이고 배포와 무관할 때
- 이미 다른 긴급 변경이 동시에 들어가 기준이 불분명할 때

이 경우 먼저 기준 커밋과 원인 범위를 확정한다.

## 작업 후 기록

- 대상 서비스와 namespace
- 장애 시작 시각
- 확인한 `Application` 상태
- pod 상태와 핵심 로그 근거
- 최종 조치: 관찰, 추가 조사, 즉시 롤백
