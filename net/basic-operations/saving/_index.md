---
title: Saving a PDF
linktitle: Saving
type: docs
weight: 20
url: /net/save-pdf-document/
description: Learn how to save a PDF file in C# Aspose.PDF for .NET PDF library. 
aliases:
    - /net/saving/
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Saving a PDF document to file system

You can save the created or manipulated PDF document to file system using `Save` method of `Document` class.
When you do not provide the format type (options), then the document is saved in Aspose.PDF v.1.7 (*.pdf) format.

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // make some manipation, i.g add new empty page
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```

## Saving a PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of `Save` methods.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // make some manipation, i.g add new empty page
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Saving a PDF document in Web applications

To save documents in Web applications, you can use the ways proposed above. In addition, the `Document` class has overloaded method `Save` for using with the [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8) class.

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// make some manipulation, i.g add a new empty page
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```

For more detailed explanation please follow to [Showcase] section.

## Saving as PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF / A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the `Save` method is used to store the documents, while the documents must be prepared using the `Convert` method.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```
