---
layout: default
title: Manual 기여
parent: 연구실 운영
nav_order: 2
permalink: /operations/manual-management/
---

# Manual 기여

## Github 저장소

- [lab-handbook-mkdocs](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs)

이 저장소의 `docs/` 폴더에 있는 Markdown 파일이 Handbook 페이지가 됩니다. `main` 브랜치에 변경이 들어가면 GitHub Actions가 사이트를 자동으로 빌드해 배포합니다.

| 상황 | 방법 | 준비물 |
| --- | --- | --- |
| 오타, 문장, 링크 몇 개 수정 | 웹에서 수정하기 | GitHub 계정 |
| 새 페이지 추가, 이미지 여러 장, 메뉴(nav) 변경, 여러 파일 수정 | 로컬에서 빌드하기 (이 페이지 맨 아래) | GitHub 계정, Git, Python, VS Code |

## 문서 기여자 표시

연구실 메뉴얼 작성에 기여해 보세요!  
본인 계정으로 수정하고 로컬에서 작업할 때는 커밋 이름과 이메일을 본인 정보로 설정하세요.

기여자와 기여 비율은 Git 기록으로 자동 계산합니다. 기여자가 한 명뿐인 문서에는 이름만 나옵니다.

![문서 하단의 기여자와 기여 비율 표시 예시]({{ '/assets/images/manual/contributors-example.png' | relative_url }})

- 기여 비율은 줄 단위 변경 기록으로 계산합니다.
- 로컬 미리보기에서 커밋하지 않은 변경은 `Not Committed Yet`으로 보일 수 있습니다. 커밋한 뒤 다시 빌드하면 사라집니다.
- 같은 사람이 이름이나 이메일이 달라 두 번 나오면 관리자에게 요청해 `.mailmap`으로 합칩니다.

## 웹에서 수정하기

설치 없이 GitHub 웹사이트에서 바로 고치는 방법입니다.

1. 본인 GitHub 계정으로 로그인합니다.
2. 수정할 Handbook 페이지 상단의 연필 아이콘(<img src="{{ '/assets/images/manual/edit-icon.png' | relative_url }}" alt="수정 아이콘" style="height: 1.4em; width: auto; vertical-align: middle;">)을 누릅니다.
3. GitHub 편집 화면에서 Markdown 파일을 고칩니다. Preview 탭에서 대략적인 모양을 볼 수 있습니다.
4. Commit changes를 누르고 무엇을 왜 바꿨는지 커밋 메시지에 적습니다. (예: `IRB 페이지에 갱신 주기 추가`)
5. 저장 방식을 고릅니다.
    - Commit directly to the `main` branch: 바로 반영됩니다. 쓰기 권한이 있을 때만 보입니다.
    - Create a new branch and start a pull request: 검토를 받은 뒤 반영합니다.
