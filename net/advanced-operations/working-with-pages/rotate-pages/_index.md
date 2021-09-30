---
title: Rotate PDF Pages Using C#
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /net/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with C#.
lastmod: "2021-09-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with C#.

## Change Page Orientation

From Aspose.PDF for .NET 9.6.0 release, we have added great new features like changing the page orientation from landscape to portrait and vice versa. To change the page orientation, set the page’s MediaBox using the following code snippet. You can also change page orientation by setting rotation angle using Rotate() method.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ChangeOrientation-ChangeOrientation.cs" >}}

## Fitting the Page Content to the New Page Orientation

Please note that when using the above code snippet, some of the document’s content might be cut because the page height is decreased. To avoid this, increase width proportionally and leave the height intact. Example of calculations:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-FitPageContents-FitPageContents.cs" >}}

Besides the above approach, consider using the PdfPageEditor facade which can apply zoom to the page contents).

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ZoomToPageContents-ZoomToPageContents.cs" >}}