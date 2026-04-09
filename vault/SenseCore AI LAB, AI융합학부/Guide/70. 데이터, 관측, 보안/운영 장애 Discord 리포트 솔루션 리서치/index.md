---
title: "운영 장애 Discord 리포트 솔루션 리서치"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b9810a9075d5d9e176d8fd__70. 데이터, 관측, 보안/children/335e313f58b981eea14ede3a1fd33ed2__운영 장애 Discord 리포트 솔루션 리서치
notion_id: 335e313f58b981eea14ede3a1fd33ed2
notion_url: https://www.notion.so/335e313f58b981eea14ede3a1fd33ed2
parent_notion_id: 330e313f58b9810a9075d5d9e176d8fd
---
# 운영 장애 Discord 리포트 솔루션 리서치

기준일: 2026-03-29  
기준 환경: 현재 운영 중인 `k3s` 클러스터와 이미 배포된 `Prometheus`, `Alertmanager`, `ArgoCD Notifications`, `Elasticsearch`, `Kibana`, `Filebeat`, `OTel`, `Tempo`

## 리서치 목표

- 이미 있는 운영 스택을 최대한 재사용하면서 Discord 채널로 운영 장애를 신뢰성 있게 리포트할 수 있는지 확인한다.
- 단순 전송이 아니라 장기적으로 dedup, correlation, ack, resolved 흐름까지 확장 가능한지 본다.
- 운영성이 떨어지거나 이미 수명 종료 단계인 솔루션은 초기에 제외한다.

## 최신 확인 요약

1. `Prometheus Alertmanager` 는 현재 공식 문서에서 `Discord` 를 네이티브 notification integration 으로 지원한다.
2. `ArgoCD Notifications` 는 Discord 전용 서비스는 아니지만 공식 `webhook` 서비스로 Discord webhook 또는 중간 relay 호출이 가능하다.
3. `ElastAlert2` 는 공식 문서에서 Discord alerter 를 지원한다.
4. `Alerta` 는 Alertmanager 등 여러 소스의 alert를 받아 correlate, deduplicate, suppress 하는 상태 기반 aggregator 로 공식 문서가 살아 있다.
5. `Grafana OnCall OSS` 는 2025-03-11 maintenance mode 진입 후 2026-03-24 archive 상태라 새 투자 대상으로는 부적합하다.

## 후보별 정리

## 1. Prometheus Alertmanager native Discord

### 확인 내용

- Prometheus 공식 integration 문서에 `Discord | discord_config` 가 명시돼 있다.
- Alertmanager 공식 configuration 문서에 `discord_configs` 와 `discord_config` 가 있다.
- 현재 문서 기준 `send_resolved` 기본값은 `true` 다.
- `webhook_url`, `title`, `message`, `content`, `username`, `avatar_url`, `http_config` 를 조정할 수 있다.

### 장점

- 현재 클러스터에 Alertmanager가 이미 있으므로 구현 비용이 가장 낮다.
- 메트릭 기반 운영 장애는 추가 컴포넌트 없이 바로 Discord 로 보낼 수 있다.
- resolved 메시지까지 기본 지원한다.

### 한계

- 인프라/앱 메트릭 경보만 자연스럽다.
- ArgoCD, 로그 알림과 포맷 및 dedup 정책을 통일하려면 별도 설계가 필요하다.
- incident 상태 저장, ack, correlation 은 Alertmanager 자체의 역할이 아니다.

### 결론

- `1차 즉시 적용` 후보로 매우 강하다.
- 단, 이것만으로 전체 incident system 이 되지는 않는다.

## 2. ArgoCD Notifications webhook

### 확인 내용

- ArgoCD 공식 문서는 `webhook` 서비스를 지원한다.
- `argocd-notifications-cm` 에 `service.webhook.<name>` 을 등록하고, 템플릿에서 `method`, `path`, `body` 를 정의할 수 있다.
- App annotation 으로 trigger subscribe 도 가능하다.

### 장점

- 현재 클러스터에 `argocd-notifications-controller` 가 이미 있다.
- GitOps 실패, degraded, sync failure 는 Alertmanager 보다 ArgoCD 쪽이 더 직접적인 근거를 가진다.
- Discord webhook 직접 호출도 가능하고, relay 호출도 가능하다.

### 한계

- Discord 전용 풍부한 메시지 계약은 직접 템플릿을 설계해야 한다.
- 상태 저장이나 incident dedup 은 없다.

### 결론

- `배포/수렴 장애` 리포트의 기본 소스로 적합하다.
- Alertmanager 와 함께 써야 운영 그림이 맞다.

## 3. ElastAlert2 for Elasticsearch logs

