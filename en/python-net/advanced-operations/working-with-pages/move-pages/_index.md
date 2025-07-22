---
title: Move PDF Pages programmatically via Python
linktitle: Move PDF Pages
type: docs
weight: 100
url: /python-net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Moving Pages between PDF documents using Python
Abstract: The article provides a comprehensive guide on moving pages between PDF documents or within a single PDF document using Python, specifically utilizing the Aspose.PDF library. It outlines step-by-step processes for three scenarios - moving a single page from one PDF to another, transferring multiple pages, and relocating a page within the same document. Each scenario involves creating `Document` class objects for source and destination PDFs, manipulating pages through the `PageCollection` class, and utilizing the `add`, `delete`, and `save` methods to achieve the desired page reorganization. Code snippets are provided for practical implementation, demonstrating how to move pages efficiently using Python scripts.
---

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using Python.
To move an page we should:

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the destination PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the destination document.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in source document.
1. Save the source PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows you how to move one page.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    page = document.pages[2]
    document.pages.add(page)
    document.pages.delete(2)
    document.save(path_outfile)
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the destination PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
    1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
    1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the destination document.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in source document using array.
1. Save the source PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Save output files
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the new location (for example to end).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in previous location.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_pdf)
```

