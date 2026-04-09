---
title: "Infisical 시크릿 관리 가이드"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__50. 인프라와 플랫폼/children/338e313f58b98101a383cf9fc68ffcf5__Infisical 시크릿 관리 가이드
notion_id: 338e313f58b98101a383cf9fc68ffcf5
notion_url: https://www.notion.so/338e313f58b98101a383cf9fc68ffcf5
parent_notion_id: 330e313f58b981a0b738ed69daa8f3a0
---
# Infisical 시크릿 관리 가이드

이 문서는 연구실 운영 시크릿이 어떤 구조로 관리되는지 설명하는 가이드다.

## 왜 별도 시크릿 시스템이 필요한가

운영 환경에는 DB 비밀번호, API 키, 토큰처럼 레포에 그대로 두면 안 되는 값이 있다.

이 문서 집합에서 중요한 기준은 아래다.

- 시크릿 원문은 레포에 두지 않는다.
- 앱은 실행 시점에 필요한 시크릿을 받아 사용한다.
- 운영자는 값 자체보다 `어디가 원천이고 어떻게 주입되는가`를 이해해야 한다.

## Infisical의 역할

Infisical은 시크릿 원천 저장소다.

운영 관점에서는 아래 세 층으로 생각하면 된다.

1. Infisical에 원본 시크릿이 저장된다.
2. 운영 정책에 따라 필요한 값이 선택된다.
3. Kubernetes 안에서는 앱이 읽을 수 있는 `Secret` 형태로 주입된다.

즉 앱은 Infisical 그 자체를 직접 읽기보다, Kubernetes 운영 경로를 통해 결과를 받는다고 이해하면 된다.

## 초보자가 자주 헷갈리는 포인트

| 헷갈리는 것 | 실제 의미 |
| --- | --- |
| Infisical에 값이 있다 | 아직 앱이 그 값을 쓰고 있다는 뜻은 아니다 |
| Kubernetes Secret이 있다 | 원천 저장소가 레포라는 뜻은 아니다 |
| env 값이 비어 있다 | 앱 문제일 수도 있지만, 시크릿 동기화 경로 문제일 수도 있다 |

## 장애를 볼 때의 기본 관점

시크릿 문제는 보통 아래 형태로 드러난다.

- 앱이 부팅 직후 죽는다
- 인증 또는 DB 연결이 실패한다
- 특정 환경 변수만 비어 있다

이때 운영자는 `값이 맞는가`만 보지 말고 아래를 같이 봐야 한다.

1. 원천 시크릿이 있는가
2. 올바른 대상에 매핑됐는가
3. Kubernetes Secret으로 주입됐는가
4. 앱이 그 Secret을 참조하는가

## 이 문서와 절차 문서의 경계

이 문서는 구조와 책임을 설명한다.

아래 같은 작업은 `Manual` 에서 다룬다.

- 시크릿 추가
- 시크릿 변경
- 시크릿 회전
- 권한 부여와 회수
