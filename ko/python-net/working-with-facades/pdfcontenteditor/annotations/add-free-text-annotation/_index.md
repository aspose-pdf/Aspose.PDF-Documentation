---
title: 자유 텍스트 주석 추가
type: docs
weight: 20
url: /ko/python-net/add-free-text-annotation/
description: 이 예제에서는 기존 PDF 파일을 로드하고 첫 페이지의 정의된 위치에 자유 텍스트 주석을 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 자유 텍스트 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 자유 텍스트 주석을 삽입하는 방법을 보여줍니다.PDF를 바인딩하고, 주석 배치를 정의하고, 사용자 지정 텍스트를 추가하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

자유 텍스트 주석을 사용하면 팝업 주석 없이 보이는 텍스트를 PDF 페이지에 직접 배치할 수 있습니다.PDFContentEditor를 사용하여 주석 사각형, 표시된 텍스트 및 대상 페이지를 지정할 수 있습니다.

1. 생성하기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. 입력 PDF를 바인딩합니다.
1. 주석 위치를 정의합니다.
1. 자유 텍스트 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
