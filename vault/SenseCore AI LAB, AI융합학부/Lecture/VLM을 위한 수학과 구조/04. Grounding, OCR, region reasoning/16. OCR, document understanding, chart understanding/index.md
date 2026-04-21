---
title: "16. OCR, document understanding, chart understanding"
source_kind: page
---
문서, 차트, UI 화면은 일반 자연 이미지보다 훨씬 더 세밀한 구조를 요구합니다. 이 강의는 OCR과 document understanding, chart understanding이 왜 VLM에서 별도의 난제로 취급되는지 설명합니다.

# 먼저 알아둘 말
- OCR: 이미지 속 글자를 읽는 문제입니다.
- document understanding: 문서의 구조와 의미를 함께 해석하는 문제입니다.
- chart understanding: 축, 범례, 값 관계를 읽는 문제입니다.
- layout: 배치와 구조 정보입니다.

# 이 강의에서 답할 질문
- OCR은 왜 captioning보다 더 어려운가
- 문서 이해는 왜 텍스트 인식만으로 끝나지 않는가
- 차트 이해는 어떤 추가 reasoning을 요구하는가

# 왜 중요한가
- 업무형 VLM은 일반 이미지보다 문서와 UI, 표, 차트에서 더 자주 쓰입니다.
- 이 과제들은 resolution, layout, grounding 문제가 동시에 얽혀 있습니다.

# 이번 강의의 핵심 축
- 작은 문자와 고해상도 요구
- layout-aware understanding
- chart semantics와 visual relation
- OCR error가 reasoning error로 이어지는 방식

# 스스로 점검
1. OCR과 captioning의 차이를 설명하라.
2. document understanding이 layout를 필요로 하는 이유를 말하라.
3. chart understanding이 추가로 요구하는 reasoning을 설명하라.
