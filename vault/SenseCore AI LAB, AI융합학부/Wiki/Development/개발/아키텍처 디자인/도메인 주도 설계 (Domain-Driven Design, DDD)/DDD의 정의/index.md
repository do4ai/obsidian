---
title: "DDD의 정의"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b9800e9209e7b3a59dd520__DDD의 정의
notion_id: 324e313f58b9800e9209e7b3a59dd520
notion_url: https://www.notion.so/324e313f58b9800e9209e7b3a59dd520
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 도메인 주도 설계(DDD)를 도입해야 하는가?
소프트웨어의 진정한 복잡성은 기술이 아닌 **도메인(Domain, 비즈니스 본질)** 그 자체에 있습니다.
기획자와 개발자가 각자의 언어로 이야기할 때 발생하는 "우리가 원하는 건 이게 아닌데..."라는 치명적인 소통 오류를 원천적으로 제거하기 위해 도입합니다. 비즈니스 규칙이 코드에 명확하게 반영되므로 요구사항이 변할 때 수정 범위를 쉽게 파악하고 유연하게 대응할 수 있습니다.
> **DDD의 한계와 초기 투자 비용**
단순한 데이터 입출력(CRUD) 위주의 시스템에는 과도한 오버엔지니어링이 될 수 있으며, 도메인을 깊이 이해하고 모델을 구축하는 초기 시간 투자가 반드시 필요합니다.
## What: 도메인 주도 설계란 무엇인가?
- **DDD(Domain-Driven Design)**는 애플리케이션을 기술적 구조가 아닌, 사용 사례와 관련된 비즈니스 현실을 기반으로 모델링하는 아키텍처 접근법입니다.
- 단순히 데이터만 담고 있는 빈약한 도메인 모델(Anemic Domain Model)의 사용을 엄격히 배척합니다.
대신, 데이터와 비즈니스 행위(Behavior)를 모두 포괄하는 **풍부한 도메인 모델(Rich Domain Model)**을 구축하여 도메인의 복잡성을 코드로 직접 증명합니다.
## How: 도메인의 분리와 기술적 패턴의 적용
DDD는 거대한 시스템의 복잡성을 관리하기 위해 전체 도메인을 독립적인 문제 영역인 **바운디드 컨텍스트(Bounded Context)**로 분리하며, 이는 현대의 **마이크로서비스(Microservice)**와 1:1로 강하게 상관 관계를 맺습니다.
- **전략적 소통**: 도메인 전문가와 개발자는 **보편 언어(Ubiquitous Language)**라는 단 하나의 공통 언어를 사용하여 바운디드 컨텍스트의 논리적 경계를 명확히 확립합니다.
- **전술적 구현**: 각 컨텍스트 내부의 구현은 **엔티티(Entity)**, **값 객체(Value Object)**, **애그리거트(Aggregate)**와 같은 기술적 패턴을 활용하여 비즈니스 일관성을 철저하게 유지합니다.

**상품(Product) 도메인**에서는 다음 5가지 방식으로 전략과 전술이 적용됩니다.
- **보편 언어(Ubiquitous Language)**: 기획자와 개발자가 '상품 노출'이라는 모호한 말 대신 `displayProduct()`라는 코드와 일치하는 단일 용어를 사용합니다.
- **바운디드 컨텍스트(Bounded Context)**: 거대한 쇼핑몰 시스템을 '상품 전시(Catalog)'와 '상품 재고(Inventory)'라는 독립적인 영역으로 명확히 분리합니다.
- **엔티티(Entity)**: `Product` 객체는 상품명이 변경되더라도 고유 식별자(`productId`)가 같으면 동일한 상품으로 인식하고 추적합니다.
- **값 객체(Value Object)**: 상품의 가격(`Money`)은 금액이나 통화 속성이 다르면 완전히 새로운 객체이므로, 내부 값을 수정하지 않고 통째로 교체합니다.
- **애그리거트(Aggregate)**: `Product`(루트 엔티티)와 `ProductOption`(내부 객체)을 하나의 트랜잭션 단위로 묶고, 옵션 변경은 반드시 루트를 통해서만 제어합니다.

출처: [https://blog.kakaocloud.com/193](https://blog.kakaocloud.com/193)
출처: [https://learn.microsoft.com/ko-kr/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice](https://learn.microsoft.com/ko-kr/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)
