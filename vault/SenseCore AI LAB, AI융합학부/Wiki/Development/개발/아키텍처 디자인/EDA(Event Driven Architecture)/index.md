---
title: "EDA(Event Driven Architecture)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/321e313f58b980c38002e123bbe88f8a__EDA(Event Driven Architecture)
notion_id: 321e313f58b980c38002e123bbe88f8a
notion_url: https://www.notion.so/321e313f58b980c38002e123bbe88f8a
parent_notion_id: 31fe313f58b980fa9269f841ad2f1e8d
---
## Why: 왜 이벤트 기반 아키텍처를 도입해야 하는가?
동기식 API 호출은 서비스 간에 **강한 결합(Tight Coupling)**을 유발하여 하나의 기능이 멈추면 전체 로직이 실패하는 치명적인 단점이 있습니다. 또한, 생산자가 상대방의 주소(Endpoint)를 반드시 알아야 하는 '지식의 결합' 때문에 새로운 요구사항 추가 시 기존 코드를 수정해야 하는 악순환이 발생합니다. EDA는 이러한 결합도를 극단적으로 낮추어, 각 시스템이 서로의 존재를 모르더라도 완벽하게 협력하고 유연하게 확장할 수 있도록 만들어 줍니다.
> **생산자의 무지(Producer Ignorance)와 독립성**
이벤트 생산자는 오직 채널의 존재만 알면 되며, 누가 구독하는지 알 필요가 없으므로 시스템 전체의 독립성과 복원력이 극대화됩니다.
## What: 이벤트와 EDA의 핵심 구성 요소
- **EDA(이벤트 기반 아키텍처)**는 시스템 내 의미 있는 사건을 불변의 사실인 **이벤트(Event)**로 발행하고 처리하는 구조입니다.
이벤트는 이미 일어난 명백한 사실이므로 `PayOrder`(명령)가 아닌 `OrderPaid`(이벤트)처럼 반드시 철저한 과거 시제로 명명해야 합니다.
- **Event Producer (이벤트 생산자)**: 사건을 비즈니스 로직에 맞춰 생성하고 발행하는 주체입니다.
- **Event Consumer (이벤트 소비자)**: 특정 이벤트에 관심을 가지고 구독하며, 발생 시 동작을 수행하는 주체입니다.
- **Message Broker (이벤트 채널)**: Kafka, RabbitMQ 등 생산자와 소비자를 완벽히 분리하여 이벤트를 안전하게 전달하는 중간 매개체입니다.
## How: 결합도를 낮추는 실제 작동 방식
EDA의 브로커(채널)를 활용하면, 앞서 언급한 두 가지 치명적인 결합을 기술적으로 완벽하게 해소할 수 있습니다.
- **지식의 결합 해소**: 새로운 소비자를 추가하더라도, 이벤트 생산자의 코드는 단 한 줄도 건드리지 않고 새로운 서비스가 채널을 구독하게만 하면 됩니다.
- **시간적 결합 해소**: 소비자가 일시적으로 꺼져 있어도 생산자는 문제없이 이벤트를 발행합니다. 이벤트는 채널에 안전하게 보관되며 소비자가 복구될 때 순차적으로 전달됩니다.
