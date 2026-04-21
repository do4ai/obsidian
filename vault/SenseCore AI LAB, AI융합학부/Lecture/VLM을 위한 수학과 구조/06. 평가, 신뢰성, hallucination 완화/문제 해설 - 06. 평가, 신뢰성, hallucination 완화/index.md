---
title: "문제 해설 - 06. 평가, 신뢰성, hallucination 완화"
source_kind: page
---
이 해설 페이지는 점수만 보는 평가에서 벗어나, faithfulness와 calibration, human evaluation까지 함께 보는 관점을 굳히기 위한 페이지입니다.

# 이 해설 페이지의 역할
- benchmark와 evaluation protocol의 차이를 정리하게 합니다.
- hallucination taxonomy와 calibration 개념을 다시 읽게 합니다.
- verifier와 human evaluation이 어디에 필요한지 연결하게 합니다.

# 문제를 풀 때 확인할 것
- 리더보드 점수만으로 놓치는 품질 문제가 무엇인지 말할 수 있는가
- uncertainty와 abstention이 왜 실서비스에서 중요한지 설명할 수 있는가
- verifier와 retrieval grounding이 어떤 failure mode를 줄이는지 정리할 수 있는가

# 연결 복습
- 이 단계가 확실해야 7단계 시스템 확장과 8단계 논문 독해에서 평가의 허점을 더 잘 볼 수 있습니다.
