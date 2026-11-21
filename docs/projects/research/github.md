---
layout: default
title: 연구 프로젝트용 GitHub
parent: 연구 프로젝트
nav_order: 3
permalink: /projects/research/github/
---

# 연구용 GitHub

## 개요
연구실 내부 프로젝트에서 raw 데이터 처리부터 논문 그림까지 재현 가능하게 관리하기 위한 표준 폴더 구조입니다. 
Git 기본 사용법은 [Git and GitHub](../../operations/github.md)를 참고하세요.

## 저장소 원칙
1. 투고 전에는 **Private**으로 두고, 논문을 공개할 때 **Public**으로 전환한다
2. 대용량 데이터 (Raw 등)은 github 에 업로드 하지 않는다 (100mb 이상 업로드 불가능)
3. 개인 정보는 올리지 않는다.
4. 분석 script 는 상대경로만 사용한다 
5. 번호로 실행 순서를 나타낸다
6. 폴더, 파일명에는 공백/한글을 사용하지 않는다
7. 재현성을 위해 분석 버전을 고정한다 (파이프라인은 -r, R 패키지는 renv.lock 사용)
8. 중간 분석 결과와 논문용 최종 분석 결과를 분리한다(시행착오는 old/, 논문용은 final/)
 
## 권장 폴더 구조

```text
2026_SkinCancer_mbio/           # 권장 이름: 연도_주제_저널
├─ README.md                    # 프로젝트 개요, 데이터 출처, 실행 순서
├─ .gitignore
├─ Rproj.Rproj
├─ renv.lock                    # R 패키지 버전 기록
│
├─ pipeline/                    # raw → process (Nextflow 실행 기록)
│  ├─ README.md                 # 파이프라인 이름·버전·실행일
│  ├─ run.sh                    # 실제 실행한 nextflow 명령어
│  ├─ params.yaml               # -params-file
│  ├─ custom.config             # 서버 자원 설정 (SLURM, 메모리, CPU)
│  ├─ samplesheet.csv
│  └─ scripts/                  # 기타 분석 script
│     └─ make_tables.R
│
├─ data/
│  ├─ raw/                      # 원본 fastq, 메타데이터 (git X, 읽기 전용)
│  ├─ pipeline_res              # 대용량의 중간 산출물
│  └─ process/                  # R 분석 시작점 (git O)
│     ├─ abundance_table.tsv
│     ├─ taxonomy_table.tsv
│     ├─ metadata.tsv
│     └─ qc_summary.tsv
│
├─ analysis/
│  ├─ old/                      # 탐색 분석 (날짜 접두어 허용)
│  │  ├─ 261020_RF_comparison.Rmd
│  │  └─ 261021_PERMANOVA_test.Rmd
│  └─ final/                    # 논문용 최종 분석 (번호순 실행)
│     ├─ 00_preprocessing.Rmd
│     ├─ 01_figure2.Rmd
│     ├─ 02_figure3.Rmd
│     ├─ 03_figure4.Rmd
│     └─ 04_supplementary_tables.Rmd
│
├─ results/
│  ├─ old/                      # 탐색 결과 (git X)
│  └─ final/
│     ├─ figures/               # PDF + 고해상도 PNG
│     ├─ figure_data/           # 그림의 기초 수치 (CSV)
│     └─ tables/
│
└─ docs/
   ├─ submission/              # git X 또는 링크만
   ├─ revision/                # git X 또는 링크만
   └─ references/
```

### run.sh 예시 
```bash
#!/bin/bash
# Pipeline: nf-core/ampliseq 2.11.0
# Run date: 2026-11-21 / Runner: 이름
# 프로젝트 루트에서 실행: bash pipeline/run.sh

nextflow run nf-core/ampliseq -r 2.11.0 \
  -profile singularity \
  -params-file pipeline/params.yaml \
  -c pipeline/custom.config \
  --input pipeline/samplesheet.csv \
  --outdir data/pipeline_out \
  -resume
```

### .gitignore 예시 

```text
# 원본·대용량·민감 데이터 (README만 예외)
data/raw/*
data/pipeline_res/*
!data/*/README.md

# Nextflow 작업 파일
work/
.nextflow/
.nextflow.log*

# 탐색 결과
results/old/

# R / RStudio
.Rproj.user/
.Rhistory
.RData
renv/library/
*_cache/
*_files/

# 원고·문헌
docs/*.docx
docs/references/*.pdf

# 시스템
.DS_Store
```
### 커밋
1. commit 시 왜 했고, 어떤 것이 수정되었고, 어떤 결과가 도출되었는지 저장
2. 중요한 버전에는 tag추가


## 투고 전 체크리스트
- [ ] 새 환경에서 clone 후 analysis/final/을 번호순 knit하면 모든 그림이 재생성된다
- [ ] pipeline/run.sh에 -r 버전이 고정되어 있다
- [ ] pipeline_info/가 커밋되어 있고 Methods 툴 버전과 일치한다
- [ ] renv.lock이 최신이다 (renv::snapshot())
- [ ] 본문 숫자(샘플 수, p값, 리드 수)가 모두 코드에서 나온다
- [ ] 랜덤 분석(rarefaction, DMM, RF, PERMANOVA 등)에 set.seed()가 있다
- [ ] data/process/와 커밋 이력에 민감정보/개인정보/비밀번호가 없다
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
