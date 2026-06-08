---
title: Stamp 类
type: docs
weight: 150
url: /zh/python-net/stamp-class/
description: 了解如何使用 Stamp 类在 Python 中向 PDF 文档添加图像、PDF 和基于文本的印章。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET 提供了 [印章](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) 用于在 PDF 页面上放置可重复使用的可视内容的类。Stamp 可以基于文字、图像，甚至来自其他 PDF 的页面，并且可以定位、旋转、设置样式，并限制在特定页面上。

本文演示了几种常见的印章工作流：

1. 为基于文本的印章创建可重复使用的文本资源。
1. 添加图像和 PDF 页面印章。
1. 添加样式化文本印章。
1. 将印章限制在所选页面。
1. 配置背景图像印章。

该示例使用两个辅助函数：一个用于创建基于文本的印章的格式化文本，另一个用于创建 `TextState` 用于设置文本印章样式的对象。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## 添加图像印章

使用 `bind_image()` 当印章应显示图像（例如徽标、徽章或图标）时。绑定图像后，您可以在将其添加到文档之前设置印章 ID 和原点。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 将 PDF 页面添加为印章

使用 `bind_pdf()` 当您想要使用另一个 PDF 文件中的页面作为印章内容时。这对于覆盖层（例如批准、模板或存储在单独文档中的预构建视觉元素）非常有用。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 添加带文本状态的文字印章

使用 `bind_logo()` 以及 `bind_text_state()` 当您想要创建具有自定义字体样式的基于文本的印章时。此方法适用于审批标记、标签以及工作流特定的注释。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 在特定页面添加印章

如果印章不应出现在每一页上，请将目标页码分配给 `pages` 属性。此示例仅在首页添加图像印章。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 添加背景图像印章

当图像应显示在页面内容后面时，使用背景印章。您还可以控制印章的不透明度、旋转、质量、大小和位置，以创建水印样式的效果。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 相关外观主题

- [在 Python 中使用 PDF Facade](/pdf/zh/python-net/working-with-facades/)
- [使用 PdfFileStamp 添加页眉、页脚和印章](/pdf/zh/python-net/pdffilestamp-class/)
- [在 Python 中为 PDF 文件添加页面印章](/pdf/zh/python-net/add-stamp/)
