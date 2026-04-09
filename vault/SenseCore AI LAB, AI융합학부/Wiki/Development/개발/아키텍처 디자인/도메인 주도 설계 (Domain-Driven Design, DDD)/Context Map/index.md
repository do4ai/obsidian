---
title: "Context Map"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809486f6d78414308d4f__도메인 주도 설계 (Domain-Driven Design, DDD)/children/324e313f58b981c38a10d7779c3770e7__Context Map
notion_id: 324e313f58b981c38a10d7779c3770e7
notion_url: https://www.notion.so/324e313f58b981c38a10d7779c3770e7
parent_notion_id: 31fe313f58b9809486f6d78414308d4f
---
# Context Map (컨텍스트 맵)
## 1. 컨텍스트 맵의 정의
컨텍스트 맵은 **Bounded Context(서비스)**들 간의 **'관계'**와 **'통신 방식'**을 정의하는 전략적 청사진입니다.
- **MSA 프로젝트의 '정치 지도'**: "어떤 팀이 어떤 팀에 의존하는가?" 혹은 "두 팀의 모델이 변경될 때 서로에게 어떤 영향을 주는가?"를 명확히 하는 역할을 합니다.
- **강한 결합(Tight Coupling) 방지**: 이 관계를 명확히 정의하지 않으면, 서비스 경계를 나눈 의미가 무색하게 서비스들 간에 불필요하게 높은 의존성이 다시 발생합니다.
다음 다이어그램은 다양한 Bounded Context들이 어떤 관계 패턴으로 서로 연결되는지를 한눈에 보여줍니다. 각 관계에 표시된 U, D, SK, ACL, OHS, PL, CF 등의 약어가 이 문서에서 설명하는 핵심 관계 패턴들입니다.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/ed0e313f-58b9-819c-a3e2-00031320a63f/c158893d-de0d-4b57-88c8-240d1bbbf05e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BRUOHTR%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T121432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx4Kni9KiTj2iG10Mu2nly5hb4xUnV3Ej%2Ft0NCW996PQIhALRWFatdc17sT8jfiMtlvUcJoySos7IhmJCm16czNIxyKv8DCGAQABoMNjM3NDIzMTgzODA1Igw9%2FvhOUTjbjJI4lT0q3AM941Ih3dTvuDnPh8m3gkH5URNQCLDyrxGrqwjKpe1Nz13pSpzuFH5XvcaNhbXTX9vxNB99WWDUpI7KDUqF9aTTysAEZJriqGHY1dDC%2FIi93uKG9qbt8VcyQeqtiuExQyrBY7VKRHjzdDOYdfmSXxl42xRl0aL7nhgk7HeGQ%2BFNh%2BTkzf06%2BCArB4KErRqoBHTnT789XI2%2FHAFwS9xkxz0QpBf6lnBZGgpnL%2FUlmcRVimXvb0MkdiFsi2YG%2Fo7OC3W2hY5dWyopoiMaZdAtpJiUmdxXMuUjH3Y2G8WyusM9ikKcMonSXd7iRQLbGJCzh7vJqRpPCvYei2XILP8OI7J5Tk9EuB6ZjoILx64PIF7sUUTv%2FMsEroyQ1IWcZFsqKu5cHqp3oj8xX%2FFn9xhY5ZAuXC9QKQ7mGplngxotKApsMMlXaUbGZPyQhvab5ZQyVriRuIPqjTibrmkhzMSdqyc7pH0%2FXd4upzzBEBe6grgnI8CNNt0MrNx%2FLIRh0EllCMdOdDOiMJTyAFta%2B%2Bz%2FrW%2Be4C2HHxYL4L3BfB%2B2RWdujSNcr2DFFmV9Ai96HylBqhVf%2BQwrd1mWSMwtu7lPuCddW3kg7LOntWQVg%2FkkNjNIRmtVwJiP%2FF3FPIe8STCKov7NBjqkARfKzMN5siHUU6joe59eppaMmR%2FANZpWclPQisTdXFN0uiAwdqQbTf9qzI%2BZi%2Bw1hQcdartjXjLHWrZZnnBlTt9KlU9LzoE8wZ5%2FcqCJVAqIfT0chmS1Q5nIriUADLy63wYXw0%2FTWxZ%2FPQCj1qN31hcmI%2F1yK1aJdmtqytFzsgpo0P8FRHoqbzEexQT9bkIDpWybR2oQHTc8yn3B%2F6jO6zxKoxVx&X-Amz-Signature=664a971fab85dab4ed8717a517dbc7d8c1e9a34b17a10bbe49ec382ec46e9844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 2. 핵심 관계 패턴
### 모든 관계의 기본: 상류와 하류
컨텍스트 간의 모든 관계는 정보와 기능의 흐름에 따라 상류와 하류로 구분됩니다.
- **Upstream (U - 상류)**: 다른 서비스에게 정보나 기능을 **제공하는** 상류 서비스입니다.
- **Downstream (D - 하류)**: 업스트림의 정보나 기능을 **소비하는** 하류 서비스입니다.
**\[상품 도메인 예시\]**: '상품(Product) 컨텍스트'가 상품 정보를 제공하는 **Upstream**이 되고, 이를 받아 주문서를 작성하는 '주문(Order) 컨텍스트'가 **Downstream**이 됩니다.
## 3. 세부 관계 패턴 및 특징
상류와 하류 관계 내에서 의존성의 강도와 통신 방식에 따라 다음과 같은 구체적인 패턴들이 사용됩니다.
### 1) SK (Shared Kernel - 공유 커널)
두 개 이상의 BC(Bounded Context)가 도메인 모델의 **일부를 공유(Share)**하는 관계입니다.
- **특징**: 모든 서비스가 공통으로 사용하는 Value Object나 클래스를 공통 라이브러리로 만들어 공유합니다.
- **주의사항**: 공통 라이브러리를 수정할 때 이 커널을 공유하는 **모든 서비스가 동시에 수정 및 재배포**되어야 하기에, 이는 MSA의 독립 배포 원칙을 깨뜨립니다.
- **적용**: 공통 라이브러리 수정 시 관련된 모든 팀이 코드를 통합하고 테스트해야 하기 때문에 **한 개 이상의 팀이 하나의 팀처럼 긴밀하게 협업하고 지속적 통합(CI)**을 완벽히 수행 가능한 조직적 환경이 뒷받침될 때에만 선택해야 합니다. 
- **\[상품 도메인 예시\]**: 상품 컨텍스트와 주문 컨텍스트가 상품의 가격을 계산하기 위해 `Money`라는 동일한 값 객체(Value Object) 코드를 라이브러리로 공유하는 경우입니다.
### 2) ACL (Anti-Corruption Layer - 안티 코럽션 레이어)
다운스트림 서비스가 업스트림의 오염된 모델로부터 자신의 **순수한 도메인 모델을 보호**하기 위해 구축하는 **방어막이자 번역기 계층**입니다.
- **특징 (느슨한 결합)**: 필요한 필드만 추출하여 BC 내부의 순수한 모델로 번역하여 사용합니다.
- **오염 방지**: 사용자가 불필요한 필드를 읽게 될 경우 맥락이 오염되어 필요한 필드에 대한 분류가 어려워지는 것을 막습니다. (오염 = 불필요한 맥락)
- **이점**: 필요한 데이터만 사용자에게 제공함으로써 개발자의 실수를 줄여줍니다.
- **\[상품 도메인 예시\]**: 주문 컨텍스트가 상품 컨텍스트의 방대한 JSON 응답(이미지, 카테고리 등) 중 주문에 꼭 필요한 '상품ID'와 '단가'만 추출하여 자신의 `OrderLineItem` 모델로 번역(ACL)하는 경우입니다.
### 3) OHS (Open Host Service) & PL (Published Language)
업스트림 서비스가 자신의 기능을 외부에 공개하는 방식입니다.
- **OHS (오픈 호스트 서비스)**: 다운스트림들이 사용할 수 있도록 잘 정의된 공개 인터페이스를 제공하는 업스트림 서비스입니다.
- **PL (공표된 언어)**: OHS가 사용하는 표준 데이터 포맷입니다. “우리 서비스와 대화하려면 반드시 이 형식을 사용해야 한다”는 약속입니다.
- **통신 방식:**
- **동기 방식: **요청 → OHS(공개 REST API) → PL 형식으로 응답 반환
- **비동기 방식: **이벤트 발생 → PL 형식으로 발행 → 브로커 → 구독된 컨텍스트가 PL을 읽고 처리
- **\[상품 도메인 예시\]**: 상품 컨텍스트가 `GET /products/{id}`라는 REST API(OHS)를 열어두고, 이를 호출하면 항상 약속된 규격의 JSON 포맷(PL)으로 상품 정보를 반환하는 경우입니다.
### 4) CF (Conformist - 준수자)
다운스트림 서비스가 업스트림의 모델을 아무런 번역이나 수정 없이 **그대로 받아들여 사용하는** 관계입니다. 다운스트림은 업스트림 모델에 대해 어떠한 영향력도 행사하지 않으며 전적으로 **순응**합니다.
- **이점**: ACL과 같은 번역 계층을 만들 필요가 없기에 개발 속도가 매우 빠르고 초기 구현이 간단합니다.
- **단점 (강한 결합)**: 다운스트림이 업스트림에 완전히 종속됩니다. 업스트림의 로직 변경으로 다운스트림에 이상이 없음에도 다운스트림은 수정, 테스트, 재배포를 해야 하므로 독립적인 배포 원칙을 위반하게 됩니다.
- **\[상품 도메인 예시\]**: 단순한 사내 통계(Analytics) 컨텍스트가 상품 컨텍스트에서 발행하는 '상품 등록 이벤트' 데이터 모델을 어떠한 변환도 없이 100% 그대로 수용하여 DB에 적재하는 경우입니다.
