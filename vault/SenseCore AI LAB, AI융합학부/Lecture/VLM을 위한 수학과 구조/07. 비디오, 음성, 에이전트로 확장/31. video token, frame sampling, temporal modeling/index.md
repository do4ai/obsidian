---
title: "31. video token, frame sampling, temporal modeling"
source_kind: page
---
비디오는 이미지에 시간축이 추가된 문제입니다. 이 강의는 video token, frame sampling, temporal modeling이 왜 새로운 구조 난제를 만드는지 설명합니다.

# 먼저 알아둘 말
- video token: 시간 정보를 포함한 시각 토큰입니다.
- frame sampling: 일부 프레임만 선택해 처리하는 전략입니다.
- temporal modeling: 시간 순서와 변화를 표현하는 방법입니다.
- event order: 사건의 순서를 이해하는 문제입니다.

# 이 강의에서 답할 질문
- 비디오는 왜 토큰 수를 폭발시키는가
- 모든 프레임을 다 보지 않아도 되는가
- 시간 순서를 무시하면 어떤 오류가 생기는가

# 왜 중요한가
- 비디오 요약, 행동 인식, 화면 녹화 분석은 이미지 VLM과 다른 구조를 요구합니다.
- temporal grounding은 정적 이미지에서 보지 못한 failure를 만듭니다.

# 이번 강의의 핵심 축
- spatial token과 temporal token 결합
- sampling과 정보 손실
- event reasoning
- long video context

# 스스로 점검
1. video token이 image token과 다른 점을 설명하라.
2. frame sampling이 필요한 이유를 말하라.
3. temporal modeling이 필요한 이유를 설명하라.
