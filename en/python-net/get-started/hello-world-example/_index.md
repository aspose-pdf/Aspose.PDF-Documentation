---
title: Example of Hello World using Python
linktitle: Hello World Example
type: docs
weight: 20
url: /python-net/hello-world-example/
description: This sample demonstrates how to create a simple PDF document with text Hello World using Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Hello World example via Python
Abstract: This article provides a Hello World example using the Aspose.PDF for Python via .NET library to create a PDF document. The example demonstrates the basic steps of using the Aspose.PDF API by generating a PDF with the text "Hello World!". The process involves instantiating a `Document` object, adding a `Page`, creating a `TextFragment` object, setting text properties such as font size and color, and using a `TextBuilder` to add the text to the page. The resultant PDF is then saved as "HelloWorld_out.pdf". The article includes a complete Python code snippet illustrating these steps, serving as an introductory guide to the library's usage.
---

A "Hello World" example shows the simplest syntax and the simplest program in any given programming language. Developers are introduced to the basic programming language syntax by learning how to print "Hello World" on the device screen. Therefore, we will traditionally start our acquaintance with our library from it.

In this article, we are creating a PDF document containing text "Hello World!". After installing **Aspose.PDF for Python via .NET** in your environment, you can execute below code sample to see how Aspose.PDF API works.

Below code snippet follows these steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) to document object
1. Create a [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) object
1. Set Text Colors
1. Create a Text Builder
1. Add [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) to the Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) resultant PDF document

The following code snippet is a "Hello World" program that demonstrates the functionality of Aspose.PDF for Python via the .NET API.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```