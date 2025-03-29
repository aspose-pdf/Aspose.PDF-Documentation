---
title: Convert other file formats to PDF in Python
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /python-net/convert-other-files-to-pdf/
lastmod: "2025-03-01"
description: This topic show you how to Aspose.PDF allows to convert other file formats such as EPUB, MD, PCL, XPS, PS, XML and LaTeX to PDF document.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: How to Convert other file formats to PDF in Python
Abstract: This article provides a comprehensive guide on converting various file formats to PDF using Python, leveraging the capabilities of Aspose.PDF for Python via .NET. The document outlines conversion processes for several formats, including EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO, and LaTeX/TeX. Each section provides specific code snippets and instructions for implementing these conversions. The article emphasizes the utility of Aspose.PDF's features, such as load options tailored for each file type, to ensure accurate and efficient conversion. Additionally, it highlights the availability of free online conversion applications for users to explore the functionality firsthand. The guide serves as a practical resource for developers seeking to integrate PDF conversion capabilities into their Python applications.
---

## Overview

This article explains how to **convert various other types of file formats to PDF using Python**. It covers the following topics.

_Format_: **EPUB**
- [Python EPUB to PDF](#python-convert-epub-to-pdf)
- [Python Convert EPUB to PDF](#python-convert-epub-to-pdf)
- [Python How to convert EPUB file to PDF](#python-convert-epub-to-pdf)

_Format_: **Markdown**
- [Python Markdown to PDF](#python-convert-markdown-to-pdf)
- [Python Convert Markdown to PDF](#python-convert-markdown-to-pdf)
- [Python How to convert Markdown file to PDF](#python-convert-markdown-to-pdf)

_Format_: **MD**
- [Python MD to PDF](#python-convert-md-to-pdf)
- [Python Convert MD to PDF](#python-convert-md-to-pdf)
- [Python How to convert MD file to PDF](#python-convert-md-to-pdf)

_Format_: **PCL**
- [Python PCL to PDF](#python-convert-pcl-to-pdf)
- [Python Convert PCL to PDF](#python-convert-pcl-to-pdf)
- [Python How to convert PCL file to PDF](#python-convert-pcl-to-pdf)

_Format_: **Text**
- [Python Text to PDF](#python-convert-text-to-pdf)
- [Python Convert Text to PDF](#python-convert-text-to-pdf)
- [Python How to convert Text file to PDF](#python-convert-text-to-pdf)

_Format_: **TXT**
- [Python TXT to PDF](#python-convert-txt-to-pdf)
- [Python Convert TXT to PDF](#python-convert-txt-to-pdf)
- [Python How to convert TXT file to PDF](#python-convert-txt-to-pdf)

_Format_: **XPS**
- [Python XPS to PDF](#python-convert-xps-to-pdf)
- [Python Convert XPS to PDF](#python-convert-xps-to-pdf)
- [Python How to convert XPS file to PDF](#python-convert-xps-to-pdf)

## Convert EPUB to PDF

**Aspose.PDF for Python via .NET** allows you simply convert EPUB files to PDF format.

<abbr title="electronic publication">EPUB</abbr> (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub. EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device.

EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.The version EPUB 3 is also endorsed by the Book Industry Study Group (BISG), a leading book trade association for standardized best practices, research, information and events, for packaging of content.

{{% alert color="success" %}}
**Try to convert EPUB to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Steps Convert EPUB to PDF in Python:

1. Load EPUB Document
1. Convert EPUB to PDF
1. Print Confirmation

Next following code snippet show you how to convert EPUB files to PDF format with Python.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.EpubLoadOptions()
    document = apdf.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert Markdown to PDF

**This feature is supported by version 19.6 or greater.**

{{% alert color="success" %}}
**Try to convert Markdown to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

This code snippet by Aspose.PDF for Python via .NET helps convert Markdown files into PDFs, allowing better document sharing, formatting preservation, and printing compatibility.o

The following code snippet shows how to use this functionality with Aspose.PDF library:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.MdLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert PCL to PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) is a Hewlett-Packard printer language developed to access standard printer features. PCL levels 1 through 5e/5c are command based languages using control sequences that are processed and interpreted in the order they are received. At a consumer level, PCL data streams are generated by a print driver. PCL output can also be easily generated by custom applications.

{{% alert color="success" %}}
**Try to convert PCL to PDF online**

Aspose.PDF for for .NET presents you online free application ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PCL to PDF with Free App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

To allow conversion from PCL to PDF, Aspose.PDF has the class [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) which is used to initialize the LoadOptions object. Later on this object is passed as an argument during Document object initialization and it helps the PDF rendering engine to determine the input format of source document.

The following code snippet shows the process of converting a PCL file into PDF format.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.PclLoadOptions()
    load_options.supress_errors = True

    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convert Text to PDF

**Aspose.PDF for Python via .NET** support the feature converting plain text and pre-formatted text file to PDF format.

Converting text to PDF means adding text fragments to the PDF page. As for text files, we are dealing with 2 types of text: pre-formatting (for example, 25 lines with 80 characters per line) and non-formatted text (plain text). Depending on our needs, we can control this addition ourselves or entrust it to the library's algorithms.

{{% alert color="success" %}}
**Try to convert TEXT to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion TEXT to PDF with Free App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = apdf.text.FontRepository.find_font("Courier New")

    document = apdf.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12

    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.Pages.Add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.defaultTextState.Font = monospace_font
            page.page_info.defaulttextstate.FontSize = 12
        else:
            text = apdf.text.TextFragment(line)
            page.paragraphs.add(text)

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convert XPS to PDF

**Aspose.PDF for Python via .NET** support feature converting <abbr title="XML Paper Specification">XPS</abbr> files to PDF format. Check this article to resolve your tasks.

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into its Windows operating system.

The following code snippet shows the process of converting XPS file into PDF format with Python.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.XpsLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Try to convert XPS format to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convert PostScript to PDF

**Aspose.PDF for Python via .NET** support features converting PostScript files to PDF format. One of the features from Aspose.PDF is that you can set a set of font folders to be used during conversion.

Following code snippet can be used to convert a PostScript file into PDF format with Aspose.PDF for Python via .NET:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.PsLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convert XML to PDF

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF:

{{% alert color="success" %}}
**Try to convert XML to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Following code snippet can be used to convert a XML to PDF format with Aspose.PDF for Python:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.XmlLoadOptions("template.xslt")
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convert XSL-FO to PDF

Following code snippet can be used to convert a XSLFO to PDF format with Aspose.PDF for Python via .NET:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_xsltfile = path.join(self.dataDir, xsltfile)
    path_xmlfile = path.join(self.dataDir, xmlfile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = apdf.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    document = apdf.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)

```

## Convert LaTeX/TeX to PDF

The LaTeX file format is a text file format with markup in the LaTeX derivative of the TeX family of languages and LaTeX is a derived format of the TeX system. LaTeX (ˈleɪtɛk/lay-tek or lah-tek) is a document preparation system and document markup language. It is widely used for the communication and publication of scientific documents in many fields, including mathematics, physics, and computer science. It also has a prominent role in the preparation and publication of books and articles that contain complex multilingual materials, such as Sanskrit and Arabic, including critical editions. LaTeX uses the TeX typesetting program for formatting its output, and is itself written in the TeX macro language.

{{% alert color="success" %}}
**Try to convert LaTeX/TeX to PDF online**

Aspose.PDF for Python via .NET presents you online free application ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

The following code snippet shows the process of converting LaTex file to PDF format with Python.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    load_options = apdf.LatexLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```