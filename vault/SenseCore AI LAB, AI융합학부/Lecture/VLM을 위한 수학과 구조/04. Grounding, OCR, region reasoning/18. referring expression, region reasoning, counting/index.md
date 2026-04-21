---
title: "18. referring expression, region reasoning, counting"
source_kind: page
---
“왼쪽 사람 뒤의 빨간 가방”처럼 복합 참조가 들어가면 VLM은 위치, 속성, 관계를 한꺼번에 추적해야 합니다. 이 강의는 referring expression과 region reasoning, counting을 묶어서 설명합니다.

# 먼저 알아둘 말
- referring expression: 특정 객체나 영역을 가리키는 언어 표현입니다.
- region reasoning: 특정 영역들 사이의 관계를 추론하는 문제입니다.
- counting: 객체 수를 세는 문제입니다.
- compositional query: 여러 조건이 결합된 질의입니다.

# 이 강의에서 답할 질문
- referring expression은 왜 단순 분류보다 어려운가
- counting은 무엇 때문에 자주 틀리는가
- region reasoning은 어떤 형태의 attention을 요구하는가

# 왜 중요한가
- 이 과제들은 VLM이 진짜로 “보고 있는지”를 드러내는 시험대입니다.
- compositional grounding 실패는 chat-style 모델에서 매우 흔한 오류 원인입니다.

# 이번 강의의 핵심 축
- 객체, 속성, 관계의 결합
- multi-step grounding
- counting과 duplicate confusion
- compositional reasoning의 난점

# 스스로 점검
1. referring expression이 어려운 이유를 설명하라.
2. counting 오류가 생기는 이유를 말하라.
3. region reasoning과 global captioning의 차이를 설명하라.
