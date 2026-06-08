---
title: 添加文件附件注释
type: docs
weight: 30
url: /zh/python-net/add-file-attachment-annotation/
description: 此示例绑定一个输入 PDF，使用文件路径在首页添加文件附件注释，并保存已更新的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加文件附件注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 通过文件路径在 PDF 中创建文件附件注释。它展示了如何定义注释位置、设置描述文本、选择图标类型以及保存修改后的文档。
---

文件附件注释允许您将外部文件嵌入为 PDF 页面上的交互式图标。使用文件路径重载，您可以直接从磁盘附加文件，而无需手动打开流。此方法还允许您自定义注释图标并为用户提供描述。

1. 创建 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 绑定输入 PDF。
1. 定义注释矩形。
1. 添加文件附件注释。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
