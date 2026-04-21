---
title: "문제 해설 - 05. 멀티모달 생성과 instruction tuning"
source_kind: page
---
이 해설 페이지는 멀티모달 assistant를 만들기 위한 tuning과 alignment 흐름을 다시 정리하는 페이지입니다.

# 이 해설 페이지의 역할
- conditional generation과 multimodal SFT의 차이를 정리하게 합니다.
- reward model과 RLHF, DPO를 비교하게 합니다.
- safety policy가 생성 품질과 어떻게 상호작용하는지 점검하게 합니다.

# 문제를 풀 때 확인할 것
- instruction data가 representation을 어떻게 재배열하는지 설명할 수 있는가
- RLHF와 DPO가 각각 어떤 장단점을 가지는지 말할 수 있는가
- refusal과 jailbreak 대응을 제품 관점에서 설명할 수 있는가

# 연결 복습
- 이 단계가 확실해야 6단계의 평가와 신뢰성 문제를 실제 제품 기준으로 읽을 수 있습니다.
