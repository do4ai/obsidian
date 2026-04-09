---
title: "UL"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/330e313f58b981dabde2c62d552b7a6b__논문 검사 솔루션/children/330e313f58b9819f89aaf0c2d4ebb459__UL
notion_id: 330e313f58b9819f89aaf0c2d4ebb459
notion_url: https://www.notion.so/330e313f58b9819f89aaf0c2d4ebb459
parent_notion_id: 330e313f58b981dabde2c62d552b7a6b
---
## 이 페이지의 목적

이 페이지는 PaperSens에서 세션, 증거, 편집자 판단을 같은 언어로 관리하게 만드는 UL 페이지다.

| 용어 | 정의 | 사용하는 문맥 | 금지 또는 주의 표현 |
| --- | --- | --- | --- |
| Manuscript | 업로드된 논문 원본 | intake | 최종 review 결과와 같은 뜻으로 쓰지 않는다. |
| Paper Session | 한 편의 논문에 대한 임시 작업 세션 | session workspace | 영구 knowledge record와 혼용하지 않는다. |
| Alias | 세션을 식별하는 표시 이름 | session UI | 파일명과 항상 같다고 가정하지 않는다. |
| Mission | 사용자가 실행하는 분석 작업 단위 | UI, orchestration | feature 이름과 무조건 1:1이라고 가정하지 않는다. |
| Integrated Analysis | 여러 미션을 순차 실행하는 기본 파이프라인 | session orchestration | 단일 review 요청과 같은 뜻으로 쓰지 않는다. |
| Dataset Analysis | 데이터셋 출처와 재현성 근거 추출 결과 | dataset provenance | 단순 키워드 탐지라고 부르지 않는다. |
| Dataset Info | review에 주입되는 dataset artifact | review synthesis | 원문 텍스트와 같은 것으로 취급하지 않는다. |
| Figure | 추출된 그림 단위 | extraction, figure intelligence | 이미지 파일만을 뜻하는 표현으로 축소하지 않는다. |
| Figure Quality | figure의 출판 품질 판단 | figure intelligence | 디자인 호불호와 혼동하지 않는다. |
| Figure Contents Check | figure와 본문/캡션의 정합성 검사 | figure intelligence | figure quality와 같은 뜻으로 쓰지 않는다. |
| Figure Context | figure 주변 문맥 정보 | extraction, review | caption만 의미하는 것으로 쓰지 않는다. |
| Review | 최종 편집자 관점 평가 결과 | editorial assessment | summary와 같은 뜻으로 쓰지 않는다. |
| Summary | 목적, 방법, 결과, 시사점 요약 | reporting | review verdict를 포함하는 완전 평가로 쓰지 않는다. |
| Abstract Translation | 초록 번역 결과 | reporting | review의 일부로 묶지 않는다. |
| Text Model | 텍스트 분석용 LLM | orchestration | VLM과 혼용하지 않는다. |
| VL Model | 시각-언어 분석용 모델 | orchestration | dataset 분석 기본 모델과 같은 것으로 보지 않는다. |

## 용어 운영 원칙

- session 언어와 editorial judgement 언어를 분리한다.
- figure quality와 figure-text consistency를 같은 용어로 뭉개지 않는다.
- review는 상위 종합 판단이라는 점을 문서와 UI 모두에서 유지한다.

## 확인 소스

- `papersens/QUICKSTART.md`
- `papersens/web_ui.py`
