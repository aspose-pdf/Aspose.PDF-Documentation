---
title: 在 Python 中向 PDF 添加图像印章
linktitle: PDF 文件中的图像印章
type: docs
weight: 10
url: /zh/python-net/image-stamps-in-pdf-page/
description: 了解如何在 Python 中向 PDF 页面添加图像印章。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中添加图像印章
Abstract: 本文提供了使用 Aspose.PDF library for Python 向 PDF 文件添加图像印章的全面指南。文中详细说明了 `ImageStamp` 类的使用，该类允许自定义基于图像的印章，包括高度、宽度、不透明度和旋转等属性。过程包括创建一个 `Document` 对象和一个具有所需属性的 `ImageStamp` 对象，然后使用 `add_stamp()` 方法将印章添加到 PDF 的特定页面。文章包含了 Python 代码片段，演示如何将图像印章应用于 PDF 并使用 `quality` 属性控制其质量，该属性以百分比形式调整图像质量。此外，文章还解释了如何使用 `FloatingBox` 类将图像印章作为浮动框的背景，并提供了另一个代码示例来展示实现方式。本指南是希望使用 Aspose.PDF 为 PDF 增强图像印章的开发者的有用资源。
---

## 在 PDF 文件中添加图像印章

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类来向 PDF 文件添加图像印章。The [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类提供创建基于图像的印章所需的属性，如高度、宽度、不透明度等。该印章可以定位、调整大小、旋转，并可部分透明，从而实现水印、品牌或注释。

以下代码片段展示了如何在 PDF 文件中添加图像印章。

1. 使用 'ap.Document()' 加载 PDF。
1. 使用 'ImageStamp()' 创建图像印章。
1. 配置印章属性。
1. 将印章添加到目标页面。
1. 保存修改后的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## 添加印章时控制图像质量

在将图像添加为印章对象时，您可以控制图像的质量。该 [质量](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 属性的 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类用于此目的。它以百分比表示图像的质量（有效值为 0..100）。
通过设置 quality 属性，您可以降低图像分辨率以优化 PDF 大小，或保持更高的保真度以获得更清晰的效果。

1. 打开 PDF 文档。
1. 创建图像印章。
1. 设置图像质量。
1. 将印章添加到目标页面。
1. 保存修改后的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## 图像印章作为浮动框的背景

创建一个 [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 在 PDF 中应用图像作为其背景。它还展示了如何添加文本、设置边框、背景颜色，以及在页面上精确定位该框。此功能对于创建视觉丰富的 PDF 内容非常有用，例如带有图像上文字的标注、横幅或高亮区域。

1. 打开或创建 PDF 文档。
1. 创建一个 'FloatingBox' 对象。
1. 向框中添加文本内容。
1. 设置框的边框和背景颜色。
1. 添加背景图像。
1. 将 FloatingBox 添加到页面。
1. 保存 PDF 文档。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```

## 相关的盖章主题

- [在 Python 中对 PDF 页面加盖印章](/pdf/zh/python-net/stamping/)
- [使用 Python 向 PDF 添加页面印章](/pdf/zh/python-net/page-stamps-in-the-pdf-file/)
- [在 Python 中向 PDF 添加文本印章](/pdf/zh/python-net/text-stamps-in-the-pdf-file/)
- [在 Python 中为 PDF 添加页码](/pdf/zh/python-net/add-page-number/)