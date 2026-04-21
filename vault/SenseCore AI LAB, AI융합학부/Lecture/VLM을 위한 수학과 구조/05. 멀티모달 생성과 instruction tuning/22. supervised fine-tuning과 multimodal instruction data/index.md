---
title: "22. supervised fine-tuning과 multimodal instruction data"
source_kind: page
---
사전학습된 VLM이 대화형 assistant처럼 동작하려면 instruction data가 필요합니다. 이 강의는 multimodal SFT와 instruction data 설계를 설명합니다.

# 먼저 알아둘 말
- supervised fine-tuning: 정답 응답을 직접 따라 하도록 학습하는 과정입니다.
- instruction data: 사용자의 지시와 기대 응답이 짝지어진 데이터입니다.
- response format: 답변이 어떤 형식과 말투를 따를지 정한 구조입니다.
- data curation: 데이터를 정리하고 품질 관리하는 작업입니다.

# 이 강의에서 답할 질문
- multimodal instruction data는 무엇을 추가로 담아야 하는가
- SFT는 모델의 어떤 행동을 바꾸는가
- 단순 QA 데이터와 instruction data는 어떻게 다른가

# 왜 중요한가
- assistant 품질은 대부분 이 단계에서 사람 친화적인 형태로 정리됩니다.
- ground truth가 있어도 형식과 근거 제시 방식은 별도로 훈련해야 합니다.

# 이번 강의의 핵심 축
- instruction-following behavior
- reasoning trace와 answer formatting
- multimodal conversational data의 특수성
- noisy instruction data의 위험

# 스스로 점검
1. SFT의 목적을 설명하라.
2. multimodal instruction data가 필요한 이유를 말하라.
3. 단순 QA 데이터와 instruction data의 차이를 설명하라.
