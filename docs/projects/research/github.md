---
layout: default
title: 연구 프로젝트용 GitHub
parent: 연구 프로젝트
nav_order: 3
permalink: /projects/research/github/
---

# 연구용 GitHub

논문과 연구 코드를 GitHub로 관리하는 방법을 안내합니다. Git 기본 사용법은 [Git and GitHub](../../operations/github.md)를 참고하세요.

## 저장소 원칙

- 투고 전에는 **Private**으로 두고, 논문을 공개할 때 **Public**으로 전환합니다.

## 권장 폴더 구조

```text

```

## 올리지 않는 것

- **원시 시퀀싱 데이터**: SRA/ENA에 제출하고 README에는 accession 번호만 적습니다.
- **환자 식별 정보**: 이름, 등록번호, 생년월일 등은 비식별화 전 자료를 올리지 않습니다.
- **비밀번호·토큰·키**: 접속 정보는 저장소 밖에서 관리합니다.
- **대용량 중간 산출물**: Zenodo에 올리고 링크만 겁니다.

## 투고 전 체크리스트
- [ ] 새 환경에서 clone 후 analysis/final/을 번호순 knit하면 모든 그림이 재생성된다
- [ ] pipeline/run.sh에 -r 버전이 고정되어 있다
- [ ] pipeline_info/가 커밋되어 있고 Methods 툴 버전과 일치한다
- [ ] renv.lock이 최신이다 (renv::snapshot())
- [ ] 본문 숫자(샘플 수, p값, 리드 수)가 모두 코드에서 나온다
- [ ] 랜덤 분석에 set.seed()가 있다
- [ ] data/process/와 커밋 이력에 개인정보·비밀번호가 없다
- [ ] raw 데이터가 SRA/ENA에 등록되었고 접근 번호가 README에 있다
- [ ] README에 제목, 초록, 실행 방법, 의존성이 있다

## 모범사례

| 사례 | 눈여겨볼 원칙 |
| --- | --- |
| [SchlossLab/new_project](https://github.com/SchlossLab/new_project) | `make write.paper` 한 줄로 raw→논문 재현, data/process만 커밋, 본문 숫자 하드코딩 금지 |
| [Kiang Lab Project Structure](https://kianglab.github.io/labmanual/projectstructure.html) | 스크립트명 `NN_verb_slug.R`, 파일명에 날짜·버전 금지, renv.lock 커밋, 민감 데이터는 data_private |
| [UCSF Decision Lab Analysis Pathway](https://decisionlab.ucsf.edu/handbook/rstudio-analysis-pathway.html) | Rmd 간 데이터 흐름 순환 금지, 샘플 제외는 삭제 대신 플래그 변수 |
| [UCSF Decision Lab Open Science](https://decisionlab.ucsf.edu/handbook/reliability-and-open-science.html) | 탐색적/확증적 분석 구분, 분석 결정을 이유와 함께 기록, 출판 시 코드 공개 |


논문 준비 전반은 [논문](../paper.md)을, 분석 재현성은 [연구 재현성](../reproducibility.md)을 참고하세요.
