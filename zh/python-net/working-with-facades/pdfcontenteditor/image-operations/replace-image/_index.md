---
title: 在 PDF 中替换图像
type: docs
weight: 30
url: /zh/python-net/replace-image/
description: 此示例绑定一个输入 PDF，将第 1 页上的第一张图像替换为新图像，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中替换 PDF 中的图像
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 替换 PDF 文档中已有的图像。它展示了如何定位页面上的特定图像并将其替换为新图像，然后保存更新后的 PDF。
---

PDF 通常包含可能需要更新或替换的图像，例如徽标、图表或照片。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以通过提供页码、图像索引和新图像文件路径来替换给定页面上的特定图像。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 替换给定页面上的特定图像。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
