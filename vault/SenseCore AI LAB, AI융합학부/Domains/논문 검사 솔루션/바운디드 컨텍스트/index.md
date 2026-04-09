---
title: "바운디드 컨텍스트"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/330e313f58b981dabde2c62d552b7a6b__논문 검사 솔루션/children/330e313f58b981c38004e4b8ef4593ff__바운디드 컨텍스트
notion_id: 330e313f58b981c38004e4b8ef4593ff
notion_url: https://www.notion.so/330e313f58b981c38004e4b8ef4593ff
parent_notion_id: 330e313f58b981dabde2c62d552b7a6b
---
## 이 페이지의 목적

이 페이지는 PaperSens의 세션, 추출, 분석, 보고 경계를 분리하는 페이지다.

| 컨텍스트 | 분류 | 핵심 책임 | 대표 개념 |
| --- | --- | --- | --- |
| Manuscript Intake & Session Workspace | Core | 업로드 수용, 파일 형식 판별, paper alias 부여, 세션 수명주기, 캐시 관리 | Manuscript, Paper Session, Alias |
| Content Extraction & Canonicalization | Core | DOCX/PDF/LaTeX별 파싱, 제목 추출, 표/그림 카운트, figure caption과 context 정리 | Extracted Text, Figure Caption, Figure Context |
| Dataset Provenance Analysis | Core | 데이터셋 이름, 출처, 수집 방식, 표본, citation 근거 추출 | Dataset Analysis, Dataset Info |
| Figure Intelligence | Core | figure preview, publication quality 판단, figure-text consistency 검사 | Figure, Figure Quality, Figure Contents Check |
| Editorial Assessment & Reporting | Core | summary, abstract translation, SCIE 스타일 review, verdict 생성 | Review, Summary, Abstract Translation |
| Model Orchestration & Runtime Integration | Generic | text model/VL model 라우팅, backend URL, timeout, 모델 발견과 fallback | Text Model, VL Model |
| Presentation/API Layer | Supporting | 미션 실행 표면, 결과 렌더링, 사용자 입력 흐름 | Mission Request, Result View |

## 경계를 이렇게 자르는 이유

- `Content Extraction`을 분리해야 PDF, DOCX, LaTeX 파싱 규칙이 분석 규칙을 오염시키지 않는다.
- `Dataset Provenance`와 `Figure Intelligence`는 서로 다른 증거 생성 컨텍스트다.
- `Editorial Assessment`는 상위 판단 컨텍스트로서 앞선 분석 결과를 소비하지만, figure 또는 dataset 규칙 자체를 소유하지 않는다.

## 번역 또는 조정이 필요한 경계

- `Content Extraction & Canonicalization`은 원본 파일을 분석 가능한 공통 표현으로 번역한다.
- `Dataset Provenance Analysis`와 `Figure Intelligence`는 서로 다른 증거를 만들지만 최종 review에서 같은 판단 언어로 합쳐진다.
- `Model Orchestration & Runtime Integration`은 분석 규칙을 소유하지 않고 호출 정책과 fallback만 제공한다.

## 확인 소스

- `papersens/QUICKSTART.md`
- `papersens/web_ui.py`
- `papersens/index.html`
