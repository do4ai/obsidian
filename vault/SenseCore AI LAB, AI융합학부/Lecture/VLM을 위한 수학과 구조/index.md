---
title: "VLM을 위한 수학과 구조"
source_kind: page
---
# VLM을 위한 수학과 구조
이 책은 [AI를 위한 수학](../AI를 위한 수학/index.md)의 학습 구조를 그대로 이어 받아, 순서대로 읽기만 해도 VLM의 표현, 정렬, 생성, grounding, 평가, 시스템 확장, 최신 연구 흐름까지 한 단계씩 이해할 수 있게 만든 교재입니다. 목표는 모델 이름을 많이 아는 것이 아니라, 어떤 VLM을 보더라도 입력 표현이 어떻게 바뀌고, 어떤 손실로 학습되며, 어느 구조에서 실패하는지를 처음부터 끝까지 스스로 설명할 수 있게 만드는 것입니다.

# 이 책의 목표
- 이미지가 patch, feature map, token 시퀀스로 바뀌는 시각 표현의 기초를 익힙니다.
- image-text alignment와 multimodal pretraining의 핵심 손실을 순서대로 읽습니다.
- cross-attention, Q-Former, decoder-only VLM 같은 대표 구조를 비교할 수 있게 합니다.
- OCR, region reasoning, hallucination, faithfulness를 실제 품질 문제로 연결합니다.
- multimodal instruction tuning, evaluation, agent 확장, frontier 논문 독해까지 하나의 흐름으로 묶습니다.

# 이 책을 읽는 방법
- 처음부터 끝까지 순서대로 읽습니다. 뒤 단계는 앞 단계의 표현과 용어를 이미 알고 있다고 가정합니다.
- 모듈 이름을 외우기보다 먼저 입력, 중간 표현, 출력이 어디로 흐르는지를 말로 읽습니다.
- 식이 나오면 벡터와 토큰이 어떻게 이동하는지 먼저 설명한 뒤 계산합니다.
- OCR, grounding, evaluation처럼 실제 실패 사례가 등장하면 구조와 연결해 다시 읽습니다.
- 한 번에 이해되지 않으면 바로 앞 단계의 용어와 정보 흐름으로 돌아갑니다.

# 이 책의 읽는 순서
1. 이미지를 토큰으로 바꾸는 시야
2. 이미지와 텍스트를 같은 공간에 맞추기
3. VLM 아키텍처와 정보 흐름
4. Grounding, OCR, region reasoning
5. 멀티모달 생성과 instruction tuning
6. 평가, 신뢰성, hallucination 완화
7. 비디오, 음성, 에이전트로 확장
8. Frontier VLM과 최신 논문 독해

이 순서는 단순 역사 순서가 아니라, 표현에서 시작해 정렬과 구조를 익히고, 그 위에서 생성과 평가를 본 뒤, 마지막에 시스템과 frontier를 읽도록 배치했습니다.

# 각 단계에서 무엇을 배우는가
## 1단계. 이미지를 토큰으로 바꾸는 시야
- 이미지가 patch, feature map, vision token으로 바뀌는 방식을 배웁니다.
- CNN과 ViT가 어떤 시각 표현을 만드는지 비교합니다.
- resolution, token budget, connector가 왜 이후 단계의 전제인지 이해합니다.

## 2단계. 이미지와 텍스트를 같은 공간에 맞추기
- shared embedding과 contrastive learning의 기본 목적을 읽습니다.
- CLIP objective, in-batch negative, retrieval를 수학적으로 해석합니다.
- pretraining objective 조합과 data mixture가 모델 성격을 어떻게 바꾸는지 정리합니다.

## 3단계. VLM 아키텍처와 정보 흐름
- encoder-decoder, decoder-only, early fusion, late fusion 구조를 비교합니다.
- cross-attention, Q-Former, resampler, visual prompt의 역할을 구분합니다.
- 대표 VLM 계열의 설계 차이를 정보 흐름 관점에서 설명합니다.

## 4단계. Grounding, OCR, region reasoning
- OCR, 문서 이해, 차트 이해가 왜 일반 captioning보다 어려운지 배웁니다.
- spatial reference, region token, referring expression을 구조와 연결합니다.
- visual reasoning과 hallucination failure를 함께 읽습니다.

