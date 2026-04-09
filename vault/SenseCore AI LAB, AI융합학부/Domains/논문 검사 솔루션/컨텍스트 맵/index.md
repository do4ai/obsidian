---
title: "컨텍스트 맵"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/domains/32be313f58b9803bb9adf68c0393a0f6__Domains/children/330e313f58b981dabde2c62d552b7a6b__논문 검사 솔루션/children/330e313f58b981328a93d0d73d843705__컨텍스트 맵
notion_id: 330e313f58b981328a93d0d73d843705
notion_url: https://www.notion.so/330e313f58b981328a93d0d73d843705
parent_notion_id: 330e313f58b981dabde2c62d552b7a6b
---
## 이 페이지의 목적

이 페이지는 PaperSens의 원본 파일 처리, 증거 생성, 최종 리뷰 합성 사이의 관계를 전략 수준에서 보여주는 페이지다.

| Upstream | Downstream | 관계 | 번역 책임 | 변경 비용 메모 |
| --- | --- | --- | --- | --- |
| Manuscript Intake & Session Workspace | Content Extraction & Canonicalization | Customer/Supplier | extraction이 업로드 원본을 공통 분석 표현으로 바꾼다. | 입력 형식이 늘어나면 extraction 경계가 가장 먼저 흔들린다. |
| Content Extraction & Canonicalization | Dataset Provenance Analysis | Published Language | 정규화된 본문과 citation 단서를 dataset 분석 입력으로 제공한다. | parser 출력 형식이 바뀌면 dataset 분석 prompt와 parser 둘 다 수정된다. |
| Content Extraction & Canonicalization | Figure Intelligence | Published Language | figure image, caption, context를 figure 분석 언어로 제공한다. | figure extraction 품질이 figure 판단 정확도를 직접 좌우한다. |
| Dataset Provenance Analysis | Editorial Assessment & Reporting | Customer/Supplier | dataset artifact를 review 근거로 제공한다. | provenance schema가 바뀌면 review synthesis도 함께 바뀐다. |
| Figure Intelligence | Editorial Assessment & Reporting | Customer/Supplier | figure quality와 consistency 결과를 review와 summary에 반영한다. | review가 figure 용어를 강하게 의존하므로 coupling이 높다. |
| Model Orchestration & Runtime Integration | Dataset Provenance Analysis | Supporting | 텍스트 모델 선택과 timeout을 제공한다. | 모델 교체 시 분석 규칙보다 호출 정책 수정이 중심이다. |
| Model Orchestration & Runtime Integration | Figure Intelligence | Supporting | VLM 라우팅과 fallback을 제공한다. | 모델 품질 변화가 figure 결과 해석에 영향을 준다. |
| Editorial Assessment & Reporting | Presentation/API Layer | Open Host Service | 최종 review, summary, translation을 사용자 표면에 노출한다. | 출력 포맷 변경은 UI와 API 계약에 직접 영향을 준다. |

## 현재 해석

- PaperSens의 핵심은 `세션 기반 근거 누적 분석`이다.
- dataset와 figure는 병렬 기능처럼 보이지만, 최종 review에서 하나의 editorial judgement로 수렴한다.

## 확인 소스

- `papersens/QUICKSTART.md`
- `papersens/web_ui.py`
- `papersens/index.html`
