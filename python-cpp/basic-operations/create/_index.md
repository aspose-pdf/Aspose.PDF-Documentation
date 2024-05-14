---
title: Create PDF document
linktitle: Create PDF
type: docs
weight: 10
url: /python-cpp/create-document/
description: This page describes how to create PDF document from scratch with Aspose.PDF for Python via C++ library.
---

For developers, there are many scenarios where it becomes necessary to programmatically generate PDF files. You may need to programmatically generate PDF reports and other PDF files in your software. It is rather long and inefficient to write your own code and functions from scratch. To create a PDF file with Python, there is a better solution - **Aspose.PDF for Python via C++**.

## Create PDF File using Python

To create a PDF file using Python, the following steps can be used.

* import all the classes and methods from the Aspose.PDF for Python via C++ library.
* Create a new Document object that represents an empty PDF document using [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)
* Gets the [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) object that contains all the pages in the document.
* Add a new page to the end of the page collection [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/)and returns the Page object that represents the added page.
* Save the document to a file with the specified name in the current working directory.
* Closes the handle to the document and releases any resources associated with it.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## Create PDF File based on DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```
