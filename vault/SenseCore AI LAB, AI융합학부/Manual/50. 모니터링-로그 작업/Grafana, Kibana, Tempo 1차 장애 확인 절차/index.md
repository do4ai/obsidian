---
title: "Grafana, Kibana, Tempo 1차 장애 확인 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98117b6efd664ee0f6659__50. 모니터링-로그 작업/children/338e313f58b981cb9d17f7c61b7d1d0c__Grafana, Kibana, Tempo 1차 장애 확인 절차
notion_id: 338e313f58b981cb9d17f7c61b7d1d0c
notion_url: https://www.notion.so/338e313f58b981cb9d17f7c61b7d1d0c
parent_notion_id: 330e313f58b98117b6efd664ee0f6659
---
# Grafana, Kibana, Tempo 1차 장애 확인 절차

## 문서 목적

이 문서는 서비스 장애가 의심될 때 `Grafana`, `Kibana`, `Tempo`를 이용해 1차 근거를 빠르게 수집하는 절차를 정리한다.

초기 목표는 원인을 완전히 확정하는 것이 아니라, 메트릭 문제인지 로그 문제인지 추적 문제인지 먼저 좁히는 것이다.

## 준비물

- 대상 서비스 이름과 namespace
- 대략적인 장애 시작 시각
- 관련 URL, API path, 또는 job 이름
- Grafana, Kibana, Tempo 접근 권한

## 절차

### 1. 장애 시간 범위를 먼저 고정한다

1. 장애 제보 시각을 메모한다.
2. 시간 범위를 최소 `전후 15분` 으로 잡는다.
3. 서비스명, namespace, endpoint를 함께 적는다.

시간 범위를 안 잡고 바로 화면을 열면 unrelated noise가 많이 섞인다.

### 2. Grafana에서 메트릭 이상 여부를 본다

먼저 아래를 확인한다.

1. error rate 증가 여부
2. latency 증가 여부
3. pod restart 또는 resource pressure 여부
4. deployment replica 부족 여부

메트릭이 먼저 이상하면 앱 런타임 또는 인프라 문제일 가능성이 높다.

### 3. Kibana에서 같은 시간대 로그를 확인한다

로그 조회 기준은 아래다.

- namespace
- app 또는 pod 이름
- 장애 시간 범위
- `error`, `exception`, `traceback`, `timeout`, `connection` 같은 핵심 키워드

로그를 볼 때는 한 줄 에러만 보지 말고 직전/직후 로그까지 같이 읽는다.

### 4. Tempo에서 trace 또는 요청 흐름을 본다

추적이 가능한 서비스라면 아래를 확인한다.

1. 특정 요청이 어디서 지연됐는가
2. 외부 API 또는 DB 호출 구간이 길어졌는가
3. 오류가 특정 span에서 반복되는가

trace가 없다고 바로 결론 내리지 말고, 로그와 메트릭에서 이미 충분한 근거가 있는지도 같이 본다.

### 5. `kubectl` 결과와 교차 검증한다

```bash
sudo kubectl get pods -n <namespace>
sudo kubectl logs deploy/<deploy-name> -n <namespace> --tail=100
```

관측 도구 화면과 live 상태가 같은 방향을 가리키는지 확인한다.

## 판정 기준

### 메트릭만 이상할 때

- resource pressure, replica 부족, readiness 문제를 먼저 의심한다.

### 로그만 이상할 때

- 코드 오류, 외부 연동 실패, 환경 변수 또는 secret 문제를 먼저 의심한다.

### trace에서 외부 호출 지연이 보일 때

- 애플리케이션 내부보다 외부 의존성 병목 가능성을 먼저 본다.

## Escalation 기준

아래 중 하나면 즉시 운영 채널에 근거와 함께 공유한다.

- 복수 서비스가 동시에 느려짐
- namespace 전체 pod 상태가 비정상
- DB 연결 실패나 인증 실패가 반복됨
- 에러율과 지연이 함께 급증함

## 작업 후 기록

- 본 시간 범위
- 확인한 대시보드와 검색 조건
- 가장 강한 근거 3개
- 1차 판정: 앱, 인프라, 외부 의존성, 미확정 중 무엇인지
