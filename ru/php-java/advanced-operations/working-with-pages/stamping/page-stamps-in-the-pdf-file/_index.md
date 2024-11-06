---
title: Добавить Штамп Страницы в PDF
linktitle: Штампы страниц в PDF файле
type: docs
weight: 30
url: ru/php-java/page-stamps-in-the-pdf-file/
description: Добавьте штамп страницы в PDF файл с использованием класса PdfPageStamp на PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить Штамп Страницы

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) может быть использован, когда нужно применить составной штамп, содержащий графику, текст, таблицы. Следующий пример показывает, как использовать штамп для создания бланков, как в Adobe InDesign, Illustrator, Microsoft Word. Предположим, у нас есть входной документ, и мы хотим применить 2 вида границ с синим и сливовым цветом.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();  
```