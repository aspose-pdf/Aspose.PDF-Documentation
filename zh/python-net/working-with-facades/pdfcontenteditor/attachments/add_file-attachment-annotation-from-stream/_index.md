---
title: 从流添加文件附件注释
type: docs
weight: 40
url: /zh/python-net/add-file-attachment-annotation-from-stream/
description: 此示例加载 PDF，读取外部文件到内存流，在第一页添加文件附件注释，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中从流向 PDF 添加文件附件注释
Abstract: 此示例演示如何使用文件流和 Aspose.PDF for Python via the Facades API 在 PDF 中创建文件附件注释。它展示了如何指定注释位置、设置描述、包含不透明度值，并保存修改后的文档。
---

文件附件注释允许将文件嵌入为 PDF 页面内的交互式图标。使用基于流的方法，您可以在不依赖物理文件路径的情况下动态附加文件。此方法还支持自定义注释的外观，包括不透明度。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 将附件文件读取为流。
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


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
