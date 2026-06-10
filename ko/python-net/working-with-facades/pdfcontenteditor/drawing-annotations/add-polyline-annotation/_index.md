---
title: 폴리라인 주석 추가
linktitle: 폴리라인 주석 추가
type: docs
weight: 50
url: /ko/python-net/add-polyline-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 첫 페이지에 솔리드 폴리라인을 만들고, 수정된 문서를 주석과 함께 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 폴리라인 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 폴리라인 주석을 추가하는 방법을 보여줍니다.꼭지점, 테두리 스타일, 주석 사각형, 텍스트의 시퀀스를 정의하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

폴리라인 주석을 사용하면 PDF에서 일련의 연결된 선 세그먼트를 강조 표시할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 꼭지점 좌표, 테두리 스타일, 페이지 번호 및 주석 경계를 지정하여 폴리라인을 그릴 수 있습니다.이는 다이어그램과 문서에서 경로, 추세 또는 연결을 시각적으로 표현하는 데 유용합니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 폴리라인 속성을 설정합니다.
1. 폴리라인 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
