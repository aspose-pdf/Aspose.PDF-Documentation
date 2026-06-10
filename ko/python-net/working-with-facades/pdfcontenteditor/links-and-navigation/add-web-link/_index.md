---
title: 웹 링크 추가
linktitle: 웹 링크 추가
type: docs
weight: 60
url: /ko/python-net/add-web-link/
description: 이 예제는 입력 PDF를 바인딩하고 페이지 1에 Aspose의 Python PDF 제품 페이지를 가리키는 파란색 웹 링크 주석을 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에 웹 링크 추가
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에 웹 링크를 추가하는 방법을 보여줍니다.웹 브라우저에서 지정된 URL을 여는 페이지에 클릭 가능한 영역을 만들고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF의 웹 링크를 통해 사용자는 온라인 리소스, 웹 사이트 또는 문서를 직접 탐색할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)클릭하면 기본 웹 브라우저에서 URL이 열리는 PDF 페이지의 사각형 영역을 정의할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 웹 링크의 사각형을 정의합니다.
1. URL, 페이지 번호 및 링크 색상을 지정합니다.
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
