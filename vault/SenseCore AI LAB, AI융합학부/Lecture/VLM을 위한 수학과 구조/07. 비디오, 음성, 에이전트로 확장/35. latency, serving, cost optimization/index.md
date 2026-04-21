---
title: "35. latency, serving, cost optimization"
source_kind: page
---
좋은 모델도 너무 느리거나 비싸면 실제 서비스에 쓰기 어렵습니다. 이 강의는 latency, serving, cost optimization이 VLM 설계에 미치는 영향을 설명합니다.

# 먼저 알아둘 말
- latency: 요청부터 응답까지 걸리는 시간입니다.
- serving: 모델을 실제 사용자 요청에 맞게 운영하는 일입니다.
- throughput: 단위 시간당 처리량입니다.
- cost optimization: 비용 대비 성능을 조정하는 전략입니다.

# 이 강의에서 답할 질문
- 왜 최고 성능 모델이 항상 최선의 선택이 아닌가
- serving은 단순 추론 호출과 무엇이 다른가
- latency와 cost는 어떤 구조 선택을 바꾸는가

# 왜 중요한가
- 비디오, OCR, agent는 토큰과 계산량이 많아 운영 비용이 급격히 커집니다.
- 제품 품질은 모델 품질과 시스템 속도 사이 균형 위에서 결정됩니다.

# 이번 강의의 핵심 축
- batching과 caching
- model size와 response time trade-off
- routing and fallback strategy
- product SLA 관점의 모델 선택

# 스스로 점검
1. serving이 중요한 이유를 설명하라.
2. latency와 cost가 architecture 선택에 미치는 영향을 말하라.
3. 최고 점수 모델이 항상 실서비스 최선이 아닌 이유를 설명하라.
