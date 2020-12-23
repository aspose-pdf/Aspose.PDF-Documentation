---
title: Convert PDF to DOC
linktitle: Convert PDF to DOC
type: docs
weight: 270
url: /net/convert-pdf-to-doc/
lastmod: "2020-12-23"
description: Convert PDF file to DOC format with ease and full control with Aspose.PDF for .NET. This page shows a code snippet to accomplish this task. 
aliases:
    - /pdf/net/convert-pdf-to-doc/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

One of the most popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. Aspose.PDF for .NET allows you to convert PDF files to DOC.

## Convert PDF to DOC (Word 97-2003) file

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Convert PDF file to DOC format with ease and full control. Aspose.PDF for .NET is flexible and supports a wide variety of conversions. Converting pages from PDF documents to images, for example, is a very popular feature.

A conversion that many of our customers have requested is PDF to DOC: converting a PDF file to a Microsoft Word document. Customers want this because PDF files cannot easily be edited, whereas Word documents can. Some companies want their users to be able to manipulate text, tables and images in files that started as PDFs.

Keeping alive the tradition of making things simple and understandable, Aspose.PDF for .NET lets you transform a source PDF file into a DOC file with two lines of code. To accomplish this feature, we have introduced an enumeration named SaveFormat and its value .Doc lets you save the source file to Microsoft Word format.

The following code snippet shows the process of converting PDF file into DOC.

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

The [`DocSaveOptions`](https://apireference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) class provides numerous properties that improve the process of converting PDF files to DOC format. Among these properties, Mode enables you to specify the recognition mode for PDF content. You can specify any value from the RecognitionMode enumeration for this property. Each of these values has specific benefits and limitations:

- [`Textbox`](https://apireference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) mode is fast and good for preserving the original look of the PDF file, but the editability of the resulting document could be limited. Every visually grouped block of text in the original PDF is converted into a textbox in the output document. This achieves maximal resemblance to the original so the output document looks good, but it consists entirely of textboxes and it could make editing in Microsoft Word quite hard.
- [`Flow`](https://apireference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) is full recognition mode, where the engine performs grouping and multi-level analysis to restore the original document as per the author's intent while producing an easily editable document. The limitation is that the output document might look different from the original.
- The [`RelativeHorizontalProximity`](https://apireference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) property can be used to control the relative proximity between textual elements and means that distance is normed by the font size. Larger fonts may have bigger distances between syllables and still be looked at as a single whole. It is specified as a percentage of the font size, for example, 1 = 100%. This means that two characters of 12pt that are placed 12 pt apart are proximal.
- [`RecognitionBullets`](https://apireference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) is used to switch on the recognition of bullets during conversion.

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
        // Enable the value to recognize bullets during conversion process
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```

