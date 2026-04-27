---
title: Extract PDF Pages in Python
linktitle: Extracting PDF Pages
type: docs
weight: 80
url: /python-net/extract-pages/
description: Learn how to extract single or multiple PDF pages into new files in Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to extract PDF pages using Python
Abstract: This article explains how to extract pages from PDF files using Aspose.PDF for Python via .NET. Learn how to copy a single page or multiple pages into a new document by using 1-based page indexing and the PageCollection API.
---

## Extract Single Page from a PDF

Extract a specific page from a PDF document and save it as a new file. Using the Aspose.PDF library, the script copies the desired page to a new PDF, leaving the original document unchanged. This is useful for splitting PDFs or isolating important pages for distribution.

1. Load the source PDF using the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to hold the extracted page.
1. Add the desired [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) from the source document to the new PDF using the destination document's [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - In this example, page 2 is extracted (1-based indexing).
1. Save the new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) with the extracted page to the specified output file.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
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
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Related Page Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Delete PDF pages in Python](/pdf/python-net/delete-pages/)
- [Move PDF pages in Python](/pdf/python-net/move-pages/)
- [Split PDF files in Python](/pdf/python-net/split-document/)
