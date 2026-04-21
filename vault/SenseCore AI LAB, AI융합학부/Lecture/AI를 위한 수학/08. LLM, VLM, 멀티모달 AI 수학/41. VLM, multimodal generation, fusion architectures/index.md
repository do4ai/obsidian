---
title: "41. VLM, multimodal generation, fusion architectures"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b981e7883de1e3a0ec86c3__41. VLM, multimodal generation, fusion architectures
notion_id: 32ce313f58b981e7883de1e3a0ec86c3
notion_url: https://www.notion.so/32ce313f58b981e7883de1e3a0ec86c3
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
VLM은 이미지와 텍스트를 한 모델 안에서 함께 다루는 구조입니다. 중요한 점은 단순히 두 입력을 같이 넣는 것이 아니라, 언제 어떤 방식으로 합칠지를 설계하는 것입니다. 이 강의에서는 왜 fusion이 필요한지, vision token이 language model로 어떻게 들어가는지, cross-attention과 projector가 어떤 역할을 하는지, grounding이 왜 핵심 품질 기준인지, 그리고 왜 VLM이 별도 심화 교재로 확장될 만한 분야인지까지 구조 중심으로 설명합니다.

# 먼저 알아둘 말
- VLM: 이미지와 텍스트를 함께 다루는 비전-언어 모델이다.
- vision encoder: 이미지를 특징 벡터나 특징 시퀀스로 바꾸는 모듈이다.
- language model: 텍스트를 읽고 생성하는 모듈이다.
- vision token: 이미지에서 추출된 특징 벡터 하나하나를 토큰처럼 다루는 표현이다.
- projector: vision encoder 출력 차원을 language model 입력 차원으로 맞추는 모듈이다.
- fusion: 서로 다른 모달리티의 정보를 합치는 방식이다.
- early fusion: 비교적 이른 단계부터 두 모달리티를 함께 섞는 방식이다.
- late fusion: 각 모달리티를 따로 처리한 뒤 나중에 결합하는 방식이다.
- cross-attention: 한 모달리티의 query가 다른 모달리티의 key/value를 참고하는 attention이다.
- grounding: 생성된 언어가 실제 입력 시각 정보와 연결되는 성질이다.
- hallucination: 입력에 없는 내용을 그럴듯하게 만들어 내는 오류다.
- multimodal generation: 시각 정보와 텍스트 문맥을 함께 사용해 답변이나 설명을 생성하는 문제다.

# 이 강의에서 답할 질문
- VLM은 어떤 부품들의 결합으로 이루어지는가?
- 이미지 표현은 어떻게 language model 안으로 들어가는가?
- fusion 방식이 여러 가지인 이유는 무엇인가?
- cross-attention은 어떤 정보를 주고받게 하는가?
- grounding이 약하면 왜 그럴듯하지만 틀린 답이 생기는가?
- 왜 VLM은 CLIP보다 더 어려운 문제인가?

# 먼저 떠올릴 장면
- 한 장의 사진을 보고 `"왼쪽에 있는 사람은 무엇을 들고 있는가?"`라는 질문에 답하는 상황을 떠올려 봅시다.
- 이때 모델은 문장만 잘 읽어도 안 되고, 이미지만 잘 보아도 안 됩니다.
- 질문의 특정 단어를 읽는 순간 실제 이미지의 특정 영역을 참고해야 정확한 답이 나옵니다.
- 즉 문제는 `"이미지와 텍스트를 같이 본다"`보다 더 정확하게는 `"언어 생성 시점마다 필요한 시각 정보를 끌어온다"`입니다.

# 이 강의의 큰 그림
이 강의는 다음 순서로 읽는 것이 좋습니다.

1. 먼저 이미지와 텍스트를 왜 함께 처리해야 하는지 봅니다.
2. 그다음 VLM의 기본 부품과 정보 흐름을 정리합니다.
3. 이어서 fusion 방식을 구분하고 cross-attention을 읽습니다.
4. 그다음 grounding과 hallucination 문제를 설명합니다.
5. 마지막으로 왜 이 분야가 별도 심화 교재로 이어질 만큼 넓은지 연결합니다.

