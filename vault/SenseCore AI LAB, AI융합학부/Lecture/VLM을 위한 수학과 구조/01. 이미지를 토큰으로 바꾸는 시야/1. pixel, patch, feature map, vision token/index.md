---
title: "1. pixel, patch, feature map, vision token"
source_kind: page
---
VLM을 이해하는 첫걸음은 이미지를 “그림”이 아니라 “계산 가능한 표현”으로 읽는 것입니다. 이 강의에서는 pixel이 patch로 묶이고, encoder를 거치며 feature map과 vision token으로 바뀌는 흐름을 설명합니다.

# 먼저 알아둘 말
- pixel: 원본 이미지의 가장 작은 값 단위입니다.
- patch: 이미지를 일정 크기 블록으로 나눈 단위입니다.
- feature map: 인코더가 추출한 중간 시각 표현입니다.
- vision token: language model과 상호작용할 수 있게 정리된 시각 토큰입니다.

# 이 강의에서 답할 질문
- 이미지를 왜 token처럼 바꾸어야 하는가
- patch와 feature map은 어떤 관계인가
- vision token은 어느 수준의 시각 정보를 담는가

# 왜 중요한가
- 이미지가 시퀀스로 보이지 않으면 attention 기반 구조를 읽기 어렵습니다.
- 이후 모든 VLM은 결국 vision token이 language 쪽과 어떻게 만나는가의 문제로 정리됩니다.

# 이번 강의의 핵심 축
- raw pixel에서 중간 표현으로 바뀌는 과정
- local pattern과 global context의 차이
- dense feature와 compressed token의 역할
- token 수가 늘어날수록 생기는 계산량 문제

# 스스로 점검
1. patch와 feature map의 차이를 설명하라.
2. vision token이 필요한 이유를 말하라.
3. 이미지도 시퀀스로 읽는 관점이 왜 중요한지 설명하라.
