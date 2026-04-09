---
title: "40. CLIP, contrastive learning, multimodal alignment"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b9816ab4d7f6fcb3917b51__40. CLIP, contrastive learning, multimodal alignment
notion_id: 32ce313f58b9816ab4d7f6fcb3917b51
notion_url: https://www.notion.so/32ce313f58b9816ab4d7f6fcb3917b51
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
멀티모달 학습의 핵심은 "서로 다른 형태의 입력을 같은 뜻으로 연결하는 것"입니다. 이미지와 문장은 모양이 완전히 다르지만, 둘 다 같은 고양이를 가리킬 수 있습니다. CLIP은 이 연결을 shared embedding space라는 하나의 공통 좌표계 위에서 만들고, contrastive learning은 그 좌표계를 학습시키는 방법입니다. 이 강의에서는 왜 공통 좌표계가 필요한지부터 시작해, positive pair와 negative pair, contrastive loss, zero-shot 분류까지 순서대로 설명합니다.

# 먼저 알아둘 말
- 모달리티: 이미지, 텍스트, 오디오처럼 서로 다른 입력 종류다.
- alignment: 서로 다른 모달리티의 표현이 같은 의미를 가리키게 맞추는 일이다.
- image encoder: 이미지를 벡터로 바꾸는 모듈이다.
- text encoder: 문장을 벡터로 바꾸는 모듈이다.
- positive pair: 실제로 서로 대응되는 이미지-텍스트 쌍이다.
- negative pair: 서로 대응되지 않는 쌍이다.
- contrastive loss: 맞는 쌍은 가깝게, 아닌 쌍은 멀게 만드는 손실이다.
- shared embedding space: 서로 다른 모달리티가 같은 좌표계에서 비교되는 공간이다.
- zero-shot: 해당 클래스로 직접 학습하지 않았어도 설명만으로 판단하는 방식이다.
- CLIP: 이미지와 텍스트를 같은 공간에 정렬하는 대표 모델이다.

# 이 강의에서 답할 질문
- 왜 이미지와 텍스트를 같은 공간에 두려 하는가?
- contrastive loss는 무엇을 끌어당기고 무엇을 밀어내는가?
- shared embedding space는 어떤 의미를 갖는가?
- CLIP은 왜 zero-shot 분류에 강한가?

# 먼저 떠올릴 장면
- 고양이 사진을 보고 "a cat"이라는 문장을 함께 보여 줍니다.
- 사람에게는 둘이 같은 뜻이지만, 모델에게는 하나는 픽셀 배열이고 다른 하나는 단어 시퀀스입니다.
- 이 둘이 같은 뜻이라는 사실을 배우려면, 서로 다른 입력을 비교할 수 있는 공통 좌표계가 필요합니다.

# 생각의 순서
1. 먼저 왜 서로 다른 모달리티를 같은 좌표계에 넣으려 하는지 봅니다.
2. 그다음 이미지와 텍스트를 각각 벡터로 바꾸는 과정을 설명합니다.
3. 이어서 positive pair와 negative pair를 정하고 contrastive loss를 봅니다.
4. 그 결과 shared embedding space가 어떤 구조를 갖는지 설명합니다.
5. 마지막으로 zero-shot 분류가 왜 가능한지 연결합니다.

# 본문
이미지 분류기와 언어 모델이 각각 잘 작동한다고 해서, 이미지와 문장을 함께 이해하는 것은 아닙니다. 멀티모달 시스템에서는 "이 문장이 이 이미지와 맞는가?", "이 이미지에 어떤 문장이 가장 잘 대응되는가?"를 판단할 수 있어야 합니다. 이를 위해서는 이미지와 텍스트를 비교 가능한 형태로 바꿔야 합니다.

CLIP은 이 문제를 "둘 다 벡터로 바꾸고 같은 공간에서 비교하자"는 방식으로 풉니다. 이미지 인코더와 텍스트 인코더의 출력을 각각

$$
z_{\text{img}}, \qquad z_{\text{text}}
$$

라고 하겠습니다. 중요한 점은 이 두 벡터가 같은 차원의 공통 공간 안에 놓인다는 것입니다. 이렇게 해야 이미지 벡터와 텍스트 벡터의 거리나 내적을 직접 비교할 수 있습니다.

왜 공통 공간이 필요한지를 직관적으로 보면 간단합니다. 이미지와 텍스트는 원래 표현 방식이 너무 다릅니다. 픽셀과 단어는 직접 비교할 수 없습니다. 하지만 둘을 같은 의미 축을 가진 벡터 공간으로 보낸다면, "같은 뜻은 가깝고 다른 뜻은 멀다"라는 규칙을 적용할 수 있습니다.

