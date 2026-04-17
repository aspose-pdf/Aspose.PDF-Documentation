---
title: Basic Text Extraction using Python
linktitle: Basic Text Extraction
type: docs
weight: 10
url: /python-net/basic-text-extraction/
description: Learn how to extract text from PDF documents using Aspose.PDF for Python — from all pages at once or from a specific page.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract text from all pages of a PDF document

Use [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) to capture all text from every page of a PDF document and write it to a text file. This approach is well suited for converting PDFs to searchable text, running content analysis, or preparing text for indexing and downstream processing.

1. Open the PDF document using [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Create a `TextAbsorber` instance.
1. Call `document.pages.accept(text_absorber)` to scan all pages.
1. Retrieve the extracted text from `text_absorber.text`.
1. Write the result to an output text file.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Extract text from a particular page

Apply [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) to a single page to isolate and save text from that section of a multi-page document. This is useful when you need content from only one page — for example, an invoice, a report section, or a form summary.

1. Open the PDF document using [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Create a `TextAbsorber` instance.
1. Call `accept` on the target page: `document.pages[page_number].accept(text_absorber)`.
1. Retrieve the extracted text and write it to a file.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
