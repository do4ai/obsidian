---
title: "구글로그인"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98114bbc9e9d8d8aa230a__20. 외부 로그인 설정/children/330e313f58b980a8b0aac94bf3a24091__구글로그인
notion_id: 330e313f58b980a8b0aac94bf3a24091
notion_url: https://www.notion.so/330e313f58b980a8b0aac94bf3a24091
parent_notion_id: 330e313f58b98114bbc9e9d8d8aa230a
---
# 구글로그인

## 문서 목적

이 문서는 `https://in.passv.co.kr` 운영 기준으로 Google 로그인을 구현하는 매뉴얼이다.

대상은 초보 운영개발자다. 따라서 아래 3가지만 끝내면 된다.

1. Google Cloud Console에서 Google 로그인 앱을 만든다.
2. PASSV가 실제로 쓰는 값을 가져온다.
3. PASSV 운영 설정에 같은 값을 넣는다.

## 먼저 알아둘 값

| 항목 | 값 |
| --- | --- |
| 운영 주소 | `https://in.passv.co.kr` |
| 로그인 화면 | `https://in.passv.co.kr/login` |
| Authorized JavaScript origins | `https://in.passv.co.kr` |
| Authorized redirect URIs | `https://in.passv.co.kr/api/auth/google/redirect` |
| PASSV에 실제로 넣는 값 | `Client ID` |
| 이번 구현에서 쓰지 않는 값 | `Client Secret` |

중요한 점은 아래 2개다.

1. `Authorized JavaScript origins`와 `Authorized redirect URIs`는 글자 하나까지 정확히 같아야 한다.
2. 현재 PASSV 운영 구현은 `Client Secret`이 아니라 `Client ID`를 사용한다.

## 캡처 파일 위치

실제 작업 캡처는 아래 폴더에 저장했다.

`notion/ssot/assets/manual/google-login-in-passv-co-kr/`

보안상 위험한 값은 캡처에서 마스킹했다.

## 전체 순서

1. Google Cloud 첫 동의 화면 통과하기
2. Google Cloud 프로젝트 만들기
3. Google 인증 플랫폼 시작하기
4. 앱 정보 입력하기
5. 대상 설정하기
6. 연락처 정보 입력하기
7. OAuth 클라이언트 만들기
8. 앱 게시하기
9. PASSV 운영 값에 반영하기
10. 운영 로그인 화면에서 마지막 확인하기

## 1. Google Cloud 첫 동의 화면 통과하기

### 작업 순서

1. `https://console.cloud.google.com/`에 접속한다.
2. 국가와 약관 동의 항목을 선택한다.
3. `동의 및 계속하기`를 누른다.

### 설명

- 이 화면은 계정마다 처음 한 번만 보일 수 있다.
- 이 단계를 통과해야 프로젝트 생성과 Google 인증 플랫폼 메뉴로 이동할 수 있다.

### 캡처

![Google Cloud 첫 동의 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/11-google-cloud-terms-completed.png)

## 2. Google Cloud 프로젝트 만들기

### 작업 순서

1. 상단 프로젝트 선택 영역을 누른다.
2. `새 프로젝트`를 누른다.
3. 프로젝트 이름을 `PASSV Google Login Prod`로 입력한다.
4. `만들기`를 누른다.
5. 생성이 끝나면 방금 만든 프로젝트를 선택한다.

### 설명

- 프로젝트 ID는 자동으로 생성된다.
- 초보자는 Google 로그인 전용 프로젝트를 따로 만드는 편이 관리하기 쉽다.

### 캡처

![Google Cloud 프로젝트 이름 입력 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/14-google-cloud-project-name-filled.png)

![Google Cloud 프로젝트 생성 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/15-google-cloud-project-created.png)

## 3. Google 인증 플랫폼 시작하기

### 작업 순서

1. 왼쪽 메뉴에서 `Google 인증 플랫폼`으로 이동한다.
2. `시작하기`를 누른다.

### 설명

