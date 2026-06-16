---
title: 자바스크립트 링크 추가
linktitle: 자바스크립트 링크 추가
type: docs
weight: 30
url: /ko/python-net/add-javascript-link/
description: 이 예제에서는 입력 PDF를 바인딩하고, 클릭 시 알림을 트리거하는 JavaScript 링크를 추가하고, 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 자바스크립트 링크 추가
Abstract: 이 예제는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 자바스크립트 링크를 추가하는 방법을 보여줍니다.클릭하면 JavaScript 코드를 실행하는 클릭 가능한 영역을 만들고 업데이트된 PDF를 저장하는 방법을 보여줍니다.
---

PDF의 JavaScript 링크를 사용하면 경고 표시, 계산 수행 또는 문서 내용의 동적 수정과 같은 대화형 기능을 사용할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)페이지에서 클릭 가능한 사각형을 정의하고 이를 사용자 지정 JavaScript 코드와 연결할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 자바스크립트 링크의 사각형을 정의합니다.
1. 페이지 번호와 링크 색상을 지정합니다.
1. 클릭 시 실행할 자바스크립트 코드를 할당합니다.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
