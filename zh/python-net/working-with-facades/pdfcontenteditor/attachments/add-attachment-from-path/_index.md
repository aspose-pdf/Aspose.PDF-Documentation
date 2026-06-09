---
title: 从路径添加附件
type: docs
weight: 20
url: /zh/python-net/add-attachment-from-path/
description: 此示例绑定一个输入 PDF，使用文件路径附加外部文件，并将带有嵌入附件的修改后 PDF 保存。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用文件路径重载将文件附加到 PDF
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 中的 'add_document_attachment()' 的文件路径重载将外部文件附加到 PDF 文档。它简化了无需手动打开文件流即可添加附件的过程。
---

PDF 可以包含嵌入的文件，例如文档、电子表格或图像，以供参考或分发。'add_document_attachment()' 的文件路径重载允许您直接从文件路径添加附件，消除手动打开文件的需求。

1. 创建 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 绑定输入 PDF。
1. 使用文件路径添加附件。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
