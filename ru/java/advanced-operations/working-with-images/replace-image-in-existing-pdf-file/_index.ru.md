---
title: Замена Изображения в Существующем PDF Файле
linktitle: Замена Изображения
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: В этом разделе описывается замена изображения в существующем PDF файле с использованием библиотеки Java.
lastmod: "2021-06-05"
---

Метод [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) коллекции [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) позволяет заменить изображение в существующем PDF файле.

Коллекция Images находится в коллекции ресурсов страницы. Чтобы заменить изображение:

1. Откройте PDF файл с помощью объекта Document.
2. Замените конкретное изображение, сохраните обновленный PDF файл с помощью метода Save объекта Document.

Следующий фрагмент кода показывает, как заменить изображение в PDF файле.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Открыть документ
        Document pdfDocument = new Document("input.pdf");
        // Заменить конкретное изображение
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Автоматически сгенерированный блок catch
            e.printStackTrace();
        }
        // Сохранить обновленный PDF файл
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```