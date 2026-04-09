---
title: "Ubiquitous Language (UL)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b98141b8decc658526d651__Ubiquitous Language (UL)
notion_id: 324e313f58b98141b8decc658526d651
notion_url: https://www.notion.so/324e313f58b98141b8decc658526d651
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
## Why: 왜 보편 언어가 필수적인가?
프로젝트에 참여하는 도메인 전문가(기획자, PM)와 개발자는 서로 다른 배경지식을 가지므로, 동일한 비즈니스 개념을 전혀 다른 용어로 해석하는 문제가 빈번하게 발생합니다. 이러한 해석의 차이를 방치하면, 회의실의 요구사항이 코드로 번역되는 과정에서 의도가 왜곡되고 치명적인 논리적 결함(Bug)으로 이어집니다. 따라서 파편화된 용어를 하나로 통일하여 소통의 번역 비용을 없애고, 오해를 원천 차단하는 절대적인 기준이 필요합니다.
> **용어 불일치의 위험성**
기획자가 말하는 '프리미엄 고객'을 개발자가 비즈니스 의도 없이 단순히 DB 테이블의 `grade` 값으로만 치부한다면, 정확한 도메인 모델링이 불가능해집니다.
## What: Ubiquitous Language의 정의와 목표
- **Ubiquitous Language(보편 언어)**는 특정 도메인 내에서 프로젝트 구성원 모두가 동의하고 사용하는 단 하나의 공통 언어를 의미합니다.
이 언어의 궁극적인 목표는 기획 문서에 적힌 비즈니스 용어와 실제 코드로 구현된 **클래스(Class)** 및 **메서드(Method)**의 이름이 완벽하게 일치하는 것입니다.
보편 언어가 명확해지고 통용되는 범위가 확정될수록, 해당 언어를 감싸는 **Bounded Context(바운디드 컨텍스트)**의 논리적 경계 또한 뚜렷해집니다.
## How: 보편 언어를 정의하는 과정과 명세 사례
보편 언어는 도메인 전문가와 개발자가 함께 비즈니스 시나리오를 분석하며 **용어사전(Glossary)**을 구축하는 과정을 통해 지속적으로 다듬어집니다.
예를 들어 주문 도메인에서 단순히 '취소'라고 부르던 모호한 단어를, 상황에 따라 **주문 취소(Cancel)**, **반품(Return)**, **환불(Refund)**이라는 명확한 행위 언어로 분리하여 정의해야 합니다.
이렇게 합의된 언어는 문서에만 머물지 않고 코드의 변수명이나 API 엔드포인트에 즉각적으로 반영되어 살아 움직여야 합니다.

**상품(Product) 도메인**에서 혼동하기 쉬운 용어들을 보편 언어로 정의하고 코드로 매핑한 명세 테이블 예시입니다.
> **보편 언어 용어사전(Glossary) 명세 예시주문(Order)**: 고객이 결제를 완료하여 배송을 기다리는 상품의 목록이며, 코드는 `Order` 클래스로 구현합니다.
**결제 대기(Pending Payment)**: 장바구니에서 주문으로 넘어갔으나 아직 카드사 승인이 나지 않은 상태이며, 코드는 `OrderStatus.PENDING`으로 명세합니다.
<table>
<tr>
<td>**보편 언어 (Ubiquitous Language)**</td>
<td>**비즈니스 의미 (Meaning)**</td>
<td>**코드 반영 예시 (Code Mapping)**</td>
</tr>
<tr>
<td>**상품 (Product)**</td>
<td>판매를 위해 등록된 독립적인 개별 품목</td>
<td>`class Product`</td>
</tr>
<tr>
<td>**옵션 (Option)**</td>
<td>색상, 사이즈 등 단일 상품에 부여할 수 있는 선택 속성</td>
<td>`class ProductOption`</td>
</tr>
<tr>
<td>**품절 (Out of Stock)**</td>
<td>재고(Stock)가 0이 되어 더 이상 주문할 수 없는 상태</td>
<td>`ProductStatus.OUT_OF_STOCK`</td>
</tr>
<tr>
<td>**진열 (Display)**</td>
<td>고객이 쇼핑몰 화면에서 상품을 볼 수 있도록 노출하는 행위</td>
<td>`displayProduct()`</td>
</tr>
<tr>
<td>**카탈로그 (Catalog)**</td>
<td>카테고리별로 분류되어 전시 대기 중인 상품들의 논리적 묶음</td>
<td>`class ProductCatalog`</td>
</tr>
</table>