- 여기서부터 Google 로그인용 기본 설정 마법사가 시작된다.
- 이후 순서는 `앱 정보 -> 대상 -> 연락처 정보 -> 완료` 순서다.

### 캡처

![Google 인증 플랫폼 개요 화면](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/17-google-auth-platform-overview-loaded.png)

![Google 인증 플랫폼 시작하기 버튼 화면](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/18-google-auth-get-started.png)

## 4. 앱 정보 입력하기

### 작업 순서

1. `앱 이름`에 `PASSV`를 입력한다.
2. `사용자 지원 이메일`에는 운영용 Google 계정을 선택한다.
3. `다음`을 누른다.

### 설명

- 앱 이름은 사용자가 Google 로그인 화면에서 보게 되는 서비스 이름이다.
- 지원 이메일은 운영자가 관리할 수 있는 계정을 사용하면 된다.

### 캡처

![앱 정보 입력 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/20-google-auth-app-info-complete.png)

## 5. 대상 설정하기

### 작업 순서

1. `대상` 화면에서 `외부`를 선택한다.
2. `다음`을 누른다.

### 설명

- PASSV는 일반 사용자가 사용하는 서비스이므로 `외부`가 맞다.
- 내부 전용 서비스가 아니면 `내부`를 선택하지 않는다.

### 캡처

![대상 외부 선택 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/23-google-auth-audience-external-complete.png)

## 6. 연락처 정보 입력하기

### 작업 순서

1. `이메일 주소`에 운영용 Google 계정을 입력한다.
2. 사용자 데이터 정책 동의 체크를 선택한다.
3. `만들기`를 누른다.

### 설명

- 이 이메일은 Google이 프로젝트 변경사항을 알릴 때 사용하는 주소다.
- 실제 문서용 캡처에서는 이메일 값을 마스킹했다.

### 캡처

![연락처 정보 입력 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/24-google-auth-contact-info-complete.png)

## 7. OAuth 클라이언트 만들기

### 작업 순서

1. 왼쪽 메뉴 `클라이언트`로 이동한다.
2. `OAuth 클라이언트 만들기`를 누른다.
3. `애플리케이션 유형`은 `웹 애플리케이션`을 선택한다.
4. 이름은 `passv-in-prod-web`로 입력한다.
5. `승인된 JavaScript 원본`에는 아래 값을 넣는다.

```text
https://in.passv.co.kr
```

6. `승인된 리디렉션 URI`에는 아래 값을 넣는다.

```text
https://in.passv.co.kr/api/auth/google/redirect
```

7. `만들기`를 누른다.
8. 생성 완료 팝업에서 `Client ID`를 확인한다.

### 설명

- 이 단계가 가장 중요하다.
- PASSV 운영 기준으로 원본 주소와 리디렉션 주소는 위 값 그대로 사용하면 된다.
- 생성 완료 팝업의 `Client ID`는 문서용 캡처에서 마스킹했다.

### 캡처

![OAuth 클라이언트 입력 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/25-google-auth-oauth-client-form-complete.png)

![OAuth 클라이언트 생성 완료 팝업](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/26-google-auth-client-created-popup.png)

## 8. 앱 게시하기

### 작업 순서

1. 왼쪽 메뉴 `대상`으로 다시 이동한다.
2. `앱 게시`를 누른다.
3. 확인 팝업에서 `확인`을 누른다.
4. 화면에 `프로덕션 단계`가 표시되는지 확인한다.

### 설명

- 운영 서비스 기준 문서이므로 마지막 상태는 `프로덕션 단계`다.
- 테스트만 할 때는 게시하지 않고 테스트 상태로 둘 수도 있지만, `in.passv.co.kr` 운영 기준 문서에서는 프로덕션 전환까지 포함한다.

### 캡처

![앱 게시 확인 팝업](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/27-google-auth-publish-confirmation.png)

![프로덕션 단계 전환 완료](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/28-google-auth-audience-production.png)

## 9. PASSV 운영 값에 반영하기

