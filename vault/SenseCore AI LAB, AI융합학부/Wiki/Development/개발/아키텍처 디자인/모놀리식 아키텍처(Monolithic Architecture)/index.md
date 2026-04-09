---
title: "모놀리식 아키텍처(Monolithic Architecture)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9801090e3f9f3c280a976__모놀리식 아키텍처(Monolithic Architecture)
notion_id: 31fe313f58b9801090e3f9f3c280a976
notion_url: https://www.notion.so/31fe313f58b9801090e3f9f3c280a976
parent_notion_id: 31fe313f58b980fa9269f841ad2f1e8d
---
## Why: 왜 모놀리식 아키텍처를 선택하는가?
초기 개발과 배포의 복잡성을 최소화하고, 모든 비즈니스 기능을 단일 코드베이스에서 직관적으로 구축하기 위해 사용되는 전통적인 개발 모델입니다. 시스템 내부에서 한 가지 형식의 통신만 수행하므로 다른 서비스 간의 통신을 변환할 부담이 없어 **DevOps**와 같은 프로세스 연동이 매우 간편합니다. 폐쇄형 시스템으로서 데이터 처리가 완전히 내부에서 이루어지기 때문에 사이버 위협으로부터 더 안전하게 보호된다는 강력한 장점이 있습니다.
> **번거로움 없는 테스트와 디버깅**
모든 기능이 한 곳에 모여 있어 중앙 로깅 시스템을 통한 엔드투엔드(End-to-End) 테스트와 디버깅 작업이 훨씬 덜 복잡하고 부담이 적습니다.
## What: 모놀리식 아키텍처란 무엇인가?
**Monolithic Architecture**는 애플리케이션 실행에 필요한 모든 코드가 하나의 중앙 저장소에 보관되는 거대한 단일 소프트웨어 구조입니다.
운영체제에서 커널이 모든 기능을 직접 관리하듯, 단일 실행 파일이나 디렉터리로 패키징되어 운영됩니다.
구성 요소가 물리적으로 분리되어 있지 않기 때문에 빌드와 배포 과정이 단순하며 초기 유지 관리가 상대적으로 용이합니다.
## How: 모놀리식의 구조적 한계와 실무적 고려사항
초기 구축은 빠르지만, 시스템이 거대해질수록 구성 요소들이 지나치게 **강한 결합(Tight Coupling)**이되어 다음과 같은 치명적인 단점이 발생합니다.
- **확장성(Scalability)의 한계**: 트래픽이 몰리는 특정 기능만 개별적으로 확장할 수 없습니다. 작은 기능 하나만 변경하더라도 거대한 전체 시스템을 다시 빌드하고 배포해야 하므로 막대한 시간과 인력이 소요됩니다.
- **새로운 기술에 대한 저항성**: 단일 코드베이스의 특성상 부분적인 신기술 도입이나 프레임워크 전환이 불가능에 가깝습니다. 새로운 기술을 통합하려면 애플리케이션 전체를 뜯어고치는 재설계 위험을 감수해야 합니다.

출처: [https://www.ibm.com/kr-ko/think/topics/monolithic-architecture](https://www.ibm.com/kr-ko/think/topics/monolithic-architecture)
