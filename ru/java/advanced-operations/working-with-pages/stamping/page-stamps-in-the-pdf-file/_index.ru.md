---
title: Добавить Штамп Страницы в PDF
linktitle: Штампы страниц в PDF файле
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Добавьте штамп страницы в PDF файл, используя класс PdfPageStamp с Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить Штамп Страницы с использованием Java

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) может быть использован, когда необходимо применить составной штамп, содержащий графику, текст, таблицы. Следующий пример показывает, как использовать штамп для создания канцелярии, как в Adobe InDesign, Illustrator, Microsoft Word. Предположим, у нас есть входной документ, и мы хотим применить 2 вида границ с синим и сливовым цветом.

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