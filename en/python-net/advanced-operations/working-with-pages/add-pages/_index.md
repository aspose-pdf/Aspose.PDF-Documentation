---
title: Adding Pages in PDF with Python
linktitle: Adding Pages
type: docs
weight: 10
url: /python-net/add-pages/
description: Discover how to add pages to a PDF document in Python using Aspose.PDF for flexible document creation and editing.
lastmod: "2025-11-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add Pages in PDF using Python
Abstract: The article provides a guide on using the Aspose.PDF for Python via .NET API to manipulate pages in a PDF document. It emphasizes the flexibility offered by the API, particularly through the `PageCollection` class, which manages all pages within a PDF. The document details procedures for adding or inserting pages at specific locations in a PDF file. It outlines two primary operations - inserting an empty page at a desired location within the document and adding an empty page at the end of the document. For both operations, the process involves creating a `Document` object, using the `PageCollection`'s `insert` or `add` methods, and saving the modified document. The article includes code snippets demonstrating these tasks, showcasing how straightforward it is to manipulate PDF documents using Python with this API.
---

Aspose.PDF for Python via .NET API provides full flexibility to work with pages in a PDF document using Python. It maintains all the pages of a PDF document in [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) that can be used to work with PDF pages.
Aspose.PDF for Python via .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.
This section shows how to add pages to a PDF using Python.

## Add or Insert Page in a PDF File

Aspose.PDF for Python via .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

### Insert Empty Page in a PDF File

To insert an empty page in a PDF file:

1. Open an existing PDF document using 'ap.Document()'.
1. Insert a new empty page at a specific index using 'document.pages.insert(index)'.
1. Save the modified document using 'document.save()' to the desired output path.

Insert an empty page into an existing PDF file at a specified position:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Open an existing PDF document using 'ap.Document()'.
1. Add a new empty page to the end of the document using 'document.pages.add()'.
1. Save the updated PDF file using 'document.save()'.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Add a Page from Another PDF Document

With Aspose.PDF for Python library, you create a new PDF, add an initial page, and then import a page from another PDF into it.

1. Create a new PDF document.
1. Add a new blank page and write some text on it.
1. Open another existing PDF - 'input_file_name'.
1. Copy a page from that document.
1. Paste the copied page into your main document.
1. Save the combined file as 'output_file_name'.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```