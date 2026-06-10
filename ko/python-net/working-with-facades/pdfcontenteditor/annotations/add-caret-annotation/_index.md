---
title: 캐럿 주석 추가
linktitle: 캐럿 주석 추가
type: docs
weight: 10
url: /ko/python-net/add-caret-annotation/
description: 이 예제에서는 기존 PDF를 로드하고 첫 페이지에 캐럿 주석을 추가하고 수정된 문서를 저장합니다.주석에는 빨간색 캐럿 기호와 설명이 포함된 주석 텍스트가 포함되어 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 캐럿 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 캐럿 주석을 추가하는 방법을 보여줍니다.이 샘플은 PDF 파일을 바인딩하고, 사각형을 사용하여 주석 배치를 정의하고, 캐럿 속성을 구성하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

캐럿 주석은 일반적으로 문서의 텍스트 삽입이나 편집 설명을 나타내는 데 사용됩니다.PDFContentEditor를 사용하면 페이지 번호, 주석 경계, 콜아웃 영역, 기호, 메모 텍스트 및 색상을 지정하여 프로그래밍 방식으로 캐럿 주석을 추가할 수 있습니다.

1. 생성하기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. 입력 PDF를 바인딩합니다.
1. 캐럿 주석 매개변수 정의:
  - 주석이 추가될 페이지 번호
  - 캐럿 사각형 (주석 위치)
  - 콜아웃 사각형 (텍스트 영역)
  - 기호 (예: “P”)
  - 주석 텍스트
  - 주석 색상
1. 캐럿 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
