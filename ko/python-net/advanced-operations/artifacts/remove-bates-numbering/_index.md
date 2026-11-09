---
title: Python에서 PDF 베이츠 넘버링 제거
linktitle: 베이츠 넘버링 제거
type: docs
weight: 100
url: /ko/python-net/remove-bates-numbering/
description: Python에서 PDF의 모든 페이지에서 베이츠 넘버링을 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 베이츠 넘버링 제거
Abstract: Python에서 PDF의 모든 페이지에서 베이츠 넘버링을 제거합니다.
---

Python에서 PDF의 모든 페이지에서 베이츠 넘버링을 제거합니다.

## 베이츠 넘버링 삭제

문서의 페이지를 `PageCollectionExtensions.delete_bates_numbering`에 전달한 다음 PDF를 저장하세요.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## 관련 항목

- [Bates 번호 매기기 추가](/pdf/ko/python-net/add-bates-numbering/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
