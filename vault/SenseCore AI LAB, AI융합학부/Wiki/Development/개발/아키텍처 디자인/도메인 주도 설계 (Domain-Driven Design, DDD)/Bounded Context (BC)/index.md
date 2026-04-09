---
title: "Bounded Context (BC)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b9817eb2bfdc304a1e7503__Bounded Context (BC)
notion_id: 324e313f58b9817eb2bfdc304a1e7503
notion_url: https://www.notion.so/324e313f58b9817eb2bfdc304a1e7503
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 명확한 경계(Bounded)가 필요한가?
소프트웨어 시스템 내에서는 같은 단어라도 **비즈니스 문맥(Context)**에 따라 의미와 모델링해야 할 데이터가 완전히 달라집니다. 이러한 경계를 명확히 나누지 않으면, 여러 부서의 요구사항이 섞여 단일 모델의 복잡도가 감당할 수 없이 증가하게 됩니다. 따라서 데이터의 오염을 막고 각 도메인의 독립성을 보장하기 위해 철저한 경계 분리가 필수적입니다.
## What: Bounded Context와 문맥(Context)의 정의
**Bounded Context**는 하나의 '용어'가 오직 '하나의 의미'로만 사용되는 명확한 논리적 경계를 의미합니다.
> **문맥(Context)이란?**
- 어떤 것을 이해하고 해석하는 데 속한 상황이나 배경을 뜻합니다.
- 소프트웨어 시스템 일부로서 독립적인 **비즈니스 문제 영역**을 나타냅니다.
## How: 이커머스 시스템의 '상품(Product)' 분리 예시
실제 이커머스 시스템에서 '**상품(Product)**'이라는 용어는 컨텍스트 경계에 따라 완전히 다른 형태로 모델링됩니다.
- **상품(Product) 컨텍스트**: 이름, 이미지, 설명, 카테고리 등 고객에게 보여줄 **'전시'** 정보를 의미합니다.
- **재고(Inventory) 컨텍스트**: 'SKU-1234'와 같은 관리 번호와 창고의 **'재고 수량**'만을 의미합니다.
- **주문(Order) 컨텍스트**: 주문서에 기록된 **'주문 항목(Order Line)'**이며, 결제 시점의 **'가격'**을 의미합니다.
