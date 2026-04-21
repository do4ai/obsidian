---
title: "10. data mixture, web-scale data, curriculum"
source_kind: page
---
어떤 데이터를 어떤 순서와 비율로 섞는지는 VLM 사전학습의 핵심입니다. 이 강의는 web-scale data와 curated data, curriculum 설계를 함께 설명합니다.

# 먼저 알아둘 말
- web-scale data: 웹에서 대규모로 수집한 데이터입니다.
- curated data: 품질 관리가 된 정제 데이터입니다.
- mixture ratio: 여러 데이터 원천을 섞는 비율입니다.
- curriculum: 학습 순서와 난이도 배치를 설계하는 방식입니다.

# 이 강의에서 답할 질문
- web-scale data는 무엇을 주고 무엇을 잃게 하는가
- curated data는 어디에서 특히 중요한가
- curriculum은 왜 학습 안정성과 능력 분화에 영향을 주는가

# 왜 중요한가
- 문서 이해, OCR, UI understanding은 일반 웹 캡션 데이터만으로는 부족할 수 있습니다.
- 데이터 조합은 모델의 상식, groundedness, instruction-following 모두에 영향을 줍니다.

# 이번 강의의 핵심 축
- noisy abundance와 clean scarcity의 trade-off
- domain-specific data의 필요성
- staged training과 mixture scheduling
- data design이 architecture 못지않게 중요한 이유

# 스스로 점검
1. web-scale data와 curated data의 차이를 설명하라.
2. mixture ratio가 중요한 이유를 말하라.
3. curriculum 설계가 모델 성격에 미치는 영향을 설명하라.