## 5단계. 멀티모달 생성과 instruction tuning
- captioning과 VQA를 넘어 instruction-following VLM이 어떻게 만들어지는지 봅니다.
- SFT, preference learning, RLHF, DPO를 멀티모달 맥락에서 다시 읽습니다.
- safety policy와 refusal이 생성 구조와 어떻게 얽히는지 이해합니다.

## 6단계. 평가, 신뢰성, hallucination 완화
- benchmark와 evaluation protocol을 비판적으로 읽는 법을 배웁니다.
- hallucination taxonomy, faithfulness, calibration을 체계적으로 정리합니다.
- verifier, retrieval grounding, human evaluation을 제품 지표와 연결합니다.

## 7단계. 비디오, 음성, 에이전트로 확장
- 비디오 토큰과 temporal modeling이 왜 새로운 난제를 만드는지 이해합니다.
- audio와 spoken dialogue가 붙을 때 multimodal 구조가 어떻게 넓어지는지 봅니다.
- multimodal RAG, tool use, GUI agent, serving 이슈를 시스템 관점에서 읽습니다.

## 8단계. Frontier VLM과 최신 논문 독해
- multimodal diffusion, unified model, MoE, world model 같은 frontier 주제를 정리합니다.
- open-source VLM 생태계와 실험 설계를 읽는 기준을 세웁니다.
- 최신 논문을 읽을 때 objective, architecture, data, evaluation을 어떻게 점검할지 익힙니다.

# 모든 강의가 따르는 공통 순서
- 먼저 어떤 입력과 출력 문제를 다루는지 세웁니다.
- 그다음 필요한 표현과 모듈을 쉬운 말로 정리합니다.
- 그다음 손실, attention, 토큰 흐름 같은 핵심 수식을 붙입니다.
- 마지막에 실제 사용 장면, 실패 사례, 다음 단계 연결로 마무리합니다.

이 책은 이 순서를 지키면서 진행하므로, 위에서 아래로 읽기만 해도 VLM의 구조가 끊기지 않도록 구성합니다.

# 읽기 전에 기억할 약속
- 이미지도 텍스트처럼 시퀀스로 읽습니다.
- 구조 이름보다 정보 흐름이 먼저입니다.
- 좋은 성능은 유창함만이 아니라 grounding과 faithfulness를 포함합니다.
- benchmark 점수는 출발점이지 최종 결론이 아닙니다.
- 이 책의 목적은 유행 모델 정리가 아니라 VLM을 읽는 습관을 만드는 것입니다.

# 이 책을 마치면
이 책을 끝내면 어떤 VLM 논문이나 제품을 보더라도, vision encoder가 무엇을 내고, text side와 어디서 만나며, 어떤 objective로 학습되고, 무엇 때문에 hallucination이 생기고, 어떤 evaluation이 부족한지를 순서대로 설명할 수 있어야 합니다. 더 나아가 이미지 VLM에서 비디오, 음성, agent, unified model로 확장되는 흐름까지 하나의 커리큘럼 안에서 연결해 볼 수 있어야 합니다.

