---
title: PDF에 페이지 나누기 추가
linktitle: PDF에 페이지 나누기 추가
type: docs
weight: 20
url: /ko/python-net/add-page-breaks-in-pdf/
description: 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 페이지 나누기를 삽입합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 프로그래밍 방식으로 PDF 페이지에 페이지 나누기 추가
Abstract: Python용 Aspose.PDF 를 사용하여 PDF 문서에 페이지 나누기를 삽입하는 방법을 알아봅니다.이 예제에서는 지정된 세로 위치에서 페이지를 분할하여 개발자가 콘텐츠를 재구성하고 추가 페이지를 동적으로 만들 수 있는 방법을 보여줍니다.
---

페이지 나누기는 긴 PDF 페이지를 여러 페이지로 분할하거나 문서 전체에 내용이 배포되는 방식을 제어해야 할 때 유용합니다.개발자는 Aspose.PDF for Python을 사용하여 PDF를 수동으로 편집하지 않고도 특정 위치에 페이지 나누기를 삽입할 수 있습니다.

이 문서에서는 의 'add_page_break' 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 선택한 페이지의 정의된 세로 좌표에 페이지 나누기를 삽입하는 클래스입니다.메서드는 새 페이지를 만들고 내용을 중단점 아래의 해당 페이지로 이동합니다.

1. PDF 파일 편집기 개체 만들기
1. 페이지 나누기 위치를 정의합니다.
1. 페이지 나누기를 삽입합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
