---
title: "02. 이미지와 텍스트를 같은 공간에 맞추기"
source_kind: page
---
이 단계는 이미지와 텍스트가 같은 뜻을 향해 어떻게 정렬되는지를 배우는 단계입니다. shared embedding을 만들고, CLIP objective와 retrieval 구조를 이해하며, 실제 VLM 사전학습이 어떤 loss 조합과 데이터 설계 위에 서 있는지 정리합니다.

# 이 단계에서 배우는 것
- image-text pair가 공통 표현 공간으로 맞춰지는 과정을 배운다.
- cosine similarity, contrastive loss, in-batch negative를 읽는다.
- retrieval과 ranking이 정렬 품질을 어떻게 드러내는지 이해한다.
- matching, captioning, contrastive objective를 어떻게 조합하는지 본다.
- data mixture와 curriculum이 모델 성격을 어떻게 바꾸는지 정리한다.

# 먼저 알고 갈 말
- 정렬: 서로 다른 모달이 같은 의미를 가리키게 만드는 과정입니다.
- shared embedding: 이미지와 텍스트를 함께 놓는 공통 벡터 공간입니다.
- negative pair: 서로 대응되지 않는 샘플 쌍입니다.
- curriculum: 학습 순서와 데이터 비율을 설계하는 방식입니다.

# 이 단계를 읽는 순서
- 6강에서는 image-text pair와 cosine similarity를 읽는다.
- 7강에서는 CLIP objective와 temperature를 정리한다.
- 8강에서는 hard negative와 retrieval를 본다.
- 9강에서는 여러 pretraining objective를 어떻게 섞는지 읽는다.
- 10강에서는 web-scale data와 curated data의 역할을 비교한다.

# 각 강의가 맡는 역할
- 06. image-text pair, shared embedding, cosine similarity: 정렬 문제의 기본 좌표계 세우기.
- 07. CLIP objective, in-batch negative, temperature: contrastive learning 핵심 계산 읽기.
- 08. hard negative, retrieval, ranking: 정렬 품질과 검색 성능 연결.
- 09. captioning, matching, contrastive objective 조합: 실제 사전학습 설계 읽기.
- 10. data mixture, web-scale data, curriculum: 데이터 설계와 스케줄링 이해.

# 이 단계를 읽을 때 기억할 점
- 멀티모달 정렬은 단순 분류보다 representation geometry 문제에 가깝다.
- loss만 좋다고 끝나지 않고, negative의 질과 데이터 혼합 방식이 함께 중요하다.
- 이후 generation 단계도 여기서 배운 alignment 품질의 영향을 크게 받는다.

# 이 단계를 마치면 할 수 있는 것
- CLIP류 objective를 식 없이도 말로 설명할 수 있다.
- retrieval 성능과 embedding 품질의 관계를 말할 수 있다.
- 여러 pretraining objective가 왜 함께 쓰이는지 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[06. image-text pair, shared embedding, cosine similarity](06. image-text pair, shared embedding, cosine similarity/index.md)
[07. CLIP objective, in-batch negative, temperature](07. CLIP objective, in-batch negative, temperature/index.md)
[08. hard negative, retrieval, ranking](08. hard negative, retrieval, ranking/index.md)
[09. captioning, matching, contrastive objective 조합](09. captioning, matching, contrastive objective 조합/index.md)
[10. data mixture, web-scale data, curriculum](10. data mixture, web-scale data, curriculum/index.md)
[문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)

## Page Tree

- [06. image-text pair, shared embedding, cosine similarity](06. image-text pair, shared embedding, cosine similarity/index.md)
- [07. CLIP objective, in-batch negative, temperature](07. CLIP objective, in-batch negative, temperature/index.md)
- [08. hard negative, retrieval, ranking](08. hard negative, retrieval, ranking/index.md)
- [09. captioning, matching, contrastive objective 조합](09. captioning, matching, contrastive objective 조합/index.md)
- [10. data mixture, web-scale data, curriculum](10. data mixture, web-scale data, curriculum/index.md)
- [문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
