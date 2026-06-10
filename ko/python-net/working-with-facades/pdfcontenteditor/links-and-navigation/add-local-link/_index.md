---
title: 로컬 링크 추가
type: docs
weight: 40
url: /ko/python-net/add-local-link/
description: 이 예제에서는 입력 PDF를 바인딩하고 페이지 1을 가리키는 1페이지에 빨간색 로컬 링크를 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 로컬 링크 추가
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에 로컬 링크를 추가하는 방법을 보여줍니다.동일한 PDF 내의 다른 페이지로 이동하는 클릭 가능한 영역을 만들고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF의 로컬 링크를 사용하면 동일한 문서 내에서 페이지 사이를 빠르게 탐색할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)한 페이지를 다른 페이지로 연결하는 클릭 가능한 사각형을 정의하여 문서 사용 편의성과 탐색을 개선할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 로컬 링크의 사각형을 정의합니다.
1. 소스 페이지와 대상 페이지를 지정합니다.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
