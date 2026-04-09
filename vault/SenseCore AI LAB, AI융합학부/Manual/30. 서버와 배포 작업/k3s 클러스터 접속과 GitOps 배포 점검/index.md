---
title: "k3s 클러스터 접속과 GitOps 배포 점검"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b9813fbc22ca7f38ac4014__30. 서버와 배포 작업/children/338e313f58b981dfbed0fc166c44a2c2__k3s 클러스터 접속과 GitOps 배포 점검
notion_id: 338e313f58b981dfbed0fc166c44a2c2
notion_url: https://www.notion.so/338e313f58b981dfbed0fc166c44a2c2
parent_notion_id: 330e313f58b9813fbc22ca7f38ac4014
---
# k3s 클러스터 접속과 GitOps 배포 점검

## 문서 목적

이 문서는 운영 서버에 접속해 `k3s` 클러스터와 `ArgoCD`, `gitops` 반영 상태를 안전하게 확인하는 절차를 정리한다.

직접 변경 전에 반드시 현재 상태를 읽고, 변경 후에는 같은 기준으로 다시 검증하는 것을 기본 원칙으로 한다.

## 준비물

- 운영 서버 SSH 접속 권한
- 서버에서 `sudo kubectl` 실행 권한
- `gitops` 레포 경로 정보
- 장애 시 연락할 운영 담당자와 공지 채널

## 작업 전 확인

1. 이번 작업이 `조회만 하는 점검`인지 `실제 변경을 포함한 배포 점검`인지 먼저 구분한다.
2. 사용자 영향이 큰 시간대인지 확인한다.
3. 직전 변경 이력과 미해결 장애가 있는지 확인한다.
4. `gitops` 기준 브랜치와 최근 커밋이 무엇인지 메모한다.

## 절차

### 1. 운영 서버에 접속한다

```bash
ssh -p 2200 sh@203.253.84.77
```

접속이 되지 않으면 서버 문제인지, 계정 문제인지, 네트워크 문제인지 먼저 구분한다. 비밀번호나 키 자체는 이 문서에 적지 않는다.

### 2. live GitOps 레포 위치를 확인한다

```bash
cd /home/sh/Documents/Github/gitops
pwd
git status --short
git log --oneline -n 3
```

여기서 확인할 것은 아래다.

- 현재 레포가 예상한 경로에 있는가
- 로컬 변경사항이 남아 있지 않은가
- 마지막 커밋이 작업자가 인지한 기준과 같은가

### 3. 클러스터 전체 상태를 확인한다

```bash
sudo kubectl get ns
sudo kubectl get applications -A
sudo kubectl get pods -A
sudo kubectl get ingress -A
```

여기서 먼저 보는 기준은 아래다.

1. 핵심 namespace가 모두 보이는가
2. `Application` 이 `Missing` 이나 `Unknown` 인 것이 없는가
3. 핵심 서비스 pod가 `CrashLoopBackOff` 나 `Pending` 으로 멈춰 있지 않은가
4. ingress host가 예상한 도메인과 어긋나지 않는가

### 4. 배포 대상 앱을 역추적한다

예를 들어 `palcar` 배포를 확인한다면 아래 순서로 본다.

```bash
grep -n "path:" k8s/clusters/do4ai-prod/*app.yaml
sed -n '1,200p' k8s/clusters/do4ai-prod/palcar-prod-app.yaml
```

그 다음 아래를 확인한다.

1. `source.path` 가 어느 overlay를 가리키는가
2. 대상 overlay가 `prod` 인가
3. 실제 수정 파일이 그 overlay 또는 base에 반영돼 있는가

### 5. 변경 후 수렴 상태를 다시 확인한다

```bash
sudo kubectl get applications -A
sudo kubectl get pods -n palcar
sudo kubectl get deploy,sts,svc,ing -n palcar
```

변경 직후에는 아래 순서로 판정한다.

1. `SYNC STATUS`
2. `HEALTH STATUS`
3. pod 재시작 여부
4. 서비스와 ingress 연결 상태

## 검증 기준

- 대상 `Application` 이 사라지지 않았는가
- 대상 namespace의 pod가 기동 실패 없이 수렴하는가
- ingress 와 service 연결이 유지되는가
- 직전 정상 상태와 비교했을 때 불필요한 namespace 전체 장애가 생기지 않았는가

## 실패 시 대응

### SSH 접속이 안 될 때

1. 동일 호스트에 다른 계정 접속이 되는지 확인한다.
2. 운영 담당자에게 서버 상태를 확인해 달라고 요청한다.
3. 자체적으로 우회 접속을 시도하지 말고 접근 경로를 확정한 뒤 다시 진행한다.

### GitOps 기준이 의심될 때

1. 서버 live clone만 믿고 바로 수정하지 않는다.
2. 기준 브랜치와 원격 최신 커밋을 다시 대조한다.
3. 기준이 불분명하면 변경 작업을 중단하고 담당자와 기준 커밋을 확정한다.

### 배포 후 앱이 수렴하지 않을 때

1. 변경 범위를 좁혀 어떤 overlay/base 수정이 원인인지 먼저 찾는다.
2. 직전 정상 커밋으로 되돌릴 수 있으면 GitOps 기준을 복구한다.
3. `Application` 상태와 pod 로그를 함께 수집해 장애 채널에 공유한다.

## 작업 후 기록

- 확인한 서버와 레포 경로
- 확인한 기준 커밋
- 점검 대상 앱과 namespace
- 최종 판정: 정상, 추가 조사 필요, 즉시 롤백 필요
- 후속 담당자와 전달한 근거
