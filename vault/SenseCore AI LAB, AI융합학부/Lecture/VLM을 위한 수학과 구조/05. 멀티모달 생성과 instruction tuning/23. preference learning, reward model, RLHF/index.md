---
title: "23. preference learning, reward model, RLHF"
source_kind: page
---
정답 하나만 정해지기 어려운 멀티모달 응답에서는 사람 선호가 중요합니다. 이 강의는 preference learning, reward model, RLHF를 멀티모달 맥락에서 설명합니다.

# 먼저 알아둘 말
- preference learning: 여러 응답 중 더 좋은 응답을 고르게 해 학습하는 방식입니다.
- reward model: 응답 품질을 점수로 근사하는 모델입니다.
- RLHF: 사람 선호를 강화학습으로 반영하는 방식입니다.
- policy: 모델이 응답을 선택하는 행동 규칙입니다.

# 이 강의에서 답할 질문
- 사람 선호는 왜 추가로 필요한가
- reward model은 무엇을 근사하는가
- RLHF는 멀티모달에서 무엇이 더 어려운가

# 왜 중요한가
- 같은 정답이라도 더 grounded하고 더 안전하고 더 유용한 답이 있을 수 있습니다.
- 멀티모달 assistant는 언어 품질과 시각 근거성을 함께 봐야 합니다.

# 이번 강의의 핵심 축
- pairwise preference 비교
- reward shaping의 위험
- visual evidence를 포함한 선호 판단
- policy optimization과 distribution shift

# 스스로 점검
1. preference learning이 필요한 이유를 설명하라.
2. reward model의 역할을 말하라.
3. RLHF가 멀티모달에서 어려운 이유를 설명하라.
