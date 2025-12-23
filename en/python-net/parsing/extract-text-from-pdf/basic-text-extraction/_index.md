---
title: Basic Text Extraction using Python
linktitle: Basic Text Extraction
type: docs
weight: 10
url: /python-net/basic-text-extraction/
description: This section contains articles on basic Text extraction from PDF documents using Aspose.PDF in Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract text from all pages of a PDF document

Aspose.PDF for Python teaches you how to extract text from every page of a PDF document. It uses the TextAbsorber class to capture all textual content from the entire document and saves it into a separate text file.
Ideal for converting PDFs into searchable text, performing content analysis, or exporting text for indexing and processing tasks.

1. Load the PDF file.
1. Create a 'TextAbsorber' object.
1. Call 'document.pages.accept(text_absorber)' so it scans all pages.
1. Get the full text via 'text_absorber.text'.
1. Write the result into a text file.

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

Extract text from a single page of a PDF document. By applying the TextAbsorber only to a specified page, you can isolate and save text from a particular section of a multi-page PDF.

Useful when you only need content from one page — for instance, extracting text from an invoice page, report section, or form field summary.

1. Open the PDF.
1. Create a TextAbsorber.
1. Accept only the designated page (pages[page_number]).
1. Extract text and write to file.

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
