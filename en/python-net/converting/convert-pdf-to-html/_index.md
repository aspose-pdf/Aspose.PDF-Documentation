---
title: Convert PDF to HTML in Python 
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2025-02-27"
description: This topic show you how to convert PDF file to HTML format with  Aspose.PDF for Python .NET library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF to HTML Format using Aspose.PDF for Python
Abstract: This article outlines the process of converting PDF files to HTML using Python, specifically with the Aspose.PDF for Python via .NET library. The conversion is beneficial for integrating PDF content into websites or online forums. The article provides a simple step-by-step guide and sample code to achieve this conversion. Key steps include creating an instance of the `Document` object with the source PDF, and saving it using `HtmlSaveOptions` via the `save()` method. Additionally, an online tool by Aspose is highlighted for users to test the PDF to HTML conversion functionality. Various related topics are also briefly mentioned, emphasizing the versatility and utility of the Aspose.PDF library for different conversion needs.
---

## Overview

This article explains how to **convert PDF to HTML using Python**. It covers these topics.

_Format_: **HTML**
- [Python PDF to HTML](#python-pdf-to-html)
- [Python Convert PDF to HTML](#python-pdf-to-html)
- [Python How to convert PDF file to HTML](#python-pdf-to-html)


## Convert PDF to HTML

**Aspose.PDF for Python via .NET** provides many features for converting various file formats into PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into <abbr title="HyperText Markup Language">HTML</abbr>. You can use just a couple of lines of code Python for converting PDF To HTML. You may need to convert PDF to HTML if you want to create a website or add content to an online forum. One way to convert PDF to HTML is to programmatically use Python.

{{% alert color="success" %}}
**Try to convert PDF to HTML online**

Aspose.PDF for Python presents you online free application ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Steps: Convert PDF to HTML in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
2. Save it to [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    # Open PDF document

    document = apdf.Document(path_infile)

    # save document in HTML format

    save_options = apdf.HtmlSaveOptions()

    document.save(path_outfile, save_options)
```

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **HTML**
- [Python PDF to HTML Code](#python-pdf-to-html)
- [Python PDF to HTML API](#python-pdf-to-html)
- [Python PDF to HTML Programmatically](#python-pdf-to-html)
- [Python PDF to HTML Library](#python-pdf-to-html)
- [Python Save PDF as HTML](#python-pdf-to-html)
- [Python Generate HTML from PDF](#python-pdf-to-html)
- [Python Create HTML from PDF](#python-pdf-to-html)
- [Python PDF to HTML Converter](#python-pdf-to-html)
