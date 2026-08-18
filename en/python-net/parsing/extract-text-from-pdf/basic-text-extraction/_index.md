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

## Extract Paragraphs by iterating through them

Use [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) when you need paragraph-aware extraction instead of plain page text. Unlike [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) or [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), this API organizes output by page, section, and paragraph, which is useful for text analysis, structured export, and layout-sensitive processing.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create a `ParagraphAbsorber` instance.
1. Call `absorber.visit(document)` to analyze all pages.
1. Iterate through `page_markups`, then through each section and paragraph.
1. Read the text fragments from each paragraph and write the result to a file.

```python
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```