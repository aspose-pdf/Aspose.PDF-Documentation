---
title: PDF 페이지 내용 크기 조정
type: docs
weight: 30
url: /ko/python-net/resize-pdf-page-contents/
description: 파이썬용 Aspose.PDF 를 사용하여 특정 PDF 페이지의 내용 크기를 조정합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 프로그래밍 방식으로 PDF 페이지 내용 크기 조정
Abstract: Python용 Aspose.PDF 를 사용하여 특정 PDF 페이지의 콘텐츠 크기를 조정하는 방법을 알아봅니다.이 예제에서는 문서 구조를 유지하면서 페이지 내용의 너비와 높이를 조정하여 인쇄 또는 보기를 위한 레이아웃을 쉽게 최적화하는 방법을 보여줍니다.
---

인쇄할 문서를 준비하거나, 내용을 특정 레이아웃에 맞추거나, 문서 전체의 페이지 형식을 표준화할 때 PDF 페이지 내용의 크기를 조정해야 하는 경우가 많습니다.개발자는 Python용 Aspose.PDF 를 사용하여 문서를 수동으로 편집하지 않고도 프로그래밍 방식으로 선택한 페이지의 내용 크기를 조정할 수 있습니다.

이 문서에서는 의 'resize_content' 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스는 PDF 파일의 특정 페이지에 대한 페이지 내용의 크기를 수정합니다.대상 너비와 높이를 지정하면 선택한 페이지의 내용 크기가 그에 맞게 조정됩니다.

1. PDF 파일 편집기 개체 만들기
1. 페이지 콘텐츠 크기 조정

파라미터:

- [1, 3] — 내용의 크기가 조정될 페이지 번호 목록입니다.
- 400 — 페이지 콘텐츠의 새 너비 (포인트)
- 750 — 페이지 콘텐츠의 새 높이 (포인트)

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
