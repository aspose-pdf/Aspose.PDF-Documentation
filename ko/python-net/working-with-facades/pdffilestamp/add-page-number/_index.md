---
title: PDF에 페이지 번호 추가
linktitle: PDF에 페이지 번호 추가
type: docs
weight: 30
url: /ko/python-net/page-number/
description: Python에서 PDFFileStamp를 사용하여 PDF 문서에 페이지 번호를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF에 페이지 번호 추가
Abstract: 이 문서에서는 PDFFileStamp 파사드를 사용하여.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 페이지 번호를 추가하는 방법을 설명합니다.기본 배치를 사용하여 페이지 번호를 추가하고, 사용자 지정 좌표에 배치하고, 정렬과 여백을 제어하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF 페이지에 반복되는 내용을 추가하기 위한 외관.이를 사용하여 기본 배치로 페이지 번호를 삽입하거나, 특정 좌표에 배치하거나, 페이지 정렬 및 여백을 제어할 수 있습니다.

## 기본 배치를 사용하여 페이지 번호 추가

용도 `add_page_number()` 기본 위치에 페이지 번호를 추가하려는 경우 추가 위치 인수를 사용하지 마십시오.문서의 모든 페이지에 번호를 매기는 가장 간단한 방법입니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 사용자 지정 좌표에 페이지 번호 추가

각 페이지의 특정 X 및 Y 위치에 페이지 번호를 표시해야 하는 경우 좌표 기반 오버로드를 사용하십시오.이 방법은 문서 레이아웃에 사용자 지정 배치가 필요할 때 유용합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 정렬 및 여백이 있는 페이지 번호 추가

페이지 번호가 표시되는 위치를 더 세밀하게 제어해야 하는 경우 위치 및 여백 인수와 함께 오버로드를 사용하십시오.이 예제에서는 숫자가 페이지의 오른쪽 상단 영역에 맞게 정렬되어 여백이 명시되어 있습니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 로마자 스타일로 페이지 번호 추가

'add_page_numbers_with_roman_style' 함수는 대문자 로마 숫자를 사용하여 페이지 번호를 추가하여 PDF 문서를 향상시키는 방법을 보여줍니다.Aspose.PDF 의 PDFFileStamp 클래스를 활용하여 모든 페이지에 일관된 번호 지정을 적용합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
