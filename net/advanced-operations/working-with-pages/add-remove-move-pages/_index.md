---
title: Add, remove, move Pages
type: docs
weight: 10
url: /net/add-remove-move-pages/
description: This article shows how to insert a page in a PDF file at the desired location, how to Insert an empty page at the end of a PDF file, and explains how to delete a page from a PDF file with C#.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for .NET API provides full flexibility to work with pages in a PDF document using C# or any other .NET language. It maintains all the pages of a PDF document in [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) that can be used to work with PDG pages. 
Aspose.PDF for .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. This section shows how to add pages to a PDF without Acrobat Reader.

## Insert Page in a PDF File at Desired Location

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

## Insert an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document. To insert an empty page at the end of a PDF file:

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

## Delete a Page from PDF File

You can delete pages from a PDF file using Aspose.PDF for .NET. To delete a particular page from the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection:

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
