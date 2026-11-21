---
layout: default
title: Manual 기여
parent: 연구실 운영
nav_order: 2
permalink: /operations/manual-management/
has_children: true
---

# Manual 기여

## Github 저장소

- [lab-handbook-mkdocs](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs)

Handbook은 이 저장소의 `docs/` 폴더에 있는 Markdown 파일로 만들어집니다. `main` 브랜치에 변경이 반영되면 GitHub Actions가 사이트를 자동으로 빌드하고 배포합니다.

## 수정 방법 고르기

| 상황 | 방법 | 준비물 |
| --- | --- | --- |
| 오타, 문장, 링크 몇 개 수정 | [웹에서 수정하기](manual/web-edit.md) | GitHub 계정 |
| 새 페이지 추가, 이미지 여러 장, 메뉴(nav) 변경, 여러 파일 수정 | [로컬에서 빌드하기](manual/local-build.md) | GitHub 계정, Git, Python, VS Code |

어느 방법이든 [작성 규칙](manual/writing-guide.md)을 따르고, 배포가 실패하면 [문제 해결](manual/troubleshooting.md)을 확인하세요.

## 문서 기여자 표시

연구실 메뉴얼 작성에 기여해 보세요!  
본인계정으로 수정하고, 로컬에서 작업할 때는 커밋 이름과 이메일을 본인 정보로 설정하세요.

기여자와 기여 비율은 Git 을 기반으로 자동 생성됩니다 (기여자가 한 명뿐인 문서에는 이름만 표시됩니다).

![문서 하단의 기여자와 기여 비율 표시 예시]({{ '/assets/images/manual/contributors-example.png' | relative_url }})

- 기여 비율은 문서의 줄 단위 변경 기록에 기반한 값입니다.
- 커밋 전의 로컬 변경은 `Not Committed Yet`으로 표시될 수 있습니다. 변경을 커밋한 뒤 다시 빌드합니다.
- 같은 사람이 여러 이름이나 이메일로 표시되면 관리자와 확인하여 `.mailmap`에서 통합할 수 있습니다.
