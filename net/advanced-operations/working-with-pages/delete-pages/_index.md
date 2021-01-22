---
title: Delete PDF Pages programmatically C#
linktitle: Delete PDF Pages
type: docs
weight: 20
url: /net/delete-pages/
description: You can delete pages from your PDF file using C# library.
lastmod: "2021-01-22"
aliases:
    - /pdf/net/delete-pdf-pages/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

You can delete pages from a PDF file using Aspose.PDF for .NET. To delete a particular page from the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection.

## Delete Page from PDF File

1. Call the [Delete](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection/methods/delete) method and specify the page’s index
1. Call the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method to save the updated PDF file
The following code snippet shows how to delete a particular page from the PDF file using C#.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteParticularPage.pdf");

// Delete a particular page
pdfDocument.Pages.Delete(2);

dataDir = dataDir + "DeleteParticularPage_out.pdf";
// Save updated PDF
pdfDocument.Save(dataDir);
```
