---
title: "k3s 운영 장애 Discord 리포트 설계"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b9810a9075d5d9e176d8fd__70. 데이터, 관측, 보안/children/335e313f58b981149d2ecb7c4ad3df4a__k3s 운영 장애 Discord 리포트 설계
notion_id: 335e313f58b981149d2ecb7c4ad3df4a
notion_url: https://www.notion.so/335e313f58b981149d2ecb7c4ad3df4a
parent_notion_id: 330e313f58b9810a9075d5d9e176d8fd
---
# k3s 운영 장애 Discord 리포트 설계

## 목표

- 운영 장애가 발생하면 사람 손으로 대시보드를 먼저 열지 않아도 Discord 채널에서 1차 상황을 바로 읽을 수 있어야 한다.
- `k3s` 클러스터, GitOps 배포 상태, 앱 런타임, 로그 이상 징후를 한 채널 체계로 묶되 메시지 형식은 일관돼야 한다.
- 기존에 이미 구축된 `Prometheus`, `Alertmanager`, `ArgoCD Notifications`, `ELK`, `OTel`, `Tempo`를 최대한 재사용하고, 새 컴포넌트는 꼭 필요한 경우에만 얇게 추가한다.

## 현재 전제

현재 운영 클러스터에는 아래 구성요소가 이미 있다.

- 메트릭/알림: `kube-prometheus-stack`, `Prometheus`, `Alertmanager`, `Grafana`
- GitOps: `ArgoCD`, `argocd-notifications-controller`
- 로그/트레이스: `Elasticsearch`, `Kibana`, `Filebeat`, `OTel Gateway`, `Tempo`
- 앱: `do4i`, `palcar`, `papersens`, `namanva`

즉 "알림 판단 엔진"은 이미 일부 있다. 빠진 것은 아래다.

- Discord 채널로 보내는 공식 전송 경로
- 장애 심각도, 앱명, 링크를 통일한 메시지 규약
- 메트릭 기반 장애와 GitOps 장애를 한 운영 채널 모델로 묶는 정책
- 로그 기반 장애를 언제부터 포함할지에 대한 단계 구분

추가로 2026-03-29 공식 문서 리서치 기준으로 아래를 반영해야 한다.

- `Alertmanager` 는 현재 `Discord` native integration 을 공식 지원한다.
- `ArgoCD Notifications` 는 `webhook` 서비스로 Discord 또는 relay 호출이 가능하다.
- `Grafana OnCall OSS` 는 2026-03-24 archive 상태라 신규 도입 후보에서 제외하는 것이 맞다.

## 다뤄야 하는 장애 범위

1. 클러스터/인프라 장애
- 노드 `NotReady`
- 디스크/메모리 압박
- 핵심 infra pod 비정상 재시작

2. GitOps/배포 장애
- `ArgoCD Application` 이 `Degraded`, `Missing`, `SyncFailed`
- 배포 후 앱이 `Healthy` 로 수렴하지 않음

3. 앱 런타임 장애
- Deployment available replica 부족
- CrashLoopBackOff
- HTTP 5xx, latency 급증

4. 로그 이상 징후
- 특정 앱에서 `error`, `exception`, `traceback` 폭증
- 인증, DB 연결, 외부 API 실패 패턴 반복

## 옵션 비교

| 옵션 | 구성 | 장점 | 한계 | 적합도 |
| --- | --- | --- | --- | --- |
| A | `Alertmanager -> Discord` 직접 전송만 사용 | 기존 메트릭 알림을 가장 빨리 붙일 수 있고 현재는 공식 native 지원이 있음 | GitOps 이벤트와 로그 이벤트 포맷이 분리되고, Discord 전용 템플릿 통일이 약함 | 보조 옵션 |
| B | `Alertmanager + ArgoCD Notifications + 얇은 Discord relay` | 기존 스택을 재사용하면서 메시지 포맷, severity, 링크를 한곳에서 통일 가능 | relay를 새로 하나 운영해야 함 | 권장 |
| C | B + `ElastAlert2` 같은 로그 룰 엔진 추가 | 로그 폭증과 에러 패턴까지 같은 채널로 편입 가능 | 룰 튜닝과 오탐 억제가 필요함 | 2단계 권장 |
| D | 새 incident aggregator 서비스가 모든 이벤트를 직접 수집 | 장기적으로 가장 유연함 | 지금 시점에는 과설계이고 구현량이 큼 | 장기 후보 |

## 권장안

현재 기준 권장안은 `옵션 B`를 1단계 기본안으로 잡고, 로그 이상 징후는 `옵션 C`로 2단계 확장하는 방식이다.

### 1단계: 기존 스택 재사용 + 얇은 relay

- `Alertmanager`가 인프라/앱 메트릭 알림을 발생시킨다.
- `ArgoCD Notifications`가 `Application` 상태 이상 이벤트를 발생시킨다.
- 둘 다 Discord webhook으로 바로 보내지 않고, 작은 `discord-relay` HTTP endpoint 하나로 먼저 보낸다.
- relay가 공통 메시지 템플릿으로 변환한 뒤 Discord 채널로 게시한다.

이 구성을 권장하는 이유는 아래와 같다.

