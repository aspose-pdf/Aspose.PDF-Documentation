---
title: Добавление штампов страниц в PDF
linktitle: Штампы страниц в PDF файле
type: docs
weight: 30
url: ru/cpp/page-stamps-in-the-pdf-file/
description: Добавьте штамп страницы в PDF файл, используя класс PdfPageStamp с C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление штампа страницы с C++

[PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) может быть использован, когда вам нужно применить составной штамп, содержащий графику, текст, таблицы. Следующий пример показывает, как использовать штамп для создания канцелярских принадлежностей, как в Adobe InDesign, Illustrator, Microsoft Word. Предположим, у нас есть входной документ, и мы хотим применить 2 вида границ с синим и сливовым цветом.

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