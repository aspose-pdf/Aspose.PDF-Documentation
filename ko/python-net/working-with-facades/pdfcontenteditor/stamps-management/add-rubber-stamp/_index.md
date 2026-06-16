---
title: 러버 스탬프 추가
linktitle: 러버 스탬프 추가
type: docs
weight: 10
url: /ko/python-net/add-rubber-stamp/
description: 이 예제에서는 입력 PDF를 바인딩하고 처음 네 페이지에 녹색 “승인됨” 고무 스탬프를 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 러버 스탬프 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 러버 스탬프 주석을 추가하는 방법을 보여줍니다.러버 스탬프를 사용하면 승인, 리뷰 또는 사용자 지정 레이블이 있는 페이지를 시각적으로 표시할 수 있습니다.
---

러버 스탬프 주석은 일반적으로 PDF에서 승인, 검토 상태 또는 기타 메모를 나타내는 데 사용됩니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)스탬프의 사각형을 정의하고, 스탬프의 텍스트와 주석을 설정하고, 색상을 선택하고, 문서의 여러 페이지에 적용할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 1~4페이지를 반복해서 살펴보세요.
1. 사용자 지정 텍스트, 설명 및 색상이 포함된 러버 스탬프 주석을 추가합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
