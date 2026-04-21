---
title: "17. box, mask, region token, spatial reference"
source_kind: page
---
질문이 “왼쪽 위의 버튼”이나 “빨간 상자 안의 객체”를 묻는 순간, VLM은 전역 설명을 넘어 특정 영역을 가리킬 수 있어야 합니다. 이 강의는 box, mask, region token, spatial reference를 설명합니다.

# 먼저 알아둘 말
- box: 사각형 영역으로 위치를 표시하는 방식입니다.
- mask: 픽셀 단위로 영역을 표시하는 방식입니다.
- region token: 특정 영역을 대표하는 토큰입니다.
- spatial reference: 위치를 가리키는 표현입니다.

# 이 강의에서 답할 질문
- 영역 표현은 왜 필요한가
- region token은 어떤 질의에서 중요한가
- spatial reference를 잘못 읽으면 어떤 오류가 나는가

# 왜 중요한가
- GUI understanding, document QA, referring expression은 모두 지역 정보가 핵심입니다.
- 전역 임베딩만으로는 위치 기반 질의를 처리하기 어렵습니다.

# 이번 강의의 핵심 축
- area-level representation
- region grounding과 spatial language alignment
- box와 mask supervision 차이
- 위치 표현이 reasoning과 연결되는 방식

# 스스로 점검
1. region token이 필요한 이유를 설명하라.
2. box와 mask의 차이를 말하라.
3. spatial reference가 중요한 과제를 예로 들어 설명하라.
