---
title: Поворот страниц PDF программным способом
linktitle: Поворот страниц PDF
type: docs
weight: 60
url: ru/java/rotate-pages/
description: Изменение ориентации страницы и подгонка содержимого страницы под новую ориентацию страницы с использованием Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Изменение ориентации страницы

Эта статья описывает, как обновить или изменить ориентацию страниц в существующем PDF-файле.

Aspose.PDF для Java имеет функцию изменения ориентации страницы с альбомной на портретную и наоборот. Чтобы изменить ориентацию страницы, установите [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) страницы, используя следующий фрагмент кода.

Вы также можете изменить ориентацию страницы, установив угол поворота с помощью метода Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // Мы должны переместить страницу вверх, чтобы компенсировать изменение размера страницы
            // // (нижний край страницы - это 0,0, и информация обычно размещается от
            // // Верхней части страницы. Вот почему мы перемещаем нижний край вверх на разницу между
            // // старой и новой высотой.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // Иногда нам также нужно установить CropBox (если он был установлен в оригинальном файле)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Установка угла поворота страницы
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Сохранить выходной файл
        pdfDocument.save(_dataDir);
    }    
}
```