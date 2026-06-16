---
title: 替换文本正则
type: docs
weight: 30
url: /zh/python-net/replace-text-regex/
description: 在本示例中，文档中的所有四位数字都被替换为占位符 "[NUMBER]"。这对于遮蔽敏感数据、规范化内容或匿名化文档非常有用。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中通过正则表达式替换文本
Abstract: 本示例演示了如何使用 Aspose.PDF for Python 通过 Facades API 结合正则表达式替换 PDF 中的文本。它展示了如何搜索模式并在整个文档中替换所有匹配项。
---

正则表达式允许基于模式而非固定字符串进行灵活的文本替换。通过在 'replace_text_strategy' 中启用正则支持，您可以匹配诸如数字、日期或格式化字符串等动态内容。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 配置替换策略以使用正则表达式。
1. 在整个文档中替换匹配的模式。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
