---
title: "02. Git, 브랜치, 커밋, PR"
---
# 02. Git, 브랜치, 커밋, PR

코드·문서 변경의 협업 규칙이다. 데이터센스의 모든 저장소(platform, wiki, cro 등)는 **트렁크 기반 개발**로 일한다. 장수 브랜치를 두지 않고, 짧게 사는 브랜치에서 작은 PR을 자주 `main`에 합치며, `main`은 언제나 배포 가능한 상태로 둔다. `main` 머지가 곧 운영 반영(GitOps·위키)이므로 이 규칙은 곧 배포 규칙이기도 하다([03. GitOps와 배포](../03. GitOps와 배포/index.md)).

## 트렁크 기반 개발이란

트렁크(`main`) 하나만 오래 살고, 나머지 브랜치는 하루 이틀 안에 합쳐지고 사라지는 방식이다. 개발 브랜치·릴리즈 브랜치를 오래 유지하면 합칠 때 충돌과 회귀가 몰려오는데, 그 비용을 없애려고 변경을 작게 쪼개 계속 트렁크에 넣는다. 미완성 기능은 브랜치에 숨기지 않고 기능 플래그로 꺼 둔 채 트렁크에 넣는다(아래 "미완성 기능을 main에 넣는 법"). 배포 성과 연구(DORA)에서 트렁크 기반 개발은 배포 빈도와 안정성을 함께 높이는 핵심 관행으로 꼽힌다.

- 트렁크 기반 개발 개요와 패턴: https://trunkbaseddevelopment.com/
- DORA 역량 설명(왜 성과와 연결되는지): https://dora.dev/capabilities/trunk-based-development/
- Atlassian 입문 글: https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- GitHub flow(브랜치 → PR → 머지의 기본 흐름): https://docs.github.com/en/get-started/using-github/github-flow

## 브랜치

- 형식: **`<깃 닉네임 축약>/<이슈 번호>`**. 닉네임 축약은 깃 닉네임에서 뒤 숫자·접미사를 뗀 것이다. 예) `say828` → `say`, 이슈 142 → **`say/142`**.
- 이슈 번호가 없는 작업은 만들지 않는다. 먼저 이슈를 만들고 마일스톤에 붙인 뒤 브랜치를 판다.
- 브랜치는 **하루 이틀 안에** 머지한다. 사흘을 넘기면 작업을 더 쪼개 먼저 합칠 수 있는 부분부터 PR로 낸다.
- 브랜치는 항상 최신 `main`에서 시작하고, PR을 열기 전에 `main`을 rebase해 충돌을 브랜치 쪽에서 푼다. `main`에 머지 커밋을 되돌려 넣는 식으로 충돌을 해결하지 않는다.
- 머지된 브랜치는 지운다(`gh pr merge --delete-branch`). 저장소 설정은 자동 삭제가 꺼져 있으므로 사람이 지운다.
- 릴리즈 브랜치·개발 브랜치를 따로 두지 않는다. 운영 반영 시점을 조절해야 하면 브랜치가 아니라 기능 플래그나 태그로 한다(아래 참고).

```bash
git switch -c say/142 origin/main
# 작업, 커밋
git fetch origin && git rebase origin/main
git push -u origin say/142
gh pr create --fill
```

- rebase 사용법: https://git-scm.com/docs/git-rebase
- 짧은 브랜치와 작은 배치가 왜 중요한지(small batches): https://dora.dev/capabilities/working-in-small-batches/

## 커밋 메시지

- **Conventional Commits 타입 접두**를 쓴다: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, `ci:`.
- 형식: `type: 요약` (필요하면 `type(scope): 요약`). 요약은 한글로 명확하게, 무엇을 왜 바꿨는지가 드러나게 쓴다.
- 예) `feat: 발화 실패 Alerta 알림 추가`, `fix: KMC 요청번호 포맷 수정`, `docs: 관측·SRE 섹션 정리`, `chore(gitops): cro-api sha-5ab3ac8 핀`.
- 한 커밋은 하나의 논리적 변경이다. "WIP"·"수정" 같은 커밋은 PR을 열기 전에 정리한다(`git rebase -i`).

