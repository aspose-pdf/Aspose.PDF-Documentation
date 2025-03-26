---
title: How to Create PDF using Python
linktitle: Create PDF Document
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create PDF File with Python
Abstract: Aspose.PDF for Python via .NET is a versatile API designed for developers to manipulate PDF files within Python applications targeting the .NET framework. It enables users to create, load, modify, and convert PDF documents effortlessly. This article provides a step-by-step guide to creating a simple PDF file using Aspose.PDF. The process involves initializing a `Document` object, adding a `Page` to the document, inserting a `TextFragment` into the page's paragraphs, and saving the file as a PDF. The included Python code snippet demonstrates these steps by creating a PDF document that contains the text "Hello World!". This API simplifies PDF handling with minimal code, enhancing productivity for developers working with PDFs in .NET environments.
---

**Aspose.PDF for Python via .NET** is a PDF manipulation API that allows developers to create, load, modify, and convert PDF files directly from Python for .NET applications with just a few lines of code.

## How to Create Simple PDF File

To create a PDF using Python via .NET with Aspose.PDF, you can follow these steps:

1. Create an object of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object to the [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) collection of the Document object
1. Add [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) to [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection of the page
1. Save the resultant PDF document

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```

