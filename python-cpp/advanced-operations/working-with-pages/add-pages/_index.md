---
title: Add Pages in PDF with Python
linktitle: Add Pages
type: docs
weight: 10
url: /python-cpp/add-pages/
description: This article teaches how to add a page to PDF file using C++
lastmod: "2023-07-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This section shows how to add pages to a PDF using Python.

## Add or Insert Page in a PDF File

Aspose.PDF for Python via C++ lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a new document object and assigns it to the variable doc.
1. Get the collection of pages in the document and assigns it to the variable pages.
1. Add a new page to the collection of pages.
1. Saves the document as a file.
1. Close the handle to the collection of pages.
1. Close the handle to the document.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page_collection_add_page(pages)
document_save(doc, "document.pdf")
close_handle(pages)
close_handle(doc)
```
