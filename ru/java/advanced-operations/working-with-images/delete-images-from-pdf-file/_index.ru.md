---
title: Удаление Изображений из PDF Файла
linktitle: Удаление Изображений
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Этот раздел объясняет, как удалить изображения из PDF файла, используя Aspose.PDF для Java.
lastmod: "2021-06-05"
---

Чтобы удалить изображение из PDF файла, просто используйте метод delete(..) коллекции Images.

1. Создайте объект Document и откройте входной PDF файл.
1. Получите страницу, содержащую изображение, из коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Изображения находятся в коллекции Images, которая содержится в коллекции [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) страницы.
1. Удалите изображение с помощью метода Delete коллекции Images.
1. Сохраните результат, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как удалить изображение из PDF файла.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Создать штамп номера страницы
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Является ли штамп фоном
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Страница # из " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Установить свойства текста
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Добавить штамп на конкретную страницу
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Сохранить выходной документ
        pdfDocument.save(_dataDir);

    }
}
```