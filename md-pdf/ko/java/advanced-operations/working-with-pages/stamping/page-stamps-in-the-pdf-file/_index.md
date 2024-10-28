---
title: Add PDF Page Stamp to PDF 
linktitle: Page stamps in PDF File
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Add a Page stamp to a PDF file using the PdfPageStamp class with Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Page Stamp with Java

A [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) can be used when you need to apply a composite stamp containing graphics, text, tables. The following example shows how to use a stamp to create stationery like in using Adobe InDesign, Illustrator, Microsoft Word. Assume we have some input document and we want apply 2 kinds of border with blue and plum color.

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```
