---
title: PdfViewer 类
type: docs
weight: 135
url: /zh/python-net/pdfviewer-class/
description: 了解如何在 Aspose.PDF for Python via .NET 中使用 PdfViewer 类来解码所有 PDF 页面、解码特定页面，并检查与查看器相关的 PDF 元数据。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfViewer 在 Python 中解码 PDF 页面并检查查看器数据
Abstract: 本文说明了如何在 Aspose.PDF for Python via .NET 中使用 PdfViewer 门面进行页面解码和查看器相关的检查任务。了解如何解码所有 PDF 页面、呈现特定页面，以及检查诸如页面计数、坐标类型和分辨率等属性。
---

Aspose.PDF for Python via .NET 提供了 [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) 用于处理 PDF 查看和页面解码场景的外观。一个常见的用例是将 PDF 页面转换为图像对象，然后可以将其保存到磁盘。

## 创建可复用的 PdfViewer 辅助类

在解码页面或读取与查看器相关的属性之前，创建一个小的帮助程序来初始化并返回一个 `PdfViewer` 实例。这使下面的示例保持自包含，并清楚地说明在将查看器对象绑定到 PDF 文档之前，它是如何创建的。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## 解码所有 PDF 页面

使用 `decode_all_pages()` 当您想将 PDF 中的每一页转换为单独的图像时，返回的页面图像随后可以逐个保存到输出目录中。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## 解码特定的 PDF 页面

使用 `decode_page()` 当您只需要文档中的单页时。这在生成预览、缩略图或特定页面的导出时非常有用。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## 检查 PDF 元数据

这 `inspect_pdf_metadata` 函数演示如何使用 Aspose.PDF 打开 PDF 文档并检索基本的与查看器相关的元数据。它侧重于提取描述文档如何被解释和显示的信息，而不是其内容。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
