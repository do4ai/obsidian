---
title: "03. VLM 아키텍처와 정보 흐름"
source_kind: page
---
이 단계는 실제 VLM 구조를 읽는 단계입니다. image-text alignment를 넘어, vision token이 language model 안으로 언제 어떻게 들어가고, 어떤 connector가 정보를 압축하며, 왜 모델 계열마다 설계 선택이 달라지는지를 구조 관점에서 정리합니다.

# 이 단계에서 배우는 것
- encoder-decoder와 decoder-only VLM의 구조 차이를 배운다.
- early fusion, late fusion, fusion map을 비교한다.
- cross-attention, resampler, Q-Former 같은 연결기를 읽는다.
- frozen LM과 visual prompt 같은 parameter-efficient 전략을 이해한다.
- representative VLM family를 정보 흐름 기준으로 비교한다.

# 먼저 알고 갈 말
- fusion map: 이미지와 텍스트가 어느 층, 어느 방향에서 만나는지에 대한 구조 지도입니다.
- resampler: 많은 vision token을 더 작은 집합으로 압축하는 모듈입니다.
- frozen LM: 언어모델 본체는 고정하고 주변 모듈만 학습하는 방식입니다.
- token compression: 표현 수를 줄여 계산량을 낮추는 과정입니다.

# 이 단계를 읽는 순서
- 11강에서는 큰 구조 지도부터 잡는다.
- 12강에서는 cross-attention과 Q-Former 계열을 읽는다.
- 13강에서는 prefix와 visual prompt 전략을 본다.
- 14강에서는 token compression과 long context 문제를 정리한다.
- 15강에서는 대표 VLM 계열을 비교해 구조 감각을 굳힌다.

# 각 강의가 맡는 역할
- 11. encoder-decoder, decoder-only, fusion map: VLM 구조의 큰 지도 그리기.
- 12. cross-attention, perceiver resampler, Q-Former: 연결기와 압축기 비교.
- 13. prefix tuning, visual prompt, frozen LM: 경량 적응 전략 읽기.
- 14. token compression, memory, long context: 계산량과 문맥 길이 문제 이해.
- 15. representative VLM families 비교: 실제 모델 계열의 설계 선택 해석.

# 이 단계를 읽을 때 기억할 점
- 구조를 읽을 때는 이름보다 토큰이 어느 방향으로 흐르는지를 먼저 본다.
- 더 큰 connector가 항상 더 좋은 것은 아니며 계산량과 grounding trade-off가 있다.
- 이 단계는 뒤에서 배우는 OCR, reasoning, tuning이 어떤 구조 위에 서 있는지 이해하게 만든다.

# 이 단계를 마치면 할 수 있는 것
- 새로운 VLM 논문을 보면 먼저 fusion point와 connector를 찾을 수 있다.
- decoder-only와 encoder-decoder 접근의 차이를 설명할 수 있다.
- 대표 모델 계열의 장단점을 정보 흐름 기준으로 비교할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[11. encoder-decoder, decoder-only, fusion map](11. encoder-decoder, decoder-only, fusion map/index.md)
[12. cross-attention, perceiver resampler, Q-Former](12. cross-attention, perceiver resampler, Q-Former/index.md)
[13. prefix tuning, visual prompt, frozen LM](13. prefix tuning, visual prompt, frozen LM/index.md)
[14. token compression, memory, long context](14. token compression, memory, long context/index.md)
[15. representative VLM families 비교](15. representative VLM families 비교/index.md)
[문제 해설 - 03. VLM 아키텍처와 정보 흐름](문제 해설 - 03. VLM 아키텍처와 정보 흐름/index.md)

## Page Tree

- [11. encoder-decoder, decoder-only, fusion map](11. encoder-decoder, decoder-only, fusion map/index.md)
- [12. cross-attention, perceiver resampler, Q-Former](12. cross-attention, perceiver resampler, Q-Former/index.md)
- [13. prefix tuning, visual prompt, frozen LM](13. prefix tuning, visual prompt, frozen LM/index.md)
- [14. token compression, memory, long context](14. token compression, memory, long context/index.md)
- [15. representative VLM families 비교](15. representative VLM families 비교/index.md)
- [문제 해설 - 03. VLM 아키텍처와 정보 흐름](문제 해설 - 03. VLM 아키텍처와 정보 흐름/index.md)
