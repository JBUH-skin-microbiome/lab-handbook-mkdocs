---
layout: default
title: 홈페이지 관리
parent: 연구실 운영
nav_order: 1
permalink: /operations/homepage/
---

# 홈페이지 관리

## 바로가기

- [연구실 홈페이지](https://jbuh-skin-microbiome.github.io/)
- [홈페이지 소스 저장소](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io)
- [연구실 매뉴얼 저장소](https://github.com/JBUH-skin-microbiome/lab-handbook-mkdocs)

## 홈페이지 작동 방식

연구실 홈페이지는 Jekyll의 al-folio 테마로 만든 사이트입니다. 소스는 [홈페이지 저장소](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io)의 `master` 브랜치에 있고 push하면 GitHub Actions가 사이트를 빌드해 배포합니다.

| 작업 | 고칠 곳 | 웹에서 수정 |
| --- | --- | --- |
| 논문 추가, 연구원 연결 | `_bibliography/papers.bib`, `_members/` | 안 됨 (스크립트 실행 필요) |
| 학회 발표, 수상 목록 | `_pages/publications.md` | 가능 |
| Gallery, Facility | `_projects/`, `assets/img/jbsm/` | 가능 |
| News | `_news/` | 가능 |
| 메뉴, 첫 화면, 디자인 | `_pages/`, `_config.yml`, `_sass/` | 가능 (로컬 미리보기 권장) |


웹에서 수정하는 방법은 Handbook과 같습니다. [Manual 기여](manual-management.md)를 참고하세요.

자주 하는 수정은 두 가지입니다.

- 연구실 출판물 업데이트 (웹에서는 안 되고 로컬 작업 필요)
- 연구실 이벤트(수상, 학회 참여, 워크숍) 업데이트 (웹에서 추가 가능)

## 논문 추가 및 연구원 연결


생성 스크립트가 `_bibliography/papers.bib` 하나를 읽어 Publications 페이지와 연구원별 논문 목록을 만듭니다. bib을 고친 뒤 스크립트를 돌려야 목록이 바뀝니다.

!!! warning "배포 서버는 생성 스크립트를 실행하지 않습니다"
    `papers.bib`만 고쳐서 push하면 사이트에 아무것도 바뀌지 않습니다. 스크립트가 만든 `_includes/publications/`와 `_includes/member-publications/`의 HTML까지 함께 커밋해야 합니다. 그래서 논문 추가는 로컬에서 작업합니다.

### 1. papers.bib에 논문 추가

`_bibliography/papers.bib`에 항목을 하나 추가합니다. 같은 연도 논문은 파일에 적힌 순서대로 나오니 보여 줄 순서에 맞춰 넣습니다.

```bibtex
@article{kim2026distinct,
  title = {Distinct site-specific bacterial microbiota within and between skin physiologic types in healthy Koreans: a pilot study},
  author = {Kim, SY and Tran, TQT and Nam, KH and Yun, SK and Park, J},
  journal = {Scientific Reports},
  abbr = {Sci Rep},
  year = {2026},
  doi = {10.1038/s41598-026-62903-7},
  html = {https://doi.org/10.1038/s41598-026-62903-7},
  bibtex_show = {true}
}
```

- 키(`kim2026distinct`)는 `제1저자성 + 연도 + 제목 첫 단어`로 짓고 다른 항목과 겹치지 않게 합니다.
- `author`는 `성, 이니셜`을 `and`로 잇습니다. 연구원 연결에 쓰이니 표기를 정확히 맞춥니다.
- `abbr`은 목록 왼쪽 배지에 나오는 저널 약칭입니다.
- 아직 권호가 없는 논문(in press)도 `year`를 넣으면 해당 연도 목록에 나옵니다.

### 2. 연구원 연결

논문 저자 중 연구실 구성원 이름에는 프로필 링크가 걸리고 그 구성원 페이지에도 논문이 모입니다. 연결 기준은 `_members/<이름>.md`의 `publication_names`입니다.

```yaml
publication_names: ["Kim, SY"]
```

- bib의 `author`에 적은 표기와 글자 하나까지 같아야 연결됩니다. `Kim, SY`와 `Kim, S-Y`는 다른 이름으로 봅니다.
- 논문마다 이름 표기가 다르면 모두 적습니다. (예: `["Kim, SY", "Kim, S"]`)
- 같은 표기를 두 구성원에게 넣으면 스크립트가 오류를 냅니다.

새 구성원은 `_members/`에 파일을 만듭니다. 기존 파일을 복사해 고치는 편이 빠릅니다.

```yaml
---
title: 홍길동 · Gildong Hong
name: 홍길동
name_en: Gildong Hong
role: MS Student
group: researcher
group_label: Researcher
order: 13
image: /assets/img/jbsm/member-placeholder.svg
publication_names: ["Hong, GD"]
---
```

- `group`은 `faculty`, `researcher`, `alumni` 중 하나입니다. 졸업하면 `alumni`로 바꿉니다.
- `order`가 작을수록 Members 페이지 앞에 나옵니다.
- `publication_names`를 넣은 구성원은 스크립트를 한 번 돌려야 페이지가 열립니다. 논문 목록 파일이 없으면 빌드가 실패합니다.

### 3. 생성 스크립트 실행

홈페이지 저장소 폴더에서 실행합니다. Python 3.9 이상이면 되고 추가 패키지는 필요 없습니다.

```bash
python scripts/generate_publication_includes.py
```

`Generated N publication entries ...`가 나오면 성공입니다. 바뀐 파일을 확인하고 함께 커밋합니다.

```bash
git status
git add _bibliography/papers.bib _members _includes/publications _includes/member-publications
git commit -m "Add 2026 Sci Rep paper"
git push
```

### 4. 학회 발표, 수상, 특허

Publications 페이지 아래쪽의 Conference 등은 자동 생성이 아닙니다. `_pages/publications.md`의 해당 연도 목록에 직접 한 줄을 추가합니다. 웹에서 고쳐도 됩니다.

```markdown
- [P] Kim SY et al. 발표 제목. 9th KSCMI, 2026.11.07.
```

`[P]`는 포스터, `[O]`는 구연, `[IL]`은 초청·교육 강연입니다.

### 5. 새해가 되면

연도가 코드에 직접 적혀 있어서 새해 첫 논문을 넣을 때 아래 두 곳을 먼저 고칩니다. 빠뜨리면 새 연도 논문이 목록에 나오지 않습니다.

- `scripts/generate_publication_includes.py`의 `YEARS`에 새 연도 추가
- `_pages/publications.md`의 Articles에 새 연도 제목과 include 줄 추가 (기존 연도 블록을 복사해 숫자만 바꿉니다)

## Gallery·Facility 추가

Gallery와 Facility는 같은 구조입니다. `_projects/`의 Markdown 파일 하나가 카드 하나가 되고 `kind` 값으로 어느 페이지에 나올지 정합니다. 웹에서 사진을 올리고 파일을 만들어도 됩니다.

### 사진 준비

- `assets/img/jbsm/`에 올립니다. 웹에서는 폴더를 연 뒤 Add file → Upload files를 씁니다.
- 파일 이름은 기존 번호를 이어 갑니다. Gallery는 `gallery-asset-23.jpg`, Facility는 `facility-16.jpg` 식입니다.
- 휴대폰 원본은 용량이 커서 페이지가 느려집니다. 긴 변 1600px, 장당 500KB 안팎으로 줄여 올립니다.
- 얼굴이 나온 사진은 당사자에게 공개해도 되는지 먼저 확인합니다.

### Gallery

`_projects/연도-행사.md` 파일을 만듭니다. (예: `_projects/2026-kscmi.md`)

```yaml
---
title: "대한피부진균및감염학회"
description: "2026.06.27"
kind: gallery
year: 2026
date_label: "2026.06.27"
order: 4
img: /assets/img/jbsm/gallery-asset-09.jpg
images:
  - /assets/img/jbsm/gallery-asset-09.jpg
  - /assets/img/jbsm/gallery-asset-10.jpg
  - /assets/img/jbsm/gallery-asset-11.jpg
---
```

- `img`는 카드 썸네일, `images`는 카드를 눌렀을 때 보이는 사진입니다.
- 카드는 `year` 값에 따라 연도별로 묶이고 같은 연도 안에서는 `order` 순서대로 나옵니다.
- 새해 첫 사진을 넣을 때는 `_pages/gallery.md`의 `gallery_years` 목록 맨 앞에 새 연도를 추가합니다. 빠뜨리면 그해 카드가 보이지 않습니다.

### Facility

`_projects/facility-공간.md` 파일을 만들거나 기존 파일에 사진과 장비를 추가합니다.

```yaml
---
title: "Wet Lab (1F)"
description: "1층 Wet Lab"
kind: facility
order: 2
img: /assets/img/jbsm/facility-03.jpg
images:
  - /assets/img/jbsm/facility-03.jpg
  - /assets/img/jbsm/facility-07.jpg
details:
  - "Clean Bench"
  - "Cell Culture Incubator"
---
```

`details`에는 그 공간의 주요 장비를 적습니다. 장비를 들이거나 옮기면 같이 고칩니다.

### News

첫 화면 News에 나오는 한 줄 소식은 `_news/날짜-제목.md`로 만듭니다. (예: `_news/2026-11-12-jbnu-awards.md`)

```markdown
---
date: 2026-11-12
inline: true
---
김소연·성기재 대학원생, 대한피부진균 및 감염학회 우수포스터상·우수연제상 수상 [🔗](https://www.jbnu.ac.kr/...)
```

- `inline: true`면 첫 화면에 한 줄로만 나옵니다.
- 관련 기사나 공지가 있으면 끝에 링크를 붙입니다.
- 행사 사진이 있으면 Gallery 카드도 함께 만듭니다.

## 홈페이지 구조 수정

메뉴, 첫 화면, 디자인을 바꾸는 작업입니다. 여러 페이지가 함께 바뀌니 로컬에서 미리 보고 PR로 올리세요.

### 어디를 고치나

| 바꿀 것 | 파일 |
| --- | --- |
| 상단 메뉴 항목과 순서 | `_pages/*.md`의 `nav`, `nav_order` |
| 첫 화면 소개, 사진, 안내 카드 | `_pages/about.md` |
| 연구 내용, 연락처 등 각 페이지 | `_pages/research.md`, `_pages/contact.md` 등 |
| 사이트 이름, 기본 설정 | `_config.yml` |
| 색상, 글꼴, 레이아웃 | `_sass/`, `_layouts/`, `_includes/` |

### 디자인 규칙

- 긴 설명은 검은색, 짧은 강조 문구는 남색(`#1a0076`)을 씁니다.
- 한글과 바닥글은 `Gothic A1`, 영문은 `Vollkorn`을 씁니다.
- 기본 강조색은 `#191970`입니다.
- 연구실 지원자 안내는 Handbook의 [연구실 지원자 페이지](https://jbuh-skin-microbiome.github.io/lab-handbook-mkdocs/onboarding/applicants/)로 연결합니다.

### 로컬 미리보기

Ruby와 Bundler를 설치한 뒤 홈페이지 저장소 폴더에서 실행합니다. 자세한 설치 방법은 저장소의 `INSTALL.md`에 있습니다.

```bash
bundle install
bundle exec jekyll serve --lsi
```

브라우저에서 <http://localhost:4000>을 엽니다. Docker를 쓴다면 `docker compose up`으로도 띄울 수 있습니다.

## 배포 확인과 주의사항

- push한 뒤 홈페이지 저장소의 [Actions](https://github.com/JBUH-skin-microbiome/JBUH-skin-microbiome.github.io/actions)에서 Deploy site 실행이 성공했는지 보고 [실제 홈페이지](https://jbuh-skin-microbiome.github.io/)에서 결과를 확인합니다.
- 배포가 실패하면 해당 실행의 로그를 열어 오류가 난 파일과 줄을 찾습니다. 고쳐서 다시 push하고 사이트까지 확인합니다.
- 공개 저장소입니다. 비밀번호, 토큰, 접속 키, 개인정보, 환자 자료는 올리지 않습니다.
- PR로 올리면 빌드 검사만 하고 merge한 뒤에 배포됩니다.
