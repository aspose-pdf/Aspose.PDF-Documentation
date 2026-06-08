---
title: 在 Python 中更改 PDF 页面大小
linktitle: 更改页面大小
type: docs
weight: 40
url: /zh/python-net/change-page-size/
description: 了解如何在 Python 中读取和更改 PDF 页面的尺寸。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 更改页面大小
Abstract: 本文展示了如何使用 Aspose.PDF 读取和修改 PDF 页面尺寸。Get Page Size 示例检索特定 PDF 页面的宽度和高度，使用户能够检查页面布局、验证格式或分析文档结构。Set Page Size 示例说明如何更改页面的尺寸——例如将首页转换为 A4 大小——同时在修改前后显示框属性（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）。
---

Aspose.PDF for Python via .NET 让您只需几行代码即可更改 PDF 页面尺寸。本主题展示了如何使用 the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 和 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API。

当您需要在 Python 中调整现有 PDF 页面大小、统一文档尺寸或检查页面框设置时，请使用本指南。

{{% alert color="primary" %}}

请注意，高度和宽度属性使用点（points）作为基本单位，其中 1 英寸 = 72 点，1 厘米 = 1/2.54 英寸 = 0.3937 英寸 = 28.3 点。

{{% /alert %}}

## 将 PDF 页面 的页面大小设置为 A4

此示例将 PDF 文档中第一页的尺寸更新为标准的 A4 大小。它还在调整大小前后打印页面的盒子尺寸（CropBox、TrimBox、ArtBox、BleedBox、MediaBox），以便您验证更改。

以下代码片段展示了如何将 PDF 页面尺寸更改为 A4 大小：

1. 访问第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 在修改之前显示页面的框大小（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）。
1. 使用页面 API 应用 A4 尺寸（597.6 × 842.4 点）。
1. 显示已更新的页面框尺寸。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到指定的输出路径。

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

此代码段读取 PDF 并获取第一页的尺寸（宽度和高度）。它使用 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API 提取页面的边界 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 并将其大小打印到控制台。这对于检查页面布局、验证格式或为进一步处理准备文档非常有用。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 访问第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 使用检索页面的边界矩形 `get_page_rect()`.
1. 提取宽度和高度值。
1. 打印页面尺寸。

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 获取 PDF 页面大小（旋转前后）

检索 PDF 页面在应用 90° 旋转前后的尺寸。这演示了旋转如何影响宽度和高度以及如何使用 `get_page_rect()` 考虑或不考虑旋转。

1. 将 PDF 打开为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 访问第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 使用 90° 旋转 `page.rotate = ap.Rotation.ON90` （请参见 [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 枚举).
1. 在不旋转的情况下检索页面矩形 `get_page_rect(False)` 并打印其宽度和高度。
1. 检索考虑旋转的页面矩形 `get_page_rect(True)` 并打印其宽度和高度。
1. 比较由于旋转导致的尺寸变化。

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中裁剪 PDF 页面](/pdf/zh/python-net/crop-pages/)
- [在 Python 中获取和设置 PDF 页面属性](/pdf/zh/python-net/get-and-set-page-properties/)
- [在 Python 中旋转 PDF 页面](/pdf/zh/python-net/rotate-pages/)