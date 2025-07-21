---
title: Change PDF Page Size with Python
linktitle: Change PDF Page Size
type: docs
weight: 60
url: /python-net/change-page-size/
description: Change Page Size from your PDF document using Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to change PDF Page Size using Python
Abstract: The article provides a guide on how to change the page size of a PDF document using Aspose.PDF for Python via .NET. It outlines the process of updating the page dimensions of an existing PDF file by utilizing the `Page` class's `set_page_size()` method. The steps involve loading the source PDF, retrieving the pages into a `PageCollection` object, selecting a specific page, and then employing the `set_page_size()` method to adjust its dimensions. Finally, the modified PDF is saved using the `Document` class's `save()` method. A code snippet is provided to demonstrate the process, where the page size is set to A4 dimensions (11.7 x 8.3 inches), converted into points for use in Aspose.PDF.
---

## Change PDF Page Size

Aspose.PDF for Python via .NET lets you change PDF page size with simple lines of code in your Python applications. This topic explains how to update/change the page dimensions (size) of an existing PDF file.

The [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class contains the [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) method which lets you set the page size. The code snippet below updates page dimensions in a few easy steps:

1. Load the source PDF file.
1. Get the pages into the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) object.
1. Get a given page.
1. Call the set_page_size() method to update its dimensions.
1. Call the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to generate the PDF file with updated page dimensions.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Save the updated document
    document.save(output_pdf)
```

