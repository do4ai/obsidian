---
title: "12. cross-attention, perceiver resampler, Q-Former"
source_kind: page
---
vision token을 모두 language model에 넣는 것은 계산량이 너무 큽니다. 이 강의는 cross-attention, perceiver resampler, Q-Former가 이를 어떻게 해결하는지 설명합니다.

# 먼저 알아둘 말
- cross-attention: 한 모달의 query가 다른 모달의 key/value를 읽는 attention입니다.
- resampler: 많은 입력 토큰을 더 작은 표현으로 압축하는 모듈입니다.
- Q-Former: 학습 가능한 query token으로 시각 정보를 압축하는 구조입니다.
- bottleneck token: 제한된 수의 압축 토큰입니다.

# 이 강의에서 답할 질문
- 왜 vision token을 압축해야 하는가
- cross-attention은 어떤 정보를 골라 가져오는가
- Q-Former는 projector보다 무엇을 더 하려고 하는가

# 왜 중요한가
- connector 설계는 계산량, grounding, long-context 처리 능력을 동시에 바꿉니다.
- 많은 현대 VLM의 차이는 이 중간 연결기에서 생깁니다.

# 이번 강의의 핵심 축
- selection versus projection
- learnable query의 의미
- token compression과 information bottleneck
- grounded reasoning과 connector 품질의 관계

# 스스로 점검
1. cross-attention의 역할을 설명하라.
2. Q-Former가 필요한 이유를 말하라.
3. resampler가 계산량과 정보 품질에 어떤 영향을 주는지 설명하라.
