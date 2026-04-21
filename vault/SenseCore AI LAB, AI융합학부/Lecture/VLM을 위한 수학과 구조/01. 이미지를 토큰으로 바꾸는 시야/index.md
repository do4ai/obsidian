---
title: "01. 이미지를 토큰으로 바꾸는 시야"
source_kind: page
---
이 단계는 VLM의 가장 아래층을 이해하기 위한 출발 단계입니다. 이미지를 픽셀 덩어리로 보는 대신, 패치와 feature map, token 시퀀스로 읽는 관점을 만들고, 뒤 단계에서 계속 쓰일 connector와 backbone 언어를 준비합니다.

# 이 단계에서 배우는 것
- 이미지가 patch와 feature map을 거쳐 vision token으로 바뀌는 흐름을 배운다.
- CNN과 ViT가 시각 표현을 만드는 방식의 차이를 비교한다.
- resolution, stride, pooling이 token budget과 계산량을 어떻게 바꾸는지 읽는다.
- projector와 adapter가 왜 VLM의 첫 관문인지 이해한다.

# 먼저 알고 갈 말
- 시각 표현: 이미지가 모델 안에서 벡터로 바뀐 형태입니다.
- 토큰 예산: 한 번에 모델이 처리하는 토큰 수와 계산량의 한계입니다.
- backbone: 상위 VLM이 기대는 기본 vision encoder입니다.
- connector: vision 쪽 표현을 language 쪽 표현과 이어 주는 다리입니다.

# 이 단계를 읽는 순서
- 1강에서는 pixel이 patch와 feature map, token으로 바뀌는 기본 시야를 만든다.
- 2강에서는 CNN과 ViT의 구조 차이를 읽는다.
- 3강에서는 해상도와 압축이 계산량과 정보 손실에 어떤 영향을 주는지 본다.
- 4강에서는 projector, adapter, connector가 왜 필요한지 정리한다.
- 5강에서는 backbone pretraining과 transfer가 실제 성능에 미치는 영향을 본다.

# 각 강의가 맡는 역할
- 1. pixel, patch, feature map, vision token: 시각 입력을 시퀀스로 읽는 첫걸음.
- 2. CNN, ViT, positional structure: 대표 vision encoder의 inductive bias 비교.
- 3. resolution, stride, pooling, token budget: 계산량과 정보량의 균형 이해.
- 4. projector, adapter, connector: vision과 language를 잇는 중간 연결층 읽기.
- 5. vision backbone pretraining과 transfer: 사전학습 backbone 재사용 전략 이해.

# 이 단계를 읽을 때 기억할 점
- 이미지도 모델 안에 들어가면 결국 시퀀스와 벡터로 읽는다.
- 좋은 backbone은 단순 정확도뿐 아니라 downstream grounding 품질과도 연결된다.
- connector는 사소한 부품이 아니라 전체 VLM 표현 품질을 좌우하는 병목이 될 수 있다.

# 이 단계를 마치면 할 수 있는 것
- 어떤 vision encoder가 어떤 형태의 토큰을 내는지 설명할 수 있다.
- token budget과 resolution trade-off를 말로 풀 수 있다.
- projector와 connector가 왜 필요한지 구조 관점에서 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[1. pixel, patch, feature map, vision token](1. pixel, patch, feature map, vision token/index.md)
[2. CNN, ViT, positional structure](2. CNN, ViT, positional structure/index.md)
[3. resolution, stride, pooling, token budget](3. resolution, stride, pooling, token budget/index.md)
[4. projector, adapter, connector](4. projector, adapter, connector/index.md)
[5. vision backbone pretraining과 transfer](5. vision backbone pretraining과 transfer/index.md)
[문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)

## Page Tree

- [1. pixel, patch, feature map, vision token](1. pixel, patch, feature map, vision token/index.md)
- [2. CNN, ViT, positional structure](2. CNN, ViT, positional structure/index.md)
- [3. resolution, stride, pooling, token budget](3. resolution, stride, pooling, token budget/index.md)
- [4. projector, adapter, connector](4. projector, adapter, connector/index.md)
- [5. vision backbone pretraining과 transfer](5. vision backbone pretraining과 transfer/index.md)
- [문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)
