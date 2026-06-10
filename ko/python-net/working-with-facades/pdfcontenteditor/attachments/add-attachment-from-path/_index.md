---
title: 경로에서 첨부 파일 추가
type: docs
weight: 20
url: /ko/python-net/add-attachment-from-path/
description: 이 예제에서는 입력 PDF를 바인딩하고, 해당 파일 경로를 사용하여 외부 파일을 첨부하고, 수정된 PDF를 포함된 첨부 파일과 함께 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 파일 경로 오버로드를 사용하여 PDF에 파일 첨부
Abstract: 이 예제에서는 Facades API를 통해 파이썬용 Aspose.PDF 의 'add_document_attach () '의 파일 경로 오버로드를 사용하여 외부 파일을 PDF 문서에 첨부하는 방법을 보여줍니다.파일 스트림을 수동으로 열지 않고도 첨부 파일을 간편하게 추가할 수 있습니다.
---

PDF에는 참조 또는 배포용 문서, 스프레드시트 또는 이미지와 같은 내장 파일이 포함될 수 있습니다.'add_document_attachment () '의 파일 경로 오버로드를 사용하면 파일 경로에서 직접 첨부 파일을 추가할 수 있으므로 파일을 수동으로 열 필요가 없습니다.

1. 생성하기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. 입력 PDF를 바인딩합니다.
1. 파일 경로를 사용하여 첨부 파일을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
