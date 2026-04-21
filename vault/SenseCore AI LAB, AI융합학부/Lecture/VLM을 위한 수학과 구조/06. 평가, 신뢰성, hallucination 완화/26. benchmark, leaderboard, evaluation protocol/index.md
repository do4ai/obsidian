---
title: "26. benchmark, leaderboard, evaluation protocol"
source_kind: page
---
점수표는 많지만, 무엇을 정말 측정하는지는 따로 읽어야 합니다. 이 강의는 benchmark, leaderboard, evaluation protocol을 비판적으로 읽는 기준을 설명합니다.

# 먼저 알아둘 말
- benchmark: 모델 비교를 위한 표준 평가 세트입니다.
- leaderboard: 점수를 순위로 보여 주는 표입니다.
- evaluation protocol: 평가 절차와 조건을 정한 규칙입니다.
- leakage: 학습과 평가가 의도치 않게 섞이는 현상입니다.

# 이 강의에서 답할 질문
- 같은 점수라도 왜 다른 의미를 가질 수 있는가
- protocol이 바뀌면 결과 해석은 어떻게 달라지는가
- benchmark만으로 보이지 않는 품질은 무엇인가

# 왜 중요한가
- VLM은 데이터 중복, prompt 설정, decoding 정책에 따라 점수가 크게 달라질 수 있습니다.
- protocol을 읽지 않으면 잘못된 비교를 하게 됩니다.

# 이번 강의의 핵심 축
- task definition과 metric alignment
- closed-set vs open-ended evaluation
- prompt sensitivity와 scoring ambiguity
- leaderboard reading habit

# 스스로 점검
1. benchmark와 protocol의 차이를 설명하라.
2. leaderboard 점수만으로 부족한 이유를 말하라.
3. evaluation leakage가 왜 문제인지 설명하라.
