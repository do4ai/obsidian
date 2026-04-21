---
title: "5. vision backbone pretraining과 transfer"
source_kind: page
---
실제 VLM은 처음부터 모든 것을 새로 배우지 않고, 이미 잘 학습된 vision backbone을 가져와 재사용하는 경우가 많습니다. 이 강의는 backbone pretraining과 transfer가 왜 중요한지 설명합니다.

# 먼저 알아둘 말
- pretraining: 큰 데이터에서 먼저 일반 표현을 익히는 과정입니다.
- transfer: 익힌 표현을 새 과제로 옮겨 쓰는 과정입니다.
- frozen backbone: backbone은 고정하고 다른 부분만 학습하는 방식입니다.
- fine-tuning: 사전학습된 모델을 새 목적에 맞게 다시 학습하는 과정입니다.

# 이 강의에서 답할 질문
- pretrained backbone은 무엇을 미리 해결해 주는가
- frozen과 full fine-tuning은 어떻게 다른가
- transfer 품질은 어떤 과제에서 특히 중요해지는가

# 왜 중요한가
- 좋은 backbone은 정렬, grounding, OCR의 출발 품질을 좌우합니다.
- compute가 제한될수록 backbone 재사용 전략은 더 중요해집니다.

# 이번 강의의 핵심 축
- general visual feature와 task-specific adaptation
- frozen vs tuned backbone trade-off
- domain shift가 transfer에 미치는 영향
- high-resolution task에서 backbone 선택 기준

# 스스로 점검
1. backbone pretraining의 장점을 설명하라.
2. frozen backbone과 fine-tuning의 차이를 말하라.
3. transfer가 어려워지는 상황을 예로 들어 설명하라.
