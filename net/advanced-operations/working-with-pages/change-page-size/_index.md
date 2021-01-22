---
title: Change PDF Page Size Programmatically with C#
linktitle: Change PDF Page Size
type: docs
weight: 40
url: /net/change-page-size/
description: Change Page Size from your PDF file using C# library.
lastmod: "2021-01-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Change PDF Page Size

Aspose.PDF for .NET lets you change PDF page size with simple lines of code in your .NET applications. This topic explains how to update/change the page dimensions (size) of an existing PDF file.

The [Page](https://apireference.aspose.com/net/pdf/aspose.pdf/page) class contains the SetPageSize(...) method which lets you set the page size. The code snippet below updates page dimensions in a few easy steps:

1. Load the source PDF file.
1. Get the pages into the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) object.
1. Get a given page.
1. Call the SetPageSize(..) method to update its dimensions.
1. Call the [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class' Save(..) method to generate the PDF file with updated page dimensions.

{{% alert color="primary" %}}

Please note that the height and width properties use points as basic unit, where 1 inch = 72 points and 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 points.

{{% /alert %}}

The following code snippet shows how to change the PDF page dimensions to A4 size.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

### **Get PDF Page Size**

You can read PDF page size of an existing PDF file using Aspose.PDF for .NET. The following code sample shows how to read PDF page dimensions using C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}
