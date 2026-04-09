---
title: "37. Attention, Transformer, positional math"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b981a3b3c8f735fc4a761e__37. Attention, Transformer, positional math
notion_id: 32ce313f58b981a3b3c8f735fc4a761e
notion_url: https://www.notion.so/32ce313f58b981a3b3c8f735fc4a761e
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
attention은 문장을 읽을 때 "지금 이 토큰을 이해하려면 다른 토큰 중 무엇을 얼마나 참고해야 하는가?"를 계산하는 장치입니다. Transformer는 이 attention을 중심으로 문맥을 반복해서 섞고 가공하는 구조입니다. 이 강의에서는 왜 attention이 필요한지부터 시작해, query, key, value의 분업, softmax와 positional encoding의 역할, 그리고 Transformer 블록의 계산 순서를 차례대로 설명합니다.

# 먼저 알아둘 말
- 토큰: 문장이나 데이터를 잘게 나눈 입력 단위다.
- 임베딩: 토큰을 숫자 벡터로 바꾼 표현이다.
- query: 지금 토큰이 찾고 싶은 정보의 기준이다.
- key: 각 토큰이 제공할 수 있는 정보의 표지다.
- value: 실제로 전달할 내용이다.
- attention: 다른 토큰을 얼마나 참고할지 정한 뒤 그 정보를 가중합하는 연산이다.
- softmax: 점수들을 합이 1인 가중치로 바꾸는 함수다.
- positional encoding: 순서 정보를 벡터에 더하는 장치다.
- self-attention: 같은 입력 안의 토큰들끼리 서로를 참고하는 attention이다.
- Transformer 블록: attention, residual, normalization, MLP를 한 묶음으로 반복하는 구조다.

# 이 강의에서 답할 질문
- attention은 왜 필요한가?
- query, key, value는 각각 어떤 역할을 하는가?
- softmax는 왜 꼭 들어가는가?
- positional encoding이 없으면 무엇을 놓치게 되는가?
- Transformer 블록은 어떤 순서로 계산되는가?

# 먼저 떠올릴 장면
- "철수가 영희를 도왔다. 그는 기뻤다."라는 문장에서 "그는"이 누구인지 이해하려면 앞에 나온 단어들을 다시 봐야 합니다.
- 이때 모든 단어를 똑같이 보는 것이 아니라, 지금 필요한 단어를 더 강하게 참고해야 합니다.
- attention은 이 참고 비율을 숫자로 계산해 주는 장치입니다.

# 생각의 순서
1. 먼저 문맥 이해에서 왜 다시 참고가 필요한지 봅니다.
2. 그다음 query, key, value가 왜 나뉘는지 설명합니다.
3. 이어서 attention 식을 계산 순서대로 읽습니다.
4. 그 뒤 softmax와 positional encoding의 필요성을 설명합니다.
5. 마지막으로 Transformer 블록 전체가 어떻게 반복되는지 정리합니다.

# 본문
문장을 읽는다는 것은 각 단어를 따로따로 처리하는 일이 아닙니다. 현재 토큰의 뜻은 주변 토큰과의 관계 속에서 정해집니다. 예를 들어 대명사, 수식어, 부정 표현은 앞뒤 문맥을 보지 않으면 제대로 이해할 수 없습니다. attention은 바로 이 "다른 토큰을 다시 참고하는 과정"을 계산식으로 만든 것입니다.

입력 토큰들의 임베딩을 행렬

$$
X
$$

로 적겠습니다. Transformer는 이 입력에서 세 가지 다른 표현을 만듭니다.

$$
Q = XW_Q,\qquad K = XW_K,\qquad V = XW_V
$$

여기서

$$
Q
$$

는 지금 토큰이 무엇을 찾고 싶은지를 나타냅니다.

$$
K
$$

는 각 토큰이 어떤 정보를 갖고 있는지를 나타냅니다.

$$
V
$$

는 실제로 전달할 정보 자체를 담습니다. 즉 query는 "무엇을 찾나", key는 "무엇을 줄 수 있나", value는 "실제로 무엇을 줄까"라는 분업을 맡습니다.

왜 굳이 셋으로 나누는가를 생각해 보면 이유가 분명합니다. 토큰은 한편으로는 남을 참고하는 주체이고, 다른 한편으로는 남에게 참고되는 대상입니다. 또 참고되었을 때 실제로 전달할 내용은 단순한 표지와 다를 수 있습니다. 그래서 찾는 기준, 비교 기준, 전달 내용을 분리해 두는 편이 더 유연합니다.

attention 계산은 보통 다음 식으로 씁니다.

$$
\mathrm{Attention}(Q, K, V)
=
\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

이 식은 반드시 순서대로 읽어야 이해됩니다. 먼저

$$
QK^\top
$$

