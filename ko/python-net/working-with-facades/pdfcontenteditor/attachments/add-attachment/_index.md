---
title: 첨부 파일 추가
linktitle: 첨부 파일 추가
type: docs
weight: 10
url: /ko/python-net/add-attachment/
description: 이 예제에서는 입력 PDF를 바인딩하고, 외부 파일을 첫 페이지에 첨부하고, 수정된 PDF를 포함된 첨부 파일과 함께 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 첨부 파일 추가
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 외부 파일을 PDF 문서에 첨부하는 방법을 보여줍니다.PDF를 바인딩하고, 설명이 포함된 첨부 파일을 추가하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF의 첨부 파일을 사용하면 추가 문서, 이미지 또는 기타 리소스를 PDF에 직접 포함할 수 있습니다.와 함께 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 프로그래밍 방식으로 특정 페이지에 파일을 첨부하고, 첨부 파일 이름을 설정하고, 설명을 제공할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 첨부 파일을 엽니다.
1. PDF에 첨부 파일을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
