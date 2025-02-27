---
title: Create PDF document programmatically
linktitle: Create PDF
type: docs
weight: 10
url: /python-net/create-document/
description: This page describes how to create PDF document from scratch with Aspose.PDF for Python via .NET library.
TechArticle: true 
AlternativeHeadline: How to create PDF file in Aspose.PDF for Python
Abstract: The article discusses the necessity for developers to programmatically generate PDF files, such as reports, within software applications. Writing custom code for this task can be time-consuming and inefficient. Instead, the article recommends using Aspose.PDF for Python via .NET as an efficient solution to create PDF files with Python. It outlines the steps to generate a PDF file - creating a `Document` object, adding a `Page` object to the document, inserting a `TextFragment` into the page, and saving the final document. The article provides a Python code snippet demonstrating these steps, showcasing how to create a simple PDF with the text "Hello, world!" using the Aspose.PDF library.
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


