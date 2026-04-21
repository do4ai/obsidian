---
title: "06. image-text pair, shared embedding, cosine similarity"
source_kind: page
---
멀티모달 정렬의 출발점은 이미지와 텍스트가 같은 뜻을 가리키게 만드는 것입니다. 이 강의에서는 image-text pair, shared embedding, cosine similarity가 왜 기본 좌표계인지 설명합니다.

# 먼저 알아둘 말
- image-text pair: 서로 대응되는 이미지와 텍스트 쌍입니다.
- embedding: 입력을 벡터로 옮긴 표현입니다.
- shared embedding: 이미지와 텍스트를 함께 놓는 공통 공간입니다.
- cosine similarity: 두 벡터 방향의 유사도를 재는 값입니다.

# 이 강의에서 답할 질문
- 공통 벡터 공간이 왜 필요한가
- cosine similarity는 무엇을 비교하는가
- alignment 문제는 왜 geometry 문제로 읽히는가

# 왜 중요한가
- retrieval, zero-shot transfer, prompt matching 모두 shared embedding 위에서 출발합니다.
- 이후 CLIP objective를 읽으려면 먼저 이 공간이 무엇을 의미하는지 이해해야 합니다.

# 이번 강의의 핵심 축
- 대응되는 쌍과 대응되지 않는 쌍
- semantic closeness와 vector geometry
- normalized embedding의 의미
- shared space가 retrieval을 가능하게 하는 이유

# 스스로 점검
1. shared embedding space의 의미를 설명하라.
2. cosine similarity가 무엇을 재는지 말하라.
3. 왜 정렬 문제를 기하학적으로 볼 수 있는지 설명하라.
