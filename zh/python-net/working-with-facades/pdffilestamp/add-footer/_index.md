---
title: 向 PDF 添加页脚
type: docs
weight: 10
url: /zh/python-net/add-footer/
description: 学习如何在 Python 中使用 PdfFileStamp 为 PDF 页面添加文本和图像页脚。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 在 Python 中为 PDF 添加文本和图像页脚
Abstract: 本文阐述了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileStamp 外观向 PDF 文档添加页脚内容。它展示了如何添加文本页脚、放置图像页脚，以及在保存更新的 PDF 之前应用自定义页脚边距。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) 用于向 PDF 页面添加重复内容的外观。您可以使用它在每页底部放置页脚文本或图像，并通过调整页脚边距来控制位置。

## 添加文本页脚

使用 `add_footer()` 与 `FormattedText` 对象，当您想在 PDF 的每页上放置相同的文本页脚时使用。第二个参数设置用于页脚放置的底部边距。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 添加图像页脚

使用 `add_footer()` 使用图像流时，当页脚应显示徽标或其他图像而不是文本。示例将图像文件作为二进制流打开，并将其放置在每页的底部。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 添加带自定义边距的页脚

当您需要更精确地控制页脚位置时，使用带有三个边距值的重载。在本例中，页脚使用自定义的底部、左侧和右侧边距进行添加。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
