---
title: "카카오로그인"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98114bbc9e9d8d8aa230a__20. 외부 로그인 설정/children/330e313f58b981ad93eff818824124a1__카카오로그인
notion_id: 330e313f58b981ad93eff818824124a1
notion_url: https://www.notion.so/330e313f58b981ad93eff818824124a1
parent_notion_id: 330e313f58b98114bbc9e9d8d8aa230a
---
# 카카오로그인

## 문서 목적

이 문서는 `https://in.passv.co.kr` 운영 기준으로 카카오 로그인을 붙이는 초안 매뉴얼이다.

2026-03-27 기준 PASSV 운영 baseline과 Kakao Developers 공식 문서를 함께 반영했다. 아직 실제 운영 화면 캡처는 붙이지 않았고, 설정 순서와 운영 값 위주로 먼저 정리했다.

이 초안에서 끝내야 하는 일은 아래 4가지다.

1. PASSV가 이미 쓰는 카카오 앱이 있는지 먼저 확인한다.
2. 카카오 로그인 사용 설정과 Redirect URI를 맞춘다.
3. PASSV가 실제로 쓰는 REST API 키, Client Secret, Redirect URI를 운영 변수에 넣는다.
4. 운영 로그인 화면에서 `카카오로 시작하기` 흐름이 시작되는지 확인한다.

## 먼저 알아둘 값

| 항목 | 값 |
| --- | --- |
| 운영 주소 | `https://in.passv.co.kr` |
| 로그인 화면 | `https://in.passv.co.kr/login` |
| 카카오 로그인 시작 경로 | `https://in.passv.co.kr/api/auth/kakao/start` |
| 카카오 로그인 콜백 URI | `https://in.passv.co.kr/api/auth/kakao/callback` |
| 프론트 변수 | `VITE_KAKAO_REST_API_KEY` |
| 백엔드 변수 1 | `KAKAO_REST_API_KEY` |
| 백엔드 변수 2 | `KAKAO_CLIENT_SECRET` |
| 백엔드 변수 3 | `KAKAO_REDIRECT_URI` |
| 현재 authorize scope | `account_email` |
| 현재 꼭 켜야 하는 동의항목 | `카카오계정(이메일)` |

중요한 점은 아래 4개다.

1. `redirect_uri`는 Kakao Developers에 등록한 값과 요청에 쓰는 값이 글자 하나까지 같아야 한다.
2. PASSV는 2026-03-27 기준 `GET /api/auth/kakao/start`에서 `scope=account_email`만 요청한다.
3. 따라서 Kakao Developers의 `동의항목`에서 `카카오계정(이메일)`이 비활성화돼 있으면 `KOE205 invalid_scope`가 날 수 있다.
4. 프론트와 백엔드는 같은 REST API 키를 공유하고, `Client Secret`은 백엔드에서만 사용한다.

## 초안 상태

- 이 문서는 2026-03-27 기준 초안이다.
- 실제 운영 캡처와 버튼 위치 캡처는 아직 추가하지 않았다.
- Kakao Developers 화면 문구는 이후 바뀔 수 있으므로, 최종 적용 직전 한 번 더 확인한다.

## 전체 순서

1. 기존 카카오 앱이 있는지 먼저 확인하기
2. 앱 기본 정보 확인하기
3. 웹 플랫폼과 로그인 Origin 정리하기
4. 카카오 로그인 사용 설정 켜기
5. Redirect URI 등록하기
6. 동의항목에서 이메일 사용 설정하기
7. Client Secret 상태 확인하기
8. PASSV 운영 변수에 반영하기
9. 운영 로그인 화면에서 마지막 확인하기

## 1. 기존 카카오 앱이 있는지 먼저 확인하기

### 작업 순서

1. `https://developers.kakao.com/`에 로그인한다.
2. 앱 목록에서 PASSV 운영용 앱이 이미 있는지 확인한다.
3. 이미 운영 중인 앱이 있다면 그 앱을 그대로 사용한다.
4. 정말 앱이 없다면 새 앱을 만든다.

### 설명

- Kakao 공식 문서는 서비스별로 한 개 앱 사용을 권장한다.
- 이미 카카오 로그인을 쓰는 서비스가 새 앱으로 갈아타면 기존 사용자 식별이 끊어질 수 있다.
- 따라서 PASSV가 이미 운영 앱을 갖고 있다면 새 앱을 만들지 않는 쪽이 안전하다.

