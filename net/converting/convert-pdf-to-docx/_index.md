---
title: Convert PDF to DOCX | C#
linktitle: Convert PDF to DOCX
type: docs
weight: 80
url: /net/convert-pdf-to-docx/
lastmod: "2021-01-15"
description: Convert PDF file to DOCX format with ease and full control with Aspose.PDF for .NET. 
aliases:
    - /pdf/net/convert-pdf-to-doc-and-docx/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convert PDF to DOCX

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this  link [products.aspose.app/pdf/conversion/pdf-to-docx](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

Aspose.PDF for .NET API lets you read and convert PDF documents to DOCX using C# and any .NET language. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.  

For quick conversion use `Save()` method with `SaveFormat.DocX` options:

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Open the source PDF document
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Save the resultant DOC file
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

The [`DocSaveOptions`](https://apireference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) class has a property named Format which provides the capability to specify the format of the resultant document, that is, DOC or DOCX. In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

Please take a look over the following code snippet which provides the capability to convert PDF file to DOCX format with C#.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Open the source PDF document
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Instantiate DocSaveOptions object
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Specify the output format as DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // Set other DocSaveOptions params
        // ....
    };
    // Save document in docx format
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
