---
title: "문제 해설 - 04. Grounding, OCR, region reasoning"
source_kind: page
---
이 해설 페이지는 VLM이 실제로 무엇을 보고 있는지를 묻는 단계입니다. grounded answer와 그럴듯한 hallucination을 구분할 수 있어야 합니다.

# 이 해설 페이지의 역할
- OCR과 chart understanding의 난점을 다시 정리하게 합니다.
- region token과 spatial reference를 복습하게 합니다.
- visual reasoning과 hallucination failure를 구조적으로 연결하게 합니다.

# 문제를 풀 때 확인할 것
- captioning과 grounded reasoning의 차이를 설명할 수 있는가
- 위치 표현과 영역 표현이 왜 중요한지 말할 수 있는가
- hallucination이 어느 구성요소에서 발생할 수 있는지 나눠 설명할 수 있는가

# 연결 복습
- 이 단계가 확실해야 5단계 alignment와 6단계 evaluation에서 무엇을 평가해야 하는지 선명해집니다.