# 먼저 문제를 세우기
CLIP은 이미지와 텍스트를 같은 공간에 정렬하는 데 강합니다. 하지만 `"이 사진을 설명하라"`, `"왼쪽 물체의 색을 말하라"`, `"표지판의 글자를 읽어라"` 같은 문제는 단순 정렬만으로 충분하지 않습니다.

왜냐하면 이런 문제는:

1. 질문을 이해해야 하고
2. 이미지 안에서 필요한 정보를 찾아야 하며
3. 그 정보를 언어로 생성해야 하기 때문입니다.

즉 VLM은 정렬 문제를 넘어 `"조건부 생성"` 문제로 들어갑니다.

# VLM의 기본 부품
VLM의 기본 구조는 크게 세 부분으로 볼 수 있습니다.

| 부품 | 역할 |
| --- | --- |
| vision encoder | 이미지를 특징 시퀀스로 바꾼다 |
| projector 또는 adapter | 시각 특징을 언어모델이 받을 수 있는 차원으로 맞춘다 |
| language model | 질문을 읽고 답을 생성한다 |

이를 아주 단순하게 적으면:

$$
I \xrightarrow{\text{vision encoder}} V
\xrightarrow{\text{projector}} \tilde{V}
\xrightarrow{\text{fusion with text}} \text{LM output}
$$

입니다.

여기서 핵심은 이미지가 raw pixel 상태로 language model 안에 들어가는 것이 아니라, 먼저 특징 시퀀스로 바뀐 뒤 언어모델과 상호작용한다는 점입니다.

# vision token은 어떻게 쓰이는가
vision encoder는 이미지를 하나의 벡터로만 압축할 수도 있지만, 실제로는 패치 단위나 영역 단위 특징 시퀀스를 내는 경우가 많습니다. 이 시퀀스를 vision token처럼 생각할 수 있습니다.

예를 들어

$$
V = [v_1, v_2, \dots, v_m]
$$

처럼 이미지 특징 시퀀스를 얻고, 텍스트 토큰 시퀀스를

$$
T = [t_1, t_2, \dots, t_n]
$$

라고 하면, VLM의 핵심은 이 두 시퀀스가 어떻게 상호작용하는가입니다.

## projector가 필요한 이유
vision encoder의 출력 차원과 language model의 hidden dimension이 다를 수 있으므로, projector가 다음 같은 역할을 합니다.

$$
\tilde{v}_i = P v_i
$$

즉 시각 특징을 언어모델이 다룰 수 있는 표현 공간으로 바꿉니다.

# fusion은 무엇을 결정하는가
바로 이 연결 방식을 정하는 것이 fusion architecture입니다. 즉 VLM 설계의 핵심은 `"이미지 정보와 텍스트 정보를 언제, 어디서, 어떤 방향으로 섞을 것인가"`입니다.

## early fusion
이미지 특징과 텍스트 토큰을 비교적 일찍부터 한 흐름 안에서 함께 처리합니다.

장점:
- 시각과 언어의 상호작용이 이른 단계부터 가능하다

부담:
- 계산량이 커질 수 있고 설계가 무거워질 수 있다

## late fusion
각 모달리티를 별도로 충분히 처리한 뒤 더 높은 수준 표현에서 결합합니다.

장점:
- 모달별 인코더를 독립적으로 강하게 만들기 쉽다

부담:
- 세밀한 상호작용이 늦게 들어와 지역 정보 결합이 약할 수 있다

즉 어느 쪽이 좋은지는 과제에 따라 달라집니다. 단순 분류나 매칭은 늦은 결합으로도 충분할 수 있지만, 세부 질의응답과 생성에서는 더 촘촘한 결합이 필요할 수 있습니다.

# cross-attention은 시각 정보를 읽는 창이다
가장 자주 쓰이는 결합 방식 중 하나는 cross-attention입니다. 텍스트 쪽 상태를

$$
Q_{\text{text}}
$$

라고 하고, 이미지 특징을

$$
K_{\text{img}},\; V_{\text{img}}
$$

라고 하면 cross-attention은 대략 다음처럼 적을 수 있습니다.

$$
\mathrm{CrossAttn}
=
\mathrm{softmax}\!\left(
\frac{Q_{\text{text}}K_{\text{img}}^\top}{\sqrt{d}}
\right)
V_{\text{img}}
$$

