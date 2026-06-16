---
title: 添加附件
type: docs
weight: 10
url: /zh/python-net/add-attachment/
description: 此示例绑定一个输入 PDF，将外部文件附加到第一页，并将带有嵌入附件的修改后 PDF 保存。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加文件附件
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 将外部文件附加到 PDF 文档。它展示了如何绑定 PDF、添加带有描述的附件以及保存更新后的文档。
---

PDF 中的文件附件允许您直接在 PDF 中包含补充的文档、图像或其他资源。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以以编程方式将文件附加到特定页面，设置附件名称并提供描述。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 打开附件文件。
1. 将附件添加到 PDF 中。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
