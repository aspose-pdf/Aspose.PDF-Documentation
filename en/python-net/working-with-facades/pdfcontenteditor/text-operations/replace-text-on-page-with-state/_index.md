---
title: Replace Text On Page With State
type: docs
weight: 20
url: /python-net/replace-text-on-page-with-state/
description: In this example, all occurrences of the word "software" on page 1 are replaced with "SOFTWARE PAGE 1", using red text with a font size of 12.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text with Custom Formatting on a Specific Page Using PdfContentEditor in Python
Abstract: This example demonstrates how to replace text on a specific page in a PDF while applying custom formatting using Aspose.PDF for Python via the Facades API. It shows how to control font size and color during text replacement.    
---

Sometimes replacing text in a PDF also requires formatting changes such as color or font size. Using TextState, you can define styling properties and apply them during replacement. This allows you to highlight modified text or enforce consistent formatting across documents.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Define a TextState with custom formatting.
1. Configure the replacement strategy.
1. Replace text on a specific page.
1. Save the updated PDF document.

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
    content_editor.replace_text_strategy.replace_scope = pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```