---
title: 폴리곤 주석 추가
linktitle: 폴리곤 주석 추가
type: docs
weight: 40
url: /ko/python-net/add-polygon-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고 첫 페이지에 단색 다각형을 그린 다음 수정된 문서를 주석과 함께 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 다각형 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 다각형 주석을 추가하는 방법을 보여줍니다.폴리곤 버텍스, 테두리 스타일, 주석 경계, 설명 텍스트를 정의하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

다각형 주석은 PDF에서 불규칙한 영역이나 모양을 강조 표시하여 시각적으로 강조하거나 특정 영역을 표시하는 데 사용됩니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 꼭지점 좌표, 테두리 스타일, 페이지 번호 및 주석 사각형을 지정하여 다각형을 만들 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 폴리곤 프로퍼티를 설정합니다.
1. 폴리곤 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
