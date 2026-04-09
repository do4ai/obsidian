---
title: "Aggregate"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b9817391b5dd68c319ada9__Aggregate
notion_id: 324e313f58b9817391b5dd68c319ada9
notion_url: https://www.notion.so/324e313f58b9817391b5dd68c319ada9
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
# Aggregate와 Aggregate Root
## Why: 왜 애그리거트(Aggregate)로 묶어야 하는가?
도메인 모델이 복잡해질수록 개별 객체 단위로 데이터를 관리하면 비즈니스 규칙의 일관성이 쉽게 깨집니다.
관련된 객체들을 하나의 **Aggregate**로 묶으면 관련된 맥락과 필요한 정보를 한곳에서 모두 파악할 수 있어 사람의 인지 부하를 크게 줄일 수 있습니다.
또한, 바운디드 컨텍스트(BC) 내부에서 데이터 변경의 명확한 단위를 확립하기 위해 반드시 필요합니다.
> **트랜잭션(Transaction) 경계의 확립**
애그리거트의 가장 중요한 존재 이유는 관련된 객체들을 묶어 데이터 무결성을 보장하는 하나의 완벽한 트랜잭션 경계를 만드는 것입니다.
## What: 애그리거트와 애그리거트 루트란?
- **Aggregate(애그리거트)**는 도메인 모델의 일관성을 유지하기 위해 밀접하게 관련된 객체들을 묶어 관리하는 단일 단위입니다. 이 묶음 내부의 데이터는 아무렇게나 접근해서는 안 되며, 일관성 보장을 위한 단일 진입점이 반드시 필요합니다. 이 묶음을 대표하는 유일한 진입점이자 루트 엔티티를 **Aggregate Root(애그리거트 루트)**라고 부릅니다.
## How: 애그리거트의 설계와 3가지 핵심 규칙
애그리거트는 **Root Entity**, 내부 **Entity**, 그리고 식별자 없이 속성 자체로 의미를 갖는 **Value Object(값 객체)**로 구성됩니다.
데이터 보호와 비즈니스 로직의 일관성을 강제하기 위해 다음 3가지 핵심 규칙을 반드시 지켜야 합니다.
- **핵심 규칙 1 (루트만 참조)**: 애그리거트 외부의 어떤 객체도 내부 객체를 직접 참조할 수 없으며, 오직 **Aggregate Root**만을 참조해야 합니다.
- **핵심 규칙 2 (루트를 통한 변경)**: 애그리거트 내부 객체의 상태를 변경하려면, 반드시 **Aggregate Root**가 제공하는 메서드를 통해서만 제어해야 합니다.
- **핵심 규칙 3 (단일 트랜잭션)**: 대상 애그리거트에 속한 모든 객체는 반드시 하나의 트랜잭션으로 DB에 저장, 수정, 삭제되어야 하며 하나라도 누락되면 전체 작업이 실패해야 합니다.
**\[상품(Product) 도메인 기준 Aggregate 적용 예시\]**
- **루트만 참조 (규칙 1 적용)**: 외부 로직에서 특정 상품의 세부 옵션(`ProductOption`) 객체를 직접 조회하거나 DB에서 꺼내올 수 없으며, 반드시 루트인 상품(`Product`) 객체를 통해서만 접근해야 합니다.
- **루트를 통한 변경 (규칙 2 적용)**: 상품 옵션의 가격을 변경할 때 `ProductOption.changePrice()`를 직접 호출하는 것은 금지되며, 반드시 `Product.changeOptionPrice()`라는 루트의 메서드를 거쳐 비즈니스 일관성 검증을 받아야 합니다.
- **트랜잭션 경계 제한 (규칙 3 보완 적용)**: `Product`와 내부의 `ProductOption` 객체들은 한 번의 DB 트랜잭션으로 동시에 저장됩니다. 단, '상품(Product)' 애그리거트와 '주문(Order)' 애그리거트를 하나의 트랜잭션으로 묶어서 동시 수정하는 것은 금지되며, 이 경우 도메인 이벤트(Domain Event)를 발행하여 결과적 일관성(Eventual Consistency)을 맞추어야 합니다.
