---
title: 删除附件
type: docs
weight: 50
url: /zh/python-net/remove-attachments/
description: 此示例绑定一个输入 PDF，删除所有附件，并将修改后的 PDF 保存为不包含任何嵌入文件的版本。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 中的所有附件
Abstract: 本示例演示了如何使用 Aspose.PDF for Python via the Facades API 从 PDF 文档中删除所有文件附件。它展示了如何绑定 PDF、删除嵌入的附件并保存更新后的文档。
---

PDF 可能包含文档、图像或其他文件等附件。在出于安全、隐私或分发目的需要清除 PDF 中所有附件的场景中。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以以编程方式删除文档中所有嵌入的附件。

1. 创建 PdfContentEditor 对象。 
1. 绑定输入 PDF。
1. 删除所有附件。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
