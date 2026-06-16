---
title: 첨부 파일 주석 추가
linktitle: 첨부 파일 주석 추가
type: docs
weight: 30
url: /ko/python-net/add-file-attachment-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 파일 경로를 사용하여 첫 페이지에 첨부 파일 주석을 추가하고, 업데이트된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 파일 첨부 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 파일 경로를 사용하여 PDF에 파일 첨부 주석을 만드는 방법을 보여줍니다.주석 배치를 정의하고, 설명 텍스트를 설정하고, 아이콘 유형을 선택하고, 수정된 문서를 저장하는 방법을 보여줍니다.
---

파일 첨부 주석을 사용하면 외부 파일을 PDF 페이지에 대화형 아이콘으로 포함할 수 있습니다.파일 경로 오버로드를 사용하면 스트림을 수동으로 열지 않고도 디스크에서 직접 파일을 첨부할 수 있습니다.또한 이 방법을 사용하면 주석 아이콘을 사용자 지정하고 사용자에게 설명을 제공할 수 있습니다.

1. 생성하기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. 입력 PDF를 바인딩합니다.
1. 주석 사각형을 정의합니다.
1. 첨부 파일 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
