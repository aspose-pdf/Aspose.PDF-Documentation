---
title: Python에서 PDF 워터마크 제거
linktitle: 워터마크 제거
type: docs
weight: 90
url: /ko/python-net/remove-watermarks/
description: Python을 사용하여 PDF 첫 페이지에서 워터마크 아티팩트를 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF의 워터마크 제거
Abstract: Python을 사용하여 PDF 첫 페이지에서 워터마크 아티팩트를 제거합니다.
---

Python을 사용하여 PDF 첫 페이지에서 워터마크 아티팩트를 제거합니다.

## 워터마크 아티팩트 제거

이 예제는 첫 페이지에서 유형이 `PAGINATION`이고 하위 유형이 `WATERMARK`인 아티팩트만 제거합니다. 일반 페이지 텍스트, 이미지 또는 주석으로 저장된 워터마크는 PDF에 남습니다.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## 관련 항목

- [워터마크 추가](/pdf/ko/python-net/add-watermarks/)
- [워터마크 세부 정보 추출](/pdf/ko/python-net/extract-watermarks/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
