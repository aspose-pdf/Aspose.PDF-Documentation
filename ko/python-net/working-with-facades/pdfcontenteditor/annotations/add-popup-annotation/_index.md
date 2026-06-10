---
title: 팝업 주석 추가
type: docs
weight: 40
url: /ko/python-net/add-popup-annotation/
description: 이 예제에서는 PDF를 로드하고, 첫 페이지에 팝업 주석을 추가하고, 수정된 문서를 저장합니다.팝업은 기본적으로 표시되도록 설정되어 있으며 지정된 주석 텍스트를 표시합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 팝업 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 팝업 주석을 삽입하는 방법을 보여줍니다.팝업 영역을 정의하고, 주석 텍스트를 설정하고, 가시성을 제어하고, 업데이트된 문서를 저장하는 방법을 설명합니다.
---

팝업 주석은 PDF 파일에 주석, 설명 또는 대화형 메모를 추가하는 데 유용합니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)위치, 내용, 가시성 및 페이지 번호를 지정하여 프로그래밍 방식으로 팝업 주석을 만들 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 팝업 주석 사각형을 정의합니다.
1. 팝업 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