- `Alertmanager`와 `ArgoCD Notifications` 는 입력 포맷이 다르다.
- Discord webhook은 단순 문자열보다 embed 형식이 운영성이 좋다.
- 앱명, namespace, severity, source, runbook link를 통일하려면 중간 변환 계층이 있는 편이 낫다.
- 새로 추가되는 컴포넌트가 "전송 포맷 정규화" 하나에만 집중하면 운영 부담이 낮다.

### 2단계: 로그 기반 장애 편입

- `Elasticsearch/Kibana` 자체 alerting에 바로 의존하지 않는다.
- 이유: 라이선스/기능 제약과 운영 복잡도를 초기에 같이 안고 갈 필요가 없다.
- 로그 이상 징후는 `ElastAlert2` 같은 룰 엔진을 별도로 붙이거나, 장기적으로 OTel/Prometheus 지표화 방식으로 흡수한다.

즉 초기에는 아래 순서를 권장한다.

1. 메트릭/인프라 장애
2. GitOps/배포 장애
3. 로그 기반 장애

## Discord 메시지 계약

모든 알림 메시지는 최소한 아래 필드를 공통으로 가져야 한다.

- `severity`: `critical`, `high`, `warning`, `info`
- `status`: `firing`, `resolved`
- `source`: `alertmanager`, `argocd`, `log-rule`
- `cluster`: `do4ai-prod-k3s` 같은 운영 식별자
- `namespace`
- `app`
- `summary`: 한 줄 요약
- `evidence`: 첫 근거 1~3개
- `started_at`
- `dashboard_links`: Grafana, Kibana, ArgoCD, Headlamp, Runbook

예시 메시지 형태는 아래 수준이 적절하다.

```text
[critical][argocd] do4i 배포 수렴 실패
- cluster: do4ai-prod-k3s
- namespace: do4i
- app: do4i
- symptom: Application Health=Degraded, Sync Status=OutOfSync
- evidence: deployment/api availableReplicas=0
- links: ArgoCD / Headlamp / Runbook
```

## 채널 운영안

- `#ops-incidents`
  - `critical`, `high`
  - 실제 장애성 이벤트만 보낸다.
- `#ops-deploy`
  - 배포 실패, sync 실패, drift 관련 알림
- `#ops-observability`
  - 로그 경고, 성능 저하, 탐지 튜닝 결과

초기에는 채널을 너무 많이 쪼개지 말고, 최소 2개 또는 3개로 시작하는 편이 낫다.

## 이벤트 소스별 역할

### Alertmanager

담당 범위:

- node/pod/deployment health
- resource pressure
- HTTP error/latency 같은 서비스 SLI

장점:

- 이미 클러스터에 있음
- `PrometheusRule` 로 선언형 관리가 가능함

### ArgoCD Notifications

담당 범위:

- sync 실패
- health degrade
- app missing

장점:

- 이미 컨트롤러가 있음
- GitOps 실패를 메트릭 알림과 별도로 즉시 잡을 수 있음

### Discord relay

담당 범위:

- 서로 다른 이벤트 payload를 Discord 전용 메시지로 통일
- severity 매핑
- 링크 조합
- dedup key 계산

새 컴포넌트지만 책임을 작게 유지해야 한다.

## 비목표

- Discord를 PagerDuty 대체제로 바로 쓰는 것
- 사람이 조치한 상태를 양방향으로 Discord에서 다시 반영하는 것
- 모든 로그 라인을 즉시 알림으로 보내는 것

초기 목표는 "운영 장애를 사람이 늦지 않게 인지하는 것"이지 "완전한 incident platform"이 아니다.

## 단계별 실행 계획

### Phase 1

- Discord 채널 구조 확정
- webhook secret 저장 위치 확정
- `Alertmanager -> relay -> Discord`
- `ArgoCD Notifications -> relay -> Discord`
- 공통 메시지 템플릿 확정

### Phase 2

- 앱별 핵심 장애 룰 정리
- `do4i`, `palcar`, `papersens`, `namanva` 우선 적용
- resolved 메시지 정책과 노이즈 억제 정책 추가

### Phase 3

- 로그 기반 장애 룰 추가
- runbook deep link 자동 생성
- 장애 fingerprint 기준 dedup, thread reply, ack 표시 검토

## 결정이 필요한 항목

- Discord 채널을 하나로 시작할지, `incident/deploy/observability` 로 나눌지
- relay를 새 Deployment로 둘지, ArgoCD Notifications webhook template만으로 1차 시작할지
- 로그 이상 징후를 1단계에 넣을지, 2단계 이후로 미룰지
- 앱별 `critical/high/warning` 기준을 어디까지 명시할지

## 현재 제안 결론

아래 순서가 가장 현실적이다.

1. `Alertmanager` 와 `ArgoCD Notifications` 를 먼저 Discord 채널에 연결한다.
2. 메시지 일관성을 위해 얇은 `discord-relay` 를 하나 둔다.
3. 로그 기반 장애는 `ElastAlert2` 또는 지표화 방식으로 2단계에 편입한다.

즉 "기존 k3s 스택 재사용 + 아주 작은 신규 relay 추가"가 현재 최적안이다.
