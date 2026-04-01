---
title: Replace Text Simple
type: docs
weight: 40
url: /python-net/replace-text-simple/
description: In this example, all occurrences of "33" are replaced with "XXXIII " in the entire document. This demonstrates straightforward string replacement without custom formatting or regex.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text Across a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to replace text throughout an entire PDF document using Aspose.PDF for Python via the Facades API. It replaces all occurrences of a specified string with new text.    
---

Simple text replacement is useful when updating repeated values in a document. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a replacement scope and substitute text globally across all pages.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Configure replacement scope for all occurrences.
1. Replace the target text.
1. Save the updated PDF document.

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
    content_editor.replace_text_strategy.replace_scope = pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```