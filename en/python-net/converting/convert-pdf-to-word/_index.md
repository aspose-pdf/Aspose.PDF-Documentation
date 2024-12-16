---
title: Convert PDF to Microsoft Word Documents in Python
linktitle: Convert PDF to Word 2003/2019
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Learn how to convert PDF documents to Word format in Python using Aspose.PDF for easy document editing.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

This article explains how to **convert PDF to Microsoft Word Documents using Python**. It covers these topics.

_Format_: **DOC**
- [Python PDF to DOC](#python-pdf-to-doc)
- [Python Convert PDF to DOC](#python-pdf-to-doc)
- [Python How to convert PDF file to DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF to DOCX](#python-pdf-to-docx)
- [Python Convert PDF to DOCX](#python-pdf-to-docx)
- [Python How to convert PDF file to DOCX](#python-pdf-to-docx)

_Format_: **Word**
- [Python PDF to Word](#python-pdf-to-docx)
- [Python Convert PDF to Word](#python-pdf-to-doc)
- [Python How to convert PDF file to Word](#python-pdf-to-docx)


## Python PDF to DOC and DOCX Conversion

One of the most popular features is the PDF to Microsoft Word DOC conversion, which makes content management easier. **Aspose.PDF for Python** allows you to convert PDF files not only to DOC but also to DOCX format, easily and efficiently.

## Convert PDF to DOC (Word 97-2003) file

Convert PDF file to DOC format with ease and full control. Aspose.PDF for Python is flexible and supports a wide variety of conversions. Converting pages from PDF documents to images, for example, is a very popular feature.

A conversion that many of our customers have requested is PDF to DOC: converting a PDF file to a Microsoft Word document. Customers want this because PDF files cannot easily be edited, whereas Word documents can. Some companies want their users to be able to manipulate text, tables and images in files that started as PDFs.

Keeping alive the tradition of making things simple and understandable, Aspose.PDF for Python lets you transform a source PDF file into a DOC file with two lines of code. To accomplish this feature, we have introduced an enumeration named SaveFormat and its value .Doc lets you save the source file to Microsoft Word format.

The following Python code snippet shows the process of converting a PDF file into DOC format.

<a name="csharp-pdf-to-doc"><strong>Steps: Convert PDF to DOC in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
2. Save it to [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Open PDF document
    document = ap.Document(input_pdf)
    # Save the file into MS Word document format
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Using the DocSaveOptions Class

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class provides numerous properties that improve the process of converting PDF files to DOC format. Among these properties, Mode enables you to specify the recognition mode for PDF content. You can specify any value from the RecognitionMode enumeration for this property. Each of these values has specific benefits and limitations:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Set the recognition mode as Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Set the Horizontal proximity as 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Enable the value to recognize bullets during conversion process
    save_options.recognize_bullets = True

    # Save the file into MS Word document format
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for Python presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for Python API lets you read and convert PDF documents to DOCX using Python via .NET. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.

The following Python code snippet shows the process of converting a PDF file into DOCX format.

<a name="csharp-pdf-to-docx"><strong>Steps: Convert PDF to DOCX in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
2. Save it to [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Set the recognition mode as Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Set the Horizontal proximity as 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Enable the value to recognize bullets during conversion process
    save_options.recognize_bullets = True

    # Save the file into MS Word document format
    document.save(output_pdf, save_options)
```

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class has a property named Format which provides the capability to specify the format of the resultant document, that is, DOC or DOCX. In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

{{% alert color="warning" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for Python presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **Word**
- [Python PDF to Word Code](#python-pdf-to-docx)
- [Python PDF to Word API](#python-pdf-to-docx)
- [Python PDF to Word Programmatically](#python-pdf-to-docx)
- [Python PDF to Word Library](#python-pdf-to-docx)
- [Python Save PDF as Word](#python-pdf-to-docx)
- [Python Generate Word from PDF](#python-pdf-to-docx)
- [Python Create Word from PDF](#python-pdf-to-docx)
- [Python PDF to Word Converter](#python-pdf-to-docx)

_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Programmatically](#python-pdf-to-doc)
- [Python PDF to DOC Library](#python-pdf-to-doc)
- [Python Save PDF as DOC](#python-pdf-to-doc)
- [Python Generate DOC from PDF](#python-pdf-to-doc)
- [Python Create DOC from PDF](#python-pdf-to-doc)
- [Python PDF to DOC Converter](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF to DOCX Code](#python-pdf-to-docx)
- [Python PDF to DOCX API](#python-pdf-to-docx)
- [Python PDF to DOCX Programmatically](#python-pdf-to-docx)
- [Python PDF to DOCX Library](#python-pdf-to-docx)
- [Python Save PDF as DOCX](#python-pdf-to-docx)
- [Python Generate DOCX from PDF](#python-pdf-to-docx)
- [Python Create DOCX from PDF](#python-pdf-to-docx)
- [Python PDF to DOCX Converter](#python-pdf-to-docx)
