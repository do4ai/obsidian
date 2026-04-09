---
title: "MSA(Microservice Architecture)"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/knowledge/32be313f58b980eaa56ef58b10517652__knowledge/children/31fe313f58b980e3a117c2c1760e85c8__Development/children/31fe313f58b980dfbab5db1fd03b7de9__개발/children/31fe313f58b980fa9269f841ad2f1e8d__아키텍처 디자인/children/31fe313f58b9809cb249cf6d07fec42e__MSA(Microservice Architecture)
notion_id: 31fe313f58b9809cb249cf6d07fec42e
notion_url: https://www.notion.so/31fe313f58b9809cb249cf6d07fec42e
parent_notion_id: 31fe313f58b980fa9269f841ad2f1e8d
---
## Why: 왜 마이크로서비스(MSA)를 도입하는가?
과거의 거대한 단일 시스템(Monolithic)의 한계를 극복하고, **복원력(Resiliency)** 있고 **확장성(Scalability)**이 뛰어난 애플리케이션을 신속하게 구축하기 위해 도입합니다. 전체 시스템을 멈추거나 다시 빌드할 필요 없이 특정 기능만 업데이트하여 빠른 비즈니스 진화를 이끌어낼 수 있습니다. 또한, 소규모 개발 팀이 하나의 서비스를 온전히 책임지고 관리함으로써 개발 효율성을 극대화하기 위함입니다.
> **독립적 배포와 진화**
다른 서비스의 배포 일정이나 로직 변경에 전혀 영향을 받지 않고, 각 팀의 속도에 맞춰 **독립적으로 배포(Independent Deployment)**할 수 있습니다.
## What: 마이크로서비스란 무엇인가?
- **MSA(Microservice Architecture)**는 작고 독립적이며 느슨하게 결합된 구성 요소(서비스)들의 집합으로 시스템을 구축하는 아키텍처 스타일입니다.
중앙 집중식 데이터베이스를 공유하는 기존 방식과 달리, 각 마이크로서비스는 별도의 코드베이스로 관리되며 **자체 데이터(Database)**를 독립적으로 소유합니다.
서로 다른 서비스 간에는 내부 구현을 철저히 숨긴 채, 오직 잘 정의된 **API**를 통해서만 통신합니다.
> **폴리글랏(Polyglot) 프로그래밍 지원**
모든 서비스가 동일한 기술 스택을 공유할 필요 없이, 각 서비스의 목적에 가장 적합한 언어와 데이터베이스를 자유롭게 선택할 수 있습니다.
## How: MSA의 행열(Row/Column) 구조와 장단점
시스템을 도식화했을 때, 각 **행(Row)**은 완전히 분리된 독립 서비스를 의미하며 한 곳의 장애가 다른 곳에 영향을 주지 않는 **기능 고립성**을 보여줍니다. 반면 각 **열(Column)**은 서비스가 아무리 작더라도, 온전히 작동하기 위해 프레젠테이션부터 데이터 계층까지 **모든 기술적 계층**을 내부적으로 갖추고 있어야 함을 의미합니다.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/ed0e313f-58b9-819c-a3e2-00031320a63f/caf0b18f-3ab0-4621-8b94-62c738acfc64/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U6SYQCE%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T113255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwA%2BQtvcgQedP8hotYaTfzVG53n96AkjmBiSjTz%2BIahwIhAN6T4PHqZPljvVaEwrINaCx8%2FKdXOCc0BwEazmDlP8INKv8DCGAQABoMNjM3NDIzMTgzODA1IgwZtQVsfNLCyeRaZ8Iq3AOcE3RyyQ66ppRb0ZYTZOeHfqKCp5VUdNdsMVHVydbJ1uOMGtdqNEfPTQuJlrFbBdm8peYckZ0FgXuArkkXVQecvM1zTTqByI4sS6pmS7C%2FH7LPlRYFpabBCcDj5vuuCPGlwKXzD%2FKFfR1hkPDu4RU3zLglXcFEhiDKbg1CMgenFVVosgoS4RiBzIRc9GLSZvnp5In4ZBfGMviNoQtVPm%2F7%2B3mhoipaqdfth7Cs766y9wFewfpxAFxgqjB4wCm20Gbll9Me1f2Yio8sq6MWnhSf%2FnLHQZC8BgbMR%2Fs%2BrdhMBDoLviAyLaBONEetPb8X5e3KrsodzPFcX3wIlQqTPra0yj7avNQM1P61Dn5v%2B9CGK%2BfNLyEfzt6ijEuvqG0vSX53e%2BLrKWhIdW39F5ZjL6yzmkn5lKtr%2B7CoZq4bdbYHtW86YUXlCq0iwsGA5TPk1i7EZy7hWxUa7Ucb9LBElx%2B0pjZH7uMBkio8HuVyScGeE28q8zGNtkqFzroIJtyiNbKYt8UoyIG6F%2BFFdTTBdkLqmxLXa%2FDQCsNdecB5GlAyTJvKClMo37oCtpqjwSh9DdvalXsl5yRyFBL%2F5zHatVytnHGKHD7oBRFV26A%2BQXKvZlHA0Pgq2ChMOCClzjCMov7NBjqkAWdhQTAtJf%2FLLru%2F5USyLyz28DNdWwamBXbmNE7vhX8zqNuPqxiTh1Wo2ZJtIQzreVD%2B7Mx%2BJNVgvJGIYd1l1N6Tj2FhDI16QpZYXLRNUi%2F%2FWJYqKx0NWRp077hfMyqBh70iwtqz%2BDn3McjcF9%2BPrP03IUb5ifYYrwY532XtMSxVa%2FugBx1g5bEw3uKEgESoh%2BowJ3MdUFN2PvVa5ZN0LKERDzN7&X-Amz-Signature=a7229e0b5344c7983b6428d296adf5f34dd615a2a6dc6b2f9f42d8599d8136a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
이러한 철저한 분리 덕분에 시스템 전체의 유연성이 증가하고 일부 실패가 전체 장애로 번지지 않는 강력한 장점을 갖습니다.
> **MSA 도입 시 주의해야 할 단점**
분산된 서비스 간 네트워크 통신이 필수가 되므로, 연결 구축과 트랜잭션 관리의 복잡성이 급증하고 초기 개발 시간이 오래 소요됩니다.

출처: [https://learn.microsoft.com/ko-kr/azure/architecture/guide/architecture-styles/microservices](https://learn.microsoft.com/ko-kr/azure/architecture/guide/architecture-styles/microservices)
