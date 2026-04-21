---
title: "40. CLIP, contrastive learning, multimodal alignment"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b9816ab4d7f6fcb3917b51__40. CLIP, contrastive learning, multimodal alignment
notion_id: 32ce313f58b9816ab4d7f6fcb3917b51
notion_url: https://www.notion.so/32ce313f58b9816ab4d7f6fcb3917b51
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
멀티모달 학습의 핵심은 "서로 다른 형태의 입력을 같은 뜻으로 연결하는 것"입니다. 이미지와 문장은 모양이 완전히 다르지만, 둘 다 같은 고양이를 가리킬 수 있습니다. CLIP은 이 연결을 shared embedding space라는 하나의 공통 좌표계 위에서 만들고, contrastive learning은 그 좌표계를 학습시키는 방법입니다. 이 강의에서는 왜 공통 좌표계가 필요한지부터 시작해, positive pair와 in-batch negative, temperature, 대칭 contrastive loss, zero-shot 분류까지 한 단계 더 깊게 설명합니다.

# 먼저 알아둘 말
- 모달리티: 이미지, 텍스트, 오디오처럼 서로 다른 입력 종류다.
- alignment: 서로 다른 모달리티의 표현이 같은 의미를 가리키게 맞추는 일이다.
- image encoder: 이미지를 벡터로 바꾸는 모듈이다.
- text encoder: 문장을 벡터로 바꾸는 모듈이다.
- positive pair: 실제로 서로 대응되는 이미지-텍스트 쌍이다.
- negative pair: 서로 대응되지 않는 쌍이다.
- in-batch negative: 같은 배치 안의 다른 샘플을 음성 예시로 쓰는 방식이다.
- contrastive loss: 맞는 쌍은 가깝게, 아닌 쌍은 멀게 만드는 손실이다.
- similarity: 두 벡터가 얼마나 비슷한지 나타내는 값이다.
- temperature: 유사도 점수의 분포를 더 날카롭게 또는 완만하게 만드는 스케일 파라미터다.
- shared embedding space: 서로 다른 모달리티가 같은 좌표계에서 비교되는 공간이다.
- zero-shot: 해당 클래스로 직접 학습하지 않았어도 설명만으로 판단하는 방식이다.
- CLIP: 이미지와 텍스트를 같은 공간에 정렬하는 대표 모델이다.

# 이 강의에서 답할 질문
- 왜 이미지와 텍스트를 같은 공간에 두려 하는가?
- contrastive loss는 무엇을 끌어당기고 무엇을 밀어내는가?
- positive, negative, in-batch negative는 각각 어떤 역할을 하는가?
- temperature는 왜 들어가는가?
- shared embedding space는 어떤 의미를 갖는가?
- CLIP은 왜 zero-shot 분류에 강한가?

# 먼저 떠올릴 장면
- 고양이 사진을 보고 `"a cat"`이라는 문장을 함께 보여 줍니다.
- 사람에게는 둘이 같은 뜻이지만, 모델에게는 하나는 픽셀 배열이고 다른 하나는 단어 시퀀스입니다.
- 이 둘이 같은 뜻이라는 사실을 배우려면, 서로 다른 입력을 비교할 수 있는 공통 좌표계가 필요합니다.
- CLIP은 바로 이 좌표계를 `"맞는 쌍은 당기고, 틀린 쌍은 밀기"`라는 규칙으로 학습합니다.

# 이 강의의 큰 그림
이 강의는 다음 순서로 읽는 것이 좋습니다.

1. 먼저 왜 서로 다른 모달리티를 같은 공간에 넣으려 하는지 봅니다.
2. 그다음 이미지와 텍스트를 각각 벡터로 바꾸는 구조를 설명합니다.
3. 이어서 positive pair와 negative pair를 정하고 contrastive loss를 봅니다.
4. 그 결과 shared embedding space가 어떤 의미 구조를 갖는지 설명합니다.
5. 마지막으로 zero-shot 분류와 retrieval가 왜 가능한지 연결합니다.

# 먼저 문제를 세우기
이미지 분류기와 언어 모델이 각각 잘 작동한다고 해서, 이미지와 문장을 함께 이해하는 것은 아닙니다. 멀티모달 시스템에서는:

