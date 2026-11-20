# JBSM Handbook


## 문서 수정 방법

사이트의 연필 버튼 또는 `docs/` 아래 Markdown 파일을 편집합니다. 기존 Jekyll 메타데이터와 링크는 작성 이력을 보존하기 위해 유지하고 `hooks/handbook.py`에서 변환합니다. 새 문서는 일반 Markdown으로 작성하고 `mkdocs.yml`의 `nav`에 추가합니다.

## 로컬 실행

```sh
python -m pip install -r requirements.txt
mkdocs serve
```

배포 전 검증: `mkdocs build --strict`. GitHub Pages의 Source를 **GitHub Actions**로 설정하면 main에 반영할 때 자동 배포됩니다.
