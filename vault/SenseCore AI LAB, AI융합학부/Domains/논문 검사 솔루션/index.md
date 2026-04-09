---
title: "논문 검사 솔루션"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/330e313f58b981dabde2c62d552b7a6b__논문 검사 솔루션
notion_id: 330e313f58b981dabde2c62d552b7a6b
notion_url: https://www.notion.so/330e313f58b981dabde2c62d552b7a6b
parent_notion_id: 32be313f58b9803bb9adf68c0393a0f6
---
## 도메인 한 줄 정의

PaperSens의 논문 검사 도메인은 논문 파일을 세션 단위로 받아 정규화하고, dataset provenance, figure quality, figure-text consistency, 요약, 초록 번역, SCIE 스타일 리뷰를 생성해 제출 준비도를 판단하도록 돕는 논문 심사 보조 도메인이다.

## 왜 이 도메인을 따로 보나

- 단순 대화가 아니라 `근거 추출 -> 품질 점검 -> 편집자 관점 평가`의 누적 흐름을 가진다.
- 업로드된 논문은 영구 레코드보다 `Paper Session`으로 다루는 편이 실제 동작과 가깝다.
- dataset, figure, review가 서로 다른 증거 생성 컨텍스트를 가진다.

## 하위 문서

- 도메인 스토리텔링: 업로드에서 review까지의 핵심 검사 여정
- 바운디드 컨텍스트: 세션, 추출, 분석, 리포팅 경계
- UL: 논문 검사에서 팀이 공통으로 써야 하는 용어
- 컨텍스트 맵: extraction, dataset, figure, review의 관계

## 설계 메모

- PaperSens의 코어는 `논문 세션 기반 근거 누적 분석`이다.
- `Dataset Provenance`, `Figure Intelligence`, `Editorial Assessment`를 세 핵심 서브도메인으로 보는 편이 가장 안정적이다.
- 제품 설명도 `논문 챗봇`보다 `제출 준비도 평가 워크벤치`가 더 맞다.

## 핵심 판단

- PaperSens의 중심 객체는 영구 논문 마스터보다 `Paper Session`에 가깝다.
- dataset provenance, figure intelligence, editorial assessment는 하나의 파이프라인이 아니라 서로 다른 증거 생성 컨텍스트다.
- 최종 사용가치는 `제출 준비도 판단`이므로, 각 분석 결과는 최종 editorial judgement로 수렴해야 한다.

## 확인 소스

- `papersens/QUICKSTART.md`
- `papersens/web_ui.py`
- `papersens/index.html`
- `papersens/manuscript.tex`
- `papersens/IEIETSPC.docx`
- `papersens/_Elsevier_NDTandE_tensile_testing_impedance_spectrum_deep_learning.zip`

---

[도메인 스토리텔링](도메인 스토리텔링/index.md)
[바운디드 컨텍스트](바운디드 컨텍스트/index.md)
[UL](UL/index.md)
[컨텍스트 맵](컨텍스트 맵/index.md)