- `"이 문장이 이 이미지와 맞는가?"`
- `"이 이미지에 어떤 문장이 가장 잘 대응되는가?"`
- `"이 질의문과 가장 가까운 이미지는 무엇인가?"`

를 판단할 수 있어야 합니다.

이를 위해서는 이미지와 텍스트를 비교 가능한 형태로 바꿔야 합니다. 픽셀과 단어는 원래 같은 공간에서 비교할 수 없기 때문입니다.

# CLIP의 기본 구조
CLIP은 이 문제를 `"둘 다 벡터로 바꾸고 같은 공간에서 비교하자"`는 방식으로 풉니다.

이미지 인코더와 텍스트 인코더의 출력을 각각

$$
z_{\text{img}}, \qquad z_{\text{text}}
$$

라고 하겠습니다. 중요한 점은 이 두 벡터가 같은 차원의 공통 공간 안에 놓인다는 것입니다. 이렇게 해야 이미지 벡터와 텍스트 벡터의 거리나 내적을 직접 비교할 수 있습니다.

보통은 길이 정규화를 적용해 코사인 유사도에 가까운 비교를 합니다.

$$
\hat{z}_{\text{img}}
=
\frac{z_{\text{img}}}{\|z_{\text{img}}\|},
\qquad
\hat{z}_{\text{text}}
=
\frac{z_{\text{text}}}{\|z_{\text{text}}\|}
$$

그러면 유사도는 보통 내적으로 적을 수 있습니다.

$$
\mathrm{sim}(i, j)
=
\hat{z}_{\text{img}, i}^{\top}\hat{z}_{\text{text}, j}
$$

# 왜 공통 공간이 필요한가
왜 굳이 공통 공간이 필요한지를 직관적으로 보면 간단합니다.

## 1. 이미지와 텍스트는 표현 형식이 다르다
이미지는 픽셀 격자이고, 텍스트는 토큰 시퀀스입니다. 원래는 직접 비교할 수 없습니다.

## 2. 비교 가능성 자체가 목표다
멀티모달 검색과 분류는 `"둘 중 어떤 것이 더 가깝나"`를 묻는 문제입니다. 그러려면 둘이 같은 좌표계 위에 있어야 합니다.

## 3. 의미를 거리로 바꾸고 싶다
같은 뜻은 가깝고, 다른 뜻은 멀게 만들면 검색과 분류가 단순한 nearest-neighbor 문제로 바뀝니다.

즉 shared embedding space는 단순한 기술적 편의가 아니라, `"의미를 거리 문제로 재표현"`하기 위한 핵심 설계입니다.

# positive pair와 negative pair
이제 학습 데이터에서 서로 실제로 대응되는 이미지-텍스트 쌍을 positive pair로 둡니다. 반대로 맞지 않는 조합은 negative pair로 둡니다.

예를 들어 배치 안에 다음 샘플이 있다고 합시다.

- 고양이 사진 - `"a cat"`
- 자동차 사진 - `"a car"`
- 바다 사진 - `"the ocean"`

그러면 첫 번째 이미지에 대해:

- `"a cat"`은 positive pair
- `"a car"`, `"the ocean"`은 negative pair

가 됩니다.

현대 contrastive learning에서는 배치 안의 다른 샘플들을 음성 예시로 쓰는 in-batch negative가 매우 중요합니다. 이것 덕분에 별도의 복잡한 음성 샘플링 없이도 많은 비교 후보를 만들 수 있습니다.

# contrastive loss를 식으로 읽기
CLIP류의 직관은 보통 다음과 같은 loss로 표현됩니다.

$$
L_{\text{img}\to\text{text}}
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
\tau
$$

는 temperature입니다.

이 식은 이미지 하나를 기준으로 `"어떤 텍스트가 정답인가"`를 맞히는 softmax 분류처럼 읽을 수 있습니다.

## 1. 분자
정답 텍스트와의 유사도를 크게 만듭니다.

## 2. 분모
배치 안의 여러 텍스트 후보 전체와 비교합니다.

## 3. temperature
유사도 분포를 얼마나 날카롭게 볼지를 조절합니다.

