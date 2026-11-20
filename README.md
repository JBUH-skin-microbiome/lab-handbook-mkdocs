# JBSM Handbook


## 문서 수정 방법
사이트의 연필 버튼 또는 `docs/` 아래 Markdown 파일을 수정하여 문서를 편집할 수 있다.
문서는 일반 Markdown으로 작성하고 `mkdocs.yml`의 `nav`에 추가한다. 

## 문서 작성 후 반영 전에 확인하기 

아래 방법으로 local 에서 실행해 보자. 
```sh
python -m pip install -r requirements.txt
mkdocs serve
```

배포 전 검증: `mkdocs build --strict`. GitHub Pages의 Source를 **GitHub Actions**로 설정하면 main에 반영할 때 자동 배포됩니다.
