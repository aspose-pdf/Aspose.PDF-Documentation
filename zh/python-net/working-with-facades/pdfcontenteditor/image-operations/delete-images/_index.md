---
title: 从 PDF 中删除图像
type: docs
weight: 20
url: /zh/python-net/delete-images/
description:
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中删除 PDF 页面上的特定图像
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 从 PDF 文档中删除特定图像。它展示了如何针对特定页面上的图像并保存更新后的文档。
---

有时，您可能只想从 PDF 中删除某些图像，而不是清除所有视觉元素。使用 With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定页码和图像索引来删除选定的图像。

此代码片段绑定一个输入 PDF，删除第 1 页上的第二个图像，并保存修改后的 PDF，保持其他图像不变。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 从指定页面删除特定图像。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
