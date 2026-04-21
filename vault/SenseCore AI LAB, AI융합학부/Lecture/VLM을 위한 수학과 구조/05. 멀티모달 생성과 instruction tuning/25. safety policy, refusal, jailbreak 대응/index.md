---
title: "25. safety policy, refusal, jailbreak 대응"
source_kind: page
---
멀티모달 assistant는 잘 대답하는 것만큼 잘 멈추는 것도 중요합니다. 이 강의는 safety policy, refusal, jailbreak 대응을 멀티모달 관점에서 설명합니다.

# 먼저 알아둘 말
- safety policy: 허용되는 응답과 금지되는 응답 기준입니다.
- refusal: 위험하거나 불확실한 상황에서 답변을 거절하는 동작입니다.
- jailbreak: 안전 제한을 우회하려는 입력 패턴입니다.
- policy violation: 정책을 어기는 응답입니다.

# 이 강의에서 답할 질문
- 멀티모달 안전성은 텍스트-only와 무엇이 다른가
- refusal은 언제 필요하고 언제 과도해지는가
- jailbreak 대응은 왜 데이터와 시스템까지 함께 봐야 하는가

# 왜 중요한가
- 이미지가 붙으면 개인 정보, 민감 장면, 위험 지시 문제가 더 복잡해집니다.
- safety failure는 제품 신뢰와 운영 리스크를 동시에 키웁니다.

# 이번 강의의 핵심 축
- visual safety signal
- grounded refusal과 blanket refusal 차이
- adversarial multimodal prompt
- policy tuning과 user experience trade-off

# 스스로 점검
1. refusal이 필요한 이유를 설명하라.
2. 멀티모달 jailbreak가 어려운 이유를 말하라.
3. safety policy와 usability 사이의 trade-off를 설명하라.
