# JBSM Handbook — MkDocs preview

Material for MkDocs 기반의 연구실 Handbook 시범판입니다. 기존 lab-handbook은 변경하지 않습니다.

## 문서 수정

사이트의 연필 버튼 또는 `docs/` 아래 Markdown 파일을 편집합니다. 기존 Jekyll 메타데이터와 링크는 작성 이력을 보존하기 위해 유지하고 `hooks/handbook.py`에서 변환합니다. 새 문서는 일반 Markdown으로 작성하고 `mkdocs.yml`의 `nav`에 추가합니다.

## 로컬 실행

```sh
python -m pip install -r requirements.txt
mkdocs serve
```

배포 전 검증: `mkdocs build --strict`. GitHub Pages의 Source를 **GitHub Actions**로 설정하면 main에 반영할 때 자동 배포됩니다.

## 이전 범위와 기여도

`migration-inventory.json`은 원본 커밋과 이전한 75개 문서, 7개 정적 파일을 기록합니다. 외부 Notion/Google Drive 문서는 링크를 유지하며 그 내용을 복제하지 않습니다. 기존 Git 이력을 보존하고 문서 본문을 수정하지 않은 채 docs/로 이동했습니다.

상단의 기여 비율은 Git에서 계산한 현재 소스 줄 수 기준이며 연구 성과의 비율이 아닙니다. 현재 원형 표시는 이름의 첫 글자입니다. GitHub 사진과 연구원별 글 목록은 후속 확장 대상입니다. 이메일 주소는 화면에 표시하지 않습니다.
