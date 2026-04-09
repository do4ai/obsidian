---
title: "3 Layer(N-tier)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/321e313f58b980679f96d8ca33f0f813__3 Layer(N-tier)
notion_id: 321e313f58b980679f96d8ca33f0f813
notion_url: https://www.notion.so/321e313f58b980679f96d8ca33f0f813
parent_notion_id: 31fe313f58b980fa9269f841ad2f1e8d
---
## Why: 왜 계층(Layer)을 분리해야 하는가?
소프트웨어의 계층은 책임을 명확히 분리하고 구성 요소 간의 종속성을 관리하기 위해 도입됩니다.
상위 계층은 하위 계층의 서비스를 사용할 수 있지만, 하위 계층은 상위 계층을 호출할 수 없는 단방향 의존성을 강제합니다. 이를 통해 특정 계층의 수정이 다른 계층에 미치는 파급 효과를 최소화하고 시스템의 복원력을 높입니다.
> **물리적 분리와 확장성(Scalability)**
논리적 계층을 별도의 서버(Tier)로 물리적으로 분리하면, 트래픽이 몰리는 특정 계층의 성능만 독립적으로 확장(Scale-out)할 수 있습니다.
## What: 3 Tier 물리적 구조와 3 Layer 논리적 구조
**3 Tier**는 장비가 물리적으로 구분되어 별도의 컴퓨터에서 실행되는 구조이며, **3 Layer**는 애플리케이션 내부에서 **Controller, Service, DAO**로 역할을 나눈 논리적 구조입니다.
- **Presentation Tier**: 사용자와 직접 상호작용하는 최상위 계층이며 프론트엔드 및 웹 서버가 위치합니다.
- **Application Tier (Middle Tier)**: 프레젠테이션과 데이터 사이의 가교 역할을 하며 백엔드 **비즈니스 로직(Business Logic)**을 전담합니다.
- **Database Tier**: 애플리케이션의 정보가 영구적으로 저장되고 관리되는 DBMS 및 데이터 액세스 계층입니다.
## How: 통신 모델 설계와 아키텍처의 장단점
각 계층은 직접 호출이나 메시지 큐를 통한 비동기 통신을 사용하며, 요구사항에 따라 두 가지 통신 모델을 결합하여 설계할 수 있습니다.
> **폐쇄형(엄격한 모델) vs 개방형(완화된 모델)**
폐쇄형은 인접 계층을 반드시 하나씩 통과해야 해 오버헤드가 큽니다. 반면 개방형은 중간 계층을 건너뛸 수 있으나 결합도가 높아져 변경이 어려워집니다.
- **장점 (이식성과 편의성)**: 개발자에게 익숙해 **학습 곡선(Learning Curve)**이 낮고, 기존 온프레미스에서 클라우드 환경으로의 마이그레이션이 가장 자연스럽습니다.
- **단점 (오버헤드와 배포 한계)**: 단순 CRUD만 수행할 경우 무의미한 네트워크 지연이 발생하며, 계층 내부가 거대하게 묶여있다면 특정 세부 기능만 독립적으로 배포하기 어렵습니다.
