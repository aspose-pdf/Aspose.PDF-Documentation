---
title: Python에서 PDF에 Bates Numbering 추가
linktitle: Bates Numbering 추가
type: docs
weight: 10
url: /ko/python-net/add-bates-numbering/
description: Python으로 PDF 페이지에 순차적인 Bates 식별자를 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 Bates Numbering 추가
Abstract: Python으로 PDF 페이지에 순차적인 Bates 식별자를 추가합니다.
---

Bates 번호 매기기는 문서 집합의 페이지에 순차적인 식별자를 할당합니다. 구성하려면 `BatesNArtifact` 페이지 범위, 시작 번호, 자리수, 접두사, 접미사 및 배치를 제어하려면.

## Bates 번호 매기기 아티팩트 추가

설정한 아티팩트와 문서의 페이지를 `PageCollectionExtensions.add_bates_numbering`에 전달하세요. 이 예제는 기존 페이지에 `000001`부터 시작하는 6자리 식별자를 부여합니다.

```python
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## 페이징 아티팩트를 사용한 Bates 번호 매기기

페이지 매김 API로 Bates 번호를 매기려면 이전 예제의 `_create_bates_artifact`를 재사용하세요. 아티팩트를 담은 목록을 `PageCollectionExtensions.add_pagination`에 전달하세요.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## 관련 항목

- [베이츠 번호 제거](/pdf/ko/python-net/remove-bates-numbering/)
- [Python에서 PDF 아티팩트를 다루기](/pdf/ko/python-net/artifacts/)
