---
title: Split PDF programmatically
linktitle: Split PDF files
type: docs
weight: 60
url: /net/split-pdf-document/
description: This topic shows how to split PDF pages into individual PDF files in your .NET applications with C#.
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
lastmod: "2021-01-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is an online free web application that allows you to investigate how presentation splitting functionality works.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This topic shows how to split PDF pages into individual PDF files in your .NET applications. To split PDF pages into single page PDF files using C#, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) object's [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection
1. For each iteration, create a new Document object and add the individual [Page](https://apireference.aspose.com/net/pdf/aspose.pdf/page) object into the empty document
1. Save the new PDF using [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method

The following C# code snippet shows you how to split PDF pages into individual PDF files.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Open document
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// Loop through all the pages
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```
