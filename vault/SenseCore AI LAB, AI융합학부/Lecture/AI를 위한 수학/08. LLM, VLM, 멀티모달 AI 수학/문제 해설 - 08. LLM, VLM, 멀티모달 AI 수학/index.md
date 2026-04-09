---
title: "문제 해설 - 08. LLM, VLM, 멀티모달 AI 수학"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b9813aa92acd49915a2672__문제 해설 - 08. LLM, VLM, 멀티모달 AI 수학
notion_id: 32ce313f58b9813aa92acd49915a2672
notion_url: https://www.notion.so/32ce313f58b9813aa92acd49915a2672
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
# 문제 해설 - 08. LLM, VLM, 멀티모달 AI 수학
이 페이지는 08단계의 연습문제 해설을 모아 둔 페이지입니다. 정답만 확인하지 말고, 어떤 정의와 원리를 써야 했는지까지 같이 점검합니다.

## 37. Attention, Transformer, positional math
### 문제 1
- 문제: query, key, value의 역할을 각각 설명하라.
- 해설: query는 찾고 싶은 정보의 기준, key는 비교 기준, value는 실제로 가져오는 내용이다.
### 문제 2
- 문제: attention weight가 커진다는 말의 의미를 설명하라.
- 해설: 해당 토큰의 value가 출력에 더 크게 반영된다는 뜻이다.
### 문제 3
- 문제: Transformer에 residual과 norm이 함께 쓰이는 이유를 설명하라.
- 해설: 깊은 구조에서도 정보와 gradient 흐름을 안정화하기 위해서다.
### 문제 4
- 문제: positional encoding이 왜 필요한가?
- 해설: 토큰 내용만으로는 순서를 알 수 없어서 위치 정보를 더해야 하기 때문이다.

## 38. LLM pretraining, scaling laws, tokenization
### 문제 1
- 문제: LLM pretraining의 기본 목적을 설명하라.
- 해설: 이전 토큰들을 보고 다음 토큰 확률을 맞히도록 학습하는 것이다.
### 문제 2
- 문제: scaling law가 왜 중요한가?
- 해설: 모델 크기, 데이터 양, 연산량을 어떻게 배분해야 효율적으로 성능을 높일지 알려 주기 때문이다.
### 문제 3
- 문제: tokenization이 모델 성능에 영향을 주는 이유를 설명하라.
- 해설: 입력 단위와 시퀀스 길이가 바뀌어 모델이 학습하는 통계 구조가 달라지기 때문이다.
### 문제 4
- 문제: perplexity를 한 문장으로 설명하라.
- 해설: 모델이 다음 토큰을 맞힐 때 평균적으로 얼마나 많은 선택지에서 망설이는지를 나타내는 지표다.

## 39. Alignment SFT, RLHF, DPO
### 문제 1
- 문제: SFT와 RLHF의 차이를 설명하라.
- 해설: SFT는 데모 정답을 모방하고, RLHF는 선호로 만든 보상으로 정책을 조정한다.
### 문제 2
- 문제: reward model이 필요한 이유를 설명하라.
- 해설: 사람 선호를 수치 보상으로 바꿔 학습 신호로 쓰기 위해서다.
### 문제 3
- 문제: DPO가 등장한 이유를 설명하라.
- 해설: 강화학습 루프 없이도 선호 최적화를 가능하게 하기 위해서다.
### 문제 4
- 문제: alignment가 pretraining과 다른 목표를 가진다는 말을 설명하라.
- 해설: pretraining은 다음 토큰 확률을 맞히지만, alignment는 사람 선호에 맞추는 것이 목표다.

