---
title: 在页面上使用状态替换文本
type: docs
weight: 20
url: /zh/python-net/replace-text-on-page-with-state/
description: 在本示例中，页面 1 上所有出现的单词 “software” 都被替换为 “SOFTWARE PAGE 1”，使用红色文本，字体大小为 12。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中对特定页面进行自定义格式的文本替换
Abstract: 本示例演示了如何在 PDF 的特定页面上进行文本替换，同时使用 Aspose.PDF for Python via the Facades API 应用自定义格式。它展示了如何在文本替换过程中控制字体大小和颜色。
---

有时在 PDF 中替换文本还需要进行格式更改，如颜色或字体大小。使用 TextState，您可以定义样式属性并在替换时应用它们。这使您能够突出显示已修改的文本或在文档间强制一致的格式。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 定义具有自定义格式的 TextState。
1. 配置替换策略。
1. 在特定页面上替换文本。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
