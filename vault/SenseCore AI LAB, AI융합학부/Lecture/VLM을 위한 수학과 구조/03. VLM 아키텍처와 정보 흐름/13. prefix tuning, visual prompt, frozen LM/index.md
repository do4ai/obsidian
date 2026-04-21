---
title: "13. prefix tuning, visual prompt, frozen LM"
source_kind: page
---
대형 language model을 최대한 유지하면서 시각 능력만 덧붙이고 싶을 때 prefix tuning과 visual prompt 전략이 등장합니다. 이 강의는 frozen LM 위 멀티모달 적응 방법을 설명합니다.

# 먼저 알아둘 말
- prefix tuning: 입력 앞부분에 학습 가능한 프리픽스를 붙이는 방식입니다.
- visual prompt: 시각 정보를 프롬프트처럼 주입하는 방식입니다.
- frozen LM: 언어모델 본체를 고정한 상태입니다.
- parameter efficiency: 적은 추가 파라미터로 적응하는 성질입니다.

# 이 강의에서 답할 질문
- LM을 고정하면 무엇을 얻고 무엇을 잃는가
- visual prompt는 어떤 정보를 전달하는가
- prefix 기반 적응은 언제 유리한가

# 왜 중요한가
- 실무에서는 거대한 LM을 전부 다시 학습하기 어렵습니다.
- 가벼운 적응 전략은 빠른 프로토타이핑과 비용 절감에 유리합니다.

# 이번 강의의 핵심 축
- prompt-like control과 structured connector의 차이
- frozen backbone/frozen LM 조합
- parameter-efficient adaptation의 장단점
- prompt 전략이 grounding에 미치는 한계

# 스스로 점검
1. frozen LM 전략의 장점을 설명하라.
2. visual prompt가 무엇을 하는지 말하라.
3. prefix tuning의 한계를 설명하라.
