---
title: "15. representative VLM families 비교"
source_kind: page
---
이제까지 배운 표현, 정렬, connector 개념을 실제 모델 계열에 대입해 볼 차례입니다. 이 강의는 대표 VLM family를 정보 흐름 기준으로 비교합니다.

# 먼저 알아둘 말
- family: 유사한 설계 철학을 공유하는 모델 계열입니다.
- connector-heavy: 중간 연결기를 강하게 설계한 계열입니다.
- LM-centric: language model 중심으로 시각 정보를 붙이는 계열입니다.
- retrieval-leaning: 정렬과 검색 성격이 강한 계열입니다.

# 이 강의에서 답할 질문
- 모델 계열은 무엇을 우선순위로 두고 갈리는가
- 어떤 family가 OCR, 어떤 family가 chat, 어떤 family가 efficiency에 유리한가
- architecture choice를 공통 언어로 비교할 수 있는가

# 왜 중요한가
- 논문 이름을 외우기보다 family 단위로 정리해야 설계 선택의 본질이 보입니다.
- 실제 제품 선택도 family 특성을 알아야 현실적으로 할 수 있습니다.

# 이번 강의의 핵심 축
- alignment-first 계열
- connector-rich 계열
- decoder-only assistant 계열
- efficiency-oriented 계열

# 스스로 점검
1. representative VLM family를 구분하는 기준을 설명하라.
2. OCR 중심 과제에서 어떤 구조가 유리할지 말하라.
3. 모델 계열 비교를 정보 흐름 기준으로 설명하라.
