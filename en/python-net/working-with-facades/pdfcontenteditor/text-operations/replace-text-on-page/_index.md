---
title: Replace Text On Page
type: docs
weight: 10
url: /python-net/replace-text-on-page/
description: In this example, the first occurrence of the word "PDF" is replaced with "Page 1 Replaced Text" using a specified font size.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text on a Specific Page Using PdfContentEditor in Python
Abstract: This example demonstrates how to replace text in a PDF document using Aspose.PDF for Python via the Facades API. It shows how to replace the first occurrence of text on a page and save the updated document.   
---

Text replacement is a common requirement when updating PDF documents. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can search for specific text and replace it with new content. The 'replace_text_strategy' property allows you to control how many occurrences are replaced.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Configure text replacement strategy.
1. Replace the target text.
1. Save the updated PDF document.

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
