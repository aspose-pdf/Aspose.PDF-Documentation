---
title: Region-Based Extraction using Python
linktitle: Region-Based Extraction
type: docs
weight: 20
url: /python-net/region-based-extraction/
description: This section contains articles on region-based extraction from PDF documents using Aspose.PDF in Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

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

## Extract Paragraphs by iterating through them

We can get text from a PDF document by searching a particular text (using "plain text" or "regular expressions") from a single page or whole document, or we can get the complete text of a single page, range of pages or complete document. However, in some cases, you require to extract paragraphs from a PDF document or text in the form of Paragraphs. We have implemented functionality for searching sections and paragraphs in the text of PDF document pages. We have introduced ParagraphAbsorber Class (like TextFragmentAbsorber and TextAbsorber), which can be used to extract paragraphs from PDF documents.

Aspose.PDF library allows you to read a PDF file and extract all paragraph text from each page using 'ParagraphAbsorber'. It organizes the output by page, section, and paragraph, and writes the extracted content into a plain text file. This is useful for text analysis, archiving, or converting structured PDF content into readable formats.

1. Open the PDF document.
1. Instantiate a 'ParagraphAbsorber'.
1. Call 'absorber.visit(document)' to scan all pages for paragraphs.
1. Loop through the absorber’s 'page_markups' collection.
1. For each page‑markup, loop through its 'sections', then each 'paragraph' in the section.
1. Within each paragraph, loop through 'lines', then each 'fragment' in the line, accumulating 'fragment.text'.
1. Write each paragraph (with page/section/paragraph indexes) to the output file.
1. Close the document when done.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf-8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extract Paragraphs with bounding polygon rendering

This code snippet extracts paragraph-level text and layout information from a specific page in a PDF. It captures each paragraph’s bounding rectangle and polygon coordinates, along with the actual text content, and writes the results to a text file. This is useful for analyzing document structure, layout mapping, or preparing data for accessibility and content extraction tasks.

1. Open the PDF and load the document.
1. Instantiate 'ParagraphAbsorber'.
1. Call 'absorber.visit(page)' for the specific page you want.
1. Get the first 'page_markup' from 'absorber.page_markups'.
1. For each section in that markup:
    - Retrieve its 'rectangle'.
1. For each paragraph in the section:
    - Get its 'points' (polygon).
    - Extract text by looping 'paragraph.lines' - 'fragment.text'.
1. Write geometry and text info to the output file.
1. Close the document.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf-8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```