temperature가 작으면 차이가 더 크게 강조되고, 크면 분포가 더 완만해집니다.

# 대칭 학습이 왜 중요한가
CLIP은 보통 한 방향만 학습하지 않습니다.

- 이미지에서 정답 텍스트를 고르는 방향
- 텍스트에서 정답 이미지를 고르는 방향

을 함께 학습합니다.

즉

$$
L
=
\frac{1}{2}\Bigl(
L_{\text{img}\to\text{text}}
+
L_{\text{text}\to\text{img}}
\Bigr)
$$

처럼 대칭적으로 놓는 경우가 많습니다.

이 대칭 구조가 중요한 이유는:

1. 이미지 검색도 잘해야 하고
2. 텍스트 검색도 잘해야 하며
3. 두 방향 정렬이 함께 좋아져야
4. 공통 공간 자체가 더 안정적으로 형성되기 때문입니다.

# contrastive learning은 무엇을 배우는가
이 학습이 반복되면 shared embedding space가 만들어집니다. 이 공간에서는 `"같은 뜻"`이 거리나 내적으로 표현됩니다.

예를 들어:

- 고양이 사진은 `"a cat"` 근처로 갑니다.
- 자동차 사진은 `"a car"` 근처로 갑니다.
- `"a cat"`과 `"a dog"`는 어느 정도 가깝지만 `"a car"`와는 더 멀 수 있습니다.

즉 이 공간은 단순히 샘플을 암기하는 것이 아니라 의미 구조를 형성합니다. 그래서 zero-shot 일반화가 가능해집니다.

# shared embedding space는 어떤 구조인가
공통 공간은 다음 세 수준에서 이해할 수 있습니다.

## 1. 개별 쌍 정렬
맞는 이미지와 문장이 서로 가까워집니다.

## 2. 의미 군집 형성
비슷한 개념끼리 주변에 모입니다. 예를 들어 동물 관련 샘플끼리 어느 정도 이웃이 될 수 있습니다.

## 3. 모달 간 비교 가능성
이미지와 텍스트가 같은 의미 축 위에서 정렬되므로, 서로 다른 입력 형식을 직접 비교할 수 있습니다.

이 때문에 CLIP은 단순한 매칭 모델이 아니라 멀티모달 의미 표현학습의 기반 모델로 취급됩니다.

# zero-shot 분류는 왜 가능한가
CLIP이 zero-shot 분류에 강한 이유도 여기서 나옵니다. 새로운 클래스라도 텍스트 설명만 만들 수 있으면, 이미지와 그 설명의 유사도를 비교해 분류할 수 있습니다.

예를 들어 클래스 후보가:

- `"a photo of a cat"`
- `"a photo of a dog"`
- `"a photo of a car"`

라면, 이미지 임베딩을 이 문장 임베딩들과 비교해 가장 가까운 설명을 고르면 됩니다.

즉 고정된 숫자 클래스 헤드 없이도, 자연어 설명 자체가 분류 기준 역할을 하게 됩니다. 그래서 zero-shot 분류는 본질적으로 `"텍스트 라벨을 공통 공간의 프로토타입으로 쓰는 것"`이라고 볼 수 있습니다.

# retrieval 관점에서 보면 더 쉽다
CLIP을 retrieval 문제로 생각하면 이해가 더 쉽습니다.

## text-to-image retrieval
문장 쿼리를 넣고 가장 가까운 이미지 벡터를 찾습니다.

## image-to-text retrieval
이미지를 넣고 가장 가까운 문장 벡터를 찾습니다.

zero-shot 분류도 사실은 `"후보 설명 문장 중 가장 가까운 것을 찾는 retrieval"`의 한 형태로 볼 수 있습니다.

# CLIP의 한계도 같이 봐야 한다
CLIP은 강력하지만 만능은 아닙니다.

## 1. 세밀한 구성 관계 이해는 한계가 있다
`"빨간 공 위에 파란 컵"`과 `"파란 컵 위에 빨간 공"`처럼 관계가 섬세한 경우는 단순 정렬만으로 부족할 수 있습니다.

