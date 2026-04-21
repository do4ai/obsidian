---
title: "문제 해설 - 03. VLM 아키텍처와 정보 흐름"
source_kind: page
---
이 해설 페이지는 VLM 구조를 읽는 기준이 생겼는지 점검하는 페이지입니다. 이름이 아니라 fusion point와 connector, token flow를 먼저 볼 수 있어야 합니다.

# 이 해설 페이지의 역할
- encoder-decoder와 decoder-only 구조 차이를 다시 정리하게 합니다.
- Q-Former와 resampler, prompt 전략을 비교하게 합니다.
- 실제 모델 family를 정보 흐름 기준으로 해석하게 합니다.

# 문제를 풀 때 확인할 것
- vision token이 language model 안으로 들어가는 경로를 설명할 수 있는가
- frozen LM 전략의 장단점을 말할 수 있는가
- token compression이 계산량과 grounding에 미치는 영향을 정리할 수 있는가

# 연결 복습
- 이 단계가 확실해야 4단계 grounded reasoning과 7단계 agent 확장을 구조적으로 읽을 수 있습니다.
