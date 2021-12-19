---
title: Add PDF Page Stamps in PDF 
linktitle: Page stamps in PDF File
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: Add a page stamp to a PDF file using the PdfPageStamp class with C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Page Stamp with C++

A [PdfPageStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) can be used when you need to apply a composite stamp containing graphics, text, tables. The following example shows how to use a stamp to create stationery like in using Adobe InDesign, Illustrator, Microsoft Word. Assume we have some input document and we want apply 2 kinds of border with blue and plum color.

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```
