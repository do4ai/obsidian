---
title: "분산 시스템"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/323e313f58b980f1b280e54c55aa1d26__분산 시스템
notion_id: 323e313f58b980f1b280e54c55aa1d26
notion_url: https://www.notion.so/323e313f58b980f1b280e54c55aa1d26
parent_notion_id: 31fe313f58b980fa9269f841ad2f1e8d
---
## Why: 왜 단일 컴퓨팅 대신 분산 컴퓨팅을 도입하는가?
단일 컴퓨터는 물리적인 자원의 한계가 뚜렷하며, 장애 발생 시 시스템 전체가 마비되는 단일 장애점(SPOF)의 위험을 안고 있습니다.
이를 극복하기 위해 필요에 따라 새 노드를 쉽게 추가하는 **확장성(Scalability)**과, 일부 컴퓨터가 고장 나도 전체 시스템이 정상 작동하는 **가용성(Availability)**을 확보해야 합니다.
고가의 단일 장비를 무리하게 구축하는 대신, 저렴한 하드웨어 자원을 최적화하여 높은 **효율성(Efficiency)**을 이끌어내기 위해 분산 아키텍처가 필수적입니다.
> **투명성(Transparency)과 일관성(Consistency)**
복잡한 인프라와 중복된 데이터 동기화 과정은 내부로 숨겨지며, 사용자는 여러 운영체제가 섞인 환경이라도 완벽한 단일 컴퓨터처럼 상호작용합니다.
## What: 시스템, 컴퓨팅, 환경의 명확한 정의
현대 아키텍처를 논할 때 이 세 가지 용어는 관점에 따라 명확히 구분되어 사용됩니다.
- **분산 시스템(Distributed System)**: 하드웨어와 소프트웨어를 모두 포함하며, 네트워크로 연결된 독립적인 컴퓨터들이 협력하여 사용자에게 '하나의 시스템'처럼 보이는 전체 구조입니다.
- **분산 컴퓨팅(Distributed Computing)**: 분산된 인프라 위에서 복잡한 연산을 여러 노드로 나누어 병렬 처리하고 통신 프로토콜을 다루는 소프트웨어적인 알고리즘이자 학문 분야입니다.
- **분산 환경(Distributed Environment)**: 네트워크 토폴로지, 클라우드 가용 영역, 컨테이너 오케스트레이션 등 시스템이 구동되는 물리적/논리적 인프라의 상태와 주변 조건을 의미합니다.
## How: 분산 시스템의 동작 방식과 내결함성 확보
분산 시스템은 여러 디바이스를 네트워크로 묶어 각자의 책임을 나누고 데이터를 지속적으로 동기화하는 방식으로 동작합니다.
- **내결함성(Fault Tolerance) 설계**: 시스템 설계 초기부터 개별 장비의 실패를 기정사실로 두고, 한 노드가 죽으면 다른 노드가 작업을 이어받도록 설계합니다.
- **데이터 복제와 정합성**: 여러 컴퓨터에 걸쳐 정보와 중복 데이터를 안전하게 공유하며, 모든 컴퓨터 간에 자동으로 데이터의 일관성을 맞추는 메커니즘을 가동합니다.
- **논리적 분리**: 물리적 디바이스의 복잡한 통신과 변환 과정을 미들웨어와 프로토콜로 감싸, 애플리케이션 계층에서는 투명하게 자원을 활용하도록 만듭니다.

출처: [https://aws.amazon.com/ko/what-is/distributed-computing/](https://aws.amazon.com/ko/what-is/distributed-computing/)
