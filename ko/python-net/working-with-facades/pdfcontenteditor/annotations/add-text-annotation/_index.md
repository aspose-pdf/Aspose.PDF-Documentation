---
title: 텍스트 주석 추가
type: docs
weight: 50
url: /ko/python-net/add-text-annotation/
description: .NET을 통해 파이썬용 Aspose.PDF 의 PDFContentEditor 클래스를 사용하여 PDF 문서에 텍스트 주석을 추가합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 텍스트 주석 추가하기
Abstract: .NET을 통해 파이썬용 Aspose.PDF 의 PDFContentEditor 클래스를 사용하여 PDF 문서에 텍스트 주석을 추가하는 방법을 알아봅니다.이 예제에서는 텍스트 주석을 특정 위치에 배치하고, 제목과 내용을 정의하고, 업데이트된 PDF 파일을 저장하는 방법을 보여줍니다.
---

이 문서에서는 를 사용하여 PDF 문서에 텍스트 주석을 추가하는 방법을 보여줍니다. [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Aspose.PDF 클래스입니다.

텍스트 주석을 사용하면 PDF 페이지의 특정 부분에 주석, 메모 또는 추가 정보를 첨부할 수 있습니다.이러한 주석은 아이콘으로 표시될 수 있으며 사용자가 문서를 볼 때 확장할 수 있습니다.

이 예에서는

- PDF 문서가 PDF 컨텐츠 편집기에 로드됩니다.
- 페이지의 특정 위치에 텍스트 주석이 추가됩니다.
- 주석에는 제목, 내용, 아이콘 유형 및 가시성 설정이 포함됩니다.
- 수정된 문서는 새 파일에 저장됩니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력된 PDF 문서를 바인딩합니다.
1. 주석 위치를 정의합니다.
1. 텍스트 주석 추가
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
