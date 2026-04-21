---
title: "33. multimodal RAG, memory, tool use"
source_kind: page
---
모델이 모든 것을 내부에 기억할 수는 없으므로, 외부 검색과 도구 호출이 붙습니다. 이 강의는 multimodal RAG, memory, tool use를 설명합니다.

# 먼저 알아둘 말
- RAG: 외부 지식을 검색해 응답에 결합하는 방식입니다.
- memory: 이전 상호작용이나 외부 상태를 저장하는 장치입니다.
- tool use: 외부 API나 도구를 호출하는 행위입니다.
- evidence retrieval: 답의 근거가 되는 자료를 가져오는 과정입니다.

# 이 강의에서 답할 질문
- 왜 모델 밖의 기억과 검색이 필요한가
- multimodal RAG는 text-only RAG와 무엇이 다른가
- tool use가 붙으면 실패 양상은 어떻게 바뀌는가

# 왜 중요한가
- 실제 업무형 시스템은 모델 지식보다 외부 근거와 도구 실행이 더 중요할 수 있습니다.
- 시각 입력이 포함되면 retrieval index와 grounding 방식도 달라집니다.

# 이번 강의의 핵심 축
- multimodal query formulation
- memory consistency
- tool routing과 verification
- evidence-grounded answer generation

# 스스로 점검
1. multimodal RAG가 필요한 이유를 설명하라.
2. memory가 없는 시스템의 한계를 말하라.
3. tool use가 붙을 때 생기는 새로운 실패를 설명하라.
