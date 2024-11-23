---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /net/save-pdf-document/
description: Learn how to save PDF file in C# Aspose.PDF for .NET PDF library. Save PDF document to file system, to stream, and in Web applications.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The next code snippet also works with [Aspose.Drawing](/pdf/net/drawing/) library.

## Save PDF document to file system

You can save the created or manipulated PDF document to file system using `Save` method of `Document` class.
When you do not provide the format type (options), then the document is saved in Aspose.PDF v.1.7 (*.pdf) format.

```csharp
public static void SaveDocument()
{
    var originalFileName = _dataDir + "SimpleResume.pdf";
    var modifiedFileName = _dataDir + "SimpleResumeModified.pdf";

    var document = new Document(originalFileName);
    // make some manipation, i.g add new empty page
    document.Pages.Add();
    document.Save(modifiedFileName);
}
```

## Save PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of `Save` methods.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = _dataDir + "SimpleResume.pdf";
    var modifiedFileName = _dataDir + "SimpleResumeModified.pdf";

    var document = new Document(originalFileName);
    // make some manipation, i.g add new empty page
    document.Pages.Add();
    document.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Save PDF document in Web applications

To save documents in Web applications, you can use the ways proposed above. In addition, the `Document` class has overloaded method `Save` for using with the [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8) class.

```csharp
var originalFileName = _dataDir + "SimpleResume.pdf";
var document = new Document(originalFileName);
// make some manipulation, i.g add a new empty page
document.Pages.Add();
document.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```

For more detailed explanation please follow to [Showcase](/pdf/net/showcases/) section.

## Save PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF/A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the `Save` method is used to store the documents, while the documents must be prepared using the `Convert` method.

```csharp
public static void SaveDocumentAsPDFx()
{
    var document = new Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    document.Pages.Add();
    document.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```
