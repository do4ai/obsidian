---
title: "20. grounding failure와 hallucination의 구조"
source_kind: page
---
VLM hallucination은 단순한 “거짓말”이 아니라, 시각 근거와 언어 생성이 약하게 연결될 때 생기는 구조적 실패입니다. 이 강의는 grounding failure를 체계적으로 설명합니다.

# 먼저 알아둘 말
- grounding failure: 시각 입력과 답변 연결이 약해지는 실패입니다.
- object hallucination: 없는 객체를 있다고 말하는 오류입니다.
- relation hallucination: 관계를 잘못 설명하는 오류입니다.
- language prior: 자주 보던 언어 패턴에 끌리는 경향입니다.

# 이 강의에서 답할 질문
- hallucination은 어디에서 생기는가
- 왜 유창한 답이 더 위험할 수 있는가
- grounding failure를 어떤 구조와 데이터 문제가 키우는가

# 왜 중요한가
- 이 문제를 이해해야 alignment와 evaluation, verifier 설계를 제대로 읽을 수 있습니다.
- hallucination 완화는 모델 구조, 데이터, decoding 정책을 함께 봐야 합니다.

# 이번 강의의 핵심 축
- vision underuse와 language overreliance
- connector bottleneck과 detail loss
- noisy supervision과 fake grounding
- grounded answer와 plausible answer의 차이

# 스스로 점검
1. grounding failure와 hallucination의 관계를 설명하라.
2. object hallucination과 relation hallucination을 구분하라.
3. 왜 유창함이 정답성을 보장하지 않는지 설명하라.
