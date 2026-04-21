---
title: "09. captioning, matching, contrastive objective 조합"
source_kind: page
---
실제 VLM 사전학습은 하나의 loss만으로 끝나지 않습니다. 이 강의에서는 contrastive, matching, captioning objective를 어떻게 섞는지 설명합니다.

# 먼저 알아둘 말
- captioning loss: 이미지 조건에서 텍스트를 생성하도록 하는 손실입니다.
- matching loss: 쌍이 맞는지 틀리는지 구분하게 하는 손실입니다.
- contrastive loss: 벡터 공간 정렬을 학습시키는 손실입니다.
- objective mixing: 여러 손실을 함께 최적화하는 방식입니다.

# 이 강의에서 답할 질문
- 서로 다른 objective는 무엇을 각자 담당하는가
- 왜 하나의 loss만으로는 충분하지 않은가
- objective 조합은 어떤 모델 성격 차이를 만드는가

# 왜 중요한가
- 이후 generation 단계의 품질은 여기서 어떤 objective를 강조했는지에 영향을 받습니다.
- 같은 구조라도 objective 조합에 따라 retrieval형 모델과 assistant형 모델로 갈립니다.

# 이번 강의의 핵심 축
- representation alignment와 conditional generation의 차이
- matching이 noisy pair를 보정하는 역할
- multi-task pretraining의 장단점
- objective imbalance가 만드는 failure mode

# 스스로 점검
1. contrastive와 captioning objective의 차이를 설명하라.
2. matching objective가 필요한 이유를 말하라.
3. objective 조합이 모델 성격을 바꾸는 이유를 설명하라.
