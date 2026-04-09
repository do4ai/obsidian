---
title: "papersens 배포 이상 대응 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98181a506fee4b158ad5a__70. 서비스별 운영 작업/children/338e313f58b981ab939ac19ea104bc05__papersens 배포 이상 대응 절차
notion_id: 338e313f58b981ab939ac19ea104bc05
notion_url: https://www.notion.so/338e313f58b981ab939ac19ea104bc05
parent_notion_id: 330e313f58b98181a506fee4b158ad5a
---
# papersens 배포 이상 대응 절차

## 문서 목적

이 문서는 `papersens` 서비스가 배포 후 정상 수렴하지 않거나, 대표 도메인 접근이 비정상일 때 따르는 상세 대응 절차를 정리한다.

공통 초기 대응은 `서비스 배포 이상 1차 대응 절차`를 먼저 적용하고, 이 문서에서는 `papersens`의 단일 앱 구조와 ingress 확인 포인트를 본다.

## 준비물

- `papersens` namespace 확인 권한
- `ArgoCD` 와 `kubectl` 확인 권한
- `papersens.do4ai.com` 또는 `*.ps.do4ai.com` 기준 URL
- 최근 변경 커밋 또는 배포 시각

## 먼저 확인할 운영 단위

- namespace: `papersens`
- 핵심 workload: `papersens` Deployment
- 핵심 ingress: `papersens-ingress`
- 먼저 볼 host/path: `papersens.do4ai.com`, `*.ps.do4ai.com`, `/`

## 절차

### 1. 공통 1차 대응 절차를 먼저 적용한다

먼저 아래를 확인한다.

1. `Application` 상태
2. namespace live 상태
3. 대표 로그

그 다음 `papersens` 특화 확인으로 내려간다.

### 2. 단일 deployment 수렴 여부를 먼저 본다

```bash
sudo kubectl get deploy,pods,svc,ing -n papersens
```

`papersens`는 핵심 앱이 단일 deployment 중심이므로 아래를 먼저 본다.

1. deployment replica 가 수렴하는가
2. pod 가 `Running` 또는 `Ready` 로 올라오는가
3. service 와 ingress 가 같이 살아 있는가

### 3. 앱 로그에서 startup 과 요청 실패를 본다

```bash
sudo kubectl logs deploy/papersens -n papersens --tail=100
```

먼저 보는 항목은 아래다.

- startup 실패
- 환경 변수 또는 secret 누락
- 외부 연동 실패
- 라우팅 또는 host 처리 오류

### 4. 대표 host 와 wildcard host 를 같이 확인한다

```bash
sudo kubectl describe ingress -n papersens papersens-ingress
sudo kubectl get svc -n papersens
```

아래를 확인한다.

1. `papersens.do4ai.com` 기준 host 가 정상인가
2. `*.ps.do4ai.com` wildcard host 가 기대한 대로 연결되는가
3. ingress backend 와 service port 가 어긋나지 않는가

### 5. 접근 장애가 앱 문제인지 ingress 문제인지 나눈다

아래 기준으로 먼저 분리한다.

- pod 와 service 는 정상인데 외부 접근만 안 된다: ingress 또는 host 문제 가능성
- pod 자체가 뜨지 않는다: 앱 기동 또는 설정 문제 가능성
- 특정 host 만 안 된다: wildcard 또는 host rule 문제 가능성

## 검증 기준

- `papersens` deployment 가 정상 수렴하는가
- 대표 host 와 wildcard host 가 기대한 경로로 응답하는가
- ingress 와 service 연결이 유지되는가
- 앱 로그에 반복 치명 오류가 남지 않는가

## Escalation 또는 롤백 기준

아래 중 하나면 즉시 공유 또는 롤백을 검토한다.

- deployment 가 계속 수렴하지 않음
- 대표 host 와 wildcard host 가 동시에 실패함
- ingress rule 변경 직후 외부 접근이 전면 실패함
- startup 실패 원인이 새 변경과 직접 연결됨

## 작업 후 기록

- `Application` 상태
- deployment, ingress, service 확인 결과
- 대표 host 와 wildcard host 검증 결과
- 최종 조치: 관찰, 추가 조사, 롤백
