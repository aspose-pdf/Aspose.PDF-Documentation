---
title: 在 PDF 中添加页码
type: docs
weight: 30
url: /zh/python-net/page-number/
description: 了解如何在 Python 中使用 PdfFileStamp 为 PDF 文档添加页码。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 在 Python 中为 PDF 添加页码
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileStamp 外观向 PDF 文档添加页码。它展示了如何使用默认位置添加页码、在自定义坐标处定位页码，以及如何控制对齐方式和边距。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) 用于向 PDF 页面添加重复内容的外观。您可以使用它插入默认位置的页码、在特定坐标处定位页码，或控制其对齐方式和边距。

## 使用默认位置添加页码

使用 `add_page_number()` 在不使用额外位置参数的情况下，当您希望页码添加在默认位置时。这是为文档中每一页编号的最简方法。

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

## 在自定义坐标处添加页码

当您需要页码出现在每页的特定 X 和 Y 位置时，请使用基于坐标的重载。当文档布局需要自定义放置时，这种方法非常有用。

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

## 添加带对齐和边距的页码

当您需要更细致地控制页码显示位置时，请使用带有位置和边距参数的重载。在本例中，页码对齐到页面的右上区域，并使用了明确的边距。

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

## 添加带罗马数字样式的页码

‘add_page_numbers_with_roman_style’ 函数演示了如何通过使用大写罗马数字添加页码来增强 PDF 文档。它利用 Aspose.PDF 中的 PdfFileStamp 类在所有页面上应用一致的编号。

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
