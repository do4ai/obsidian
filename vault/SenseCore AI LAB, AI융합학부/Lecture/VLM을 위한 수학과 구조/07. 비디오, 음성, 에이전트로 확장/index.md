---
title: "07. 비디오, 음성, 에이전트로 확장"
source_kind: page
---
이 단계는 이미지 VLM이 실제 멀티모달 시스템으로 넓어지는 모습을 보는 단계입니다. 비디오, 음성, multimodal RAG, GUI agent, serving 문제까지 묶어, VLM이 더 이상 단일 모델 문제가 아니라 시스템 문제라는 점을 이해합니다.

# 이 단계에서 배우는 것
- 비디오 토큰과 temporal modeling이 왜 새로운 계산 문제를 만드는지 배운다.
- 음성과 spoken dialogue가 붙을 때 구조가 어떻게 확장되는지 이해한다.
- multimodal RAG와 tool use가 retrieval와 planning 문제를 어떻게 바꾸는지 본다.
- GUI agent와 robotics가 embodied reasoning을 왜 요구하는지 정리한다.
- latency, serving, cost optimization이 실제 배포에서 왜 중요한지 읽는다.

# 먼저 알고 갈 말
- temporal modeling: 시간 순서가 있는 입력을 처리하는 방식입니다.
- spoken dialogue: 음성 입력과 출력이 포함된 대화 구조입니다.
- tool use: 외부 도구 호출을 문제 해결 루프에 넣는 방식입니다.
- serving: 실제 사용자 요청을 빠르고 안정적으로 처리하는 배포 운영입니다.

# 이 단계를 읽는 순서
- 31강에서는 비디오 토큰과 frame sampling을 본다.
- 32강에서는 음성과 spoken dialogue 확장을 읽는다.
- 33강에서는 multimodal RAG와 tool use를 정리한다.
- 34강에서는 GUI agent와 embodied reasoning을 본다.
- 35강에서는 latency와 serving 이슈를 제품 관점에서 읽는다.

# 각 강의가 맡는 역할
- 31. video token, frame sampling, temporal modeling: 시간축 확장 이해.
- 32. speech, audio, spoken dialogue extension: 오디오 모달 확장 읽기.
- 33. multimodal RAG, memory, tool use: 검색과 외부 도구 연결.
- 34. GUI agent, robotics, embodied reasoning: 행동이 붙은 멀티모달 시스템 읽기.
- 35. latency, serving, cost optimization: 실제 배포 운영 기준 세우기.

# 이 단계를 읽을 때 기억할 점
- 비디오와 에이전트는 단순히 입력 모달 하나가 추가되는 문제가 아니다.
- memory와 retrieval가 붙으면 모델 오류와 시스템 오류가 함께 생긴다.
- 실서비스에서는 품질뿐 아니라 latency와 cost가 아키텍처 선택을 바꾼다.

# 이 단계를 마치면 할 수 있는 것
- 이미지 VLM과 비디오/에이전트 시스템의 차이를 구조적으로 설명할 수 있다.
- multimodal RAG가 왜 단순 검색 이상의 문제인지 말할 수 있다.
- serving과 cost 제약이 모델 설계에 미치는 영향을 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[31. video token, frame sampling, temporal modeling](31. video token, frame sampling, temporal modeling/index.md)
[32. speech, audio, spoken dialogue extension](32. speech, audio, spoken dialogue extension/index.md)
[33. multimodal RAG, memory, tool use](33. multimodal RAG, memory, tool use/index.md)
[34. GUI agent, robotics, embodied reasoning](34. GUI agent, robotics, embodied reasoning/index.md)
[35. latency, serving, cost optimization](35. latency, serving, cost optimization/index.md)
[문제 해설 - 07. 비디오, 음성, 에이전트로 확장](문제 해설 - 07. 비디오, 음성, 에이전트로 확장/index.md)

## Page Tree

- [31. video token, frame sampling, temporal modeling](31. video token, frame sampling, temporal modeling/index.md)
- [32. speech, audio, spoken dialogue extension](32. speech, audio, spoken dialogue extension/index.md)
- [33. multimodal RAG, memory, tool use](33. multimodal RAG, memory, tool use/index.md)
- [34. GUI agent, robotics, embodied reasoning](34. GUI agent, robotics, embodied reasoning/index.md)
- [35. latency, serving, cost optimization](35. latency, serving, cost optimization/index.md)
- [문제 해설 - 07. 비디오, 음성, 에이전트로 확장](문제 해설 - 07. 비디오, 음성, 에이전트로 확장/index.md)
