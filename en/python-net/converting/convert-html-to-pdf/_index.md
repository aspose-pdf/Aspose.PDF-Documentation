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

## Convert HTML to PDF using media type

This example shows how to convert an HTML file to PDF using Aspose.PDF for Python via .NET with specific rendering options.

1. Create an instance of the [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) class. The 'html_media_type' applies CSS rules intended for on-screen display. The 'html_media_type' property can have multiple values. You can set it to HtmlMediaType.SCREEN or HtmlMediaType.PRINT.
1. Load the HTML into an ap.Document using the load options.
1. Save the document as a PDF.

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

Some documents may contain layout settings that utilize [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), which can create ambiguity when generating the layout. You can control the priority using the 'is_priority_css_page_rule' property. If this property is set to 'True', the CSS rule is applied first.

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) class.
1. Set 'is_priority_css_page_rule = False' to disable prioritizing @page CSS rules, allowing other styles to take precedence.
1. Load the HTML into an ap.Document with the configured options.
1. Save the document as a PDF.

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

## Convert HTML to PDF with Embeded Fonts

This example shows how to convert an HTML file to PDF while embedding fonts. If you need a PDF document with Embedded Fonts, you should set 'is_embed_fonts' to True.

1. Create 'HtmlLoadOptions()' to configure HTML to PDF conversion.
1. Set 'is_embed_fonts = True' to ensure that all fonts used in the HTML are embedded directly into the PDF, preserving visual fidelity.
1. Load the HTML into an ap.Document with these options.
1. Save the document as a PDF.

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

## Render Content on single Page during HTML to PDF conversion

This example demonstrates how to convert an HTML file into a single-page PDF using Aspose.PDF for Python.
You can display all content on one page using the 'is_render_to_single_page property'.

1. Create an instance of 'HtmlLoadOptions()' to configure the conversion process.
1. Enable 'is_render_to_single_page' to render the entire HTML content onto a single continuous PDF page.
1. Load the document with the configured options into an 'ap.Document'.
1. Save the result as a PDF file.

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

This example shows how to convert an MHT (MHTML) file into a PDF document using Aspose.PDF for Python with specific page dimensions.

1. Create an instance of ap.MhtLoadOptions() to configure MHT file processing.
1. Set various parameters, such as page size.
1. Initialize the document with the input file and configured loading options.
1. Save the resulting document as a PDF.

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