---
title: "05. 멀티모달 생성과 instruction tuning"
source_kind: page
---
이 단계는 정렬된 표현을 실제 생성형 assistant로 바꾸는 단계입니다. captioning과 VQA에서 출발해, multimodal instruction data, RLHF, DPO, safety policy가 어떻게 결합되는지 읽습니다.

# 이 단계에서 배우는 것
- captioning, VQA, conditional generation의 공통 구조를 배운다.
- multimodal SFT 데이터와 instruction tuning의 역할을 이해한다.
- preference learning, reward model, RLHF를 멀티모달 맥락에서 읽는다.
- DPO와 rejection sampling 같은 alignment 대안을 비교한다.
- safety policy와 refusal이 실제 제품 동작을 어떻게 바꾸는지 본다.

# 먼저 알고 갈 말
- conditional generation: 이미지나 질문을 조건으로 두고 답을 생성하는 방식입니다.
- SFT: 지도학습으로 instruction-following을 익히는 fine-tuning입니다.
- preference learning: 여러 답 중 더 나은 답을 고르게 해 학습하는 방식입니다.
- refusal: 안전 또는 불확실성 때문에 답변을 거절하는 동작입니다.

# 이 단계를 읽는 순서
- 21강에서는 생성형 멀티모달 과제의 공통 구조를 잡는다.
- 22강에서는 instruction data와 SFT를 읽는다.
- 23강에서는 reward model과 RLHF를 본다.
- 24강에서는 DPO와 rejection sampling을 비교한다.
- 25강에서는 안전 정책과 jailbreak 대응을 정리한다.

# 각 강의가 맡는 역할
- 21. captioning, VQA, conditional generation: 생성형 멀티모달 과제 지도.
- 22. supervised fine-tuning과 multimodal instruction data: 지시 따르기 학습 읽기.
- 23. preference learning, reward model, RLHF: 선호 기반 정렬 이해.
- 24. DPO, rejection sampling, policy alignment: RLHF 대안 비교.
- 25. safety policy, refusal, jailbreak 대응: 제품 수준 안전성 이해.

# 이 단계를 읽을 때 기억할 점
- 좋은 답은 정답성, 근거성, 안전성이 함께 맞아야 한다.
- instruction tuning은 능력을 마법처럼 만드는 것이 아니라, 이미 있는 표현과 reasoning을 재배치한다.
- alignment는 품질 향상과 동시에 새로운 failure mode도 만들 수 있다.

# 이 단계를 마치면 할 수 있는 것
- multimodal SFT와 preference tuning의 차이를 설명할 수 있다.
- RLHF와 DPO가 무엇을 바꾸는지 말할 수 있다.
- safety policy가 모델 구조와 분리된 후처리만이 아니라는 점을 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[21. captioning, VQA, conditional generation](21. captioning, VQA, conditional generation/index.md)
[22. supervised fine-tuning과 multimodal instruction data](22. supervised fine-tuning과 multimodal instruction data/index.md)
[23. preference learning, reward model, RLHF](23. preference learning, reward model, RLHF/index.md)
[24. DPO, rejection sampling, policy alignment](24. DPO, rejection sampling, policy alignment/index.md)
[25. safety policy, refusal, jailbreak 대응](25. safety policy, refusal, jailbreak 대응/index.md)
[문제 해설 - 05. 멀티모달 생성과 instruction tuning](문제 해설 - 05. 멀티모달 생성과 instruction tuning/index.md)

## Page Tree

- [21. captioning, VQA, conditional generation](21. captioning, VQA, conditional generation/index.md)
- [22. supervised fine-tuning과 multimodal instruction data](22. supervised fine-tuning과 multimodal instruction data/index.md)
- [23. preference learning, reward model, RLHF](23. preference learning, reward model, RLHF/index.md)
- [24. DPO, rejection sampling, policy alignment](24. DPO, rejection sampling, policy alignment/index.md)
- [25. safety policy, refusal, jailbreak 대응](25. safety policy, refusal, jailbreak 대응/index.md)
- [문제 해설 - 05. 멀티모달 생성과 instruction tuning](문제 해설 - 05. 멀티모달 생성과 instruction tuning/index.md)
