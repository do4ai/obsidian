---
title: "Entity"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b980e0a01fe5ccf8349609__Entity
notion_id: 324e313f58b980e0a01fe5ccf8349609
notion_url: https://www.notion.so/324e313f58b980e0a01fe5ccf8349609
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 엔티티(Entity)가 필요한가?
비즈니스 도메인에는 시간이 흐르고 상태가 변하더라도 지속적으로 추적하고 관리해야 하는 핵심 개념들이 존재합니다.
만약 데이터의 속성만으로 대상을 식별한다면, 고객이 이름을 바꾸거나 주소를 변경했을 때 완전히 다른 사람으로 인식하는 치명적인 시스템 오류가 발생합니다.
따라서 대상의 속성 변화와 무관하게 동일한 객체임을 시스템에 보장해 주는 강력한 식별 기준이 필수적입니다.
> **연속성(Continuity)과 추적성**
대상의 생명주기(Lifecycle) 내내 상태가 수시로 변하더라도, 시스템은 이를 동일한 객체로 인식하고 일관되게 추적해야 합니다.
## What: 엔티티(Entity)란 무엇인가?
- **Entity(엔티티)**는 자신이 가진 속성(Attribute)이 아닌, 고유한 **식별자(Identity)**를 통해 정의되는 도메인 객체입니다.
데이터베이스의 기본 키(PK)처럼 시스템 내에서 유일한 ID를 가지며, 이 ID가 같다면 나머지 속성이 모두 달라도 완전히 동일한 객체로 취급됩니다.
## How: 엔티티의 설계와 실무 적용 예시
실무에서 엔티티는 식별자를 중심으로 비즈니스의 핵심 상태를 변경(Mutable)하는 풍부한 행위(Behavior)를 가져야 합니다.
- **식별자 기반 동등성**: 두 개의 `Member` 객체가 있을 때, 이름과 나이가 달라도 `member_id`가 같다면 같은 회원으로 판별하도록 코드를 설계합니다.
- **비즈니스 의도가 담긴 상태 변경**: 단순히 무의미한 `setter`를 열어두는 것이 아니라, `changePassword()`나 `upgradeMembership()`처럼 비즈니스 의도가 명확한 메서드를 통해서만 내부 상태를 변경해야 합니다.
**\[상품(Product) 도메인 기준 Entity 적용 예시\]**
- **식별자 기반 동등성 보장**: 두 개의 `Product` 객체가 메모리에 로드되었을 때, 한쪽의 상품명이 '여름 티셔츠'에서 '반팔 티셔츠'로 수정되었더라도 `productId`가 `PROD-1001`로 동일하다면 시스템은 이를 같은 엔티티로 취급하여 비즈니스 로직을 이어갑니다.
- **비즈니스 의도가 담긴 상태 변경**: 상품을 품절 처리할 때 단순한 `product.setStatus("OUT_OF_STOCK")` 대신, 도메인의 언어가 반영된 `product.markAsOutOfStock()`이라는 명확한 행위(Behavior) 메서드를 호출하여 내부 상태를 변경합니다.
