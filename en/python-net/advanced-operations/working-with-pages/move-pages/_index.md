---
title: Moving PDF Pages programmatically via Python
linktitle: Moving PDF Pages
type: docs
weight: 100
url: /python-net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for Python via .NET.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Moving Pages between PDF documents using Python
Abstract: The article provides a comprehensive guide on moving pages between PDF documents or within a single PDF document using Python, specifically utilizing the Aspose.PDF library. It outlines step-by-step processes for three scenarios - moving a single page from one PDF to another, transferring multiple pages, and relocating a page within the same document. Each scenario involves creating `Document` class objects for source and destination PDFs, manipulating pages through the `PageCollection` class, and utilizing the `add`, `delete`, and `save` methods to achieve the desired page reorganization. Code snippets are provided for practical implementation, demonstrating how to move pages efficiently using Python scripts.
---

## Moving a Page from one PDF Document to Another

Aspose.PDF for Python lets you move a page (not just copy it) from one PDF to another. It removes the selected page from the original document and then adds it to a new PDF file.

Think of it as cutting out a page from one book and gluing it into another — the page no longer exists in the original file after the move.

1. Open the source PDF document.
1. Select a specific page to move (in this case, page 2).
1. Create a new PDF document.
1. Add the selected page to the new PDF document.
1. Delete the page from the original document.
1. Save both documents.

The following code snippet shows you how to move one page.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Moving bunch of Pages from one PDF Document to Another

Unlike copying, this operation transfers the selected pages — removing them from the source file and saving them in a new PDF.

1. Create a new, empty destination document.
1. Select multiple pages (in this case, pages 1 and 3).
1. Loop through the selected pages and add each one to the destination document.
1. Save the destination document containing the moved pages.
1. Delete the moved pages from the source document.
1. Save the modified source document with a new file name to preserve both versions.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Moving a Page in new location in the current PDF Document

It shows how to move a specific page to a different position within the same document — a common need when reorganizing or editing PDF layouts.

1. Load the input PDF document.
1. Select the page you want to move (page 2).
1. Add it to the end of the document.
1. Delete the original page from its previous location.
1. Save the modified document as a new file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```

