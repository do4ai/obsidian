---
title: "08. hard negative, retrieval, ranking"
source_kind: page
---
정렬이 잘되었는지는 결국 검색과 구분 능력에서 드러납니다. 이 강의에서는 hard negative와 retrieval, ranking 지표가 representation 품질을 어떻게 보여 주는지 설명합니다.

# 먼저 알아둘 말
- hard negative: 정답과 헷갈리기 쉬운 오답 예시입니다.
- retrieval: 한 모달에서 다른 모달의 대응 항목을 찾는 문제입니다.
- ranking: 후보를 점수 순으로 정렬하는 문제입니다.
- recall: 정답을 얼마나 잘 찾아오는지 보는 지표입니다.

# 이 강의에서 답할 질문
- 쉬운 negative만 쓰면 왜 한계가 생기는가
- retrieval은 alignment 품질을 어떻게 드러내는가
- ranking 지표는 실제 사용성과 어떻게 연결되는가

# 왜 중요한가
- 검색 품질은 zero-shot transfer와 downstream VLM 품질의 초기 신호가 되기도 합니다.
- hard negative를 이해해야 representation이 정말 세밀해졌는지 볼 수 있습니다.

# 이번 강의의 핵심 축
- confusion이 큰 음성 예시의 역할
- semantic granularity와 ranking quality
- false negative 문제
- retrieval benchmark를 읽는 관점

# 스스로 점검
1. hard negative가 왜 중요한지 설명하라.
2. retrieval과 ranking의 차이를 말하라.
3. alignment 품질이 검색 품질로 드러나는 이유를 설명하라.
