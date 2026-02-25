---
title: 使用 Python 更改页面大小
linktitle: 更改页面大小
type: docs
weight: 40
url: /zh/python-net/change-page-size/
description: 使用 Aspose.PDF for Python via .NET 库更改 PDF 文档的页面大小。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 更改页面大小
Abstract: 本文演示了如何使用 Aspose.PDF 读取和修改 PDF 页面尺寸。Get Page Size 示例检索特定 PDF 页面的宽度和高度，帮助用户检查页面布局、验证格式或分析文档结构。Set Page Size 示例展示了如何更改页面尺寸，例如将首页转换为 A4 大小，同时在修改前后显示框属性（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）。
---

Aspose.PDF for Python via .NET 让您只需几行代码即可更改 PDF 页面大小。本章节展示如何使用 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 和 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API 更新页面尺寸。

{{% alert color="primary" %}}

请注意，高度和宽度属性使用点（point）作为基本单位，其中 1 英寸 = 72 点，1 厘米 = 1/2.54 英寸 = 0.3937 英寸 = 28.3 点。

{{% /alert %}}

### 将 PDF 页面尺寸设置为 A4

该示例将 PDF 文档的首页尺寸更新为标准 A4 大小。同时在调整前后打印页面的框尺寸（CropBox、TrimBox、ArtBox、BleedBox、MediaBox），以便您验证更改。

以下代码片段展示了如何将 PDF 页面尺寸更改为 A4 大小：

1. 访问 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 的第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 在修改前显示页面的框尺寸（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）。
1. 使用页面 API 应用 A4 尺寸（597.6 × 842.4 点）。
1. 显示更新后的页面框尺寸。
1. 将修改后的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到指定的输出路径。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## 获取 PDF 页面大小

此代码片段读取 PDF 并获取首页的尺寸（宽度和高度）。它使用 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API 提取页面的边界 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/)，并将其大小打印到控制台。这对于检查页面布局、验证格式或为后续处理准备文档非常有用。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 访问第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 使用 `get_page_rect()` 获取页面的边界矩形。
1. 提取宽度和高度值。
1. 打印页面尺寸。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 获取 PDF 页面尺寸（旋转前后）

获取 PDF 页面在应用 90° 旋转前后的尺寸。这演示了旋转如何影响宽度和高度，以及如何在考虑或不考虑旋转的情况下使用 `get_page_rect()`。

1. 将 PDF 打开为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 访问第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 使用 `page.rotate = ap.Rotation.ON90` 应用 90° 旋转（参见 [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 枚举）。
1. 使用 `get_page_rect(False)` 获取未旋转的页面矩形并打印其宽度和高度。
1. 使用 `get_page_rect(True)` 获取考虑旋转的页面矩形并打印其宽度和高度。
1. 比较因旋转导致的尺寸变化。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