## 2. 앱 기본 정보 확인하기

### 작업 순서

1. 앱 관리 페이지에서 `앱 > 일반 > 앱 기본 정보`로 이동한다.
2. `앱 이름`은 실제 사용자에게 보일 서비스명으로 확인한다.
3. `회사명`은 실제 운영 주체명으로 입력돼 있는지 확인한다.
4. `앱 대표 도메인`은 현재 운영 도메인 정책과 맞는지 확인한다.

### 설명

- Kakao 공식 문서에 따르면 앱 기본 정보는 로그인 동의 화면과 연결된 서비스 관리 화면에 노출된다.
- 따라서 초안 기준 권장 앱 이름은 `PASSV`다.
- 대표 도메인은 서비스 운영 정책에 맞춰 유지하고, 이미 운영 중인 앱에 값이 들어 있다면 함부로 바꾸지 않는다.

## 3. 웹 플랫폼과 로그인 Origin 정리하기

### 작업 순서

1. 앱 관리 페이지에서 웹 플랫폼 설정 화면으로 이동한다.
2. 로그인 Origin으로 아래 값을 등록하거나 기존 등록값에 포함돼 있는지 확인한다.

```text
https://in.passv.co.kr
```

3. 운영 외 환경을 같이 관리한다면 DEV/LOCAL 값을 운영값과 섞지 말고 별도로 관리한다.

### 설명

- PASSV 모바일 웹은 `https://in.passv.co.kr`에서 로그인 버튼을 노출한다.
- 따라서 운영 Origin은 최소한 위 주소를 기준값으로 관리해야 한다.
- 이 단계는 현재 PASSV 웹 로그인 표면을 기준으로 정리한 운영 메모다.

## 4. 카카오 로그인 사용 설정 켜기

### 작업 순서

1. `카카오 로그인 > 사용 설정`으로 이동한다.
2. `상태`를 `ON`으로 바꾼다.
3. 저장 후 설정이 유지되는지 확인한다.

### 설명

- Kakao 공식 문서 기준으로 `상태`가 `OFF`이면 로그인 요청 시 `KOE004` 에러가 발생한다.
- 새 앱을 만들었으면 이 단계가 가장 먼저 필요하다.

## 5. Redirect URI 등록하기

### 작업 순서

1. `앱 > 플랫폼 키 > REST API 키 > 리다이렉트 URI`로 이동한다.
2. 아래 값을 등록한다.

```text
https://in.passv.co.kr/api/auth/kakao/callback
```

3. 저장 후 중복 등록이나 오탈자가 없는지 다시 확인한다.

### 설명

- Kakao 공식 문서 기준으로 REST API 방식 카카오 로그인은 REST API 키 쪽에 Redirect URI를 등록해야 한다.
- `redirect_uri`가 다르면 `KOE006` 에러가 발생한다.
- PASSV 운영값은 2026-03-27 기준 `https://in.passv.co.kr/api/auth/kakao/callback`이다.

## 6. 동의항목에서 이메일 사용 설정하기

### 작업 순서

1. `카카오 로그인 > 동의항목`으로 이동한다.
2. `카카오계정(이메일)` 항목을 찾는다.
3. 최소한 사용 상태를 켠다.
4. 서비스 정책에 맞춰 `선택 동의` 또는 `필수 동의`로 저장한다.

### 설명

- PASSV 현재 운영 baseline은 authorize `scope`로 `account_email`만 요청한다.
- 그래서 이메일 동의항목이 꺼져 있으면 로그인 시작 단계에서 바로 실패할 수 있다.
- Kakao 공식 문서 기준으로 이메일을 `필수 동의`로 강제하려면 비즈 앱 전환과 관련 심사가 필요할 수 있다.
- 비즈 앱 전환 전이라면 우선 `선택 동의`라도 켜서 흐름이 막히지 않게 맞추는 편이 실무적으로 안전하다.

## 7. Client Secret 상태 확인하기

### 작업 순서

1. `앱 > 플랫폼 키 > REST API 키 > 클라이언트 시크릿`으로 이동한다.
2. Client Secret이 발급돼 있는지 확인한다.
3. 백엔드 운영 변수에 넣을 값을 안전하게 복사한다.

