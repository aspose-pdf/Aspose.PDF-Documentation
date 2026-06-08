---
title: 在 Python 中创建 PDF 文件
linktitle: 创建 PDF 文档
type: docs
weight: 10
url: /zh/python-net/create-pdf-document/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中创建 PDF 文件并构建可搜索的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 创建 PDF 文件
Abstract: Aspose.PDF for Python via .NET 是一个多功能 API，专为开发人员在针对 .NET 框架的 Python 应用程序中操作 PDF 文件而设计。它使用户能够轻松创建、加载、修改和转换 PDF 文档。本文提供了使用 Aspose.PDF 创建简单 PDF 文件的循序指导。该过程包括初始化一个 `Document` 对象、向文档添加 `Page`、在页面的段落中插入 `TextFragment`，并将文件保存为 PDF。文中附带的 Python 代码片段演示了这些步骤，创建了一个包含文本 “Hello World!” 的 PDF 文档。该 API 通过极少的代码简化了 PDF 处理，提高了在 .NET 环境下进行 PDF 开发的生产力。
---

**Aspose.PDF for Python via .NET** 是一个 PDF 操作 API，允许开发人员仅用几行代码即可直接从 Python 为 .NET 应用程序创建、加载、修改和转换 PDF 文件。

当您需要从头生成新的 PDF 文件或将 OCR 输出转换为可搜索的 PDF 文档时，请使用这些示例。

## 如何创建简单的 PDF 文件

要使用 Python via .NET 与 Aspose.PDF 创建 PDF，您可以按照以下步骤操作：

1. 创建一个对象 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类
1. 添加一个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象到 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Document 对象的集合
1. 添加 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 到 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 页面集合
1. 保存生成的 PDF 文档

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## 如何创建可搜索的 PDF 文档

Aspose.PDF for Python via .NET 允许创建和操作现有的 PDF 文档。向 PDF 文件添加 Text 元素时，生成的 PDF 是可搜索的。然而，将包含文本的图像转换为 PDF 文件时，生成的 PDF 内容不可搜索。作为变通方法，我们可以对生成的文件应用 OCR，以使其可搜索。

以下是完成此需求的完整代码：

1. 使用 'ap.Document' 加载 PDF。
1. 配置渲染分辨率。
1. 使用 'PngDevice.process' 将选定的 PDF 页面转换为图像。
1. 对生成的图像运行 OCR。
1. 从 OCR 输出创建一个新 PDF。
1. 保存可搜索的 PDF。

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## 相关文档主题

- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中格式化 PDF 文档](/pdf/zh/python-net/formatting-pdf-document/)
- [在 Python 中操作 PDF 文档](/pdf/zh/python-net/manipulate-pdf-document/)
- [在 Python 中优化 PDF 文件](/pdf/zh/python-net/optimize-pdf/)

