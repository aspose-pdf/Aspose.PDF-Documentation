---
title: 向 PDF 添加页眉
type: docs
weight: 20
url: /zh/python-net/add-header/
description: 了解如何使用 PdfFileStamp 在 Python 中为 PDF 页面添加文字和图像页眉。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 在 Python 中为 PDF 添加文字和图像页眉
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileStamp facade 向 PDF 文档添加页眉内容。它展示了如何添加文字页眉、放置图像页眉以及在保存更新的 PDF 之前应用自定义页眉边距。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) 用于向 PDF 页面添加重复内容的 facade。您可以使用它在每页顶部放置文字或图像页眉，并调整页眉边距以控制位置。

## 添加文本标题

使用 `add_header()` 与 `FormattedText` 对象，当您想在 PDF 的每一页上放置相同的页眉文本时使用。第二个参数定义页眉的上边距。

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

## 添加图片标题

使用 `add_header()` 使用图像文件或图像流，当页眉需要显示徽标或其他图形时。这对于品牌化文档布局非常有用。

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

## 添加带自定义边距的页眉

当您需要更精细地控制标题位置时，请使用包含三个边距值的重载。在本示例中，标题使用自定义的上、左、右边距添加。

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
