---
layout: default
title: 연구용 GitHub
parent: 연구 프로젝트
nav_order: 3
permalink: /projects/research/github/
---

# 연구용 GitHub

논문과 연구 코드를 GitHub로 관리하는 방법을 안내합니다. Git 기본 사용법은 [Git and GitHub](../../operations/github.md)를 참고하세요.

## 저장소 원칙

- 논문 한 편당 저장소 하나를 만듭니다.
- 저장소 이름은 `연도-주제-저자` 형식으로 짓습니다. (예: `2026-skin-microbiome-kim`)
- 투고 전에는 **Private**으로 두고, 논문을 공개할 때 **Public**으로 전환합니다.
- 저장소 About 칸에 논문 제목과 DOI를 적습니다.

## 권장 폴더 구조

```text
2026-topic-author/
├── README.md            # 연구 개요와 재현 절차
├── environment.yml      # conda 환경 (R은 renv.lock)
├── workflow/            # Nextflow 또는 Snakemake 파이프라인
├── scripts/             # 분석·시각화 스크립트
├── metadata/            # 비식별화한 샘플 메타데이터
└── figures/             # 논문 그림 생성 결과
```

## 올리지 않는 것

- **원시 시퀀싱 데이터**: SRA/ENA에 제출하고 README에는 accession 번호만 적습니다.
- **환자 식별 정보**: 이름, 등록번호, 생년월일 등은 비식별화 전 자료를 올리지 않습니다.
- **비밀번호·토큰·키**: 접속 정보는 저장소 밖에서 관리합니다.
- **대용량 중간 산출물**: Zenodo에 올리고 링크만 겁니다.

## 투고·출판할 때 할 일

1. README에 환경 구성부터 그림 생성까지의 재현 절차를 정리합니다.
2. 저장소를 Public으로 전환합니다.
3. GitHub–Zenodo 연동을 켜고 Release를 만들어 DOI를 발급받습니다.
4. 논문의 Code/Data Availability 항목에 저장소 주소, Zenodo DOI, 시퀀싱 데이터 accession을 적습니다.

논문 준비 전반은 [논문](../paper.md)을, 분석 재현성은 [연구 재현성](../reproducibility.md)을 참고하세요.

## 계정과 권한

- 프로젝트 참여자에게만 저장소 권한을 부여하고, 참여가 끝나면 권한을 정리합니다.
- 파일 삭제나 구조 변경 같은 큰 변경은 Pull Request로 검토한 뒤 반영합니다.