## 2. 텍스트 프롬프트에 민감할 수 있다
클래스 설명 문장을 어떻게 쓰느냐에 따라 zero-shot 결과가 달라질 수 있습니다.

## 3. 생성 모델은 아니다
CLIP은 기본적으로 정렬과 비교 모델이지, 긴 언어 생성 자체를 담당하는 구조는 아닙니다.

즉 CLIP은 `"같은 뜻을 맞춘다"`에는 강하지만, `"풍부한 언어 생성"`과 `"정교한 시각 추론"`까지 혼자 책임지지는 않습니다. 그래서 이후 VLM 구조가 필요해집니다.

# 자주 생기는 오해
## 오해 1. CLIP은 이미지 caption 모델이다
아닙니다. CLIP은 이미지와 텍스트를 같은 공간에 정렬하는 모델입니다.

## 오해 2. contrastive loss는 단순히 멀고 가깝게만 만든다
그 이상입니다. 전체 배치 안의 상대적 순위를 학습하고, 공통 의미 공간을 형성합니다.

## 오해 3. zero-shot 분류는 마법 같은 일반화다
사실은 텍스트 설명을 클래스 프로토타입처럼 사용하는 공통 공간 비교 문제입니다.

# 예제
1. positive pair의 의미
문제: 고양이 사진과 `"a cat"` 문장이 한 데이터 예시에서 함께 주어졌다면 어떤 쌍인가?
풀이: positive pair다.
해설: 서로 실제로 대응되는 이미지-텍스트 쌍이기 때문이다.

2. contrastive loss의 방향
문제: contrastive loss는 맞는 쌍과 틀린 쌍에 각각 어떤 힘을 가하는가?
풀이: 맞는 쌍은 가깝게 만들고, 틀린 쌍은 멀게 만든다.
해설: 공통 공간 안에서 의미 구조를 만드는 기본 원리다.

3. temperature의 역할
문제: contrastive loss에서 temperature는 무엇을 조절하는가?
풀이: 유사도 점수 분포를 얼마나 날카롭게 해석할지 조절한다.
해설: 점수 차이를 더 강하게 또는 더 완만하게 반영하는 스케일 파라미터다.

4. zero-shot 분류의 직관
문제: CLIP에서 텍스트 설명만으로 새 클래스를 분류할 수 있는 이유는 무엇인가?
풀이: 이미지와 텍스트가 같은 좌표계에 있으므로, 새 텍스트 설명도 즉시 비교 기준으로 쓸 수 있기 때문이다.
해설: 분류 기준을 고정된 번호표가 아니라 자연어 설명으로 바꿀 수 있다.

# 핵심 정리
- CLIP의 목표는 이미지와 텍스트를 같은 의미 공간에 정렬하는 것이다.
- positive pair는 당기고 negative pair는 민다.
- in-batch negative는 contrastive 학습을 효율적으로 만든다.
- temperature는 유사도 분포의 날카로움을 조절한다.
- shared embedding space가 만들어지면 retrieval와 zero-shot 분류가 가능해진다.
- CLIP은 멀티모달 생성 모델이 아니라 멀티모달 정렬 모델이다.

# 스스로 점검
## 연습 문제
1. shared embedding space가 왜 필요한지 설명하라.
2. positive pair와 negative pair를 예로 들어 설명하라.
3. in-batch negative가 왜 유용한지 설명하라.
4. contrastive loss가 어떤 구조를 만들려 하는지 설명하라.
5. temperature가 어떤 역할을 하는지 설명하라.
6. CLIP이 zero-shot 분류에 강한 이유를 말하라.

## 복습 질문
1. 이미지와 텍스트를 같은 공간에 맞춘다는 말은 무엇인가?
2. contrastive loss는 무엇을 당기고 무엇을 미는가?
3. 대칭 학습이 왜 중요한가?
4. CLIP은 왜 멀티모달의 기초 모델로 불리는가?

## 체크포인트
1. multimodal alignment의 목표를 설명할 수 있다.
2. shared embedding space의 의미를 이해한다.
3. contrastive loss와 temperature의 직관을 말할 수 있다.
4. CLIP과 zero-shot 분류의 관계를 설명할 수 있다.
