---
title: 在页面上替换文本
type: docs
weight: 10
url: /zh/python-net/replace-text-on-page/
description: 在本例中，单词 "PDF" 的第一次出现被替换为 "Page 1 Replaced Text"，使用了指定的字体大小。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中替换特定页面上的文本
Abstract: 本例演示了如何使用 Aspose.PDF for Python 通过 Facades API 在 PDF 文档中替换文本。它展示了如何替换页面上文本的第一次出现并保存更新后的文档。
---

在更新 PDF 文档时，文本替换是一个常见需求。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以搜索特定文本并将其替换为新内容。‘replace_text_strategy’ 属性允许您控制要替换的出现次数。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 配置文本替换策略。
1. 替换目标文本。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
