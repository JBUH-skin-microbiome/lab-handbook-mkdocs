---
layout: default
title: 로컬에서 빌드하기
parent: Manual 기여
grand_parent: 연구실 운영
nav_order: 2
permalink: /operations/manual/local-build/
---

# 로컬에서 빌드하기

내 PC에서 Handbook을 띄워 미리 보고, 오류가 없는지 확인한 뒤 push하는 방법입니다. 명령어는 배포에 쓰는 GitHub Actions(`.github/workflows/pages.yml`)와 같게 맞췄습니다.

## 준비물

| 도구 | 용도 | 비고 |
| --- | --- | --- |
| [Git](https://git-scm.com/downloads) | 저장소 받기, 커밋, push | Windows는 Git for Windows 설치 |
| [Python 3.12](https://www.python.org/downloads/) | MkDocs 실행 | 배포 서버와 같은 버전 |
| [VS Code](https://code.visualstudio.com/) | Markdown 편집 | 다른 텍스트 편집기도 가능 |

!!! warning "Windows에서 Python 설치"
    python.org 설치 프로그램을 쓰고, 첫 화면에서 **Add python.exe to PATH**를 체크합니다. 설치 없이 `python`을 입력하면 Microsoft Store 바로가기가 실행되어 아무 일도 일어나지 않을 수 있습니다. `python --version`으로 버전이 나오는지 확인하세요.

Git 기본 개념은 [Git and GitHub](../github.md)를 참고하세요.

## 처음 한 번만 하는 설정

### 1. 커밋 작성자 설정

기여자 표시는 커밋의 이름과 이메일로 만들어집니다. GitHub 계정에 등록된 이메일을 사용하세요.

```bash
git config --global user.name "홍길동"
git config --global user.email "github-email@example.com"
```

### 2. 저장소 받기

```bash
git clone https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs.git
cd lab-handbook-mkdocs
```

!!! note
    수정일과 기여자 표시는 전체 커밋 기록을 읽습니다. `--depth` 옵션 없이 전체를 clone하세요.

### 3. 가상환경 만들고 패키지 설치

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

`.venv` 폴더는 `.gitignore`에 들어 있어 커밋되지 않습니다. 다음부터는 가상환경 활성화(두 번째 줄)만 하면 됩니다.

## 작업 순서

### 1. 최신 내용 받기

다른 사람이 웹에서 고친 내용이 있을 수 있으니 작업 전에 항상 먼저 받습니다.

```bash
git pull --rebase
```

### 2. 미리보기 띄우기

```bash
mkdocs serve
```

브라우저에서 <http://127.0.0.1:8000/lab-handbook-mkdocs/>를 엽니다. 파일을 저장하면 페이지가 자동으로 새로고침됩니다. 끝낼 때는 터미널에서 `Ctrl+C`를 누릅니다.

### 3. 수정하기

- 페이지는 `docs/` 아래 Markdown 파일입니다.
- 새 페이지를 만들면 `mkdocs.yml`의 `nav`에도 추가해야 메뉴에 보입니다.
- 형식은 [작성 규칙](writing-guide.md)을 따릅니다.

### 4. 배포와 같은 조건으로 검사하기

```bash
mkdocs build --strict
```

`--strict`는 경고를 오류로 취급합니다. 배포 서버도 이 옵션으로 빌드하므로, 여기서 오류가 나면 push해도 배포가 실패합니다. 오류 메시지는 [문제 해결](troubleshooting.md)을 참고하세요.

!!! tip
    새로 만든 파일에 `has no git logs` 경고가 보이는 것은 아직 커밋 전이라 그렇습니다. 이 경고 때문에 `--strict`가 멈춘다면, 먼저 커밋한 뒤 다시 검사하세요. 다른 경고는 모두 고친 뒤에 push합니다.

### 5. 커밋하고 push하기

```bash
git status
git add docs/바꾼-파일.md mkdocs.yml
git commit -m "무엇을 왜 바꿨는지"
git push
```

push 후 [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포 성공을 확인하고, 실제 사이트에서 결과를 봅니다.

검토가 필요한 변경은 `main`에 바로 push하지 말고 브랜치를 만들어 PR로 올립니다.

```bash
git switch -c 브랜치-이름
# 수정, 커밋
git push -u origin 브랜치-이름
```

push 후 GitHub 저장소 페이지에 나타나는 **Compare & pull request** 버튼으로 PR을 만듭니다.
