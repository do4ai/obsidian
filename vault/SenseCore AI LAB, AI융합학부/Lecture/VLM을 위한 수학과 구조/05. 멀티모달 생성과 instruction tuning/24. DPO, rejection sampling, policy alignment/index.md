---
title: "24. DPO, rejection sampling, policy alignment"
source_kind: page
---
RLHF는 강력하지만 복잡합니다. 이 강의는 DPO, rejection sampling, policy alignment 같은 대안 접근을 비교합니다.

# 먼저 알아둘 말
- DPO: 선호 비교를 직접 최적화하는 방식입니다.
- rejection sampling: 여러 후보를 생성한 뒤 더 나은 것을 골라 남기는 방식입니다.
- policy alignment: 모델 응답 분포를 원하는 방향으로 맞추는 과정입니다.
- reference model: 비교의 기준이 되는 모델입니다.

# 이 강의에서 답할 질문
- DPO는 RLHF와 무엇이 다른가
- rejection sampling은 언제 실용적인가
- alignment 대안들은 어떤 trade-off를 가지는가

# 왜 중요한가
- 실무에서는 RLHF 전체 파이프라인보다 더 가벼운 방법이 필요할 때가 많습니다.
- 멀티모달 환경에서는 reward 신뢰도가 낮아 대안 접근이 더 매력적일 수 있습니다.

# 이번 강의의 핵심 축
- direct preference optimization의 직관
- candidate generation과 selection
- stability와 implementation complexity
- alignment quality와 compute cost

# 스스로 점검
1. DPO가 무엇을 직접 최적화하는지 설명하라.
2. rejection sampling의 장단점을 말하라.
3. policy alignment 대안이 필요한 이유를 설명하라.
