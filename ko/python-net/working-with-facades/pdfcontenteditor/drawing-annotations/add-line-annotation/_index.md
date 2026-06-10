---
title: 라인 주석 추가
type: docs
weight: 30
url: /ko/python-net/add-line-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 사각형 선 끝이 있는 빨간색 선 주석을 그리고, 수정된 PDF를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 줄 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 줄 주석을 추가하는 방법을 보여줍니다.줄의 시작점과 끝점, 사각형 경계, 모양 속성을 정의하고 업데이트된 문서를 저장하는 방법을 설명합니다.
---

선 주석은 텍스트를 강조하거나 관계를 강조하거나 PDF의 특정 영역에 주의를 집중시키는 데 유용합니다.와 함께 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)시작점 및 끝점, 경계 사각형, 색상, 테두리 스타일 및 선 끝을 지정하여 프로그래밍 방식으로 선 주석을 작성할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 선 주석 속성을 정의합니다.
1. 라인 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
