---
title: Move PDF Pages programmatically C#
linktitle: Move PDF Pages
type: docs
weight: 20
url: /net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using C#.
To move an page we should:

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class object with the destination PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
1. [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the destination document.
1. Save the output PDF using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.
1. [Delete](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) page in source document.
1. Save the source PDF using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to move one page.

```csharp
public static void MovePage()
{
    var srcFileName = "<enter file name>";
    var dstFileName = "<enter file name>";
    var srcDocument = new Aspose.Pdf.Document();
    var dstDocument = new Aspose.Pdf.Document();
    var page = srcDocument.Pages[2];
    dstDocument.Pages.Add(page);
    // Save output file
    dstDocument.Save(srcFileName);
    srcDocument.Pages.Delete(2);
    srcDocument.Save(dstFileName);
}
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class object with the destination PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
    1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
    1. [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the destination document.
1. Save the output PDF using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.
1. [Delete](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) page in source document using array.
1. Save the source PDF using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```csharp
public static void MoveBunchPages()
{
    var srcFileName = "<enter file name>";
    var dstFileName = "<enter file name>";
    var srcDocument = new Aspose.Pdf.Document(srcFileName);
    var dstDocument = new Aspose.Pdf.Document();
    var pages = new []{ 1, 3 };
    foreach (var pageIndex in pages)
    {
        var page = srcDocument.Pages[pageIndex];
        dstDocument.Pages.Add(page);
    }                       
    // Save output files
    dstDocument.Save(srcFileName);
    srcDocument.Pages.Delete(pages);
    srcDocument.Save(dstFileName);
}
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
1. [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the new location (for example to end).
1. [Delete](https://apireference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) page in previous location.
1. Save the output PDF using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

```csharp
public static void MovePagesInOnePDF()
{
    var srcFileName = "<enter file name>";
    var dstFileName = "<enter file name>";
    var srcDocument = new Aspose.Pdf.Document(srcFileName);
   
    var page = srcDocument.Pages[2];
    srcDocument.Pages.Add(page);
    srcDocument.Pages.Delete(2);          
   
    // Save output file
    srcDocument.Save(dstFileName);
}
```
