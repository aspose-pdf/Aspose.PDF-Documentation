---
title: Replace Text Regex
type: docs
weight: 30
url: /python-net/replace-text-regex/
description: In this example, all four-digit numbers in the document are replaced with the placeholder "[NUMBER]". This is useful for masking sensitive data, normalizing content, or anonymizing documents.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text Using Regular Expressions with PdfContentEditor in Python
Abstract: This example demonstrates how to replace text in a PDF using regular expressions with Aspose.PDF for Python via the Facades API. It shows how to search for patterns and replace all matches across the document.    
---

Regular expressions allow flexible text replacement based on patterns instead of fixed strings. By enabling regex support in 'replace_text_strategy', you can match dynamic content such as numbers, dates, or formatted strings.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Configure replacement strategy to use regex.
1. Replace matching patterns across the entire document.
1. Save the updated PDF document.

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
