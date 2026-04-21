---
title: "29. data filtering, verifier, retrieval grounding"
source_kind: page
---
hallucination 완화는 한 가지 방법으로 끝나지 않습니다. 이 강의는 data filtering, verifier, retrieval grounding이 각각 무엇을 줄이려 하는지 설명합니다.

# 먼저 알아둘 말
- data filtering: 학습 데이터의 오류나 노이즈를 줄이는 작업입니다.
- verifier: 생성된 답을 다시 점검하는 별도 판단기입니다.
- retrieval grounding: 외부 근거를 검색해 답을 지지하는 방식입니다.
- post-hoc check: 답변 생성 후에 다시 확인하는 절차입니다.

# 이 강의에서 답할 질문
- 데이터 정리만으로 줄일 수 있는 오류는 무엇인가
- verifier는 어떤 실패를 잡는가
- retrieval grounding은 어떤 과제에서 특히 효과적인가

# 왜 중요한가
- hallucination은 학습 시점과 추론 시점 모두에서 줄여야 합니다.
- 외부 근거를 붙이면 faithfulness를 높일 수 있지만 시스템 복잡도도 커집니다.

# 이번 강의의 핵심 축
- train-time mitigation과 inference-time mitigation
- verifier design의 한계
- retrieved evidence와 answer consistency
- system complexity trade-off

# 스스로 점검
1. data filtering의 역할을 설명하라.
2. verifier가 필요한 이유를 말하라.
3. retrieval grounding의 장단점을 설명하라.
