---
title: "07. 딥러닝과 생성모델"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b98136b5e8e10cfe7f2d50__07. 확률분포와 최적화
notion_id: 32be313f58b98136b5e8e10cfe7f2d50
notion_url: https://www.notion.so/32be313f58b98136b5e8e10cfe7f2d50
parent_notion_id: 32be313f58b981e7b26fea2d45e6fa7f
---
# 이 단계에서 배우는 것
이 단계에서는 모델이 어떻게 스스로 맞춰 가는지와 새로운 데이터를 어떻게 만들어 내는지를 한 흐름으로 읽습니다. 앞에서 배운 기본 도구들이 실제 과정에서 어떻게 맞물리는지 차례대로 확인합니다.

# 먼저 알고 갈 말
- 학습: 예측을 조금씩 고쳐 가며 더 좋은 답을 찾는 과정
- 손실: 지금의 예측이 얼마나 틀렸는지 나타내는 수
- 기울기: 손실을 줄이기 위해 무엇을 얼마나 바꿔야 하는지를 알려 주는 값
- 초기화: 학습을 시작하기 전에 가중치의 첫 값을 정하는 일
- 정규화: 중간값의 크기와 분포를 일정하게 맞춰 흔들림을 줄이는 일
- residual 연결: 원래 정보를 지름길로 보내는 연결
- 표현학습: 데이터의 의미를 잘 담는 표현을 배우는 일
- 잠재변수: 관측되지 않지만 데이터를 만든다고 가정하는 숨은 요인
- 확률과정: 시간이 지나며 상태가 확률적으로 변하는 과정
- diffusion: 노이즈를 넣고 다시 제거하는 생성 방식

# 이 단계를 읽는 순서
1. 32강에서 학습의 기본 구조(계산그래프와 역전파)를 잡습니다.
2. 33강에서 학습이 흔들리는 이유와 안정화 장치를 봅니다.
3. 34강에서 정답표 없이도 표현을 배우는 방법을 이해합니다.
4. 35강에서 잠재변수 생성모델과 변분추론을 배웁니다.
5. 36강에서 노이즈 과정 기반 생성모델을 정리합니다.

# 각 강의가 맡는 역할
- 32. 신경망, 계산그래프, backprop: 학습이 어떻게 진행되는지 큰 구조를 만든다.
- 33. 초기화, 정규화, residual, optimization tricks: 학습이 실제로 되게 만드는 안정화 장치를 정리한다.
- 34. self-supervised learning과 표현학습: 라벨 없이 표현을 만드는 핵심 원리를 다룬다.
- 35. variational inference, ELBO, VAE: 숨은 변수를 가진 생성모델의 학습 논리를 설명한다.
- 36. 확률과정, score matching, diffusion: 노이즈를 활용한 생성의 큰 흐름을 연결한다.

# 이 단계를 마치면 할 수 있는 것
- 학습이 왜 기울기 계산으로 돌아가는지 설명할 수 있습니다.
- 깊은 모델이 잘 배우기 위한 조건을 말할 수 있습니다.
- self-supervised, 잠재변수 모델, diffusion이 하나의 흐름으로 연결됨을 이해합니다.

아래 순서대로 읽습니다.
[32. 신경망, 계산그래프, backprop](32. 신경망, 계산그래프, backprop/index.md)
[33. 초기화, 정규화, residual, optimization tricks](33. 초기화, 정규화, residual, optimization tricks/index.md)
[34. self-supervised learning과 표현학습](34. self-supervised learning과 표현학습/index.md)
[35. variational inference, ELBO, VAE](35. variational inference, ELBO, VAE/index.md)
[36. 확률과정, score matching, diffusion](36. 확률과정, score matching, diffusion/index.md)
[문제 해설 - 07. 딥러닝과 생성모델](문제 해설 - 07. 딥러닝과 생성모델/index.md)
