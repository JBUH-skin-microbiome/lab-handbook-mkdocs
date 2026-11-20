---
layout: default
title: Manual 페이지 관리
parent: 연구실 GitHub 관리
grand_parent: 연구실 운영
nav_order: 1
permalink: /operations/manual-management/
---

# Manual 페이지 관리

연구실 Manual(Handbook)의 문서 수정, 메뉴 추가 및 기여자 표시를 관리합니다.

## Handbook 문서 수정

1. 본인 GitHub 계정으로 로그인합니다.
2. 수정할 Handbook 페이지 상단의 연필 아이콘을 누릅니다.
3. `lab-handbook-mkdocs` 저장소의 `docs/` 아래 Markdown 파일을 수정합니다.
4. 변경 내용을 확인하고, 무엇을 수정했는지 커밋 메시지에 적습니다.
5. 검토가 필요한 변경은 새 브랜치에서 커밋하고 Pull Request를 만듭니다. 쓰기 권한이 없다면 저장소 관리자에게 권한을 요청합니다.
6. 변경이 `main`에 반영되면 [Actions](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs/actions)에서 배포 결과를 확인합니다.
7. [실제 Handbook](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/)에서 내용과 링크를 확인합니다.

새 문서를 추가할 때는 `docs/`의 해당 분류에 Markdown 파일을 만들고, `mkdocs.yml`의 `nav`에도 경로를 추가합니다. 본문 목차는 제목에서 자동 생성되므로 별도의 수동 목차는 넣지 않습니다.
## 문서 기여자 표시

Handbook 하단의 기여자와 기여 비율은 Git 기록을 바탕으로 자동 생성됩니다. 본인 계정으로 수정하고, 로컬에서 작업할 때는 커밋 이름과 이메일을 본인 정보로 설정하세요.

- 기여 비율은 문서의 줄 단위 변경 기록에 기반한 값이며, 연구 성과나 작업 시간의 비율을 뜻하지 않습니다.
- 커밋 전의 로컬 변경은 `Not Committed Yet`으로 표시될 수 있습니다. 변경을 커밋한 뒤 다시 빌드합니다.
- 같은 사람이 여러 이름이나 이메일로 표시되면 관리자와 확인하여 `.mailmap`에서 통합할 수 있습니다.
