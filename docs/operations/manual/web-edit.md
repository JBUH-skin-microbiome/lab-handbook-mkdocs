---
layout: default
title: 웹에서 수정하기
parent: Manual 기여
grand_parent: 연구실 운영
nav_order: 1
permalink: /operations/manual/web-edit/
---

# 웹에서 수정하기

설치 없이 GitHub 웹사이트에서 바로 고치는 방법입니다. 오타, 문장, 링크처럼 작은 수정에 적합합니다.

## 수정 순서

1. 본인 GitHub 계정으로 로그인합니다.
2. 수정할 Handbook 페이지 상단의 연필 아이콘(<img src="{{ '/assets/images/manual/edit-icon.png' | relative_url }}" alt="수정 아이콘" style="height: 1.4em; width: auto; vertical-align: middle;">)을 누릅니다.
3. GitHub 편집 화면에서 Markdown 파일을 수정합니다. **Preview** 탭에서 대략적인 모양을 확인할 수 있습니다.
4. **Commit changes**를 누르고, 무엇을 왜 바꿨는지 커밋 메시지에 적습니다. (예: `IRB 페이지에 갱신 주기 추가`)
5. 저장하는 방식을 고릅니다.
    - **Commit directly to the `main` branch**: 바로 반영됩니다. 쓰기 권한이 있을 때만 보입니다.
    - **Create a new branch and start a pull request**: 검토를 받은 뒤 반영합니다.
6. [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포가 성공(초록색 체크)했는지 확인합니다. 보통 1~2분 걸립니다.
7. [실제 Handbook](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/)에서 내용과 링크를 확인합니다.

## Pull Request로 반영하기

- 여러 페이지에 걸친 변경이나 내용 확인이 필요한 수정은 Pull Request(PR)로 올립니다.
- PR을 만들면 Actions가 **빌드 검사만** 하고 배포는 하지 않습니다. 깨진 링크나 문법 오류가 있으면 PR에 빨간 X가 표시됩니다.
- 관리자가 PR을 merge하면 그때 자동으로 배포됩니다.
- 쓰기 권한이 없으면 GitHub가 저장소를 본인 계정으로 fork한 뒤 PR을 만듭니다. 처음 기여하는 계정의 PR은 관리자가 **Approve and run**을 눌러야 검사가 시작될 수 있습니다.

## 웹 수정이 불편한 경우

다음 작업은 [로컬에서 빌드하기](local-build.md)가 더 편합니다.

- 새 페이지를 만들고 메뉴(`mkdocs.yml`의 `nav`)에 추가할 때
- 이미지를 여러 장 올릴 때
- 여러 파일을 한 번에 고칠 때
- 배포 전에 실제 모양을 미리 보고 싶을 때
