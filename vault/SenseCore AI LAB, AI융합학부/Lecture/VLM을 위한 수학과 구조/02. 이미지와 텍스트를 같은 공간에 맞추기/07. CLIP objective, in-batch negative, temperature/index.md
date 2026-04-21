---
title: "07. CLIP objective, in-batch negative, temperature"
source_kind: page
---
CLIP은 멀티모달 정렬을 대표하는 출발점입니다. 이 강의에서는 CLIP objective가 어떤 pair를 밀고 당기며, in-batch negative와 temperature가 왜 중요한지 설명합니다.

# 먼저 알아둘 말
- contrastive loss: 정답 쌍은 가깝게, 오답 쌍은 멀게 만드는 손실입니다.
- in-batch negative: 같은 배치 안의 다른 샘플을 음성 예시로 쓰는 방식입니다.
- temperature: 분포 sharpness를 조절하는 스케일 값입니다.
- positive pair: 서로 대응되는 정답 쌍입니다.

# 이 강의에서 답할 질문
- CLIP objective는 무엇을 최적화하는가
- in-batch negative는 왜 효율적인가
- temperature가 바뀌면 학습 신호는 어떻게 달라지는가

# 왜 중요한가
- CLIP은 이후 multimodal retrieval과 representation pretraining의 기본 문법이 되었습니다.
- temperature와 negative 품질을 모르면 정렬 실패를 해석하기 어렵습니다.

# 이번 강의의 핵심 축
- symmetric contrastive objective
- batch 안의 오답 활용
- similarity scale과 gradient strength
- alignment quality와 optimization stability

# 스스로 점검
1. CLIP objective가 무엇을 가깝게 만드는지 설명하라.
2. in-batch negative가 필요한 이유를 말하라.
3. temperature가 너무 크거나 작을 때 어떤 문제가 생기는지 설명하라.
