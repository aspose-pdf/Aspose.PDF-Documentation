---
title: Convert HTML to PDF in Python
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2025-02-27"
description: Learn how to convert HTML content into a PDF document using Aspose.PDF for Python via .NET
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert HTML to PDF using Aspose.PDF for Python
Abstract: Aspose.PDF for Python via .NET offers a robust solution for creating PDF files from web pages and raw HTML code within applications. This article provides a guide on converting HTML to PDF using Python, outlining the use of Aspose.PDF for Python, a PDF manipulation API that enables seamless conversion of HTML documents to PDF format. The conversion process can be customized as needed. The article includes a Python code sample demonstrating the conversion process, which involves creating an instance of the HtmlLoadOptions class, initializing a Document object, and saving the output PDF document using the Document.Save() method. Additionally, Aspose offers an online tool for converting HTML to PDF, allowing users to explore the functionality and quality of the conversion process.
---

## Overview

Aspose.PDF for Python via .NET is a professional solution that allows you to create PDF files from web pages and raw HTML code in your applications.

This article explains how to **convert HTML to PDF using Python**. It covers the following topics.

_Format_: **HTML**
- [Python HTML to PDF](#python-html-to-pdf)
- [Python Convert HTML to PDF](#python-html-to-pdf)
- [Python How to convert HTML to PDF](#python-html-to-pdf)

## Python HTML to PDF Conversion

**Aspose.PDF for Python** is a PDF manipulation API that lets you convert any existing HTML documents to PDF seamlessly. The process of converting HTML to PDF can be flexibly customized.

## Convert HTML to PDF

The following Python code sample shows how to convert an HTML document to a PDF.

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) class.
2. Initialize [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
3. Save output PDF document by calling **Document.Save()** method.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.HtmlLoadOptions()

    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Try to convert HTML to PDF online**

Aspose presents you online free application ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}




