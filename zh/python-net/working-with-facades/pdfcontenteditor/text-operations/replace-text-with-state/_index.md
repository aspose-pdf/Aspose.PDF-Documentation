---
title: 使用状态替换文本
type: docs
weight: 50
url: /zh/python-net/replace-text-with-state/
description: 在此示例中，所有出现的 “software” 都被替换为 “SOFTWARE”，并使用蓝色、14号字体进行格式化。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 PDF 中使用 PdfContentEditor（Python）进行自定义格式的文本替换
Abstract: 本示例演示了如何在 PDF 文档中替换文本，同时使用 Aspose.PDF for Python via the Facades API 应用自定义格式。它展示了如何在替换过程中控制文本颜色和字体大小。
---

在 PDF 中更新文本时，您可能希望替换的内容突出显示。通过使用 TextState 对象，您可以定义颜色、字体大小等样式，然后将其应用于所有被替换的文本。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  实例。
1. 绑定输入的 PDF 文档。
1. 定义具有自定义格式的 TextState。
1. 配置替换范围。
1. 替换整个文档中的文本。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