- Conventional Commits 규격(한국어): https://www.conventionalcommits.org/ko/v1.0.0/
- 좋은 커밋 메시지 쓰기: https://cbea.ms/git-commit/

## PR

- **PR 단위로 작업한다.** 한 PR은 하나의 목적만 담아 작고 명확하게 유지한다. 리뷰어가 15분 안에 읽을 수 있는 크기가 기준이다.
- PR 본문에는 무엇을, 왜, 어떻게 확인했는지를 적고, 마지막에 `Closes #<이슈 번호>`를 넣어 머지와 함께 이슈가 닫히게 한다.
- **리뷰는 에이전트에게 위임한다.** PR 단위로 에이전트 특화 리뷰(코드 리뷰 에이전트)를 돌려 검토한다. 사람은 리뷰 결과와 설계 판단만 본다.
- 머지 전에 저장소의 게이트(빌드, 타입 검사, `image-pin-gate` 같은 정합성 검사, 문서라면 링크 점검·dry-run)를 통과시킨다. `main` 머지는 곧 운영 반영이다.
- 머지 방식은 **merge commit**을 기본으로 한다(`gh pr merge --merge`). 브랜치의 커밋 이력이 그대로 남아 어떤 PR로 무엇이 들어갔는지 추적하기 쉽다. 정리되지 않은 커밋이 많은 브랜치는 squash로 합쳐도 되지만, 그 경우 PR 제목이 곧 커밋 메시지이므로 Conventional Commits 형식으로 쓴다.
- 이슈 번호가 있어야 PR을 연다. 이슈 없는 PR은 리뷰하지 않는다.

- 머지 방식 세 가지의 차이: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
- `Closes #n` 키워드로 이슈 연결: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
- 코드 리뷰를 작게 유지하는 이유(Google 엔지니어링 관행): https://google.github.io/eng-practices/review/developer/small-cls.html

## main 보호

`main`에는 직접 푸시하지 않는다. 브랜치 → PR → 게이트 통과 → 머지만 허용한다.

⚠️ 지금 조직 저장소는 비공개 저장소라 GitHub의 브랜치 보호 규칙을 켤 수 없다(무료 요금제에서는 공개 저장소에만 적용된다). 그래서 `main` 보호는 GitHub가 막아 주는 것이 아니라 **관행과 도구가 지킨다**. PR 게이트(GitHub Actions), 에이전트 훅(예: platform의 `.claude/hooks/image_pin_guard.sh`), 그리고 "직접 푸시하지 않는다"는 약속이 그것이다. 요금제를 올리거나 저장소를 공개로 바꾸면 브랜치 보호 규칙(직접 푸시 금지, 필수 체크, 리뷰 승인)을 켠다. TODO(확정 필요): 요금제 결정.

- 브랜치 보호 규칙: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- 저장소 규칙(rulesets, 보호 규칙의 후속): https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets

## 미완성 기능을 main에 넣는 법

트렁크 기반에서는 기능이 끝날 때까지 브랜치를 붙들고 있지 않는다. 대신 기능을 끈 채로 `main`에 넣는다.

- **기능 플래그**: 환경변수·설정값으로 기능을 켜고 끈다. 예) 시크릿이 없으면 대체 모드로 뜨는 API(cro의 설계 도우미는 모델 키가 없으면 규칙 기반으로 동작한다), 라우트는 있지만 메뉴에 노출하지 않는 화면.
- **추상화로 갈아타기(branch by abstraction)**: 큰 교체는 새 구현을 옛 구현 옆에 두고 스위치로 바꾼 뒤 옛 것을 지운다.
- 플래그는 기능이 자리 잡으면 지운다. 죽은 플래그가 쌓이면 코드가 읽히지 않는다.

