---
title: Delete PDF Pages in Python
linktitle: Deleting PDF Pages
type: docs
weight: 80
url: /python-net/delete-pages/
description: Learn how to delete pages from PDF files in Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or more PDF pages in Python
Abstract: This article explains how to remove pages from PDF files using Aspose.PDF for Python via .NET. Learn how to delete a single page or multiple pages from a document by using the PageCollection API and then save the updated PDF.
---

You can delete pages from a PDF file using Aspose.PDF for Python via .NET. To delete a particular page, use the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) of a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Use this workflow when you need to remove unwanted pages from a PDF before sharing, archiving, or combining documents.

## Delete Page from PDF File

Aspose.PDF for Python via .NET deletes page 2 from the input PDF and saves the updated document to a new file. This feature is helpful for removing unwanted or sensitive pages without altering the rest of the document.

1. Load the input PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Delete the page using the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Call the [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to save the updated PDF file.

The following code snippet shows how to delete a particular page from the PDF file using Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Delete Multiple Pages from a PDF Document

Deleting multiple pages allows you to remove a set of specified pages in a single operation, which is more efficient than deleting pages one by one. The resulting PDF is saved to a new file, preserving the original document.

1. Load the input PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Delete the pages listed in the pages array using the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Save the updated [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to a new file.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Related Page Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Add PDF pages in Python](/pdf/python-net/add-pages/)
- [Move PDF pages in Python](/pdf/python-net/move-pages/)
- [Extract PDF pages in Python](/pdf/python-net/extract-pages/)
