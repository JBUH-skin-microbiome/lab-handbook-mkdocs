---
layout: default
title: 연구실 GitHub 사용하기
parent: 연구실 GitHub 관리
grand_parent: 연구실 운영
nav_order: 2
permalink: /operations/github-usage/
---

# 연구실 GitHub 사용하기

연구실 GitHub 저장소의 용도와 홈페이지 수정, 계정·권한 관리 방법을 안내합니다.

## 저장소 바로가기

[연구실 GitHub 조직](https://github.com/JBUH-skin-microbiome)에서 저장소를 확인할 수 있습니다.

| 저장소 | 용도 | 수정할 브랜치 |
| --- | --- | --- |
| [JBUH-skin-microbiome.github.io](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io) | 연구실 홈페이지 | `master` |
| [lab-handbook-mkdocs](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs) | 현재 사용하는 MkDocs Handbook | `main` |
| [lab-handbook](https://github.com/JBUH-skin-microbiome/lab-handbook) | 이전 Just the Docs Handbook 보관 | 새 문서는 MkDocs 저장소에서 수정 |
## 홈페이지 수정

- [홈페이지 저장소](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io)의 `master` 브랜치에 변경을 반영합니다.
- 홈페이지에서 연결하는 Handbook 링크는 현재 MkDocs 사이트 주소를 사용합니다.
- 연구실 지원자 안내는 [연구실 지원자 페이지](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/onboarding/applicants/)로 연결합니다.
- 변경 후 Actions의 배포 결과와 [실제 홈페이지](https://jbuh-skin-microbiome.github.io/)를 확인합니다.

홈페이지 콘텐츠 관리 업무는 [홈페이지 관리](homepage.md)를 참고하세요.
## 계정과 저장소 관리

- 공개 저장소에는 비밀번호, 토큰, 접속 키, 개인정보 및 환자 자료를 올리지 않습니다.
- 구성원에게는 업무에 필요한 저장소 권한을 부여하고, 합류·이동·퇴실 시 권한을 확인합니다.
- 저장소 설명에는 용도와 관련 사이트 주소를 적습니다.
- 파일 삭제나 대규모 구조 변경은 Pull Request로 변경 범위를 확인한 뒤 반영하는 것을 권장합니다.
- 배포가 실패하면 해당 Actions 실행의 오류 로그를 확인하고, 수정 후 실제 사이트까지 다시 확인합니다.

Git 기본 사용법은 [Git 과 Github](github.md)를 참고하세요.
