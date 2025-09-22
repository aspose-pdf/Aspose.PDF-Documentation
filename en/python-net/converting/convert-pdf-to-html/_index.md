---
title: Convert PDF to HTML in Python 
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: This topic show you how to convert PDF file to HTML format with  Aspose.PDF for Python via .NET library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to Convert PDF to HTML in Python
Abstract: This article provides a comprehensive guide on converting PDF files to HTML using Python, specifically through the Aspose.PDF for Python via .NET library. It outlines the necessary steps to achieve this conversion programmatically, highlighting the creation of a `Document` object from the source PDF and utilizing the `HtmlSaveOptions` for saving the document in HTML format. The article includes a concise Python code snippet demonstrating the conversion process. Additionally, it introduces an online tool, Aspose.PDF's "PDF to HTML" application, for users to explore the functionality and quality of the conversion. The article is structured to cater to various related topics, ensuring a thorough understanding of using Python for PDF to HTML conversion.
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

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with Stored Images

This function converts a PDF file into HTML format using Aspose.PDF for Python via .NET. All extracted images are stored in a specified folder instead of being embedded in the HTML file.

1. Configure HTML save options.
1. Save as HTML with external images.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to Multi-Page HTML

This function converts a PDF file into multi-page HTML, where each PDF page is exported as a separate HTML file. This makes the output easier to navigate and reduces loading time for large PDFs.

1. Load the source PDF using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and 'set split_into_pages'.
1. Save the document as HTML with pages split into separate files.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with saving SVG images in specified folder

This function converts a PDF into HTML format while storing all images as SVG files in a specified folder, instead of embedding them directly in the HTML.

1. Load the source PDF using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and 'set special_folder_for_svg_images' to the target folder.
1. Save the document as HTML with external SVG images.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with Compressed SVG Images

This snippet converts a PDF into HTML format, storing all images as SVG files in a specified folder and compressing them to reduce file size.

1. Load the PDF document using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and:
   - Set 'special_folder_for_svg_images' to store SVG images externally.
   - Enable 'compress_svg_graphics_if_any' to compress SVG images.
1. Save the document as HTML with compressed external SVG images.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with Embedded Raster Images

This snippet converts a PDF into HTML format, embedding raster images as PNG page backgrounds. This approach preserves image quality and page layout within the HTML.

1. Load the PDF document using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and 'set raster_images_saving_mode' to 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Save the document as HTML with embedded raster images.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML (Body Content Only, Multi-Page)

This function converts a PDF into HTML format, generating only the 'body' content without extra 'html' or 'head' tags, and splits the output into separate pages.

1. Load the PDF document using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and configure:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' to generate only the 'body' content.
   - 'split_into_pages' to create separate HTML files for each PDF page.
1. Save the document as HTML with the specified options.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with Transparent Text Rendering

This function converts a PDF into HTML format, rendering all text as transparent, including shadowed texts, which preserves visual fidelity while allowing flexible styling in the output HTML.

1. Load the PDF document using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and configure:
    - 'save_transparent_texts' to render normal text as transparent.
    - 'save_shadowed_texts_as_transparent_texts' to render shadowed text as transparent.
1. Save the document as HTML with transparent text rendering.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to HTML with Document Layers Rendering

This function converts a PDF into HTML format, preserving document layers by converting marked content into separate layers in the output HTML. This allows layered elements (like annotations, backgrounds, and overlays) to be rendered accurately.

1. Load the PDF document using 'apdf.Document'.
1. Create 'HtmlSaveOptions' and enable 'convert_marked_content_to_layers' to preserve layers.
1. Save the document as HTML with layered content.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
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