이 식의 뜻은 분명합니다. 지금 생성 중인 텍스트 상태가 이미지 특징들 중 어디를 얼마나 참고할지 결정한 뒤, 필요한 시각 정보를 끌어와 다음 언어 표현을 만드는 것입니다.

즉 cross-attention은 `"언어가 시각 정보를 읽는 창"`이라고 볼 수 있습니다.

## self-attention과의 차이
- self-attention: 텍스트가 텍스트를 참고한다
- cross-attention: 텍스트가 이미지를 참고한다

따라서 self-attention만으로는 언어 내부 문맥은 읽을 수 있어도, 이미지의 특정 위치 정보를 직접 끌어오지는 못합니다.

# 어떤 질문이 cross-attention을 강하게 요구하는가
다음 같은 질문은 시각 grounding이 특히 중요합니다.

- `"왼쪽 사람은 무엇을 들고 있는가?"`
- `"빨간 컵 옆에 있는 물체는 무엇인가?"`
- `"표지판에 적힌 글자를 읽어라"`
- `"사진의 중앙 아래쪽에 있는 버튼 색은?"`

이런 경우 언어 모델은 질문을 읽는 순간:

1. 위치 표현을 해석하고
2. 이미지 내 후보 영역을 찾고
3. 그 영역에서 시각 정보를 읽고
4. 언어로 답을 만들어야 합니다

즉 VLM은 `"문장을 잘 쓰는 모델"`에 시각 검색 메커니즘이 결합된 구조라고 볼 수 있습니다.

# grounding은 왜 핵심 품질 기준인가
하지만 시각 정보를 참고한다고 해서 자동으로 올바른 답이 보장되지는 않습니다. 모델이 이미지를 제대로 보지 않고, 언어적 습관만으로 문장을 이어 쓰면 겉보기에는 자연스럽지만 실제 입력과 어긋난 응답이 나올 수 있습니다.

예를 들어 이미지에 개가 없는데 `"개가 공을 물고 있다"`고 답하면 언어는 유창하지만 입력과는 맞지 않습니다.

이를 막기 위해 중요한 개념이 grounding입니다. grounding은 출력 문장이 실제 입력과 연결되어 있다는 뜻입니다.

즉 좋은 VLM은:

- 문장을 잘 만드는 것만으로 충분하지 않고
- 그 문장이 실제 시각 정보에 의해 뒷받침되어야 합니다

grounding이 약하면 hallucination이 늘어나고, 모델은 그럴듯하지만 틀린 설명을 자주 내놓게 됩니다.

# hallucination은 왜 생기는가
VLM hallucination은 보통 다음 원인들이 섞여 나옵니다.

## 1. 언어 prior가 너무 강한 경우
이미지를 덜 보고, 자주 본 언어 패턴으로 답을 이어 쓸 수 있습니다.

## 2. 시각 특징이 부족한 경우
작은 글자, 복잡한 배치, 세밀한 관계를 충분히 구분하지 못할 수 있습니다.

## 3. fusion이 약한 경우
필요한 시점에 필요한 시각 정보를 제대로 끌어오지 못할 수 있습니다.

즉 hallucination은 단순한 "거짓말"이라기보다, 언어 생성과 시각 grounding 사이 연결이 약할 때 생기는 구조적 오류입니다.

# VLM이 CLIP보다 더 어려운 이유
CLIP은 `"이미지와 텍스트가 같은 뜻인지"`를 맞추는 정렬 문제에 가깝습니다. 반면 VLM은:

1. 질문을 이해하고
2. 이미지의 관련 부분을 찾고
3. 그 정보를 문맥 안에 결합하고
4. 자연어로 생성해야 합니다

즉 정렬 + 선택 + 추론 + 생성이 동시에 들어갑니다. 그래서 VLM은 CLIP보다 구조적으로 더 어렵고, 별도 심화 교재로 확장할 가치가 큰 분야입니다.

# 왜 이 주제는 별도 심화 교재로 분리할 만한가
이 강의에서는 큰 흐름을 설명하지만, VLM 자체는 다음 세부 주제만으로도 별도 교재가 가능합니다.