## 40. CLIP, contrastive learning, multimodal alignment
### 문제 1
- 문제: contrastive loss의 목표를 설명하라.
- 해설: 맞는 쌍은 가깝게, 아닌 쌍은 멀게 만들어 정렬한다.
### 문제 2
- 문제: 멀티모달 alignment가 필요한 이유를 설명하라.
- 해설: 이미지와 텍스트를 같은 의미 공간에서 비교하고 연결하기 위해서다.
### 문제 3
- 문제: CLIP이 zero-shot 분류에 도움이 되는 이유를 설명하라.
- 해설: 텍스트 설명과 이미지를 같은 공간에서 비교할 수 있기 때문이다.
### 문제 4
- 문제: shared embedding space를 한 문장으로 설명하라.
- 해설: 서로 다른 모달리티가 같은 좌표계에서 의미를 비교할 수 있는 공간이다.

## 41. VLM, multimodal generation, fusion architectures
### 문제 1
- 문제: VLM이란 무엇인지 설명하라.
- 해설: 이미지와 텍스트를 함께 다루는 비전-언어 모델이다.
### 문제 2
- 문제: fusion architecture가 필요한 이유를 설명하라.
- 해설: 서로 다른 모달리티 정보를 하나의 출력으로 연결해야 하기 때문이다.
### 문제 3
- 문제: cross-attention이 self-attention과 다른 점을 설명하라.
- 해설: 한 모달리티의 query가 다른 모달리티의 key/value를 참고한다.
### 문제 4
- 문제: grounding이 중요한 이유를 설명하라.
- 해설: 출력이 실제 입력과 연결되지 않으면 그럴듯하지만 틀린 답이 된다.

## 42. Frontier topics optimal transport, graphs, manifolds, mechanistic interpretability, 최신 논문 독해
### 문제 1
- 문제: optimal transport를 한 문장으로 설명하라.
- 해설: 한 분포의 질량을 다른 분포로 옮기는 최소 비용 문제다.
### 문제 2
- 문제: mechanistic interpretability가 다루는 질문을 설명하라.
- 해설: 모델 내부가 실제로 어떤 계산을 하는지 밝히는 질문이다.
### 문제 3
- 문제: 논문 appendix를 반드시 봐야 하는 이유를 설명하라.
- 해설: 핵심 유도와 구현 조건이 부록에 담기는 경우가 많기 때문이다.
### 문제 4
- 문제: 최신 논문을 읽을 때 수식 앞에서 멈추지 않기 위한 기본 습관을 제시하라.
- 해설: 변수의 역할과 분포 타입을 먼저 적고, 손실 항의 의미를 자연어로 풀어 본다.

# 이 해설 페이지를 읽는 법
1. 37강과 38강은 식을 순서대로 읽는 연습이 중요합니다. 기호를 보기 전에 "무엇을 비교하고 무엇을 예측하는가"를 먼저 말해 보십시오.
2. 39강은 pretraining과 alignment의 목표 차이를 먼저 분명히 해야 합니다.
3. 40강과 41강은 "같은 공간에 맞춘다", "다른 모달을 참고한다", "입력과 출력이 연결된다"는 세 문장으로 먼저 요약한 뒤 세부 구조를 읽는 것이 좋습니다.
4. 42강은 새 주제를 전부 이해하려 하기보다, 어떤 수학이 어떤 문제 때문에 등장했는지를 분류하는 식으로 읽어야 합니다.

# 마지막 점검
- 37강에서는 attention 식의 각 항을 말로 읽을 수 있어야 합니다.
- 38강에서는 tokenization이 왜 모델 구조와 손실 해석에 영향을 주는지 설명할 수 있어야 합니다.
- 39강에서는 SFT, RLHF, DPO의 차이를 학습 신호 관점에서 구분할 수 있어야 합니다.
- 40강에서는 multimodal alignment가 왜 필요한지, positive pair가 무엇인지 설명할 수 있어야 합니다.
- 41강에서는 fusion과 grounding을 함께 설명할 수 있어야 합니다.
- 42강에서는 새로운 논문을 읽을 때 문제 정의, 변수 역할, 손실 구조, appendix 순서로 내려갈 수 있어야 합니다.
