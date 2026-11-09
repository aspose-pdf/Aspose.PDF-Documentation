---
title: Python에서 PDF 배경 제거
linktitle: 배경 제거
type: docs
weight: 80
url: /ko/python-net/remove-backgrounds/
description: Python에서 PDF 첫 페이지의 배경 아티팩트를 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF의 배경을 제거
Abstract: Python에서 PDF 첫 페이지의 배경 아티팩트를 제거합니다.
---

Python에서 PDF 첫 페이지의 배경 아티팩트를 제거합니다.

## 배경 아티팩트 제거

삭제하기 전에 하위 유형이 `BACKGROUND`인 페이지 매김 아티팩트를 모으세요.

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## 관련 항목

- [배경 추가](/pdf/ko/python-net/add-backgrounds/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
