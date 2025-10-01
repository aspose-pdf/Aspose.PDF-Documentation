---
title: Convert PDF to EPUB, LaTeX, Text, XPS in Python
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: This topic shows you how to convert PDF file to other file formats like EPUB, LaTeX, Text, XPS etc using Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to Convert PDF to other formats in Python
Abstract: The article provides a comprehensive guide on converting PDF files into various formats using Aspose.PDF for Python. It covers the conversion of PDFs into EPUB, LaTeX/TeX, Text, XPS, and XML formats. Each section starts with an invitation to try online free applications provided by Aspose for converting PDFs to the respective formats, highlighting the ease of use and quality of these tools.
---

## Convert PDF to EPUB

{{% alert color="success" %}}
**Try to convert PDF to EPUB online**

Aspose.PDF for Python presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.
EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

Aspose.PDF for Python also supports the feature to convert PDF documents to EPUB format. Aspose.PDF for Python has a class named 'EpubSaveOptions' which can be used as the second argument to [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method, to generate an EPUB file.
Please try using the following code snippet to accomplish this requirement with Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to LaTeX/TeX

**Aspose.PDF for Python via .NET** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

{{% alert color="success" %}}
**Try to convert PDF to LaTeX/TeX online**

Aspose.PDF for Python presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) which provides the property OutDirectoryPath for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Convert PDF to Text

**Aspose.PDF for Python** support converting whole PDF document and single page to a Text file. You can convert PDF document to TXT file using 'TextDevice' class. The following code snippet explains how to extract the texts from the all pages.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Try to convert Convert PDF to Text online**

Aspose.PDF for Python presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convert PDF to XPS

**Aspose.PDF for Python** gives a possibility to convert PDF files to XPS format. Let try to use the presented code snippet for converting PDF files to XPS format with Python.

{{% alert color="success" %}}
**Try to convert PDF to XPS online**

Aspose.PDF for Python presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

To convert PDF files to XPS, Aspose.PDF has the class [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) that is used as the second argument to the [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to generate the XPS file.

The following code snippet shows the process of converting PDF file into XPS format.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to MD

Aspose.PDF has the class 'MarkdownSaveOptions()', which converts a PDF document into Markdown (MD) format while preserving images and resources.

1. Load the source PDF using 'ap.Document'.
1. Create an instance of 'MarkdownSaveOptions'.
1. Set 'resources_directory_name' to 'images' – extracted images will be stored in this folder.
1. Save the converted Markdown document using the configured options.
1. Print a confirmation message after conversion.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

A Markdown file with text and linked images stored in the specified images folder.

## Convert PDF to MobiXML

This method converts a PDF document into the MOBI (MobiXML) format, which is commonly used for eBooks on Kindle devices.

1. Load the source PDF document using 'ap.Document'.
1. Save the document with the format 'ap.SaveFormat.MOBI_XML'.
1. Print a confirmation message once the conversion is complete.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```