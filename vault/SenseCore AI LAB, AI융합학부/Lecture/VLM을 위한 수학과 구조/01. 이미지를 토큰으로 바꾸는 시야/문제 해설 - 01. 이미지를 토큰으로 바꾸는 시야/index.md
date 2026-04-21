---
title: "문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야"
source_kind: page
---
이 해설 페이지는 1단계 강의를 읽고 난 뒤, 시각 표현과 token budget, connector 이해가 제대로 잡혔는지 점검하기 위한 페이지입니다.

# 이 해설 페이지의 역할
- patch와 feature map, token의 차이를 말로 설명하게 합니다.
- CNN과 ViT의 차이를 구조 수준에서 다시 정리하게 합니다.
- projector와 backbone이 downstream VLM에 어떤 영향을 주는지 복습하게 합니다.

# 문제를 풀 때 확인할 것
- 입력 해상도와 token 수가 어떻게 연결되는지 설명할 수 있는가
- connector가 왜 병목이 되는지 구조적으로 말할 수 있는가
- pretrained backbone을 고르는 기준을 데이터와 과제 기준으로 설명할 수 있는가

# 연결 복습
- 이 단계가 확실해야 2단계의 image-text alignment와 3단계의 VLM architecture를 읽을 때 막히지 않습니다.
