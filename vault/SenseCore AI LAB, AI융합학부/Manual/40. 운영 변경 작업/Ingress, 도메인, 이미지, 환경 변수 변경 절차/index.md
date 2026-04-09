---
title: "Ingress, 도메인, 이미지, 환경 변수 변경 절차"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98127a3a5c1d5d883a489__40. 운영 변경 작업/children/338e313f58b98158aed9cb71470b8ec5__Ingress, 도메인, 이미지, 환경 변수 변경 절차
notion_id: 338e313f58b98158aed9cb71470b8ec5
notion_url: https://www.notion.so/338e313f58b98158aed9cb71470b8ec5
parent_notion_id: 330e313f58b98127a3a5c1d5d883a489
---
# Ingress, 도메인, 이미지, 환경 변수 변경 절차

## 문서 목적

이 문서는 운영 중인 서비스의 `ingress`, 도메인, 이미지 태그, 환경 변수를 바꿀 때 따르는 공통 절차를 정리한다.

이 종류의 변경은 작은 diff처럼 보여도 실제 영향 범위가 넓기 때문에, 변경 전 확인과 변경 후 검증을 같은 무게로 다룬다.

## 준비물

- 대상 서비스와 namespace 정보
- 변경할 GitOps 파일 경로
- 현재 운영 ingress host 와 service 포트 정보
- 변경 후 확인할 URL 또는 health endpoint

## 작업 전 확인

1. 무엇을 바꾸는지 하나의 문장으로 적는다.
2. 변경 이유와 기대 결과를 적는다.
3. 되돌릴 기준 커밋을 미리 확보한다.
4. 도메인, 이미지, 환경 변수 중 둘 이상을 한 번에 바꾸는 경우 영향 범위를 다시 검토한다.

## 절차

### 1. 대상 overlay와 현재 live 구성을 확인한다

```bash
cd /home/sh/Documents/Github/gitops
grep -n "path:" k8s/clusters/do4ai-prod/*app.yaml
sudo kubectl get deploy,svc,ing -n <namespace>
```

확인 포인트는 아래다.

- 실제 운영이 어느 overlay를 보고 있는가
- 현재 ingress host 와 backend service가 무엇인가
- 현재 이미지는 무엇인가

### 2. 변경 파일을 좁힌다

자주 보는 파일은 아래다.

- `ingress.yaml`
- `kustomization.yaml`
- `deployment.yaml`
- `values.yaml`
- secret 또는 config 참조 파일

변경 범위가 넓으면 한 번에 진행하지 말고 도메인/이미지/환경 변수 변경을 나눠서 처리한다.

### 3. 변경 전 diff 기준을 잡는다

```bash
git status --short
git diff -- <target-file>
```

여기서 의도한 변경만 들어가는지 확인한다. unrelated diff가 섞이면 먼저 분리한다.

### 4. 변경 후 영향 경로를 다시 읽는다

변경했으면 아래를 확인한다.

1. ingress host가 올바른가
2. backend service 이름과 포트가 맞는가
3. 이미지 태그가 기대한 버전인가
4. 환경 변수 이름과 secret/config 참조가 끊기지 않았는가

### 5. 반영 후 수렴 여부를 확인한다

```bash
sudo kubectl get applications -A
sudo kubectl get deploy,svc,ing -n <namespace>
sudo kubectl get pods -n <namespace>
```

필요하면 아래도 함께 본다.

```bash
sudo kubectl describe ingress -n <namespace> <ingress-name>
sudo kubectl logs deploy/<deploy-name> -n <namespace> --tail=100
```

## 검증 기준

- 도메인 변경이면 새 host가 ingress에 반영됐는가
- 이미지 변경이면 새 image tag로 pod가 올라왔는가
- 환경 변수 변경이면 앱이 기동 실패 없이 올라오는가
- `/health` 또는 주요 진입 URL이 응답하는가

## 롤백 기준

아래 중 하나라도 해당하면 즉시 롤백을 검토한다.

- pod가 반복 재시작한다
- ingress backend 연결이 끊긴다
- 핵심 URL이 응답하지 않는다
- 환경 변수 누락으로 애플리케이션이 시작되지 않는다

## 롤백 절차

1. 변경 전 기준 커밋을 확인한다.
2. 변경한 파일을 직전 정상 상태로 되돌린다.
3. GitOps 기준이 정상 diff인지 다시 확인한다.
4. `Application` 과 pod가 직전 정상 상태로 수렴하는지 확인한다.

## 작업 후 기록

- 바꾼 항목: ingress, 도메인, 이미지, 환경 변수 중 무엇인지
- 바꾼 파일 경로
- 검증한 URL 또는 health endpoint
- 롤백 여부와 최종 상태
