---
title: Python에서 PDF 아티팩트 카운트
linktitle: 아티팩트 카운트
type: docs
weight: 40
url: /ko/python-net/counting-artifacts/
description: Python에서 PDF 페이지의 페이지네이션 아티팩트 하위 유형별로 워터마크, 배경, 헤더 및 푸터를 카운트합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 아티팩트 카운트
Abstract: PDF 페이지에서 페이지네이션 아티팩트를 카운트하여 워터마크, 배경, 헤더 및 푸터를 확인합니다.
---

PDF 페이지에서 페이지네이션 아티팩트를 카운트하여 워터마크, 배경, 헤더 및 푸터를 확인합니다.

## 하위 유형별 아티팩트 수 집계

첫 페이지의 `artifacts` 컬렉션에서 유형이 `PAGINATION`인 항목을 걸러 낸 다음 하위 유형별로 개수를 세세요. 예제는 해당 하위 유형이 없으면 0을 출력합니다.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## 관련 항목

- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
- [워터마크 세부 정보 추출](/pdf/ko/python-net/extract-watermarks/)
- [워터마크 제거](/pdf/ko/python-net/remove-watermarks/)
- [배경 제거](/pdf/ko/python-net/remove-backgrounds/)
- [헤더 및 푸터 제거](/pdf/ko/python-net/remove-headers-footers/)
