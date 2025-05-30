---
title: Add Pages in PDF with Python
linktitle: Add Pages
type: docs
weight: 10
url: /python-net/add-pages/
description: Discover how to add pages to a PDF document in Python using Aspose.PDF for flexible document creation and editing.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
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

### Insert Empty Page in a PDF File at Desired Location

To insert an empty page in a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's [insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) method with specified index.
1. Save the output PDF using the [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert a page in a PDF file.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.pages.insert(2)
    document.save(path_outfile)
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) method, without any parameters.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_pdf)
```