### 설명

- Kakao 공식 문서는 REST API 키 보안을 위해 Client Secret 기능 사용을 권장한다.
- PASSV 백엔드는 `KAKAO_CLIENT_SECRET`을 사용한다.
- 프론트에는 Client Secret을 넣지 않는다.

## 8. PASSV 운영 변수에 반영하기

### 이 단계에서 기억할 규칙

카카오 앱에서 확인한 값을 아래처럼 넣으면 된다.

| 위치 | 변수명 | 넣는 값 |
| --- | --- | --- |
| 프론트 운영 변수 | `VITE_KAKAO_REST_API_KEY` | Kakao Developers의 `REST API 키` |
| 백엔드 운영 변수 | `KAKAO_REST_API_KEY` | 같은 `REST API 키` |
| 백엔드 운영 변수 | `KAKAO_CLIENT_SECRET` | Kakao Developers의 `Client Secret` |
| 백엔드 운영 변수 | `KAKAO_REDIRECT_URI` | `https://in.passv.co.kr/api/auth/kakao/callback` |

### PASSV 코드 기준으로 보면

| 구분 | 파일 | 의미 |
| --- | --- | --- |
| 프론트 예시 변수 | `client/mobile/.env.example` | `VITE_KAKAO_REST_API_KEY` 자리 |
| 백엔드 예시 변수 | `server/.env.example` | `KAKAO_REST_API_KEY`, `KAKAO_CLIENT_SECRET`, `KAKAO_REDIRECT_URI` 자리 |
| 프론트 시작 URL | `client/mobile/src/mobile-auth/kakaoIdentity.ts` | `/api/auth/kakao/start`로 진입 |
| 운영 상태 기록 | `passv/sdd/05_operate/02_delivery_status/service_status.md` | 2026-03-27 기준 운영 Redirect URI와 scope 기록 |

### 설명

- 프론트는 Kakao REST API 키 존재 여부로 버튼 노출을 제어한다.
- 백엔드는 같은 REST API 키와 Client Secret으로 code exchange를 처리한다.
- `KAKAO_REDIRECT_URI`는 현재 운영에서 `https://in.passv.co.kr/api/auth/kakao/callback`로 고정해 맞추는 편이 안전하다.

## 9. 운영 로그인 화면에서 마지막 확인하기

### 작업 순서

1. `https://in.passv.co.kr/login`으로 이동한다.
2. `카카오로 시작하기` 버튼이 보이는지 확인한다.
3. 버튼을 눌렀을 때 `https://in.passv.co.kr/api/auth/kakao/start`로 시작되는 흐름이 열리는지 확인한다.
4. 실패 시 Kakao authorize URL의 `redirect_uri`와 `scope`를 먼저 확인한다.

### 설명

- 2026-03-27 운영 기록 기준으로 live `GET https://in.passv.co.kr/api/auth/kakao/start`는 `HTTP 307`과 함께 Kakao authorize URL을 반환한다.
- 현재 정상값은 `redirect_uri=https://in.passv.co.kr/api/auth/kakao/callback`와 `scope=account_email`이다.
- 여기서 다르면 운영 변수 또는 Kakao Developers 설정이 어긋난 것이다.

## 초보 운영개발자용 최종 체크리스트

1. PASSV 운영용 기존 카카오 앱이 있는지 먼저 확인했다.
2. 새 앱이 필요할 때만 만들었다.
3. 카카오 로그인 사용 설정을 `ON`으로 켰다.
4. 운영 Origin `https://in.passv.co.kr`를 기준으로 웹 표면을 정리했다.
5. Redirect URI에 `https://in.passv.co.kr/api/auth/kakao/callback`를 등록했다.
6. `카카오계정(이메일)` 동의항목을 켰다.
7. `REST API 키`를 `VITE_KAKAO_REST_API_KEY`와 `KAKAO_REST_API_KEY`에 같은 값으로 넣었다.
8. `Client Secret`을 `KAKAO_CLIENT_SECRET`에 넣었다.
9. `KAKAO_REDIRECT_URI`를 운영 콜백 URI와 같게 맞췄다.
10. 운영 로그인 화면에서 `카카오로 시작하기` 버튼을 눌러 흐름이 시작되는지 확인했다.
