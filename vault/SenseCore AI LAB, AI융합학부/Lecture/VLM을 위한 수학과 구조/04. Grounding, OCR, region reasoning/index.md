---
title: "04. Grounding, OCR, region reasoning"
source_kind: page
---
이 단계는 VLM이 실제로 무엇을 보고 있는지 시험하는 단계입니다. 단순 captioning에서 멈추지 않고, OCR, region reference, counting, visual reasoning을 통해 grounding이 왜 핵심 품질 기준인지 구조적으로 이해합니다.

# 이 단계에서 배우는 것
- OCR과 document understanding이 왜 고해상도 문제인지 배운다.
- box, mask, region token, spatial reference가 어떻게 쓰이는지 읽는다.
- referring expression과 counting 같은 세밀한 reasoning 과제를 이해한다.
- multimodal chain-of-thought가 visual reasoning에 미치는 영향을 본다.
- grounding failure와 hallucination이 구조적으로 어떻게 생기는지 정리한다.

# 먼저 알고 갈 말
- grounding: 답변이 실제 시각 입력과 연결되어 있는 성질입니다.
- spatial reference: 왼쪽, 위, 가운데처럼 위치를 가리키는 표현입니다.
- region token: 특정 영역 표현을 따로 다루는 토큰입니다.
- hallucination: 입력에 없는 내용을 그럴듯하게 만들어 내는 오류입니다.

# 이 단계를 읽는 순서
- 16강에서는 OCR과 문서 이해를 본다.
- 17강에서는 영역 표현과 위치 참조를 읽는다.
- 18강에서는 region reasoning과 counting을 정리한다.
- 19강에서는 visual reasoning과 chain-of-thought를 본다.
- 20강에서는 grounding failure가 왜 생기는지 구조로 묶는다.

# 각 강의가 맡는 역할
- 16. OCR, document understanding, chart understanding: 문자와 구조 정보 읽기.
- 17. box, mask, region token, spatial reference: 영역 표현과 위치 참조 이해.
- 18. referring expression, region reasoning, counting: 세밀한 grounded reasoning 읽기.
- 19. multimodal chain-of-thought와 visual reasoning: 추론 과정과 근거 연결.
- 20. grounding failure와 hallucination의 구조: 오류 메커니즘 정리.

# 이 단계를 읽을 때 기억할 점
- 유창한 답변은 grounded한 답변과 다르다.
- OCR 실패는 단순 vision 문제라기보다 resolution, token budget, structure 이해의 결합 문제일 수 있다.
- grounding을 이해해야 뒤 단계의 alignment와 evaluation도 제대로 읽을 수 있다.

# 이 단계를 마치면 할 수 있는 것
- region reasoning과 captioning의 차이를 설명할 수 있다.
- OCR과 spatial reference가 왜 어려운지 구조적으로 말할 수 있다.
- hallucination이 어디서 생기는지 vision, connector, LM 관점으로 나눠 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[16. OCR, document understanding, chart understanding](16. OCR, document understanding, chart understanding/index.md)
[17. box, mask, region token, spatial reference](17. box, mask, region token, spatial reference/index.md)
[18. referring expression, region reasoning, counting](18. referring expression, region reasoning, counting/index.md)
[19. multimodal chain-of-thought와 visual reasoning](19. multimodal chain-of-thought와 visual reasoning/index.md)
[20. grounding failure와 hallucination의 구조](20. grounding failure와 hallucination의 구조/index.md)
[문제 해설 - 04. Grounding, OCR, region reasoning](문제 해설 - 04. Grounding, OCR, region reasoning/index.md)

## Page Tree

- [16. OCR, document understanding, chart understanding](16. OCR, document understanding, chart understanding/index.md)
- [17. box, mask, region token, spatial reference](17. box, mask, region token, spatial reference/index.md)
- [18. referring expression, region reasoning, counting](18. referring expression, region reasoning, counting/index.md)
- [19. multimodal chain-of-thought와 visual reasoning](19. multimodal chain-of-thought와 visual reasoning/index.md)
- [20. grounding failure와 hallucination의 구조](20. grounding failure와 hallucination의 구조/index.md)
- [문제 해설 - 04. Grounding, OCR, region reasoning](문제 해설 - 04. Grounding, OCR, region reasoning/index.md)
