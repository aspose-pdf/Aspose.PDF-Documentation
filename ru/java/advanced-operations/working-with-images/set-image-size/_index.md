---
title: Установить Размер Изображения
linktitle: Установить Размер Изображения
type: docs
weight: 80
url: /ru/java/set-image-size/
description: Этот раздел описывает, как установить размер изображения в PDF файле, используя библиотеку Java.
lastmod: "2021-06-05"
---

Возможно установить размер изображения, которое добавляется в PDF файл. Чтобы задать размер, вы можете использовать методы [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) и [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) класса com.aspose.pdf.Image.

Следующий фрагмент кода демонстрирует, как установить размер изображения:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Создание экземпляра объекта Document
        Document doc = new Document();
        // добавление страницы в коллекцию страниц PDF файла
        Page page = doc.getPages().add();
        // Создание экземпляра изображения
        Image img = new Image();
        // Установить ширину и высоту изображения в пунктах
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Установить тип изображения как SVG
        img.setFileType (ImageFileType.Svg);
        // Путь к исходному файлу
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Установить свойства страницы
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // сохранить полученный PDF файл
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```