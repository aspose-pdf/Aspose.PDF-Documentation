---
title: Extract PDF Pages in Python
linktitle: Extracting PDF Pages
type: docs
weight: 80
url: /python-net/extract-pages/
description: Learn how to extract single or multiple PDF pages into new files in Python.
lastmod: "2026-04-15"
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
import sys
import aspose.pdf as ap
from os import path

def extract_page(input_file_name, output_file_name):
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
import sys
import aspose.pdf as ap
from os import path

def extract_bunch_pages(input_file_name, output_file_name):
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