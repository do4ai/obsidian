---
title: "Value Object"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b980ceaa57f44936e70e4c__Value Object
notion_id: 324e313f58b980ceaa57f44936e70e4c
notion_url: https://www.notion.so/324e313f58b980ceaa57f44936e70e4c
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 값 객체(Value Object)를 분리해야 하는가?
금액, 주소, 좌표 같은 속성들을 단순히 기본 타입(String, int)이나 무거운 엔티티로만 다루면 도메인 모델의 의미가 퇴색되고 코드 복잡도가 크게 증가합니다. 이러한 개념들을 하나의 응집된 묶음으로 만들지 않으면, 데이터의 유효성 검증 로직이 시스템 곳곳에 파편화됩니다. 또한 여러 곳에서 참조하는 값이 무분별하게 변경되어 발생하는 부작용(Side Effect)을 원천적으로 차단하기 위한 안전장치가 필요합니다.
> **부작용(Side Effect) 방지와 데이터 무결성**
값의 무결성을 보장하기 위해, 상태가 마음대로 변하지 않는 안전하고 예측 가능한 객체 설계가 필수적입니다.
## What: 값 객체(Value Object)란 무엇인가?
- **Value Object(값 객체, VO)**는 고유한 식별자(Identity)가 없으며, 객체가 가진 **속성들의 조합 그 자체**로만 비즈니스적 의미를 갖는 객체입니다.
VO의 가장 중요한 핵심 특징은 한 번 생성되면 내부 상태를 절대 변경할 수 없는 **불변성(Immutability)**을 가져야 한다는 것입니다.
## How: 값 객체의 설계와 실무 적용 예시
값 객체는 도메인의 개념을 명확히 표현하고, 생성 시점에 스스로 데이터의 유효성을 검증(Validation)하는 역할을 수행해야 합니다.
- **속성 기반 동등성**: 두 개의 `Address` 객체가 있을 때 식별자가 없으므로, '도시, 거리, 우편번호' 등 내부의 모든 속성 값이 100% 일치할 때만 같은 객체로 판별합니다.
- **불변 객체 통째로 교체**: 회원이 이사를 간 경우, 기존 `Address` 객체의 '도시' 필드를 수정하는 것이 아닙니다. 새로운 속성값을 가진 `Address` 객체를 통째로 새로 생성하여 엔티티에 갈아 끼워야 합니다.
- **풍부한 행위(Behavior)**: 단순히 데이터를 담는 DTO가 아닙니다. 화폐 단위가 같은지 검증하고 금액을 더하는 `addMoney()`처럼 자기 자신의 상태를 활용하는 비즈니스 로직을 내부에 포함해야 합니다.
**\[상품(Product) 도메인 기준 Value Object 적용 예시\]**
- **속성 기반 동등성 (규칙 1 적용)**: 상품의 물리적 크기를 나타내는 `Dimensions(width, height, depth)` 객체는 내부의 세 가지 수치가 모두 동일하면 완전히 같은 크기로 판별하여 로직을 수행합니다.
- **불변 객체 통째로 교체 (규칙 2 적용)**: 상품의 가격(`Money`)을 10,000원에서 12,000원으로 인상할 때, 기존 `Money` 객체 내부의 값을 `money.setAmount(12000)`으로 수정하는 것은 엄격히 금지됩니다. 반드시 `new Money(12000)`이라는 완전히 새로운 객체를 생성하여 엔티티에 갈아 끼워야 무결성이 보장됩니다.
- **풍부한 행위 (규칙 3 적용)**: 상품 가격(`Money`) 객체 내부에 'KRW'와 'USD'처럼 통화(Currency)가 다를 경우 덧셈을 막고 예외를 발생시키거나, 환율을 계산하여 합산하는 `add(Money other)` 비즈니스 로직을 객체 스스로가 포함하도록 설계합니다.
