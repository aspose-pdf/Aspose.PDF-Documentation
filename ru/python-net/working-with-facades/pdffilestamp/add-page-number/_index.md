---
title: Добавить номер страницы в PDF
type: docs
weight: 30
url: /python-net/page-number/
description: Узнайте, как добавить номера страниц в PDF-документы с помощью PdfFileStamp в Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Добавить номера страниц в PDF на Python
Abstract: В этой статье объясняется, как добавить номера страниц в PDF-документы с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileStamp. Показано, как добавить номера страниц с расположением по умолчанию, разместить их в пользовательских координатах и управлять выравниванием и полями.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Facade для добавления повторяющегося контента на страницы PDF. Вы можете использовать её для вставки номеров страниц с размещением по умолчанию, позиционирования их в определённых координатах или управления их выравниванием и отступами.

## Добавить номера страниц с размещением по умолчанию

Используйте `add_page_number()` без дополнительных аргументов позиции, когда вы хотите, чтобы номера страниц добавлялись в месте по умолчанию. Это самый простой способ пронумеровать каждую страницу в документе.

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

## Добавить номера страниц в пользовательских координатах

Используйте перегрузку на основе координат, когда вам нужно, чтобы номера страниц отображались в конкретных позициях X и Y на каждой странице. Такой подход полезен, когда макет документа требует пользовательского размещения.

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

## Добавьте номера страниц с выравниванием и полями

Используйте перегрузку с аргументами позиции и полей, когда вам нужен более точный контроль над тем, где отображаются номера страниц. В этом примере номера выровнены по верхнему правому углу страницы с явно заданными полями.

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

## Добавить нумерацию страниц в римском стиле

Функция 'add_page_numbers_with_roman_style' демонстрирует, как улучшить PDF‑документ, добавив нумерацию страниц с использованием заглавных римских цифр. Она использует класс PdfFileStamp из Aspose.PDF для применения последовательной нумерации на всех страницах.

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
