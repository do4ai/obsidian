---
title: "Infisical 시크릿 반영과 권한 변경 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98140bc33f493356b50dc__60. 시크릿-권한 작업/children/338e313f58b98168ba1ddcebbea85b42__Infisical 시크릿 반영과 권한 변경 절차
notion_id: 338e313f58b98168ba1ddcebbea85b42
notion_url: https://www.notion.so/338e313f58b98168ba1ddcebbea85b42
parent_notion_id: 330e313f58b98140bc33f493356b50dc
---
# Infisical 시크릿 반영과 권한 변경 절차

## 문서 목적

이 문서는 `Infisical` 과 `infisical-operator` 를 사용하는 환경에서 시크릿 값을 추가하거나 바꾸고, 관련 권한을 조정할 때 따르는 절차를 정리한다.

시크릿 작업은 값 자체보다 반영 경로와 검증 기준이 더 중요하다. 값은 문서에 남기지 않고, 경로와 확인 결과만 남긴다.

## 준비물

- 대상 서비스 이름과 namespace
- 어떤 시크릿 키를 바꿀지에 대한 명확한 목록
- Infisical 접근 권한
- 반영 후 앱 재기동 또는 재수렴 확인 권한

## 작업 전 확인

1. 새 값인지, 기존 값 교체인지 구분한다.
2. 어떤 서비스가 그 값을 읽는지 적는다.
3. 변경 즉시 영향이 나는지, 재기동이 필요한지 확인한다.
4. 되돌릴 수 있는 이전 상태가 있는지 확인한다.

## 절차

### 1. 시크릿 소비 경로를 먼저 확인한다

먼저 아래를 확인한다.

1. 어떤 namespace에서 쓰는가
2. 어떤 deployment 또는 job이 읽는가
3. `Infisical` 에서 `Kubernetes Secret` 으로 어떻게 내려오는가

시크릿 값을 바꾸기 전에 소비 경로를 안 보면 잘못된 namespace에 반영할 위험이 있다.

### 2. Infisical에서 값을 추가 또는 수정한다

작업 시 주의점은 아래다.

- 키 이름을 기존 참조와 정확히 맞춘다
- 값 포맷이 바뀌는지 확인한다
- 같은 이름의 키가 다른 환경에 중복돼 있지 않은지 본다

### 3. operator 반영 여부를 확인한다

```bash
sudo kubectl get secrets -n <namespace>
sudo kubectl describe secret -n <namespace> <secret-name>
```

여기서 확인할 것은 아래다.

- 대상 secret 이 생성 또는 갱신됐는가
- 기대한 key가 존재하는가
- 반영 지연이 비정상적으로 길지 않은가

### 4. 앱이 새 값을 정상적으로 읽는지 확인한다

```bash
sudo kubectl get pods -n <namespace>
sudo kubectl logs deploy/<deploy-name> -n <namespace> --tail=100
```

기동 실패, 인증 실패, 외부 API 연결 실패가 생기지 않는지 확인한다.

### 5. 권한 변경이 함께 있다면 최소 범위로 적용한다

권한 변경은 아래 원칙으로 한다.

1. 필요한 사용자 또는 서비스 계정만 대상으로 한다.
2. 읽기/쓰기/관리 권한을 한 번에 넓히지 않는다.
3. 변경 후 실제 접근이 되는지 한 번만 검증한다.

## 검증 기준

- `Kubernetes Secret` 이 기대한 namespace에 존재하는가
- 앱이 기동 실패 없이 수렴하는가
- 변경한 키를 참조하는 기능이 정상 동작하는가
- 불필요하게 넓은 권한이 추가되지 않았는가

## 실패 시 대응

### secret 반영이 안 될 때

1. 키 이름과 대상 환경을 다시 확인한다.
2. operator가 정상인지 확인한다.
3. 값을 반복해서 덮어쓰기 전에 반영 경로를 다시 점검한다.

### 앱이 새 값으로 실패할 때

1. 직전 정상 값으로 복구할 수 있는지 확인한다.
2. 로그에서 인증, 연결, 파싱 오류가 무엇인지 확인한다.
3. 필요하면 이전 값으로 되돌린 뒤 원인을 분리한다.

### 권한 변경이 과했을 때

1. 추가한 권한을 즉시 최소 범위로 줄인다.
2. 영향을 받은 사용자와 서비스 계정을 다시 확인한다.
3. 변경 이력을 운영 채널에 공유한다.

## 작업 후 기록

- 바꾼 키 이름 목록
- 대상 namespace와 서비스
- 반영 확인 시각
- 최종 결과와 후속 조치 필요 여부