이제 학습 데이터에서 서로 실제로 대응되는 이미지-텍스트 쌍을 positive pair로 둡니다. 반대로 맞지 않는 조합은 negative pair로 둡니다. 모델은 positive pair는 가까워지게 만들고, negative pair는 멀어지게 만들고 싶어 합니다.

이 직관은 보통 다음과 같은 contrastive loss로 표현됩니다.

$$
L
=
-\log
\frac{
\exp(\mathrm{sim}(z_{\text{img}}, z_{\text{text}}^+)/\tau)
}{
\sum_j \exp(\mathrm{sim}(z_{\text{img}}, z_{\text{text},j})/\tau)
}
$$

여기서

$$
z_{\text{text}}^+
$$

는 실제로 맞는 문장 벡터이고, 분모에는 현재 이미지와 비교되는 여러 문장 후보가 들어갑니다. 이 식의 뜻은 단순합니다. 정답 문장과의 유사도는 높이고, 다른 문장들과는 구분되게 만들겠다는 것입니다.

이 학습이 반복되면 shared embedding space가 만들어집니다. 이 공간에서는 "같은 뜻"이 거리나 내적으로 표현됩니다. 예를 들어 고양이 사진은 "a cat" 문장 근처로 가고, 자동차 사진은 "a car" 문장 근처로 갑니다. 결국 서로 다른 모달리티가 같은 의미 축 위에서 비교될 수 있게 됩니다.

이 공통 좌표계가 중요한 이유는 단순한 검색을 넘어서기 때문입니다. 이미지 검색에서는 문장 쿼리와 가까운 이미지를 찾을 수 있고, 반대로 이미지 설명도 텍스트 공간에서 찾을 수 있습니다. 더 나아가 이 정렬이 되어 있어야 VLM에서 시각 정보와 언어 정보를 함께 다루는 질의응답이 가능해집니다.

CLIP이 zero-shot 분류에 강한 이유도 여기서 나옵니다. 새로운 클래스라도 텍스트 설명만 만들 수 있으면, 이미지와 그 설명의 유사도를 비교해 분류할 수 있습니다. 즉 고정된 숫자 클래스 헤드 없이도, 자연어 설명 자체가 분류 기준 역할을 하게 됩니다. 그래서 CLIP은 단순한 이미지-텍스트 매칭 모델이 아니라, 멀티모달 표현학습의 기초 모델로 취급됩니다.

# 예제
1. positive pair의 의미
문제: 고양이 사진과 "a cat" 문장이 한 데이터 예시에서 함께 주어졌다면 어떤 쌍인가?
풀이: positive pair다.
해설: 서로 실제로 대응되는 이미지-텍스트 쌍이기 때문이다.

2. contrastive loss의 방향
문제: contrastive loss는 맞는 쌍과 틀린 쌍에 각각 어떤 힘을 가하는가?
풀이: 맞는 쌍은 가깝게 만들고, 틀린 쌍은 멀게 만든다.
해설: 공통 공간 안에서 의미 구조를 만드는 기본 원리다.

3. zero-shot 분류의 직관
문제: CLIP에서 텍스트 설명만으로 새 클래스를 분류할 수 있는 이유는 무엇인가?
풀이: 이미지와 텍스트가 같은 좌표계에 있으므로, 새 텍스트 설명도 즉시 비교 기준으로 쓸 수 있기 때문이다.
해설: 분류 기준을 고정된 번호표가 아니라 자연어 설명으로 바꿀 수 있다.

# 스스로 점검
## 연습 문제
1. shared embedding space가 왜 필요한지 설명하라.
2. positive pair와 negative pair를 예로 들어 설명하라.
3. contrastive loss가 어떤 구조를 만들려 하는지 설명하라.
4. CLIP이 zero-shot 분류에 강한 이유를 말하라.

## 복습 질문
1. 이미지와 텍스트를 같은 공간에 맞춘다는 말은 무엇인가?
2. contrastive loss는 무엇을 당기고 무엇을 미는가?
3. CLIP은 왜 멀티모달의 기초 모델로 불리는가?

## 체크포인트
1. multimodal alignment의 목표를 설명할 수 있다.
2. shared embedding space의 의미를 이해한다.
3. contrastive loss의 직관을 말할 수 있다.
4. CLIP과 zero-shot 분류의 관계를 설명할 수 있다.