를 계산합니다. 이 값은 각 토큰이 다른 토큰을 얼마나 참고하고 싶은지에 대한 점수표입니다. 즉 "누가 누구를 얼마나 볼 것인가?"를 아직 정규화되지 않은 수치로 적어 둔 것입니다.

그다음

$$
\sqrt{d_k}
$$

로 나눕니다. 차원이 커지면 내적값이 지나치게 커져 softmax가 너무 뾰족해질 수 있기 때문입니다. 이 나눗셈은 점수의 스케일을 안정화하는 역할을 합니다.

그다음 softmax를 적용합니다. 그러면 각 토큰이 참고하는 비율의 합이 1이 되도록 가중치가 만들어집니다. 즉 단순한 점수표가 "실제로 어느 토큰을 얼마나 반영할지"를 말하는 비율표로 바뀝니다.

마지막으로 그 가중치를

$$
V
$$

에 곱합니다. 그러면 많이 참고해야 하는 토큰의 정보는 크게 들어오고, 거의 참고하지 않아도 되는 토큰의 정보는 작게 반영됩니다. 그래서 attention의 결과는 "문맥을 반영해 다시 만든 토큰 표현"이라고 볼 수 있습니다.

softmax가 꼭 필요한 이유도 여기 있습니다. attention은 결국 가중합을 해야 하는데, 그 가중치가 비교 가능하고 안정적이어야 합니다. softmax를 거치면 큰 점수는 더 강조되고, 전체 합은 1이 되어 각 토큰이 얼마나 반영되는지를 해석하기 쉬워집니다.

하지만 attention만으로는 순서를 알 수 없습니다. "개가 사람을 물었다"와 "사람이 개를 물었다"는 같은 단어를 써도 의미가 완전히 다릅니다. attention은 기본적으로 토큰들 사이의 관계를 비교하는 연산이지, 절대적인 순서를 저절로 기억하지는 않습니다. 그래서 positional encoding을 임베딩에 더해 각 토큰이 문장 안에서 어느 위치에 놓였는지를 알려 줘야 합니다.

Transformer 블록은 보통 self-attention, residual connection, normalization, MLP를 하나의 묶음으로 반복합니다. self-attention은 문맥 정보를 섞고, MLP는 각 위치에서 비선형 가공을 더하며, residual과 normalization은 깊은 층에서도 학습이 안정되도록 돕습니다. 즉 Transformer는 "어디를 볼지 정하는 단계"와 "본 정보를 가공하는 단계"를 반복하면서 표현을 점점 정교하게 만듭니다.

그래서 Transformer를 이해할 때는 attention 식 하나만 보는 것으로 끝나면 안 됩니다. query, key, value의 분업, softmax에 의한 가중치화, positional encoding에 의한 순서 정보, 그리고 블록 반복 구조까지 함께 봐야 합니다. 이 요소들이 합쳐져야 긴 문맥을 안정적으로 처리할 수 있는 현대 언어모델의 기본 구조가 만들어집니다.

# 예제
1. 관련 토큰에 더 큰 가중치
문제: 현재 토큰의 query가 어떤 이전 토큰의 key와 매우 비슷하다면 어떤 일이 일어나는가?
풀이: 그 이전 토큰에 대한 attention weight가 커지고, 그 토큰의 value가 더 크게 반영된다.
해설: attention은 "관련성이 큰 곳을 더 본다"는 직관을 수치로 구현한 것이다.

2. softmax의 역할
문제: query-key 점수에 softmax를 적용하는 이유는 무엇인가?
풀이: 점수들을 비교 가능한 가중치로 바꾸고, 참고 비율의 총합을 1로 맞추기 위해서다.
해설: 단순한 점수 차이를 실제 정보 결합 비율로 바꾸는 단계다.

3. 순서 정보의 필요성
문제: positional encoding이 없다면 어떤 문장 차이를 놓치기 쉬운가?
풀이: 같은 단어들이라도 순서만 다른 문장을 잘 구분하기 어려워진다.
해설: attention은 내용 비교는 잘하지만, 위치 정보는 따로 주지 않으면 직접 알 수 없다.

# 스스로 점검
## 연습 문제
1. query, key, value를 각각 자연어로 설명하라.
2. attention 식을 계산 순서대로 읽으며 각 단계의 역할을 설명하라.
3. softmax가 없다면 어떤 문제가 생길지 설명하라.
4. positional encoding이 필요한 이유를 예를 들어 설명하라.

## 복습 질문
1. attention은 무엇의 비율을 계산하는가?
2. Transformer 블록에서 attention과 MLP는 각각 어떤 일을 하는가?
3. 위치 정보는 왜 따로 넣어야 하는가?

## 체크포인트
1. attention 식의 각 기호를 말로 풀 수 있다.
2. query, key, value의 분업을 설명할 수 있다.
3. softmax와 positional encoding의 필요성을 설명할 수 있다.
4. Transformer가 어떤 흐름으로 계산되는지 말할 수 있다.
