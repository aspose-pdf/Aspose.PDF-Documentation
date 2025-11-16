---
title: Extracting Pages programmatically Python
linktitle: Extracting PDF Pages
type: docs
weight: 80
url: /python-net/extract-pages/
description: You can extract pages from your PDF file using Aspose.PDF for Python via .NET library.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to extract PDF pages using Python
Abstract: This article demonstrates how to extract pages from a PDF document using the Aspose.PDF library for Python. The techniques cover both single-page extraction and multi-page extraction, allowing developers to create new PDF files containing only selected pages. The examples illustrate how to access specific pages by 1-based indexing, copy them to a new PDF document, and save the results while keeping the original document intact. These methods are useful for splitting large documents, sharing selected sections, or creating customized PDF subsets for distribution or analysis.
---

## Extract Single Page from a PDF

Extract a specific page from a PDF document and save it as a new file. Using the Aspose.PDF library, the script copies the desired page to a new PDF, leaving the original document unchanged. This is useful for splitting PDFs or isolating important pages for distribution.

1. Load the source PDF using 'ap.Document()'.
1. Create a new PDF document to hold the extracted page.
1. Add the desired page from the source document to the new PDF:
  - In this example, page 2 is extracted (1-based indexing).
1. Save the new PDF with the extracted page to the specified output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Extract Multiple Pages from a PDF

Extract multiple specific pages from a PDF document and save them into a new file. Using the Aspose.PDF library, selected pages are copied to a new PDF while leaving the original document intact. This is useful for creating smaller PDFs containing only relevant sections of a larger document.

1. Load the source PDF using 'ap.Document()'.
1. Create a new PDF document to hold the extracted pages.
1. Select the pages to extract (in this example, pages 2 and 3 using 1-based indexing).
1. Add each selected page from the source document to the new PDF.
1. Save the new PDF with the extracted pages to the specified output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    document = ap.Document(input_file_name)
    pages = [2,3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```