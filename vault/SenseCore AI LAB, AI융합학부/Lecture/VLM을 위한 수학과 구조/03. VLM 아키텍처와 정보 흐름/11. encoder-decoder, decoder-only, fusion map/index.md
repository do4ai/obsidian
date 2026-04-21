---
title: "11. encoder-decoder, decoder-only, fusion map"
source_kind: page
---
VLM 구조를 읽을 때 가장 먼저 볼 것은 이미지와 텍스트가 어디서 만나는가입니다. 이 강의는 encoder-decoder와 decoder-only VLM을 하나의 fusion map 위에서 비교합니다.

# 먼저 알아둘 말
- encoder-decoder: 입력을 읽는 인코더와 출력을 만드는 디코더가 분리된 구조입니다.
- decoder-only: 다음 토큰 예측 중심의 단일 생성 구조입니다.
- fusion point: 이미지와 텍스트가 결합되는 지점입니다.
- conditioning: 한 입력이 다른 출력을 조건짓는 방식입니다.

# 이 강의에서 답할 질문
- 두 구조는 정보를 어떻게 다르게 흐르게 하는가
- fusion point는 왜 구조 이해의 핵심인가
- 어떤 과제에서 어느 구조가 더 자연스러운가

# 왜 중요한가
- captioning, QA, chat-style assistant는 서로 다른 정보 흐름을 요구합니다.
- fusion map을 이해하면 복잡한 모델도 큰 구조부터 읽을 수 있습니다.

# 이번 강의의 핵심 축
- seq2seq와 autoregressive generation 비교
- early fusion과 late fusion의 직관
- 조건부 생성의 경로
- 구조 선택이 latency와 flexibility에 미치는 영향

# 스스로 점검
1. encoder-decoder와 decoder-only의 차이를 설명하라.
2. fusion point가 중요한 이유를 말하라.
3. 과제에 따라 구조 선택이 달라지는 이유를 설명하라.
