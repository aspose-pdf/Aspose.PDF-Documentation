---
title: Convert PDF to Microsoft Word Documents in .NET
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Learn how to write C# code for PDF to Microsoft Word formats conversion with Aspose.PDF for .NET. and tune up conversion PDF to DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

This article explains how to **convert PDF to Microsoft Word Documents using C#**. It covers these topics.

_Format_: **DOC**

- [C# PDF to DOC](#csharp-pdf-to-doc)
- [C# Convert PDF to DOC](#csharp-pdf-to-doc)
- [C# How to convert PDF file to DOC](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDF to DOCX](#csharp-pdf-to-docx)
- [C# Convert PDF to DOCX](#csharp-pdf-to-docx)
- [C# How to convert PDF file to DOCX](#csharp-pdf-to-docx)

_Format_: **Word**

- [C# PDF to Word](#csharp-pdf-to-docx)
- [C# Convert PDF to Word](#csharp-pdf-to-doc)
- [C# How to convert PDF file to Word](#csharp-pdf-to-docx)

The following code snippet also works with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## PDF to DOC and DOCX Conversion

One of the most popular features is the PDF to Microsoft Word DOC conversion, which makes content management more effortless. **Aspose.PDF for .NET** allows you to convert PDF files to DOC and DOCX format quickly and efficiently.

## Convert PDF to DOC (Microsoft Word 97-2003) file

Convert PDF files to DOC format with ease and complete control. Aspose.PDF for .NET is flexible and supports a wide variety of conversions. Converting pages from PDF documents to images, for example, is a very popular feature.

Many of our customers have requested a conversion from PDF to DOC: converting a PDF file to a Microsoft Word document. Customers want this because PDF files cannot easily be edited, whereas Word documents can. Some companies want their users to be able to manipulate text, tables and images in files that started as PDFs.

Keeping alive the tradition of making things simple and understandable, Aspose.PDF for .NET lets you transform a source PDF file into a DOC file with two lines of code. To accomplish this feature, we have introduced an enumeration named SaveFormat and its value .Doc lets you save the source file to Microsoft Word format.

The following C# code snippet shows converting a PDF file into DOC format.

<a name="csharp-pdf-to-doc"><strong>Steps: Convert PDF to DOC in C#</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) object with the source PDF document.
2. Save it to **SaveFormat.Doc** format by calling **Document.Save()** method.

```csharp
public static void ConvertPDFtoWord()
{
    // Open the source PDF document
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Save the file into MS document format
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
}
```

### Using the DocSaveOptions Class

The [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) class provides numerous properties that improve converting PDF files to DOC format. Among these properties, Mode enables you to specify the recognition mode for PDF content. You can select any value from the RecognitionMode enumeration for this property. Each of these values has specific benefits and limitations:

- [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) mode is fast and good for preserving the original look of the PDF file, but the editability of the resulting document could be limited. Every visually grouped text block in the original PDF is converted into a textbox in the output document. This achieves maximal resemblance to the original, so the output document looks good, but it consists entirely of text boxes, which could be edited in Microsoft Word, which is quite challenging.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) is full recognition mode, where the engine performs grouping and multi-level analysis to restore the original document as per the author's intent while producing an easily editable document. The limitation is that the output document might look different from the original.

The [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) property can be used to control the relative proximity between textual elements. It means that distance is normed by the font size. Larger fonts may have bigger spaces between syllables and still be considered a single whole. It is specified as a percentage of the font size; for example, 1 = 100%. This means that two characters of 12pt placed 12 pt apart are proximal.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) is used to switch on bullet recognition during conversion.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Set the recognition mode as Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Set the Horizontal proximity as 2.5
        RelativeHorizontalProximity = 2.5f,
        // Enable the value to recognize bullets during the conversion process
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for .NET presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convert PDF to DOCX (Microsoft Word 2007-2021) file

Aspose.PDF for .NET API lets you read and convert PDF documents to DOCX using C# and any .NET language. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and later versions but not with earlier versions of MS Word, which support DOC file extensions.

The following C# code snippet shows converting a PDF file into DOCX format.

<a name="csharp-pdf-to-docx"><strong>Steps: Convert PDF to DOCX in C#</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) object with the source PDF document.
2. Save it to **SaveFormat.DocX** format by calling **Document.Save()** method.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Open the source PDF document
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Save the resultant DOC file
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Convert PDF to DOCX in Enhanced Mode

To get better results of PDF to DOCX conversion, you can use `EnhancedFlow` mode.
The main difference between Flow and Enhanced Flow is that tables (both with and without borders) are recognized as real tables, not as text with a picture in the background.
There is also recognition of numbered lists and many other minor things.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Open the source PDF document
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Instantiate DocSaveOptions object
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Specify the output format as DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // Set other DocSaveOptions params
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Save document in docx format
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```

{{% alert color="warning" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for .NET presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## See Also

This article also covers these topics. The codes are the same as above.

_Format_: **Word**

- [C# PDF to Word Code](#csharp-pdf-to-docx)
- [C# PDF to Word API](#csharp-pdf-to-docx)
- [C# PDF to Word Programmatically](#csharp-pdf-to-docx)
- [C# PDF to Word Library](#csharp-pdf-to-docx)
- [C# Save PDF as Word](#csharp-pdf-to-docx)
- [C# Generate Word from PDF](#csharp-pdf-to-docx)
- [C# Create Word from PDF](#csharp-pdf-to-docx)
- [C# PDF to Word Converter](#csharp-pdf-to-docx)

_Format_: **DOC**

- [C# PDF to DOC Code](#csharp-pdf-to-doc)
- [C# PDF to DOC API](#csharp-pdf-to-doc)
- [C# PDF to DOC Programmatically](#csharp-pdf-to-doc)
- [C# PDF to DOC Library](#csharp-pdf-to-doc)
- [C# Save PDF as DOC](#csharp-pdf-to-doc)
- [C# Generate DOC from PDF](#csharp-pdf-to-doc)
- [C# Create DOC from PDF](#csharp-pdf-to-doc)
- [C# PDF to DOC Converter](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDF to DOCX Code](#csharp-pdf-to-docx)
- [C# PDF to DOCX API](#csharp-pdf-to-docx)
- [C# PDF to DOCX Programmatically](#csharp-pdf-to-docx)
- [C# PDF to DOCX Library](#csharp-pdf-to-docx)
- [C# Save PDF as DOCX](#csharp-pdf-to-docx)
- [C# Generate DOCX from PDF](#csharp-pdf-to-docx)
- [C# Create DOCX from PDF](#csharp-pdf-to-docx)
- [C# PDF to DOCX Converter](#csharp-pdf-to-docx)
