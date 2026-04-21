---
title: "3. resolution, stride, pooling, token budget"
source_kind: page
---
VLM은 더 많이 보면 더 잘 볼 것 같지만, 실제로는 resolution과 token budget 사이에서 끊임없이 타협합니다. 이 강의는 stride, pooling, compression이 성능과 비용을 어떻게 바꾸는지 설명합니다.

# 먼저 알아둘 말
- resolution: 입력 이미지의 해상도입니다.
- stride: 입력을 건너뛰며 읽는 간격입니다.
- pooling: 표현을 압축하는 연산입니다.
- token budget: 모델이 감당 가능한 토큰 수와 계산량 한계입니다.

# 이 강의에서 답할 질문
- 해상도를 높이면 언제 도움이 되고 언제 부담이 되는가
- stride와 pooling은 무엇을 잃고 무엇을 얻는가
- token budget은 왜 실제 VLM 설계의 핵심 제약인가

# 왜 중요한가
- document QA, UI understanding, chart reasoning은 고해상도 정보를 많이 요구합니다.
- 하지만 token이 늘어나면 attention 비용과 memory 비용이 급격히 커집니다.

# 이번 강의의 핵심 축
- information density와 compute cost trade-off
- downsampling이 작은 객체 인식에 미치는 영향
- OCR에서의 해상도 민감성
- long-context vision의 현실적 제약

# 스스로 점검
1. token budget이 무엇인지 설명하라.
2. stride와 pooling이 왜 필요한지 말하라.
3. 고해상도 입력이 항상 좋은 것은 아닌 이유를 설명하라.
