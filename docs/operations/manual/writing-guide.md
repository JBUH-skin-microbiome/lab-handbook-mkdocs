---
layout: default
title: 작성 규칙
parent: Manual 기여
grand_parent: 연구실 운영
nav_order: 3
permalink: /operations/manual/writing-guide/
---

# 작성 규칙

## 저장소 구조

| 경로 | 내용 |
| --- | --- |
| `docs/` | 모든 페이지(Markdown)와 이미지 |
| `docs/assets/images/<분류>/` | 페이지에 넣는 이미지 |
| `mkdocs.yml` | 사이트 설정과 왼쪽 메뉴(`nav`) |
| `hooks/handbook.py` | 링크 변환, 제목 번호 매기기 등 사이트 전용 처리 |
| `overrides/` | 테마 화면 수정 |
| `.github/workflows/pages.yml` | 자동 빌드·배포 설정 |

일반적인 문서 수정은 `docs/`와 `mkdocs.yml`만 건드리면 됩니다.

## 새 페이지 만들기

### 1. 파일 만들기

해당 분류 폴더에 영문 소문자와 하이픈으로 파일 이름을 짓습니다. (예: `docs/operations/server.md`)

### 2. front matter 작성

파일 맨 위에 페이지 정보를 적습니다.

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
- `permalink`: 페이지 주소. 한 번 정하면 바꾸지 않는 것이 좋습니다. 주소를 바꾸면 기존 링크가 열리지 않습니다.
- `has_children: true`: 하위 페이지가 있는 분류의 첫 페이지에 넣으면 본문 끝에 "관련 문서" 목록이 자동으로 붙습니다.

### 3. 메뉴에 추가

`mkdocs.yml`의 `nav`에서 알맞은 위치에 한 줄을 추가합니다. 들여쓰기는 공백 2칸입니다.

```yaml
- 연구실 운영:
  - operations/index.md
  - 서버 관리: operations/server.md
```

## 본문 작성

- 페이지 제목(`#`)은 하나만 쓰고, 본문은 `##`부터 시작합니다. 제목 번호와 오른쪽 목차는 자동으로 붙으므로 직접 쓰지 않습니다.
- 공개 사이트이므로 개인정보, 환자 자료, 비밀번호, 토큰은 넣지 않습니다. 구성원 전용 자료는 노션이나 구글 드라이브 링크로 연결합니다.

### 링크

- 다른 Handbook 페이지: Markdown 파일의 상대 경로로 겁니다. 경로가 틀리면 빌드가 실패하므로 깨진 링크를 미리 잡을 수 있습니다.

```markdown
[작성 규칙](writing-guide.md)
[Git and GitHub](../github.md)
```

- 외부 사이트: 전체 주소를 적습니다.

### 이미지

이미지는 `docs/assets/images/<분류>/`에 영문 파일 이름으로 넣고, 기존 페이지들과 같은 형식으로 연결합니다. 대괄호 안에는 이미지를 설명하는 문장을 적습니다.

<pre><code>![문서 하단의 기여자 표시 예시](&#123;&#123; '/assets/images/manual/contributors-example.png' | relative_url &#125;&#125;)</code></pre>

글자 크기의 작은 아이콘은 HTML로 높이를 지정합니다.

<pre><code>&lt;img src="&#123;&#123; '/assets/images/manual/edit-icon.png' | relative_url &#125;&#125;" alt="수정 아이콘" style="height: 1.4em; width: auto; vertical-align: middle;"&gt;</code></pre>

!!! warning
    중괄호 두 개와 `relative_url` 형식은 정확히 지켜야 합니다. 따옴표나 닫는 괄호가 빠지면 빌드가 실패합니다.

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

## 커밋 메시지

무엇을 바꿨는지 알 수 있게 씁니다. `Update index.md`처럼 GitHub가 자동으로 채운 메시지는 나중에 기록을 찾기 어렵습니다.

- 좋은 예: `IRB 페이지에 갱신 주기 추가`, `안전교육 페이지 링크 수정`
- 피할 예: `Update index.md`, `수정`
