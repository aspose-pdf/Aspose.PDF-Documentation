---
title: Программное обрезание страниц PDF
linktitle: Обрезка страниц
type: docs
weight: 80
url: /java/crop-pages/
description: Вы можете получить свойства страницы, такие как ширина, высота, поля обрезки и обрезной блок, используя Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение свойств страницы

Каждая страница в PDF файле имеет ряд свойств, таких как ширина, высота, поля обрезки и обрезной блок. Aspose.PDF для Java позволяет вам получить доступ к этим свойствам.

- **Медиабокс**: Медиабокс — это самый большой блок страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т. д.), выбранному при печати документа в PostScript или PDF. Другими словами, медиабокс определяет физический размер носителя, на котором отображается или печатается PDF документ.
- **Бокс для обрезки**: Если документ имеет поля обрезки, у PDF также будет бокс для обрезки.
 Bleed - это количество цвета (или графики), которое выходит за край страницы. Оно используется, чтобы убедиться, что когда документ будет напечатан и обрезан до нужного размера ("по линии реза"), чернила будут доходить до края страницы. Даже если страница будет обрезана неправильно - срезана немного за пределами меток обрезки - на странице не появятся белые края.
- **Trim box**: Trim box обозначает окончательный размер документа после печати и обрезки.
- **Art box**: Art box - это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка страницы используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box - это размер "страницы", при котором ваш PDF-документ отображается в Adobe Acrobat. В нормальном режиме отображается только содержимое crop box в Adobe Acrobat. Для подробного описания этих свойств прочитайте спецификацию Adobe.Pdf, в частности 10.10.1 Page Boundaries.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Картинка ниже иллюстрирует эти свойства.  
Для получения более подробной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Пример ниже показывает, как обрезать страницу:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // Создать новый Box Rectagle
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [здесь](crop_page.pdf). Изначально наша страница выглядит как показано на рисунке 1.  
![Рисунок 1. Обрезанная страница](crop_page.png)

После изменения страница будет выглядеть как на рисунке 2.  
![Рисунок 2. Обрезанная страница](crop_page2.png)