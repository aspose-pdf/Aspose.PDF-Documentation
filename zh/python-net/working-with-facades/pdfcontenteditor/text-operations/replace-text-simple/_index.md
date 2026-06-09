---
title: 简单替换文本
type: docs
weight: 40
url: /zh/python-net/replace-text-simple/
description: 在此示例中，文档中所有出现的“23”均被替换为“XXXIII ”。这演示了不使用自定义格式或正则表达式的直接字符串替换。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中跨 PDF 替换文本
Abstract: 此示例演示了如何使用 Aspose.PDF for Python via the Facades API 在整个 PDF 文档中替换文本。它会将指定字符串的所有出现替换为新文本。
---

在文档中更新重复值时，简单的文本替换非常有用。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以定义替换范围，并在所有页面上全局替换文本。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 为所有出现配置替换范围。
1. 替换目标文本。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
