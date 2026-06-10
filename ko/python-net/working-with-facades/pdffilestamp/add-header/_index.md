---
title: PDF에 머리글 추가
linktitle: PDF에 머리글 추가
type: docs
weight: 20
url: /ko/python-net/add-header/
description: Python에서 PDFFileStamp를 사용하여 PDF 페이지에 텍스트 및 이미지 헤더를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: Python에서 PDF에 텍스트 및 이미지 헤더 추가
Abstract: 이 문서에서는 PDFFileStamp 파사드를 사용하여.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 헤더 콘텐츠를 추가하는 방법을 설명합니다.업데이트된 PDF를 저장하기 전에 텍스트 헤더를 추가하고, 이미지 헤더를 배치하고, 사용자 지정 헤더 여백을 적용하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF 페이지에 반복되는 내용을 추가하기 위한 외관.이를 사용하여 각 페이지 상단에 머리글 텍스트 또는 이미지를 배치하고 머리글 여백을 조정하여 배치를 제어할 수 있습니다.

## 텍스트 헤더 추가

용도 `add_header()` 와 함께 `FormattedText` PDF의 모든 페이지에 동일한 헤더 텍스트를 배치하려는 경우 오브젝트를 선택합니다.두 번째 인수는 머리글의 위쪽 여백을 정의합니다.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 이미지 헤더 추가

용도 `add_header()` 헤더에 로고나 다른 그래픽이 표시되어야 하는 경우 이미지 파일 또는 이미지 스트림을 사용합니다.이는 브랜드 문서 레이아웃에 유용합니다.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 사용자 지정 여백이 있는 헤더 추가

헤더 배치를 더 세밀하게 제어해야 하는 경우 여백 값이 3개인 오버로드를 사용하십시오.이 예에서는 머리글에 사용자 지정 위쪽, 왼쪽 및 오른쪽 여백이 추가됩니다.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
