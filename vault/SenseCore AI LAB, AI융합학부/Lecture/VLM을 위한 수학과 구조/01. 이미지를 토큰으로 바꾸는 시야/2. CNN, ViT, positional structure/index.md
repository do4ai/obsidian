---
title: "2. CNN, ViT, positional structure"
source_kind: page
---
같은 이미지를 보더라도 CNN과 ViT는 서로 다른 방식으로 시각 구조를 읽습니다. 이 강의에서는 locality bias와 attention 기반 interaction, positional structure의 차이를 비교합니다.

# 먼저 알아둘 말
- convolution: 지역 가중치 공유를 사용하는 연산입니다.
- self-attention: 토큰 간 관계를 직접 계산하는 연산입니다.
- positional structure: 위치 정보를 표현 안에 반영하는 방식입니다.
- inductive bias: 모델이 기본적으로 선호하는 구조적 가정입니다.

# 이 강의에서 답할 질문
- CNN과 ViT는 무엇을 다르게 잘하는가
- 위치 정보는 왜 별도로 다뤄야 하는가
- backbone 선택이 downstream VLM에 어떤 영향을 주는가

# 왜 중요한가
- OCR, grounding, counting처럼 세밀한 시각 과제에서는 backbone의 inductive bias 차이가 크게 드러납니다.
- positional structure를 이해해야 later stage의 spatial reasoning을 읽을 수 있습니다.

# 이번 강의의 핵심 축
- local receptive field와 global relation
- absolute/relative positional handling
- patch token interaction
- pretrained backbone 재사용 전략

# 스스로 점검
1. CNN과 ViT의 inductive bias 차이를 설명하라.
2. positional structure가 중요한 이유를 말하라.
3. vision backbone 선택이 과제에 따라 달라지는 이유를 설명하라.
