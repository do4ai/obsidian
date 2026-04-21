---
title: "34. GUI agent, robotics, embodied reasoning"
source_kind: page
---
VLM이 화면을 보고 클릭하거나, 카메라를 보고 행동하려면 perception만으로는 부족합니다. 이 강의는 GUI agent, robotics, embodied reasoning을 설명합니다.

# 먼저 알아둘 말
- GUI agent: 화면을 보고 조작하는 에이전트입니다.
- robotics: 센서 입력을 바탕으로 실제 행동을 수행하는 시스템입니다.
- embodied reasoning: 관찰과 행동이 결합된 추론입니다.
- action space: 모델이 선택할 수 있는 행동 집합입니다.

# 이 강의에서 답할 질문
- 보는 것과 행동하는 것은 무엇이 다른가
- GUI agent는 왜 grounding이 더 중요해지는가
- embodied setting에서 world model이 왜 필요해지는가

# 왜 중요한가
- agent는 오답 설명보다 잘못된 행동이 더 큰 피해를 만들 수 있습니다.
- perception failure가 곧 action failure로 이어지므로 안전성과 검증이 더 중요합니다.

# 이번 강의의 핵심 축
- perception-to-action pipeline
- screen grounding과 action selection
- closed-loop interaction
- safety in embodied systems

# 스스로 점검
1. GUI agent와 일반 VLM chat의 차이를 설명하라.
2. embodied reasoning이 필요한 이유를 말하라.
3. action failure가 왜 더 위험한지 설명하라.