6. [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포가 성공(초록색 체크)했는지 봅니다. 보통 1~2분 걸립니다.
7. [실제 Handbook](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/)에서 내용과 링크를 확인합니다.

### Pull Request로 반영하기

여러 페이지를 함께 고치거나 다른 사람이 내용을 봐야 하는 수정은 Pull Request(PR)로 올립니다. PR 단계에서 Actions는 빌드 검사만 하고 배포는 하지 않습니다. 깨진 링크나 문법 오류가 있으면 PR에 빨간 X가 붙습니다. 관리자가 PR을 merge하면 그때 자동으로 배포됩니다.

쓰기 권한이 없으면 GitHub가 저장소를 본인 계정으로 fork한 뒤 PR을 만듭니다. 처음 기여하는 계정의 PR은 관리자가 Approve and run을 눌러야 검사가 시작될 수 있습니다.

## 작성 규칙

### 저장소 구조

| 경로 | 내용 |
| --- | --- |
| `docs/` | 모든 페이지(Markdown)와 이미지 |
| `docs/assets/images/<분류>/` | 페이지에 넣는 이미지 |
| `mkdocs.yml` | 사이트 설정과 왼쪽 메뉴(`nav`) |
| `hooks/handbook.py` | 링크 변환, 제목 번호 매기기 등 이 사이트에만 있는 처리 |
| `overrides/` | 테마 화면 수정 |
| `.github/workflows/pages.yml` | 자동 빌드·배포 설정 |

문서만 고칠 때는 `docs/`와 `mkdocs.yml`만 건드리면 됩니다.

### 새 페이지 만들기

1. 해당 분류 폴더에 파일을 만듭니다. 이름은 영문 소문자와 하이픈으로 짓습니다. (예: `docs/operations/server.md`)
2. 파일 맨 위에 페이지 정보(front matter)를 적습니다.

    ```yaml
    ---
    layout: default
    title: 서버 관리
    parent: 연구실 운영
    nav_order: 3
    permalink: /operations/server/
    ---
    ```

    - `title`: 메뉴와 탭에 보이는 이름
    - `parent` / `grand_parent`: 상위 메뉴 이름
    - `permalink`: 페이지 주소. 주소를 바꾸면 기존 링크가 열리지 않으니 한 번 정하면 그대로 둡니다.
    - `has_children: true`: 하위 페이지가 있는 분류의 첫 페이지에 넣으면 본문 끝에 "관련 문서" 목록이 자동으로 붙습니다.

3. `mkdocs.yml`의 `nav`에서 알맞은 위치에 한 줄을 추가합니다. 들여쓰기는 공백 2칸입니다.

    ```yaml
    - 연구실 운영:
      - operations/index.md
      - 서버 관리: operations/server.md
    ```

### 본문 작성

- 페이지 제목(`#`)은 하나만 쓰고 본문은 `##`부터 시작합니다. 제목 번호와 오른쪽 목차는 자동으로 붙으니 직접 쓰지 않습니다.
- 누구나 볼 수 있는 사이트입니다. 개인정보, 환자 자료, 비밀번호, 토큰은 넣지 말고 구성원 전용 자료는 노션이나 구글 드라이브 링크로 연결합니다.

### 링크

다른 Handbook 페이지는 Markdown 파일의 상대 경로로 겁니다. 경로가 틀리면 빌드가 멈추니 깨진 링크를 배포 전에 잡을 수 있습니다. 외부 사이트는 전체 주소를 적습니다.

```markdown
[Git and GitHub](github.md)
[홈페이지 관리](homepage.md)
```

### 이미지

이미지는 `docs/assets/images/<분류>/`에 영문 파일 이름으로 넣고 기존 페이지와 같은 형식으로 연결합니다. 대괄호 안에는 이미지를 설명하는 문장을 적습니다.

<pre><code>![문서 하단의 기여자 표시 예시](&#123;&#123; '/assets/images/manual/contributors-example.png' | relative_url &#125;&#125;)</code></pre>

글자 크기만 한 아이콘은 HTML로 높이를 정합니다.

<pre><code>&lt;img src="&#123;&#123; '/assets/images/manual/edit-icon.png' | relative_url &#125;&#125;" alt="수정 아이콘" style="height: 1.4em; width: auto; vertical-align: middle;"&gt;</code></pre>

!!! warning
    중괄호 두 개와 `relative_url` 형식을 정확히 지켜야 합니다. 따옴표나 닫는 괄호가 하나라도 빠지면 빌드가 실패합니다. 그 줄을 고칠 때까지는 이후 수정도 사이트에 올라가지 않습니다.

### 알림 상자

```markdown
!!! note "참고"
    본문은 4칸 들여씁니다.
```

`note`, `tip`, `warning`, `danger` 등을 쓸 수 있습니다.

!!! note "참고"
    이렇게 보입니다.

### 탭

```markdown
=== "Windows"

    Windows 내용

=== "macOS"

    macOS 내용
```

### 체크리스트

```markdown
- [ ] 아직 안 한 항목
- [x] 끝난 항목
```

- [ ] 아직 안 한 항목
- [x] 끝난 항목

### 커밋 메시지

무엇을 바꿨는지 알 수 있게 씁니다. GitHub가 자동으로 채운 `Update index.md` 같은 메시지로는 나중에 기록을 찾기 어렵습니다.

- 좋은 예: `IRB 페이지에 갱신 주기 추가`, `안전교육 페이지 링크 수정`
- 피할 예: `Update index.md`, `수정`

## 로컬에서 빌드하기

내 PC에 Handbook을 띄워 미리 보고 오류가 없는지 확인한 뒤 push하는 방법입니다. 명령어는 배포에 쓰는 GitHub Actions(`.github/workflows/pages.yml`)와 같게 맞췄습니다. Git 기본 개념은 [Git and GitHub](github.md)를 참고하세요.

### 준비물

| 도구 | 용도 | 비고 |
| --- | --- | --- |
| [Git](https://git-scm.com/downloads) | 저장소 받기, 커밋, push | Windows는 Git for Windows 설치 |
| [Python 3.12](https://www.python.org/downloads/) | MkDocs 실행 | 배포 서버와 같은 버전 |
| [VS Code](https://code.visualstudio.com/) | Markdown 편집 | 다른 텍스트 편집기도 가능 |

!!! warning "Windows에서 Python 설치"
    python.org 설치 프로그램을 쓰고 첫 화면에서 Add python.exe to PATH를 체크합니다. Python 없이 `python`을 입력하면 Microsoft Store 바로가기가 실행될 뿐 아무 일도 일어나지 않습니다. `python --version`으로 버전이 나오는지 확인하세요.

### 처음 한 번만 하는 설정

#### 커밋 작성자 설정

기여자 표시에는 커밋의 이름과 이메일이 쓰입니다. GitHub 계정에 등록한 이메일을 넣으세요.

```bash
git config --global user.name "홍길동"
git config --global user.email "github-email@example.com"
```

#### 저장소 받기

```bash
git clone https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs.git
cd lab-handbook-mkdocs
```

!!! note
    수정일과 기여자는 전체 커밋 기록에서 읽어 옵니다. `--depth` 옵션 없이 전체를 clone하세요.

#### 가상환경 만들고 패키지 설치

=== "Windows (PowerShell)"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

`.venv` 폴더는 `.gitignore`에 들어 있어 커밋되지 않습니다. 다음부터는 두 번째 줄(가상환경 활성화)만 실행하면 됩니다.

### 작업 순서

#### 최신 내용 받기

다른 사람이 웹에서 고친 내용이 있을 수 있으니 작업 전에 먼저 받습니다.

```bash
git pull --rebase
```

#### 미리보기 띄우기

```bash
mkdocs serve
```

브라우저에서 <http://127.0.0.1:8000/lab-handbook-mkdocs/>를 엽니다. 파일을 저장할 때마다 페이지가 새로고침됩니다. 끝낼 때는 터미널에서 `Ctrl+C`를 누릅니다.

#### 수정하기

페이지는 `docs/` 아래 Markdown 파일입니다. 새 페이지를 만들었다면 `mkdocs.yml`의 `nav`에도 추가해야 메뉴에 나옵니다. 형식은 위의 작성 규칙을 따릅니다.

#### 배포와 같은 조건으로 검사하기

```bash
mkdocs build --strict
```

`--strict`는 경고를 오류로 다룹니다. 배포 서버도 이 옵션으로 빌드하니 여기서 오류가 나면 push해도 배포가 실패합니다.

!!! tip
    새로 만든 파일에 `has no git logs` 경고가 뜨는 건 아직 커밋하지 않아서입니다. 이 경고로 `--strict`가 멈추면 먼저 커밋하고 다시 검사하세요. 다른 경고는 모두 고친 뒤에 push합니다.

#### 커밋하고 push하기

```bash
git status
git add docs/바꾼-파일.md mkdocs.yml
git commit -m "무엇을 왜 바꿨는지"
git push
```

push한 뒤 [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포 성공을 확인하고 실제 사이트에서 결과를 봅니다. push가 거부되면 다른 사람이 먼저 올린 내용이 있다는 뜻입니다. `git pull --rebase`로 받은 뒤 다시 push합니다.

검토가 필요한 변경은 `main`에 바로 올리지 말고 브랜치를 만들어 PR로 올립니다.

```bash
git switch -c 브랜치-이름
# 수정, 커밋
git push -u origin 브랜치-이름
```

push하면 GitHub 저장소 페이지에 Compare & pull request 버튼이 나타납니다. 이 버튼으로 PR을 만듭니다.

[개인별 기여 보기 →](../other/contributions.md)
