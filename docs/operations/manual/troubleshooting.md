---
layout: default
title: 문제 해결
parent: Manual 기여
grand_parent: 연구실 운영
nav_order: 4
permalink: /operations/manual/troubleshooting/
---

# 문제 해결

## 배포가 실패했을 때

[Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 빨간 X가 붙은 실행을 열고, `build` → `Run mkdocs build --strict` 단계의 로그를 확인합니다. 배포가 실패하면 사이트는 마지막으로 성공한 버전에 머물러 있습니다. 그 뒤의 수정은 실패 원인을 고칠 때까지 반영되지 않습니다.

| 로그 메시지 | 원인 | 해결 |
| --- | --- | --- |
| `Unconverted Liquid in ...` | 이미지·링크의 중괄호 형식이 깨짐 (따옴표, `}}` 누락 등) | 해당 파일에서 [작성 규칙](writing-guide.md)의 이미지 형식과 비교해 고칩니다 |
| `... contains a link to '...', but the target is not found` | 링크한 파일 경로가 틀림 | 파일 이름과 상대 경로를 확인합니다 |
| `A reference to '...' is included in the 'nav' configuration, which is not found` | `mkdocs.yml`의 `nav`에 적은 파일이 없음 | 경로 오타나 옮긴 파일을 확인합니다 |
| `Aborted with N warnings in strict mode!` | 위의 경고가 하나 이상 있음 | 로그 위쪽의 `WARNING` 줄을 하나씩 고칩니다 |
| YAML 관련 오류 | `mkdocs.yml`이나 front matter의 들여쓰기·콜론 오류 | 들여쓰기를 공백 2칸으로 맞춥니다 |

!!! example "실제 사례"
    홈 화면에 체크리스트 링크를 추가하면서 따옴표와 닫는 중괄호가 빠져 `Unconverted Liquid` 오류가 났고, 이후 수정 세 번이 모두 배포되지 않았습니다. 한 줄을 고치자 쌓여 있던 변경이 한 번에 반영되었습니다.

## push가 거부될 때

`rejected ... (non-fast-forward)`는 다른 사람이 먼저 push한 내용이 있다는 뜻입니다. 받아서 내 커밋을 그 위에 올린 뒤 다시 push합니다.

```bash
git pull --rebase
git push
```

같은 줄을 둘이 고쳐 충돌이 나면 Git이 파일에 `<<<<<<<`, `=======`, `>>>>>>>` 표시를 남깁니다. 남길 내용만 정리하고 표시를 지운 뒤 다음을 실행합니다.

```bash
git add 충돌난-파일.md
git rebase --continue
git push
```

## 로컬 환경 문제

### `python`을 입력해도 아무 일이 없거나 Store가 열림 (Windows)

Python이 설치되지 않아 Microsoft Store 바로가기가 실행되는 것입니다. python.org에서 Python을 설치하고 **Add python.exe to PATH**를 체크합니다.

### `mkdocs`를 찾을 수 없음

가상환경이 활성화되지 않은 상태입니다. 저장소 폴더에서 `.venv\Scripts\Activate.ps1`(Windows) 또는 `source .venv/bin/activate`(macOS/Linux)를 실행합니다.

### `detected dubious ownership in repository`

저장소 폴더를 다른 Windows 사용자 계정이 만든 경우입니다. 오류 메시지에 나온 명령으로 이 폴더를 신뢰 목록에 추가합니다.

```bash
git config --global --add safe.directory C:/경로/lab-handbook-mkdocs
```

### `Author identity unknown`

커밋 작성자가 설정되지 않았습니다. [로컬에서 빌드하기](local-build.md)의 "커밋 작성자 설정"을 먼저 합니다.

## 기여자 표시가 이상할 때

- **내 이름이 두 번 나옴**: 커밋마다 이메일이 달라서입니다. 관리자에게 요청해 `.mailmap`으로 합칩니다.
- **비율(%)이 안 보임**: 기여자가 한 명뿐인 문서는 이름만 표시됩니다.
- **`Not Committed Yet`이 보임**: 로컬 미리보기에서 커밋 전 변경이 있을 때 나타납니다. 커밋하면 사라집니다.
