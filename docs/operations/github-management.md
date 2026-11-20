---
layout: default
title: 연구실 GitHub 관리
parent: 연구실 운영
nav_order: 1.5
permalink: /operations/github-management/
---

# 연구실 GitHub 관리

연구실 GitHub 저장소와 홈페이지·Handbook의 수정 및 배포 방법을 안내합니다.

## 저장소 바로가기

[연구실 GitHub 조직](https://github.com/JBUH-skin-microbiome)에서 저장소를 확인할 수 있습니다.

| 저장소 | 용도 | 수정할 브랜치 |
| --- | --- | --- |
| [JBUH-skin-microbiome.github.io](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io) | 연구실 홈페이지 | `master` |
| [lab-handbook-mkdocs](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs) | 현재 사용하는 MkDocs Handbook | `main` |
| [lab-handbook](https://github.com/JBUH-skin-microbiome/lab-handbook) | 이전 Just the Docs Handbook 보관 | 새 문서는 MkDocs 저장소에서 수정 |

## Handbook 문서 수정

1. 본인 GitHub 계정으로 로그인합니다.
2. 수정할 Handbook 페이지 상단의 연필 아이콘을 누릅니다.
3. `lab-handbook-mkdocs` 저장소의 `docs/` 아래 Markdown 파일을 수정합니다.
4. 변경 내용을 확인하고, 무엇을 수정했는지 커밋 메시지에 적습니다.
5. 검토가 필요한 변경은 새 브랜치에서 커밋하고 Pull Request를 만듭니다. 쓰기 권한이 없다면 저장소 관리자에게 권한을 요청합니다.
6. 변경이 `main`에 반영되면 [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포 결과를 확인합니다.
7. [실제 Handbook](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/)에서 내용과 링크를 확인합니다.

새 문서를 추가할 때는 `docs/`의 해당 분류에 Markdown 파일을 만들고, `mkdocs.yml`의 `nav`에도 경로를 추가합니다. 본문 목차는 제목에서 자동 생성되므로 별도의 수동 목차는 넣지 않습니다.

## 홈페이지 수정

- [홈페이지 저장소](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io)의 `master` 브랜치에 변경을 반영합니다.
- 홈페이지에서 연결하는 Handbook 링크는 현재 MkDocs 사이트 주소를 사용합니다.
- 연구실 지원자 안내는 [연구실 지원자 페이지](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/onboarding/applicants/)로 연결합니다.
- 변경 후 Actions의 배포 결과와 [실제 홈페이지](https://jbuh-skin-microbiome.github.io/)를 확인합니다.

홈페이지 콘텐츠 관리 업무는 [홈페이지 관리](homepage.md)를 참고하세요.

## 문서 기여자 표시

Handbook 하단의 기여자와 기여 비율은 Git 기록을 바탕으로 자동 생성됩니다. 본인 계정으로 수정하고, 로컬에서 작업할 때는 커밋 이름과 이메일을 본인 정보로 설정하세요.

- 기여 비율은 문서의 줄 단위 변경 기록에 기반한 값이며, 연구 성과나 작업 시간의 비율을 뜻하지 않습니다.
- 커밋 전의 로컬 변경은 `Not Committed Yet`으로 표시될 수 있습니다. 변경을 커밋한 뒤 다시 빌드합니다.
- 같은 사람이 여러 이름이나 이메일로 표시되면 관리자와 확인하여 `.mailmap`에서 통합할 수 있습니다.

## 계정과 저장소 관리

- 공개 저장소에는 비밀번호, 토큰, 접속 키, 개인정보 및 환자 자료를 올리지 않습니다.
- 구성원에게는 업무에 필요한 저장소 권한을 부여하고, 합류·이동·퇴실 시 권한을 확인합니다.
- 저장소 설명에는 용도와 관련 사이트 주소를 적습니다.
- 파일 삭제나 대규모 구조 변경은 Pull Request로 변경 범위를 확인한 뒤 반영하는 것을 권장합니다.
- 배포가 실패하면 해당 Actions 실행의 오류 로그를 확인하고, 수정 후 실제 사이트까지 다시 확인합니다.

Git 기본 사용법은 [Git 과 Github](github.md)를 참고하세요.
