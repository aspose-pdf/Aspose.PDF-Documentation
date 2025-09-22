---
title: Convert HTML to PDF in Python
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
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
1. Initialize [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Save output PDF document by calling **document.save()** method.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Try to convert HTML to PDF online**

Aspose presents you online free application ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Convert HTML to PDF media type

1. Create an instance of the [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) class. 'html_media_type' applies CSS rules intended for on-screen display.
1. Load and convert HTML.
1. Save output PDF document by calling **document.save()** method.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert HTML to PDF priority CSS Page Rule

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) class.
1. Optionally sets how CSS is applied. The commented line 'is_priority_css_page_rule' can override how CSS rules affect page layout.
1. Converts and saves it as a PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert HTML to PDF Embed Fonts

1. Loads an HTML file.
1. Embeds fonts into the resulting PDF to preserve appearance across devices.
1. Saves the PDF to a specified output location.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Render content on single page during HTML to PDF conversion

Aspose.PDF for Python via .NET to convert an HTML file into a single-page PDF.

1. Loads an HTML file.
1. Configures Aspose to render everything on a single PDF page.
1. Saves the PDF to a specified location.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Convert MHTML to PDF

Loads an MHT (MHTML) file from disk and converts it into a PDF using Aspose.PDF for Pyhton via .NET. Allows specifying custom page dimensions to ensure a consistent layout. With this operation, you can support embedded HTML, CSS, and images in MHT files, as well as Configurable page width and height, and save the converted document to a specified output folder.

1. Loads an MHT (MHTML) file.
1. Sets the page size for the converted document.
1. Converts the content into PDF (or another format) using Aspose.PDF.
1. Saves the file to a specific folder and prints a confirmation.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```