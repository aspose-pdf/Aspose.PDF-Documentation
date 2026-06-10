---
title: 애플리케이션 링크 추가
type: docs
weight: 10
url: /ko/python-net/add-application-link/
description: 이 예제에서는 입력 PDF를 바인딩하고, 첫 페이지에 응용 프로그램 시작 링크를 추가하고, 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 응용 프로그램 시작 링크 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 애플리케이션 시작 링크를 추가하는 방법을 보여줍니다.클릭하면 지정된 응용 프로그램이 열리는 클릭 가능 영역을 만들고 업데이트된 PDF를 저장하는 방법을 보여줍니다.
---

PDF에는 외부 응용 프로그램을 실행하는 링크와 같은 대화형 요소가 포함될 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)클릭하면 특정 실행 파일이 열리는 페이지의 사각형 영역을 정의할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 링크의 사각형 영역을 정의합니다.
1. 실행할 애플리케이션 경로를 지정합니다.
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
