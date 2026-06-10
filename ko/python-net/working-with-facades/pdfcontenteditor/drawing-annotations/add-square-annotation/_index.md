---
title: 정사각형 주석 추가
type: docs
weight: 60
url: /ko/python-net/add-square-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고 첫 페이지에 채워진 파란색 사각형 주석을 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에 정사각형 주석 추가
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에 사각형 주석을 추가하는 방법을 보여줍니다.주석 사각형, 텍스트 내용, 색상, 채우기 옵션을 정의하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

정사각형 주석은 일반적으로 관심 영역을 강조하거나 중요한 부분을 표시하거나 PDF 문서에서 시각적 단서를 제공하는 데 사용됩니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)경계 사각형, 내용 텍스트, 테두리 색상, 채우기 옵션, 페이지 번호 및 테두리 너비를 지정하여 정사각형 (또는 원형) 주석을 만들 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 정사각형 주석을 정의합니다.
1. 정사각형 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
