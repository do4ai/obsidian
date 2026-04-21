---
title: "27. hallucination taxonomy와 faithfulness"
source_kind: page
---
모든 hallucination이 같은 것은 아닙니다. 이 강의는 hallucination taxonomy를 정리하고, faithfulness를 별도의 기준으로 설명합니다.

# 먼저 알아둘 말
- taxonomy: 오류를 유형별로 나누는 체계입니다.
- object hallucination: 없는 객체를 있다고 말하는 오류입니다.
- relation hallucination: 관계를 잘못 말하는 오류입니다.
- faithfulness: 설명과 답이 실제 입력 근거를 충실히 반영하는 정도입니다.

# 이 강의에서 답할 질문
- hallucination은 어떤 유형으로 나눌 수 있는가
- faithfulness는 정답성과 어떻게 다른가
- 왜 설명이 길어도 faithful하지 않을 수 있는가

# 왜 중요한가
- 오류를 제대로 나눠야 완화 전략도 제대로 세울 수 있습니다.
- 제품에서는 정답성뿐 아니라 근거 충실성이 사용자 신뢰를 좌우합니다.

# 이번 강의의 핵심 축
- object/relation/attribute hallucination
- answer correctness와 evidence faithfulness 차이
- rationale mismatch 문제
- taxonomy가 디버깅에 주는 이점

# 스스로 점검
1. hallucination 유형을 두 가지 이상 설명하라.
2. faithfulness와 정답성의 차이를 말하라.
3. taxonomy가 왜 필요한지 설명하라.
