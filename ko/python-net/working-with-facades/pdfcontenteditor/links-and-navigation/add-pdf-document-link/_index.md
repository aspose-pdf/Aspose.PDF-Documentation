---
title: PDF 문서 링크 추가
linktitle: PDF 문서 링크 추가
type: docs
weight: 50
url: /ko/python-net/add-pdf-document-link/
description: 이 예제에서는 입력 PDF를 바인딩하고, 다른 PDF의 페이지에 녹색 링크를 추가하고, 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 콘텐츠 편집기를 사용하여 PDF 문서 링크 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 다른 PDF 문서에 링크를 추가하는 방법을 보여줍니다.다른 PDF를 여는 클릭 가능한 영역을 만들고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF 문서 링크를 통해 사용자는 한 PDF에서 다른 PDF로 원활하게 이동할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)다른 PDF 파일의 페이지로 연결되는 클릭 가능한 사각형을 정의하여 문서를 대화형으로 만들고 연결할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 링크의 사각형을 정의합니다.
1. 연결된 PDF 파일, 소스 페이지 및 대상 페이지를 지정합니다.
1. 링크 색상을 설정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
