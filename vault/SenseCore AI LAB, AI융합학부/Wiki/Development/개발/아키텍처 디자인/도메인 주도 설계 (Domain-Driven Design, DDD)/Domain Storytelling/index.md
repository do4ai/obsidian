---
title: "Domain Storytelling"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/325e313f58b98080b152c750bda868fb__Domain Storytelling
notion_id: 325e313f58b98080b152c750bda868fb
notion_url: https://www.notion.so/325e313f58b98080b152c750bda868fb
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 도메인 스토리텔링이 필요한가?
복잡한 비즈니스 요구사항을 UML 같은 추상적인 다이어그램이나 두꺼운 명세서로만 소통하면, 도메인 전문가와 개발자 간의 이해도 차이가 발생하기 쉽습니다. 사람은 본능적으로 딱딱한 사양서보다 구체적인 시계열적 '이야기(Story)'의 흐름을 훨씬 더 빠르고 정확하게 이해합니다. 전문가가 실제 업무를 수행하는 과정을 이야기로 들으면서, 자연스럽게 **Ubiquitous Language(보편 언어)**를 도출하고 시스템의 경계를 파악하기 위해 이 기법을 도입합니다.
> **소통의 단절 극복**
기술적인 용어를 완전히 배제하고 오직 비즈니스 관점의 행동에만 집중하므로, 기획자와 개발자가 완벽히 동일한 이해를 바탕으로 모델링을 시작할 수 있습니다.
## What: 도메인 스토리텔링이란 무엇인가?
**Domain Storytelling(도메인 스토리텔링)**은 도메인 전문가와 개발팀이 모여 실제 비즈니스 프로세스를 시각적인 이야기로 풀어내는 협력적 모델링 기법입니다. 복잡한 표기법 대신 **Actor(주체)**, **Activity(행위/동사)**, **Work Object(작업 대상/명사)**라는 3가지 직관적인 픽토그램(그림 문자) 문법만을 사용하여 일련의 흐름을 화살표와 순서대로 그립니다. 이렇게 그려진 구체적인 시나리오들은 살아있는 요구사항이 되며, 궁극적으로 **Bounded Context(바운디드 컨텍스트)**를 식별하는 가장 강력한 기초 자료가 됩니다.
## How: 도메인 스토리텔링의 문법과 상품(Product) 도메인 적용
워크숍에서는 비즈니스 흐름을 번호를 매겨 순차적으로 기록하며, 여기서 등장하는 명사와 동사들은 곧바로 코드의 클래스(Class)와 메서드(Method)로 직역됩니다.
**\[상품(Product) 도메인 기준 신상품 전시 스토리텔링 예시\]**
- **Step 1 (입력)**: '상품 MD(Actor)'가 '신상품 스펙(Work Object)'을 상품 시스템에 '작성(Activity)'합니다.
- **Step 2 (검증)**: '상품 시스템(Actor)'이 스펙 내의 필수 데이터 누락 여부를 '검증(Activity)'합니다.
- **Step 3 (전시)**: 검증이 완료되면 '상품 MD'가 '카탈로그(Work Object)'에 신상품을 '전시(Activity)'합니다.
- **코드 번역 결과**: 위 3단계의 이야기는 개발자의 코드로 전환되어, `ProductMD`(Actor)가 `Catalog`(Work Object)에 `display(ProductSpec)`(Activity)를 수행하는 객체 지향적인 코드로 완벽하게 구현됩니다.