### 이 단계에서 기억할 규칙

Google Console에서 가져온 `Client ID` 1개를 아래 두 위치에 같은 값으로 넣으면 된다.

| 위치 | 변수명 | 넣는 값 |
| --- | --- | --- |
| 프론트 운영 변수 | `PASSV_PROD_GOOGLE_CLIENT_ID` | Google Console에서 복사한 `Client ID` |
| 백엔드 운영 변수 | `GOOGLE_CLIENT_ID` | 같은 `Client ID` |

### 작업 순서

1. Google Console에서 복사한 `Client ID`를 준비한다.
2. PASSV 운영 프론트 변수에 `PASSV_PROD_GOOGLE_CLIENT_ID`로 등록한다.
3. PASSV 운영 백엔드 런타임 변수에 `GOOGLE_CLIENT_ID`로 등록한다.
4. 운영 배포를 다시 진행한다.

### PASSV 코드 기준으로 보면

| 구분 | 파일 | 의미 |
| --- | --- | --- |
| 프론트 예시 변수 | `client/mobile/.env.example` | `VITE_GOOGLE_CLIENT_ID` 자리 |
| 백엔드 예시 변수 | `server/.env.example` | `GOOGLE_CLIENT_ID` 자리 |
| 운영 배포 참조 | `.github/workflows/deploy.yml` | `PASSV_PROD_GOOGLE_CLIENT_ID`를 읽어 `GOOGLE_CLIENT_ID`로 전달 |

### 설명

- 운영 프론트는 GitHub Actions 변수 `PASSV_PROD_GOOGLE_CLIENT_ID`를 사용한다.
- 운영 백엔드는 같은 값을 `GOOGLE_CLIENT_ID`로 사용한다.
- `VITE_GOOGLE_REDIRECT_URI`는 현재 구현상 필수가 아니다. 기본값으로 `https://in.passv.co.kr/api/auth/google/redirect`를 사용한다.
- 이번 구현에서는 `Client Secret`을 넣지 않는다.

### 캡처

![프론트 운영 변수 반영 예시](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/30-passv-client-env-google-client-id.png)

![백엔드 운영 변수 반영 예시](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/31-passv-server-env-google-client-id.png)

![운영 배포 변수 전달 예시](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/32-passv-deploy-workflow-google-client-id.png)

## 10. 운영 로그인 화면에서 마지막 확인하기

### 작업 순서

1. `https://in.passv.co.kr/login`으로 이동한다.
2. `구글로 시작하기` 버튼이 보이는지 확인한다.
3. 버튼을 눌렀을 때 Google 로그인 흐름이 시작되는지 확인한다.

### 설명

- 운영 화면에서 버튼이 보이면 프론트 설정은 정상 반영된 것이다.
- 이후 실제 로그인 성공 여부는 운영 배포와 백엔드 설정까지 반영된 뒤 확인하면 된다.

### 캡처

![운영 로그인 화면 구글 버튼](https://in.passv.co.kr/manual/google-login-in-passv-co-kr/33-passv-login-google-button.png)

## 초보 운영개발자용 최종 체크리스트

1. Google Cloud 프로젝트를 만들었다.
2. Google 인증 플랫폼에서 `PASSV` 앱 정보를 입력했다.
3. 대상은 `외부`로 설정했다.
4. 연락처 정보와 정책 동의를 완료했다.
5. `웹 애플리케이션` OAuth 클라이언트를 만들었다.
6. `https://in.passv.co.kr`를 JavaScript 원본으로 등록했다.
7. `https://in.passv.co.kr/api/auth/google/redirect`를 리디렉션 URI로 등록했다.
8. `Client ID`를 복사했다.
9. `PASSV_PROD_GOOGLE_CLIENT_ID`에 같은 값을 넣었다.
10. 백엔드 `GOOGLE_CLIENT_ID`에도 같은 값을 넣었다.
11. 운영 로그인 화면에서 `구글로 시작하기` 버튼을 확인했다.
