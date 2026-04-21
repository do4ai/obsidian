---
title: "14. token compression, memory, long context"
source_kind: page
---
고해상도 이미지와 긴 비디오, 많은 대화 이력을 다루려면 토큰 수를 줄이고 필요한 정보만 오래 유지해야 합니다. 이 강의는 compression, memory, long context 문제를 설명합니다.

# 먼저 알아둘 말
- token compression: 토큰 수를 줄여 계산량을 낮추는 과정입니다.
- memory: 이전 정보를 유지하거나 재사용하는 구조입니다.
- long context: 매우 긴 입력 시퀀스를 처리하는 문제입니다.
- eviction: 오래된 정보를 버리는 정책입니다.

# 이 강의에서 답할 질문
- 무엇을 버리고 무엇을 남길 것인가
- memory가 없으면 어떤 과제에서 곧바로 한계가 드러나는가
- long context 문제는 vision과 language 양쪽에서 어떻게 다르게 나타나는가

# 왜 중요한가
- 현실의 멀티모달 시스템은 한 장 이미지보다 더 긴 문맥을 다뤄야 합니다.
- compression을 잘못하면 grounding에 필요한 디테일이 사라집니다.

# 이번 강의의 핵심 축
- compression과 faithfulness의 trade-off
- memory token과 cached state
- long image context와 long dialogue context 차이
- serving 비용과 context 길이의 관계

# 스스로 점검
1. token compression이 필요한 이유를 설명하라.
2. memory가 중요한 과제를 예로 들어라.
3. long context가 왜 단순히 더 긴 입력 이상의 문제인지 설명하라.
