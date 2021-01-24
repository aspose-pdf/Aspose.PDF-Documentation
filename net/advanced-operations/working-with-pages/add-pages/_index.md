---
title: Add Pages in PDF with C#
linktitle: Add Pages
type: docs
weight: 10
url: /net/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using C#.
lastmod: "2020-12-22"
aliases:
    - /net/insert-pdf-pages/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. This section shows how to add pages to a PDF without Acrobat Reader.

Aspose.PDF for .NET API provides full flexibility to work with pages in a PDF document using C# or any other .NET language. It maintains all the pages of a PDF document in [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) that can be used to work with PDF pages.

Check out all the possibilities of the Aspose.PDF for .NET library in working with Pages:

- Insert pages into a PDF
- [Move Pages](/pdf/net/move-pages/)
- [Delete pages from a PDF](/pdf/net/delete-pages/)
- Change page size of a PDF
- Rotate pages in a PDF
- Split PDF Pages into one or multiple PDF

## Add or Insert Page in a PDF File

Aspose.PDF for .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. This section shows how to add pages to a PDF without Acrobat Reader. 

### Insert Page in a PDF File at Desired Location

This topic explains how to insert a page in a PDF document using C#. The new page is inserted as an empty page at the specified index. To insert an empty page in a PDF file:

1. Create a [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection's [Add](https://apireference.aspose.com/net/pdf/aspose.pdf.pagecollection/add/methods/1) method, without any parameters.
1. Save the output PDF using the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert a page in a PDF file.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-InsertEmptyPage-InsertEmptyPage.cs" >}}

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document. To insert an empty page at the end of a PDF file:

1. Create a [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection's [Add](https://apireference.aspose.com/net/pdf/aspose.pdf.pagecollection/add/methods/1) method, without any parameters.
1. Save the output PDF using the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-InsertEmptyPageAtEnd-InsertEmptyPageAtEnd.cs" >}}
