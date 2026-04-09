---
title: "do4i 배포 이상 대응 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98181a506fee4b158ad5a__70. 서비스별 운영 작업/children/338e313f58b981c4993dc26c50d26040__do4i 배포 이상 대응 절차
notion_id: 338e313f58b981c4993dc26c50d26040
notion_url: https://www.notion.so/338e313f58b981c4993dc26c50d26040
parent_notion_id: 330e313f58b98181a506fee4b158ad5a
---
# do4i 배포 이상 대응 절차

## 문서 목적

이 문서는 `do4i` 서비스가 배포 후 정상 수렴하지 않거나, 대표 기능이 비정상일 때 따르는 상세 대응 절차를 정리한다.

공통 판단은 `서비스 배포 이상 1차 대응 절차`를 먼저 따르고, 이 문서에서는 `do4i`에 특화된 리소스와 검증 지점을 본다.

## 준비물

- `do4i` namespace 확인 권한
- `ArgoCD` 와 `kubectl` 확인 권한
- `agents.do4i.com/api` 또는 `admin.do4ai.com/api` 기준 URL
- 최근 변경 커밋 또는 배포 시각

## 먼저 확인할 운영 단위

- namespace: `do4i`
- 핵심 workload: `api` Deployment, `mysql` StatefulSet
- 핵심 ingress: `api-ingress`
- 먼저 볼 host/path: `agents.do4i.com/api`, `admin.do4ai.com/api`

## 절차

### 1. 공통 1차 대응 절차를 먼저 적용한다

아래를 먼저 끝낸다.

1. `Application` 상태 확인
2. namespace live 상태 확인
3. 대표 로그 확인

그 다음부터 `do4i` 특화 확인으로 내려간다.

### 2. `api` 와 `mysql` 관계를 먼저 본다

```bash
sudo kubectl get deploy,sts,pods,svc,ing -n do4i
```

아래를 우선 확인한다.

1. `api` Deployment 가 replica 부족 상태인가
2. `mysql` StatefulSet 이 정상 기동 중인가
3. `api` 는 떴지만 DB 연결 때문에 readiness가 깨진 것은 아닌가

`do4i`는 앱과 DB가 같이 흔들릴 수 있으므로 `api`만 보고 끝내면 안 된다.

### 3. `api` 로그에서 시작 실패 원인을 본다

```bash
sudo kubectl logs deploy/api -n do4i --tail=100
```

먼저 보는 키워드는 아래다.

- DB 연결 실패
- 환경 변수 누락
- secret 누락
- migration 또는 startup 실패

### 4. ingress 와 backend 연결을 확인한다

```bash
sudo kubectl describe ingress -n do4i api-ingress
sudo kubectl get svc -n do4i
```

아래를 확인한다.

1. ingress host 가 `agents.do4i.com` 또는 `admin.do4ai.com` 기준과 맞는가
2. path 가 `/api` 로 연결되는가
3. ingress backend service 와 port 가 어긋나지 않는가

### 5. DB 쪽 이상 여부를 분리한다

`api` 가 뜨지 않거나 readiness가 회복되지 않으면 `mysql` 쪽 상태를 함께 본다.

```bash
sudo kubectl get pods -n do4i
sudo kubectl logs statefulset/mysql -n do4i --tail=100
```

아래 중 무엇인지 분리한다.

- 앱 설정 문제
- DB 기동 문제
- 앱과 DB 간 연결 문제

## 검증 기준

- `api` pod 가 재시작 루프 없이 수렴하는가
- `mysql` 이 정상 상태를 유지하는가
- ingress 와 service 연결이 유지되는가
- 대표 `/api` 진입점이 응답하는가

## Escalation 또는 롤백 기준

아래 중 하나면 즉시 공유 또는 롤백을 검토한다.

- `api` 와 `mysql` 이 동시에 비정상
- DB 연결 실패가 반복되어 `api` 가 계속 재시작
- ingress 는 정상인데 앱이 대표 API 응답을 못 함
- 직전 배포 변경이 원인이라는 근거가 명확함

## 작업 후 기록

- 확인한 `Application` 상태
- `api` 와 `mysql` 상태
- ingress, service, 대표 URL 검증 결과
- 최종 조치: 관찰, 추가 조사, 롤백
