---
title: 커브 주석 추가
type: docs
weight: 20
url: /ko/python-net/add-curve-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고 첫 페이지에 대시 곡선을 그린 다음 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에 곡선 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 곡선 주석을 추가하는 방법을 보여줍니다.곡선 꼭지점, 테두리 스타일, 주석 경계, 텍스트 내용을 정의하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

곡선 주석은 PDF에서 불규칙한 경로나 모양을 강조하여 시각적으로 강조하거나 중요한 영역을 표시하는 데 사용됩니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 일련의 꼭지점, 경계 스타일, 가시성, 주석 사각형 및 설명 텍스트를 지정하여 곡선을 그릴 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 커브 프로퍼티를 설정합니다.
1. 커브 주석을 그립니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