- 기능 토글 종류와 수명: https://martinfowler.com/articles/feature-toggles.html
- Branch by Abstraction: https://martinfowler.com/bliki/BranchByAbstraction.html

## 배포와 릴리즈 연결

- gitops 매니페스트와 위키는 **`main` 머지 = 배포**다. 이미지는 `newTag`와 `digest`를 함께 핀한다([03. GitOps와 배포](../03. GitOps와 배포/index.md)).
- do4i 프런트·API처럼 배포 워크플로가 따로 있는 서비스는 릴리즈 태그(`admin-<버전>`, `api-<버전>`, `landing-<버전>`, `agents-<버전>`)나 `workflow_dispatch`로 배포를 트리거한다. 태그도 `main`의 커밋에만 붙인다.
- 버전은 유의적 버전(SemVer)으로 올린다. 사용자에게 보이는 변화가 있으면 minor, 고치기만 했으면 patch.
- 롤백은 두 가지뿐이다. 코드는 `git revert`로 되돌리는 PR을 내고, gitops는 이전 digest로 다시 핀한다. 서버에서 손으로 되돌리지 않는다.

- GitOps 원칙(OpenGitOps): https://opengitops.dev/
- 유의적 버전(한국어): https://semver.org/lang/ko/
- `git revert` 사용법: https://git-scm.com/docs/git-revert

## 핫픽스

핫픽스도 같은 길로 간다. `main`에서 브랜치를 파고, 고치고, PR을 열고, 게이트를 통과시켜 머지한 뒤 배포한다. 태그에서 브랜치를 따 따로 고치는 방식(핫픽스 브랜치)은 쓰지 않는다. 트렁크에 먼저 넣어야 다음 배포에서 같은 문제가 다시 나오지 않는다. 급해도 PR을 건너뛰지 않는다. 대신 PR을 아주 작게 만든다.

## 이슈 → 브랜치 → PR → SDD

SDD를 쓰는 저장소(platform, cro)에서는 PR이 코드만 바꾸지 않는다. 순서는 이렇다.

1. 이슈를 만들고 마일스톤에 붙인다. 이슈가 작업의 시작점이다.
2. `sdd/01_planning`의 해당 문서를 먼저 고치고, `sdd/02_plan`에 범위·가정·수용 기준·검증 방법을 적는다.
3. 브랜치에서 구현한다.
4. PR에 `sdd/03_build`(현재 상태)와 `sdd/03_verify`(실측)를 같이 넣고 `Closes #n`을 적는다.
5. 머지 뒤 배포가 일어나면 `sdd/05_operate`에 기록한다.

문서 없이 코드만 있는 PR, 코드 없이 계획만 있는 PR 모두 허용되지만, 하나의 이슈에는 결국 계획·구현·검증이 모두 남아야 이슈를 닫는다.

## 자주 하는 실수

- ⚠️ 이슈 없이 브랜치를 판다. 먼저 이슈부터 만든다.
- ⚠️ 브랜치를 일주일 넘게 끌고 간다. 쪼개서 먼저 합칠 수 있는 것부터 낸다.
- ⚠️ PR 하나에 기능 둘을 담는다. 리뷰도 롤백도 어려워진다.
- ⚠️ gitops에서 `newTag`만 바꾸고 `digest`를 두고 온다. digest가 이기므로 옛 이미지가 그대로 돈다.
- ⚠️ 급하다고 `main`에 직접 푸시한다. GitHub가 막아 주지 않으므로 사람이 지켜야 한다.

---

> **온보딩 트랙 4부. 운영 변경과 컨벤션**
> 이전: [문서 작성 규칙](../01. 문서 작성 규칙/index.md) · 다음: [GitOps와 배포](../03. GitOps와 배포/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../시작하기/index.md)
