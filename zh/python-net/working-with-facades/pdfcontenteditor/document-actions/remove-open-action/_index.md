---
title: 删除打开操作
type: docs
weight: 30
url: /zh/python-net/remove-open-action/
description: 此示例加载现有 PDF，删除打开操作，并保存已清理的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 中删除文档打开操作
Abstract: 此示例演示如何使用 Aspose.PDF for Python 通过 Facades API 从 PDF 中删除文档打开操作。它展示了如何绑定 PDF，清除打开操作，并保存更新后的文档。
---

PDF 文档可能包含在打开文件时自动执行的操作，例如 JavaScript 警报、导航命令或其他行为。在某些情况下，可能需要出于安全、合规或用户体验的原因删除这些操作。

使用 PdfContentEditor，您可以轻松删除文档打开操作，并确保 PDF 打开时不执行任何自动行为。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 删除文档打开操作。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
