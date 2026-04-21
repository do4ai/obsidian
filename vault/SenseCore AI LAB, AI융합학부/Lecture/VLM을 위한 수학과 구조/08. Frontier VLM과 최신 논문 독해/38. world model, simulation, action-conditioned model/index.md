---
title: "38. world model, simulation, action-conditioned model"
source_kind: page
---
관찰만 하는 모델에서 한 걸음 더 나아가면, 행동 결과를 예측하는 모델이 필요해집니다. 이 강의는 world model과 action-conditioned model을 설명합니다.

# 먼저 알아둘 말
- world model: 관찰과 행동의 변화를 예측하는 내부 모델입니다.
- simulation: 가상의 환경에서 상호작용을 모사하는 과정입니다.
- action-conditioned model: 행동을 조건으로 다음 상태를 예측하는 모델입니다.
- rollout: 여러 단계 앞까지 예측을 전개하는 과정입니다.

# 이 강의에서 답할 질문
- world model은 VLM과 무엇이 다른가
- 왜 행동 조건이 붙으면 문제가 더 어려워지는가
- simulation은 어떤 학습 이점을 주는가

# 왜 중요한가
- agent와 robotics로 가면 perception만으로는 충분하지 않습니다.
- 미래 상태 예측 능력은 planning과 safer action에 중요합니다.

# 이번 강의의 핵심 축
- observation-only model과 action-aware model 차이
- rollout consistency
- planning-oriented representation
- embodied learning direction

# 스스로 점검
1. world model의 역할을 설명하라.
2. action-conditioned model이 필요한 이유를 말하라.
3. simulation이 학습에 주는 이점을 설명하라.
