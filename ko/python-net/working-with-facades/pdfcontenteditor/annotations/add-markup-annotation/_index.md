---
title: 마크업 주석 추가
type: docs
weight: 30
url: /ko/python-net/add-markup-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고 첫 페이지에 네 가지 마크업 주석을 추가하고 업데이트된 문서를 저장합니다.각 주석은 서로 다른 마크업 스타일과 색상을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 강조 표시, 밑줄, 취소선 및 구불구불한 마크업 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 강조 표시, 밑줄, 취소선 및 물결 모양의 여러 마크업 주석을 추가하는 방법을 보여줍니다.이 샘플은 주석 영역을 정의하고, 마크업 유형을 지정하고, 색상을 적용하고, 수정된 문서를 저장하는 방법을 보여줍니다.
---

마크업 주석은 PDF 내의 텍스트를 강조하거나 검토하는 데 사용됩니다.PDFContentEditor를 사용하면 사각형 영역, 주석 텍스트, 마크업 유형, 페이지 번호 및 색상을 지정하여 프로그래밍 방식으로 다양한 마크업 스타일을 적용할 수 있습니다.

1. 생성하기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. 입력 PDF를 바인딩합니다.
1. 주석 사각형을 정의합니다.
1. 마크업 주석 추가
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
