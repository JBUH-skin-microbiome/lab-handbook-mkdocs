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

## 투고·출판할 때 할 일
1. REAMD 에 프로젝트 목적 및 결과 (논문 초록으로 대체 가능), 프로젝트 script 구조 및 재현을 위한 실행 단계를 설명합니다.  
2. 저장소를 Public으로 전환합니다.
3. GitHub–Zenodo 연동을 켜고 Release를 만들어 DOI를 발급받습니다.
4. 논문의 Code/Data Availability 항목에 저장소 주소, Zenodo DOI, 시퀀싱 데이터 accession을 적습니다.

논문 준비 전반은 [논문](../paper.md)을, 분석 재현성은 [연구 재현성](../reproducibility.md)을 참고하세요.
