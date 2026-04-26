---
title: Replace Text With State
type: docs
weight: 50
url: /python-net/replace-text-with-state/
description: In this example, all occurrences of "software" are replaced with "SOFTWARE" and formatted in blue with a font size of 14.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text with Custom Formatting in a PDF Using PdfContentEditor in Python 
Abstract: This example demonstrates how to replace text in a PDF document while applying custom formatting using Aspose.PDF for Python via the Facades API. It shows how to control text color and font size during replacement.
---

When updating text in a PDF, you may want the replacement content to stand out. By using a TextState object, you can define styling such as color and font size, then apply it to all replaced text.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  instance.
1. Bind the input PDF document.
1. Define a TextState with custom formatting.
1. Configure replacement scope.
1. Replace text across the entire document.
1. Save the updated PDF document.

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
