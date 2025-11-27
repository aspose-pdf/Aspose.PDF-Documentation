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

1. Load the source PDF using the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to hold the extracted page.
1. Add the desired [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) from the source document to the new PDF using the destination document's [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - In this example, page 2 is extracted (1-based indexing).
1. Save the new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) with the extracted page to the specified output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## Extract Multiple Pages from a PDF

Extract multiple specific pages from a PDF document and save them into a new file. Using the Aspose.PDF library, selected pages are copied to a new PDF while leaving the original document intact. This is useful for creating smaller PDFs containing only relevant sections of a larger document.

1. Load the source PDF using the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to hold the extracted pages.
1. Select the pages to extract (in this example, pages 2 and 3 using 1-based indexing).
1. Add each selected [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) from the source document to the new PDF using its [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Save the new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) with the extracted pages to the specified output file.

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
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```