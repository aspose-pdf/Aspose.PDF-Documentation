---
title: Move PDF Pages programmatically C#
linktitle: Move PDF Pages 
type: docs
weight: 10
url: /net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for .NET.
lastmod: "2020-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document. To insert an empty page at the end of a PDF file.

## Insert Page in PDF File at Desired Location

This topic explains how to insert a page in a PDF document using C#. The new page is inserted as an empty page at the specified index. To insert an empty page in a PDF file:

1. Create a [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection’s [Add](https://apireference.aspose.com/net/pdf/aspose.pdf.pagecollection/add/methods/1) method, without any parameters.
1. Save the output PDF using the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method.
The following code snippet shows you how to insert a page in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Open document
Document pdfDocument1 = new Document(dataDir + "InsertEmptyPage.pdf");

// Insert a empty page in a PDF
pdfDocument1.Pages.Insert(2);
dataDir = dataDir + "InsertEmptyPage_out.pdf";
// Save output file
pdfDocument1.Save(dataDir);
```

## Insert Empty Page at the End of PDF File

1. Create a [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection’s [Add](https://apireference.aspose.com/net/pdf/aspose.pdf.pagecollection/add/methods/1) method, without any parameters.
1. Save the output PDF using the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Open document
Document pdfDocument1 = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Insert an empty page at the end of a PDF file
pdfDocument1.Pages.Add();

dataDir = dataDir + "InsertEmptyPageAtEnd_out.pdf";
// Save output file
pdfDocument1.Save(dataDir);
```