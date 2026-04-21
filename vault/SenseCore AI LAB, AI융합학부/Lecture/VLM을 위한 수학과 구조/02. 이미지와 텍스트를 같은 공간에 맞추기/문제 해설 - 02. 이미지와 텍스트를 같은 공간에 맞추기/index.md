---
title: "문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기"
source_kind: page
---
이 해설 페이지는 contrastive learning과 multimodal pretraining objective를 읽은 뒤, 정렬 문제를 실제 검색과 생성의 출발점으로 이해했는지 점검하기 위한 페이지입니다.

# 이 해설 페이지의 역할
- shared embedding과 contrastive loss를 말로 다시 읽게 합니다.
- hard negative와 temperature가 왜 중요한지 설명하게 합니다.
- data mixture가 모델 성격을 어떻게 바꾸는지 정리하게 합니다.

# 문제를 풀 때 확인할 것
- CLIP objective가 무엇을 가깝게 하고 무엇을 멀게 하는지 설명할 수 있는가
- retrieval 품질과 representation geometry의 관계를 말할 수 있는가
- web-scale data와 curated data의 역할을 구분할 수 있는가

# 연결 복습
- 이 단계가 확실해야 3단계 구조 비교와 5단계 생성형 tuning을 자연스럽게 읽을 수 있습니다.
