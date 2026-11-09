---
title: Python에서 PDF 머리글 및 바닥글 제거
linktitle: 머리글 및 바닥글 제거
type: docs
weight: 110
url: /ko/python-net/remove-headers-footers/
description: Python을 사용하여 PDF의 첫 페이지에서 머리글 및 바닥글 흔적을 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에서 머리글 및 바닥글 제거
Abstract: Python을 사용하여 PDF의 첫 페이지에서 머리글 및 바닥글 흔적을 제거합니다.
---

Python을 사용하여 PDF의 첫 페이지에서 머리글 및 바닥글 흔적을 제거합니다.

## 머리글 및 바닥글 아티팩트 제거

삭제하기 전에 하위 유형이 `HEADER` 또는 `FOOTER`인 페이지 매김 아티팩트를 모으세요.

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## 관련 항목

- [머리글 및 바닥글 추가](/pdf/ko/python-net/artifacts-header-footer/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
