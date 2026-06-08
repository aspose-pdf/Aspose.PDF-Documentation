---
title: 从 PDF 中删除所有图像
type: docs
weight: 10
url: /zh/python-net/delete-all-images/
description: 使用 Aspose.PDF for Python 通过 Facades API 删除 PDF 文档中的所有图像。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 PdfContentEditor 从 PDF 中删除所有图像
Abstract: 本示例演示如何使用 Aspose.PDF for Python 通过 Facades API 删除 PDF 文档中的所有图像。它展示了如何绑定 PDF、删除所有嵌入的图像，并保存更新后的文档。
---

PDF 文档通常包含用于插图、品牌或装饰的图像。可能会出现需要从 PDF 中删除所有图像的情况，例如降低文件大小、保护敏感视觉内容或准备仅文本版本。

使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以通过编程方式从 PDF 中删除所有图像，确保文档仅包含文本内容。此示例绑定一个输入 PDF，删除所有图像，并保存修改后的文件。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 删除所有图像。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
