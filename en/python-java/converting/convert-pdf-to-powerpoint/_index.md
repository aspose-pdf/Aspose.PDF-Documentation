---
title: Convert PDF to PowerPoint in Python
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /python-java/convert-pdf-to-powerpoint/
description: Master the conversion of PDFs to PowerPoint slides using Aspose.PDF for Python via Java. Follow our detailed instructions for high-quality PPTX results.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

Is it possible to convert a PDF file into a PowerPoint? Yes, you can! And it's easy!
This article explains how to **convert PDF to PowerPoint using Python**. It covers these topics.

_Format_: **PPTX**
- [Python PDF to PPTX](#python-pdf-to-pptx)
- [Python Convert PDF to PPTX](#python-pdf-to-pptx)
- [Python How to convert PDF file to PPTX](#python-pdf-to-pptx)

_Format_: **PowerPoint**
- [Python PDF to PowerPoint](#python-pdf-to-powerpoint)
- [Python Convert PDF to PowerPoint](#python-pdf-to-powerpoint)
- [Python How to convert PDF file to PowerPoint](#python-pdf-to-powerpoint)

## Python PDF to PowerPoint and PPTX Conversion

**Aspose.PDF for Python via Java** lets you track the progress of PDF to PPTX conversion.

We have an API named Aspose.Slides which offers the feature to create as well as manipulate PPT/PPTX presentations. This API also provides the feature to convert PPT/PPTX files to PDF format. During this conversion, the individual pages of the PDF file are converted to separate slides in the PPTX file.

During PDF to <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> conversion, the text is rendered as Text where you can select/update it. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). An object of the PptxSaveOptions class is passed as a second argument to the [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). The following code snippet shows the process for converting PDF files into PPTX format.

## Simple conversion PDF to PowerPoint using Python and Aspose.PDF for Python

In order to convert PDF to PPTX, Aspose.PDF for Python advice to use the following code steps.

<a name="csharp-pdf-to-powerpoint"><strong>Steps: Convert PDF to PowerPoint in Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Steps: Convert PDF to PPTX in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document) class
2. Create an instance of [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions) class
3. Use the **Save** method of the **Document** object to save the PDF as PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Open PDF document
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Save the file into MS Word document format
document.save(output_pdf, save_options)
```

## Convert PDF to PPTX with Slides as Images

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for Python presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) class. To achieve this, set property [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) of [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) class to 'true' as shown in the following code sample.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Open PDF document
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Save the file into MS Word document format
document.save(output_pdf, save_options)
```

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **PowerPoint**
- [Python PDF to PowerPoint Code](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Programmatically](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Library](#python-pdf-to-powerpoint)
- [Python Save PDF as PowerPoint](#python-pdf-to-powerpoint)
- [Python Generate PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python Create PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Converter](#python-pdf-to-powerpoint)

_Format_: **PPTX**
- [Python PDF to PPTX Code](#python-pdf-to-pptx)
- [Python PDF to PPTX API](#python-pdf-to-pptx)
- [Python PDF to PPTX Programmatically](#python-pdf-to-pptx)
- [Python PDF to PPTX Library](#python-pdf-to-pptx)
- [Python Save PDF as PPTX](#python-pdf-to-pptx)
- [Python Generate PPTX from PDF](#python-pdf-to-pptx)
- [Python Create PPTX from PDF](#python-pdf-to-pptx)
- [Python PDF to PPTX Converter](#python-pdf-to-pptx)
