---
title: "4. projector, adapter, connector"
source_kind: page
---
vision encoder가 만든 표현은 그대로 language model이 받아들이기 어렵습니다. 이 강의에서는 projector, adapter, connector가 두 표현 공간을 어떻게 이어 주는지 설명합니다.

# 먼저 알아둘 말
- hidden dimension: 모델 내부 표현 차원입니다.
- projector: 차원을 맞추는 변환기입니다.
- adapter: 경량 추가 모듈입니다.
- connector: vision과 language를 이어 주는 일반적인 연결 블록입니다.

# 이 강의에서 답할 질문
- 왜 단순 연결만으로는 충분하지 않은가
- projector와 adapter는 무엇을 다르게 하는가
- connector는 어디에서 병목이 되는가

# 왜 중요한가
- VLM 품질의 상당 부분은 vision token이 LM hidden space로 얼마나 잘 옮겨지는지에 달려 있습니다.
- connector는 계산량과 grounding 품질을 동시에 바꿉니다.

# 이번 강의의 핵심 축
- 차원 정합과 표현 변환
- frozen backbone 위 adapter 학습 전략
- token compression과 connector 설계
- linear bridge와 richer bridge의 차이

# 스스로 점검
1. projector가 필요한 이유를 설명하라.
2. adapter와 connector의 차이를 말하라.
3. connector가 병목이 될 때 어떤 현상이 생기는지 설명하라.
