---
title: Change PDF Page Size with Python
linktitle: Change PDF Page Size
type: docs
weight: 60
url: /python-net/change-page-size/
description: Change Page Size from your PDF document using Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to change PDF Page Size with Python
Abstract: The article titled "Change PDF Page Size with Python", published by Aspose.PDF Doc Team, provides a beginner-level guide on resizing PDF pages using the Aspose.PDF for Python via .NET library. The tutorial explains the process of changing the page dimensions of an existing PDF file with straightforward Python code. Key steps include loading the PDF, accessing the pages through the `PageCollection` object, selecting a specific page, and using the `set_page_size()` method from the `Page` class to adjust its dimensions. The updated document is then saved using the `Document` class's `save()` method. A code snippet is provided to illustrate these steps, showcasing how to set a page size to A4 dimensions using points. The article is intended for those looking to manipulate PDF documents programmatically with Python, utilizing the Aspose.PDF library's capabilities.
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