- vision encoder 종류
- projector와 adapter 설계
- Q-Former 계열 구조
- OCR 및 region grounding
- multimodal instruction tuning
- hallucination 완화와 grounding 평가
- image-text generation과 diffusion 결합

즉 본편에서는 `"정보 흐름 구조"`를 이해하는 데 집중하고, 세부 아키텍처와 구현 변형은 별도 심화 자료로 파는 것이 맞습니다.

# 자주 생기는 오해
## 오해 1. 이미지를 텍스트로 바꿔 넣으면 VLM이다
단순 캡션 전처리만으로는 충분하지 않습니다. 질문 시점에 시각 정보를 다시 읽어야 하는 경우가 많습니다.

## 오해 2. cross-attention만 있으면 grounding이 자동으로 해결된다
구조는 필요조건에 가깝지만, 실제 학습 데이터와 시각 인코더 품질까지 함께 좋아야 합니다.

## 오해 3. VLM은 CLIP에 language model만 붙이면 끝난다
정렬, fusion, 시각 세부 인식, hallucination 완화까지 모두 별도 난제를 가집니다.

# 예제
1. cross-attention의 역할
문제: 질문 텍스트를 생성하는 중에 이미지의 특정 영역 정보를 참고하려면 어떤 구조가 적합한가?
풀이: 텍스트 query가 이미지 key/value를 참고하는 cross-attention 구조가 적합하다.
해설: 현재 언어 상태가 필요한 시각 정보를 선택해 가져오는 방식이기 때문이다.

2. grounding 실패의 징후
문제: 이미지와 관계없는 그럴듯한 설명을 계속 만들어 낸다면 무엇이 약한 것인가?
풀이: grounding이 약한 것이다.
해설: 출력 언어가 실제 입력 시각 정보와 충분히 연결되지 않았다는 뜻이다.

3. fusion 방식의 차이
문제: 왜 fusion 방식이 하나로 고정되지 않고 여러 가지가 존재하는가?
풀이: 과제마다 어느 시점에 모달리티를 결합하는 것이 더 유리한지가 다르기 때문이다.
해설: 정보 결합이 필요한 위치와 강도는 과제마다 다르므로, 설계도 여러 형태가 나온다.

4. projector의 역할
문제: vision encoder와 language model 사이에 projector가 자주 필요한 이유는 무엇인가?
풀이: 시각 특징 차원을 언어모델 hidden space에 맞추고, 두 표현 공간을 연결하기 위해서다.
해설: 이미지 특징을 LM이 소비할 수 있는 형태로 바꾸는 다리 역할을 한다.

# 핵심 정리
- VLM은 vision encoder, projector, language model의 결합 구조로 이해할 수 있다.
- 핵심 문제는 `"이미지와 텍스트를 언제 어디서 섞는가"`라는 fusion 설계다.
- cross-attention은 언어가 시각 정보를 읽는 대표 통로다.
- grounding이 약하면 hallucination이 늘어난다.
- VLM은 정렬을 넘어 선택, 추론, 생성까지 포함하므로 CLIP보다 더 어려운 문제다.
- 그래서 본편에서는 큰 구조를 잡고, 세부 아키텍처는 별도 심화 교재로 파는 것이 적절하다.

# 스스로 점검
## 연습 문제
1. VLM의 기본 부품을 설명하라.
2. projector가 왜 필요한지 설명하라.
3. early fusion과 late fusion의 차이를 설명하라.
4. cross-attention이 self-attention과 어떻게 다른지 설명하라.
5. grounding이 왜 중요한 품질 기준인지 설명하라.
6. VLM이 CLIP보다 더 어려운 이유를 설명하라.

## 복습 질문
1. VLM에서 fusion은 무엇을 결정하는가?
2. cross-attention은 어느 방향의 정보 흐름을 만드는가?
3. grounding이 약하면 어떤 오류가 생기는가?
4. 왜 VLM은 별도 심화 교재로 확장할 만한 주제인가?

## 체크포인트
1. VLM의 기본 구조를 설명할 수 있다.
2. fusion 방식이 여러 개인 이유를 이해한다.
3. cross-attention의 수식을 말로 읽을 수 있다.
4. grounding과 hallucination의 관계를 설명할 수 있다.
5. 본편과 심화 교재의 분리 이유를 말할 수 있다.
