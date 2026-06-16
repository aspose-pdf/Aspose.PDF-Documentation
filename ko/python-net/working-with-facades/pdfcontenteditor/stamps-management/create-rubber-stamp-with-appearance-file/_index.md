---
title: 모양 파일로 러버 스탬프 만들기
linktitle: 모양 파일로 러버 스탬프 만들기
type: docs
weight: 20
url: /ko/python-net/create-rubber-stamp-with-appearance-file/
description: 이 예제에서는 입력 PDF를 바인딩하고, 이미지 파일을 스탬프 모양으로 사용하여 1페이지에 러버 스탬프를 만들고, 업데이트된 PDF를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFContentEditor를 사용하여 PDF에 사용자 지정 모양의 러버 스탬프 만들기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 사용자 지정 모양 (이미지) 이 있는 러버 스탬프 주석을 추가하는 방법을 보여줍니다.사용자 지정 스탬프를 사용하면 로고, 서명 또는 브랜드 이미지를 스탬프의 일부로 포함할 수 있습니다.
---

러버 스탬프 주석은 텍스트뿐만 아니라 이미지 파일을 모양으로 사용하여 사용자 정의할 수 있습니다.이 방법은 회사 로고, 서명 스탬프 또는 기타 시각적 지표를 PDF 페이지에 추가할 때 유용합니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 스탬프의 직사각형을 정의합니다.
1. 사용자 지정 이미지 파일을 사용하여 러버 스탬프의 모양을 정의합니다.
1. 스탬프의 텍스트와 색상을 설정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```
