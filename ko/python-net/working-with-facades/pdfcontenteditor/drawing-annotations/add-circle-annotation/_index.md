---
title: 원 주석 추가
linktitle: 원 주석 추가
type: docs
weight: 10
url: /ko/python-net/add-circle-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 첫 페이지에 원 주석을 만들고, 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에 원 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 원 주석을 추가하는 방법을 보여줍니다.주석 범위를 정의하고, 내용 텍스트를 설정하고, 색상과 모양을 구성하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

원 주석은 PDF 문서의 관심 영역을 강조 표시하는 데 유용합니다.와 함께 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 주석 텍스트, 색상, 채우기 옵션, 페이지 번호 및 테두리 너비와 함께 원의 경계를 정의하는 사각형을 지정하여 원형 모양을 만들 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 원 경계를 정의합니다.
1. 서클 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
