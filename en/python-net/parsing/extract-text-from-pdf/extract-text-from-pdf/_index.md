---
title: Extract Text from PDF using Python
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /python-net/extract-text-from-pdf-file/
description: This section contains articles on text extraction from PDF documents using Aspose.PDF in Python.
lastmod: "2025-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Text from PDF via Python
Abstract: The article provides a step-by-step guide on extracting text from PDF documents using two different methods. The first method involves converting the entire content of a PDF into plain text, which is useful for applications like text analysis, search indexing, or data extraction. This process includes loading the PDF, initializing a text absorber, extracting text from all pages, and writing the extracted text to a file. The second method focuses on extracting highlighted text from a PDF, which aids in reviewing key points or summarizing content. This involves identifying and printing text from highlight annotations found on specific pages of the document. Both methods utilize the Aspose.PDF library in Python to accomplish the tasks.
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
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
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

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extract text from a specific region of a page

Extract text from a defined rectangular region on a particular page of a PDF using Aspose.PDF for Python. By specifying coordinates, you can focus extraction on a specific area — such as a table cell, paragraph block, or form field region.

Ideal for zone-based text extraction, such as pulling data from headers, footers, invoices, or fixed-layout reports where text appears in predictable positions.

1. Open the PDF document.
1. Create a 'TextAbsorber'.
1. Configure 'text_search_options' to restrict to the rectangle region.
1. Accept the absorber on the specific page.
1. Write the extracted text.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extract text based on columns

### Reduce font size manually and then extract

Extraction accuracy in multi-column PDFs is achieved by first reducing the font size of all text fragments before extraction. The process helps prevent overlapping text issues that can occur in tightly formatted or multi-column layouts.
It helps for extracting text from complex layouts—such as magazines, academic papers, or brochures—where resizing text improves layout clarity and extraction results.

1. Load the PDF.
1. Reduce font size of existing text fragments, save and reopen document.
1. Use 'TextAbsorber' to extract text from pages.
1. Write out the extracted text.

```python

import io
import aspose.pdf as ap

def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)
    try:
        frag_absorber = ap.text.TextFragmentAbsorber()
        doc.pages.accept(frag_absorber)
        for frag in frag_absorber.text_fragments:
            frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
        # Save to memory stream and reopen (to apply changes)
        ms = io.BytesIO()
        doc.save(ms)
        ms.seek(0)
        doc2 = ap.Document(ms)
        text_absorber = ap.text.TextAbsorber()
        doc2.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```

### Extract text with scale factor

Extract text from PDFs with multi-column layouts by applying a scale factor to the document. Adjusting the scale factor ensures that the text fragments are interpreted correctly, reducing overlap or misalignment during extraction.
It's useful for PDFs with columns, tables, or dense layouts, where scaling helps maintain proper reading order and structure in the extracted text.

1. Load the PDF.
1. Configure 'TextExtractionOptions.ScaleFactor'.
1. Use 'TextAbsorber' to extract text from pages.
1. Write out the extracted text.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```