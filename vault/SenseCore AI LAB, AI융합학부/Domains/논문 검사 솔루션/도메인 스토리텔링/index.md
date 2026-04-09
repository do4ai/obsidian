---
title: "도메인 스토리텔링"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/330e313f58b981dabde2c62d552b7a6b__논문 검사 솔루션/children/330e313f58b981d88b20e4d3031a9201__도메인 스토리텔링
notion_id: 330e313f58b981d88b20e4d3031a9201
notion_url: https://www.notion.so/330e313f58b981d88b20e4d3031a9201
parent_notion_id: 330e313f58b981dabde2c62d552b7a6b
---
## 이 페이지의 목적

이 페이지는 PaperSens의 논문 업로드에서 편집자 관점 결과물 생성까지의 핵심 흐름을 고정하는 페이지다.

## 핵심 액터

- 연구자 또는 사용자: 논문 파일을 업로드하고 필요한 분석 미션을 선택한다.
- Paper Session workspace: 업로드 파일을 정규화하고 결과를 누적하는 작업 공간이다.
- 모델 오케스트레이션: 텍스트 모델과 VLM을 선택해 분석 단계를 수행한다.

## 핵심 work object

- Manuscript: 업로드된 DOCX, PDF, LaTeX ZIP 원본이다.
- Paper Session: 한 편의 논문에 대한 임시 작업 세션이다.
- Dataset Analysis / Figure Analysis / Review: 세션 위에 누적되는 분석 산출물이다.

## 80% 핵심 시나리오

1. 사용자는 DOCX, PDF, LaTeX ZIP 중 하나의 논문 파일을 업로드한다.
2. 시스템은 텍스트, 표, 이미지, figure caption을 추출해 하나의 paper session으로 정규화한다.
3. 사용자는 dataset 분석, figure quality 검사, figure-text consistency 검사, review 생성 중 필요한 미션을 선택한다.
4. 기본 통합 흐름에서는 dataset, figure, review 순으로 근거를 누적한다.
5. dataset 분석은 데이터셋 이름, 출처, 수집 방식, 표본 규모, citation 근거를 뽑는다.
6. figure 분석은 그림의 publication quality와 본문/캡션 정합성을 판단한다.
7. review synthesis는 앞선 분석 결과와 원문을 결합해 summary, verdict, 보완 포인트를 포함한 SCIE 스타일 리뷰를 만든다.
8. 필요하면 초록 번역과 summary도 함께 제공하고 사용자는 세션 안에서 결과를 재사용한다.

## 주요 variation

- 사용자는 통합 흐름 대신 dataset만, figure만, review만 별도로 실행할 수 있다.
- 모델 설치 상태에 따라 텍스트 모델과 VLM fallback이 달라질 수 있다.
- 입력 형식에 따라 파서와 이미지 추출 경로가 달라진다.

## 경계 판단 포인트

- 업로드 직후 객체는 영구 논문 엔티티보다 `Paper Session`으로 보는 편이 현재 제품과 맞다.
- dataset, figure, review는 각각 다른 증거 생성 컨텍스트를 가진다.
- review는 독립 분석이 아니라 앞선 증거를 종합하는 상위 판단 단계다.

## 확인 소스

- `papersens/QUICKSTART.md`
- `papersens/web_ui.py`
- `papersens/index.html`
- `papersens/manuscript.tex`
