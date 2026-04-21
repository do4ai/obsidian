---
title: "37. mixture-of-experts, adaptive compute, token routing"
source_kind: page
---
모든 입력에 같은 계산량을 쓰는 것은 비효율적일 수 있습니다. 이 강의는 mixture-of-experts, adaptive compute, token routing이 계산 자원을 어떻게 분배하는지 설명합니다.

# 먼저 알아둘 말
- mixture-of-experts: 여러 전문가 모듈 중 일부만 활성화하는 구조입니다.
- adaptive compute: 입력 난이도에 따라 계산량을 다르게 쓰는 방식입니다.
- token routing: 토큰을 어떤 경로와 모듈로 보낼지 결정하는 과정입니다.
- sparse activation: 전체 모듈을 다 쓰지 않고 일부만 쓰는 활성화 방식입니다.

# 이 강의에서 답할 질문
- 왜 모든 토큰에 같은 연산을 쓰면 비효율적인가
- MoE는 어떤 비용 문제를 해결하려 하는가
- token routing은 멀티모달에서 왜 더 어렵나

# 왜 중요한가
- 고해상도 비전과 긴 비디오에서는 계산 자원 분배가 핵심 병목입니다.
- adaptive compute는 효율성과 성능을 동시에 노리는 중요한 연구 방향입니다.

# 이번 강의의 핵심 축
- sparse expert activation
- easy token과 hard token 분리
- routing error와 specialization failure
- multimodal compute allocation

# 스스로 점검
1. mixture-of-experts의 핵심 아이디어를 설명하라.
2. adaptive compute가 필요한 이유를 말하라.
3. token routing이 멀티모달에서 어려운 이유를 설명하라.