### 확인 내용

- ElastAlert2 공식 문서는 Discord alerter 를 제공한다.
- `discord_webhook_url` 이 필수고, embed color/footer/icon 같은 옵션이 있다.

### 장점

- 현재 ELK 위에 로그 패턴 기반 경보를 빠르게 붙일 수 있다.
- 특정 앱의 `error`, `traceback`, DB 연결 실패, auth 실패 burst 룰을 선언형으로 추가하기 쉽다.

### 한계

- 룰 품질이 나쁘면 오탐이 많아진다.
- 메트릭/배포 이벤트와 상태가 분리된다.
- 본질적으로는 "로그 알림 엔진"이지 incident manager 는 아니다.

### 결론

- `2단계 로그 알림` 용도로 적합하다.
- 초기 단계 핵심 경로보다는 후순위가 맞다.

## 4. Alerta as incident aggregator

### 확인 내용

- Alerta 공식 문서는 여러 소스의 alert 를 받아 `correlates`, `de-duplicates`, `suppresses` 한다고 설명한다.
- Alertmanager webhook integration 이 공식 문서에 있다.
- post-receive hook 과 status change hook 을 통한 외부 통합도 지원한다.

### 장점

- 단순 전송이 아니라 상태 기반 alert/incident 집계 계층 역할을 할 수 있다.
- 장기적으로 ack, blackout, suppress, bi-directional workflow 로 갈 수 있다.
- "소스는 많고 채널은 하나" 인 운영 모델에 잘 맞는다.

### 한계

- 새 서비스를 추가 운영해야 한다.
- Discord는 기본 목적지라기보다 hook/plugin 확장 쪽에 가깝다.
- 초기 구축 난이도는 relay 보다 높다.

### 결론

- `이상적인 중장기 OSS 집계 계층` 후보로 가장 의미가 있다.
- 하지만 지금 당장 붙이기엔 relay 보다 무겁다.

## 5. Grafana OnCall OSS

### 확인 내용

- Grafana 공식 문서에 따르면 2025-03-11 maintenance mode 진입, 2026-03-24 archive 라고 명시돼 있다.

### 결론

- 현재 날짜 2026-03-29 기준으로 신규 도입 후보에서 제외하는 것이 맞다.

## 비교 표

| 솔루션 | 공식 지원 상태 | 현재 스택 재사용성 | Discord 직접 전송 | 상태 집계/중복 제거 | 권장 단계 |
| --- | --- | --- | --- | --- | --- |
| Alertmanager native Discord | 높음 | 매우 높음 | 가능 | 낮음 | Phase 1 |
| ArgoCD Notifications webhook | 높음 | 매우 높음 | 가능 | 낮음 | Phase 1 |
| ElastAlert2 | 높음 | 높음 | 가능 | 낮음 | Phase 2 |
| Alerta | 높음 | 중간 | hook/plugin 설계 필요 | 높음 | Phase 2~3 |
| Grafana OnCall OSS | 비권장 | 중간 | 가능 | 높음 | 제외 |

## 현재 시점 권장안

현실적인 권장안은 아래 두 레이어다.

### 단기 권장안

- `Alertmanager -> Discord`
- `ArgoCD Notifications -> Discord 또는 relay`

이 단계에서는 새 운영 컴포넌트를 최소화하고, 현재 클러스터에 이미 있는 기능부터 붙인다.

### 중기 권장안

- `ElastAlert2` 로 로그 장애 룰 추가
- 필요 시 `Alerta` 또는 자체 `incident-gateway` 를 넣어 dedup/correlation 계층으로 승격

즉 "지금 바로 붙일 것" 과 "나중에 incident system 으로 커질 것" 을 분리해야 한다.

## 연구 결론

2026-03-29 시점 기준으로 가장 타당한 결론은 아래다.

1. 메트릭과 GitOps 장애는 현재 스택만으로도 Discord 전송이 가능하다.
2. 로그 장애는 `ElastAlert2` 가 가장 현실적인 추가 후보다.
3. 장기적으로는 `Alertmanager + ArgoCD + ElastAlert2` 의 출력을 `Alerta` 또는 자체 incident gateway 로 모으는 구조가 가장 이상적이다.
4. `Grafana OnCall OSS` 는 현재 시점 신규 후보에서 제외한다.

## 사용한 공식 소스

- Prometheus Notification Integrations
- Prometheus Alertmanager Configuration
- Argo CD Notifications Services Overview
- Argo CD Notifications Webhook Service
- ElastAlert2 Alerts Documentation
- Alerta Server & API
- Alerta Integrations & Plugins
- Grafana OnCall OSS documentation and maintenance notice
