---
title: Add PDF Page Stamps in PDF using C#
linktitle: Page stamps in PDF File
type: docs
weight: 30
url: /net/page-stamps-in-the-pdf-file/
description: Add a page stamp to a PDF document using the PdfPageStamp class with Aspose.PDF for .NET library.
lastmod: "2021-09-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Page Stamp with C\#

A [PdfPageStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp) can be used when you need to apply a composite stamp containing graphics, text, tables. The following example shows how to use a stamp to create stationery like in using Adobe InDesign, Illustrator, Microsoft Word. Assume we have some input document and we want apply 2 kinds of border with blue and plum color.

```csharp
public static void AddPageStamp()
{
    var inputFileName = "sample-4pages.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "PageStamp.pdf";
    var document = new Document(_dataDir + inputFileName);

    var bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1)
    {
        Height = 800,
        Background = true
    };

    var plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2)
    {
        Height = 800,
        Background = true
    };

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.Pages[i].AddStamp(bluePageStamp);
        else
            document.Pages[i].AddStamp(plumPageStamp);
    }

    document.Save(_dataDir + outputFileName);
}
```
