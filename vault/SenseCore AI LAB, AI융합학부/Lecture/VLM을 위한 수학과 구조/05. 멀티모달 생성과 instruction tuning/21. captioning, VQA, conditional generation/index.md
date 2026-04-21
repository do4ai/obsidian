---
title: "21. captioning, VQA, conditional generation"
source_kind: page
---
정렬된 표현이 실제로 말을 하려면 conditional generation 구조가 필요합니다. 이 강의는 captioning, VQA, chat-style response를 하나의 생성 문제로 묶어 설명합니다.

# 먼저 알아둘 말
- captioning: 이미지를 설명 문장으로 생성하는 과제입니다.
- VQA: 이미지와 질문을 함께 보고 답을 생성하는 과제입니다.
- conditional generation: 조건 입력에 맞춰 출력을 생성하는 방식입니다.
- decoder state: 현재까지 생성된 문맥을 담는 내부 상태입니다.

# 이 강의에서 답할 질문
- captioning과 VQA는 무엇이 같고 무엇이 다른가
- 조건 입력은 생성 과정에 어떻게 들어가는가
- 왜 정렬 모델만으로는 답변 생성이 부족한가

# 왜 중요한가
- 멀티모달 assistant의 핵심은 검색이 아니라 조건부 생성입니다.
- 생성형 과제를 이해해야 이후 tuning과 alignment를 읽을 수 있습니다.

# 이번 강의의 핵심 축
- image-conditioned next-token prediction
- question-conditioned answering
- retrieval형 표현과 generation형 표현의 차이
- 답변 품질과 grounding 연결

# 스스로 점검
1. captioning과 VQA의 차이를 설명하라.
2. conditional generation이 무엇인지 말하라.
3. alignment만으로 생성 문제를 해결할 수 없는 이유를 설명하라.
