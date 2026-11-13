---
title: Python에서 PDF 워터마크 세부 정보 추출
linktitle: 워터마크 세부 정보 추출
type: docs
weight: 50
url: /ko/python-net/extract-watermarks/
description: Python에서 PDF의 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF의 워터마크 세부 정보 추출
Abstract: Python에서 PDF의 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.
---

Python에서 PDF의 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.

## 워터마크 텍스트 및 경계 읽기

하위 유형이 `WATERMARK`인 각 페이지 매김 아티팩트의 텍스트와 경계 사각형을 출력하세요.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## 관련 항목

- [워터마크 추가](/pdf/ko/python-net/add-watermarks/)
- [워터마크 제거](/pdf/ko/python-net/remove-watermarks/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
