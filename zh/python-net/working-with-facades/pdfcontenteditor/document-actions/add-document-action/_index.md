---
title: 添加文档操作
type: docs
weight: 20
url: /zh/python-net/add-document-action/
description: 本示例添加了一个在打开 PDF 时出现的 JavaScript 警报。该脚本附加到文档打开事件，并在支持的 PDF 查看器中自动执行。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加文档打开 JavaScript 操作
Abstract: 本示例演示了如何添加一个在打开 PDF 时触发的文档级 JavaScript 操作。使用 Aspose.PDF for Python via the Facades API，示例展示了如何绑定文档、分配打开事件操作并保存更新后的 PDF。
---

文档级操作允许您定义在特定事件发生时自动执行的行为，例如打开 PDF。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以将 JavaScript 代码附加到这些事件。这可用于通知、验证逻辑或交互式工作流。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 添加文档级别操作。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
