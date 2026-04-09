---
title: "palcar 배포 이상 대응 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98181a506fee4b158ad5a__70. 서비스별 운영 작업/children/338e313f58b9811d8079c6f3a370d74b__palcar 배포 이상 대응 절차
notion_id: 338e313f58b9811d8079c6f3a370d74b
notion_url: https://www.notion.so/338e313f58b9811d8079c6f3a370d74b
parent_notion_id: 330e313f58b98181a506fee4b158ad5a
---
# palcar 배포 이상 대응 절차

## 문서 목적

이 문서는 `palcar` 서비스가 배포 후 정상 수렴하지 않거나, 핵심 경로가 비정상일 때 따르는 상세 대응 절차를 정리한다.

공통 초기 대응은 `서비스 배포 이상 1차 대응 절차`를 먼저 적용하고, 이 문서에서는 `palcar`에 특화된 검증 포인트를 본다.

## 준비물

- `palcar` namespace 확인 권한
- `ArgoCD` 와 `kubectl` 확인 권한
- `palcar.do4ai.com/api`, `admin.palcar.do4ai.com/api`, `/health` 기준 URL
- 최근 변경 커밋 또는 배포 시각

## 먼저 확인할 운영 단위

- namespace: `palcar`
- 핵심 workload: `api` Deployment, `mysql` StatefulSet
- 핵심 ingress: `palcar`
- 먼저 볼 경로: `/api`, `/health`

## 절차

### 1. 공통 1차 대응 절차를 먼저 적용한다

먼저 아래를 끝낸다.

1. `Application` 상태 확인
2. namespace live 상태 확인
3. 대표 로그 확인

그 다음 `palcar` 고유 경로와 DB 의존성을 본다.

### 2. `/health` 와 `/api` 기준을 분리해 본다

```bash
sudo kubectl get deploy,sts,pods,svc,ing -n palcar
```

아래 질문을 먼저 분리한다.

1. 앱 자체가 안 뜨는가
2. 앱은 뜨지만 `/health` 만 실패하는가
3. `/health` 는 되지만 `/api` 흐름만 실패하는가

이 분리가 되면 ingress 문제인지 앱 기능 문제인지 더 빨리 좁혀진다.

### 3. `api` 와 `mysql` 상태를 같이 본다

```bash
sudo kubectl logs deploy/api -n palcar --tail=100
sudo kubectl logs statefulset/mysql -n palcar --tail=100
```

먼저 찾는 것은 아래다.

- DB 연결 실패
- 환경 변수 또는 secret 누락
- startup 실패
- 외부 연동 실패

### 4. ingress 경로와 backend 연결을 확인한다

```bash
sudo kubectl describe ingress -n palcar palcar
sudo kubectl get svc -n palcar
```

아래를 확인한다.

1. host 가 `palcar.do4ai.com`, `admin.palcar.do4ai.com` 기준과 맞는가
2. `/api`, `/health` path 가 기대한 backend로 연결되는가
3. service port 와 ingress backend 가 어긋나지 않는가

### 5. `/health` 기준으로 회복 여부를 먼저 본다

가능하면 대표 기능보다 먼저 `/health` 회복 여부를 본다.

이유는 아래와 같다.

- 앱 기동 회복 여부를 더 빠르게 판단할 수 있다
- 사용자 기능 장애와 인프라 수렴 장애를 나눠서 볼 수 있다

## 검증 기준

- `api` 와 `mysql` 이 정상 상태로 수렴하는가
- ingress 경로 `/api`, `/health` 가 끊기지 않는가
- 앱 로그에 반복 치명 오류가 사라지는가
- 대표 health 기준이 정상인가

## Escalation 또는 롤백 기준

아래 중 하나면 즉시 공유 또는 롤백을 검토한다.

- `ImagePullBackOff` 또는 `CrashLoopBackOff` 가 계속됨
- `/health` 가 회복되지 않음
- DB 연결 실패가 반복됨
- ingress path 변경 직후 API 또는 health 가 동시에 깨짐

## 작업 후 기록

- `Application` 상태
- `/api`, `/health` 검증 결과
- `api`, `mysql`, ingress 확인 결과
- 최종 조치: 관찰, 추가 조사, 롤백
