---
title: Create PDF document programmatically
linktitle: Create PDF
type: docs
weight: 10
url: /python-net/create-document/
description: This page describes how to create PDF document from scratch with Aspose.PDF for Python via .NET library.
---

For developers, there are many scenarios where it becomes necessary to programmatically generate PDF files. You may need to programmatically generate PDF reports and other PDF files in your software. It is rather long and inefficient to write your own code and functions from scratch. To create a PDF file with Python, there is a better solution - **Aspose.PDF for Python via .NET**.

## How to Create PDF File using Python

To create a PDF file usingPython, the following steps can be used.

1. Create an object of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object to the [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) collection of the Document object
1. Add [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) to [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection of the page
1. Save the resultant PDF document

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```


