---
title: Convert PDF to PowerPoint in Python
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /python-net/convert-pdf-to-powerpoint/
description: Learn how to convert PDF to PowerPoint in Python, including PDF to PPTX, slides as images, and custom image resolution with Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convert PDF to PPTX PowerPoint slides in Python
Abstract: This article shows how to convert PDF files to PowerPoint presentations with Aspose.PDF for Python via .NET. It covers PDF to PPTX conversion, converting slides as images, and setting image resolution for presentation output.
---

## Convert PDF to PowerPoint in Python

**Aspose.PDF for Python via .NET** lets you convert PDF files to PowerPoint PPTX presentations from Python code.

Use this workflow when you need to repurpose PDF reports, slide decks, brochures, or handouts as PowerPoint files. During conversion, individual PDF pages are converted to separate slides in the PPTX file.

During PDF to PPTX conversion, text can be rendered as selectable text that you can update in PowerPoint. To convert PDF files to PPTX format, Aspose.PDF provides the [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class. Pass a `PptxSaveOptions` object as the second argument to the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

## Convert PDF to PPTX in Python

To convert PDF to PPTX, use the following code steps.

Steps: Convert PDF to PowerPoint in Python

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.
1. Create an instance of [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class.
1. Call the [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Convert PDF to PPTX with Slides as Images

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF provides an online ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) application where you can test the conversion quality.


[![Aspose.PDF Convertion PDF to PPTX with App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class. To achieve this, set property [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) of [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class to 'true' as shown in the following code sample.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Convert PDF to PPTX with Custom Image Resolution

This method converts a PDF document into a PowerPoint (PPTX) file while setting a custom image resolution (300 DPI) for improved quality.

1. Load the PDF into an 'ap.Document' object.
1. Create a 'PptxSaveOptions' instance.
1. Set the 'image_resolution' property to 300 DPI for high-quality rendering.
1. Save the PDF as a PPTX file using the defined save options.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Related conversions

- [Convert PDF to Word](/pdf/python-net/convert-pdf-to-word/) for editable document output instead of slides.
- [Convert PDF to Excel](/pdf/python-net/convert-pdf-to-excel/) when the source PDF contains table-heavy business data.
- [Convert PDF to HTML](/pdf/python-net/convert-pdf-to-html/) for browser-ready publishing workflows.