# 단계 목록
[01. 이미지를 토큰으로 바꾸는 시야](01. 이미지를 토큰으로 바꾸는 시야/index.md)
[02. 이미지와 텍스트를 같은 공간에 맞추기](02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
[03. VLM 아키텍처와 정보 흐름](03. VLM 아키텍처와 정보 흐름/index.md)
[04. Grounding, OCR, region reasoning](04. Grounding, OCR, region reasoning/index.md)
[05. 멀티모달 생성과 instruction tuning](05. 멀티모달 생성과 instruction tuning/index.md)
[06. 평가, 신뢰성, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/index.md)
[07. 비디오, 음성, 에이전트로 확장](07. 비디오, 음성, 에이전트로 확장/index.md)
[08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/index.md)

## Page Tree

- [01. 이미지를 토큰으로 바꾸는 시야](01. 이미지를 토큰으로 바꾸는 시야/index.md)
  - [1. pixel, patch, feature map, vision token](01. 이미지를 토큰으로 바꾸는 시야/1. pixel, patch, feature map, vision token/index.md)
  - [2. CNN, ViT, positional structure](01. 이미지를 토큰으로 바꾸는 시야/2. CNN, ViT, positional structure/index.md)
  - [3. resolution, stride, pooling, token budget](01. 이미지를 토큰으로 바꾸는 시야/3. resolution, stride, pooling, token budget/index.md)
  - [4. projector, adapter, connector](01. 이미지를 토큰으로 바꾸는 시야/4. projector, adapter, connector/index.md)
  - [5. vision backbone pretraining과 transfer](01. 이미지를 토큰으로 바꾸는 시야/5. vision backbone pretraining과 transfer/index.md)
  - [문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](01. 이미지를 토큰으로 바꾸는 시야/문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)
- [02. 이미지와 텍스트를 같은 공간에 맞추기](02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
  - [06. image-text pair, shared embedding, cosine similarity](02. 이미지와 텍스트를 같은 공간에 맞추기/06. image-text pair, shared embedding, cosine similarity/index.md)
  - [07. CLIP objective, in-batch negative, temperature](02. 이미지와 텍스트를 같은 공간에 맞추기/07. CLIP objective, in-batch negative, temperature/index.md)
  - [08. hard negative, retrieval, ranking](02. 이미지와 텍스트를 같은 공간에 맞추기/08. hard negative, retrieval, ranking/index.md)
  - [09. captioning, matching, contrastive objective 조합](02. 이미지와 텍스트를 같은 공간에 맞추기/09. captioning, matching, contrastive objective 조합/index.md)
  - [10. data mixture, web-scale data, curriculum](02. 이미지와 텍스트를 같은 공간에 맞추기/10. data mixture, web-scale data, curriculum/index.md)
  - [문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](02. 이미지와 텍스트를 같은 공간에 맞추기/문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
- [03. VLM 아키텍처와 정보 흐름](03. VLM 아키텍처와 정보 흐름/index.md)
  - [11. encoder-decoder, decoder-only, fusion map](03. VLM 아키텍처와 정보 흐름/11. encoder-decoder, decoder-only, fusion map/index.md)
  - [12. cross-attention, perceiver resampler, Q-Former](03. VLM 아키텍처와 정보 흐름/12. cross-attention, perceiver resampler, Q-Former/index.md)
  - [13. prefix tuning, visual prompt, frozen LM](03. VLM 아키텍처와 정보 흐름/13. prefix tuning, visual prompt, frozen LM/index.md)
  - [14. token compression, memory, long context](03. VLM 아키텍처와 정보 흐름/14. token compression, memory, long context/index.md)
  - [15. representative VLM families 비교](03. VLM 아키텍처와 정보 흐름/15. representative VLM families 비교/index.md)
  - [문제 해설 - 03. VLM 아키텍처와 정보 흐름](03. VLM 아키텍처와 정보 흐름/문제 해설 - 03. VLM 아키텍처와 정보 흐름/index.md)
- [04. Grounding, OCR, region reasoning](04. Grounding, OCR, region reasoning/index.md)
  - [16. OCR, document understanding, chart understanding](04. Grounding, OCR, region reasoning/16. OCR, document understanding, chart understanding/index.md)
  - [17. box, mask, region token, spatial reference](04. Grounding, OCR, region reasoning/17. box, mask, region token, spatial reference/index.md)
  - [18. referring expression, region reasoning, counting](04. Grounding, OCR, region reasoning/18. referring expression, region reasoning, counting/index.md)
  - [19. multimodal chain-of-thought와 visual reasoning](04. Grounding, OCR, region reasoning/19. multimodal chain-of-thought와 visual reasoning/index.md)
  - [20. grounding failure와 hallucination의 구조](04. Grounding, OCR, region reasoning/20. grounding failure와 hallucination의 구조/index.md)
  - [문제 해설 - 04. Grounding, OCR, region reasoning](04. Grounding, OCR, region reasoning/문제 해설 - 04. Grounding, OCR, region reasoning/index.md)
- [05. 멀티모달 생성과 instruction tuning](05. 멀티모달 생성과 instruction tuning/index.md)
  - [21. captioning, VQA, conditional generation](05. 멀티모달 생성과 instruction tuning/21. captioning, VQA, conditional generation/index.md)
  - [22. supervised fine-tuning과 multimodal instruction data](05. 멀티모달 생성과 instruction tuning/22. supervised fine-tuning과 multimodal instruction data/index.md)
  - [23. preference learning, reward model, RLHF](05. 멀티모달 생성과 instruction tuning/23. preference learning, reward model, RLHF/index.md)
  - [24. DPO, rejection sampling, policy alignment](05. 멀티모달 생성과 instruction tuning/24. DPO, rejection sampling, policy alignment/index.md)
  - [25. safety policy, refusal, jailbreak 대응](05. 멀티모달 생성과 instruction tuning/25. safety policy, refusal, jailbreak 대응/index.md)
  - [문제 해설 - 05. 멀티모달 생성과 instruction tuning](05. 멀티모달 생성과 instruction tuning/문제 해설 - 05. 멀티모달 생성과 instruction tuning/index.md)
- [06. 평가, 신뢰성, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/index.md)
  - [26. benchmark, leaderboard, evaluation protocol](06. 평가, 신뢰성, hallucination 완화/26. benchmark, leaderboard, evaluation protocol/index.md)
  - [27. hallucination taxonomy와 faithfulness](06. 평가, 신뢰성, hallucination 완화/27. hallucination taxonomy와 faithfulness/index.md)
  - [28. calibration, uncertainty, abstention](06. 평가, 신뢰성, hallucination 완화/28. calibration, uncertainty, abstention/index.md)
  - [29. data filtering, verifier, retrieval grounding](06. 평가, 신뢰성, hallucination 완화/29. data filtering, verifier, retrieval grounding/index.md)
  - [30. human evaluation과 product metric](06. 평가, 신뢰성, hallucination 완화/30. human evaluation과 product metric/index.md)
  - [문제 해설 - 06. 평가, 신뢰성, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/문제 해설 - 06. 평가, 신뢰성, hallucination 완화/index.md)
- [07. 비디오, 음성, 에이전트로 확장](07. 비디오, 음성, 에이전트로 확장/index.md)
  - [31. video token, frame sampling, temporal modeling](07. 비디오, 음성, 에이전트로 확장/31. video token, frame sampling, temporal modeling/index.md)
  - [32. speech, audio, spoken dialogue extension](07. 비디오, 음성, 에이전트로 확장/32. speech, audio, spoken dialogue extension/index.md)
  - [33. multimodal RAG, memory, tool use](07. 비디오, 음성, 에이전트로 확장/33. multimodal RAG, memory, tool use/index.md)
  - [34. GUI agent, robotics, embodied reasoning](07. 비디오, 음성, 에이전트로 확장/34. GUI agent, robotics, embodied reasoning/index.md)
  - [35. latency, serving, cost optimization](07. 비디오, 음성, 에이전트로 확장/35. latency, serving, cost optimization/index.md)
  - [문제 해설 - 07. 비디오, 음성, 에이전트로 확장](07. 비디오, 음성, 에이전트로 확장/문제 해설 - 07. 비디오, 음성, 에이전트로 확장/index.md)
- [08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/index.md)
  - [36. multimodal diffusion과 unified model](08. Frontier VLM과 최신 논문 독해/36. multimodal diffusion과 unified model/index.md)
  - [37. mixture-of-experts, adaptive compute, token routing](08. Frontier VLM과 최신 논문 독해/37. mixture-of-experts, adaptive compute, token routing/index.md)
  - [38. world model, simulation, action-conditioned model](08. Frontier VLM과 최신 논문 독해/38. world model, simulation, action-conditioned model/index.md)
  - [39. open-source VLM ecosystem과 실험 설계](08. Frontier VLM과 최신 논문 독해/39. open-source VLM ecosystem과 실험 설계/index.md)
  - [40. 최신 VLM 논문 독해 프레임워크](08. Frontier VLM과 최신 논문 독해/40. 최신 VLM 논문 독해 프레임워크/index.md)
  - [문제 해설 - 08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/문제 해설 - 08. Frontier VLM과 최신 논문 독해/index.md)
