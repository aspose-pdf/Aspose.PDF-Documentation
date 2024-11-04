---
title: Извлечение изображений из PDF файла
linktitle: Извлечение изображений
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Этот раздел показывает, как извлечь изображения из PDF файла с использованием Java библиотеки.
lastmod: "2021-06-05"
---

Каждая страница содержит коллекцию [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources), которая, в свою очередь, содержит коллекцию Images, где хранятся все изображения на странице. Объект [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) получает заданное изображение из коллекции Images.

Чтобы извлечь изображение со страницы:

Получите изображение из коллекции Images, используя индекс изображения.
Используйте метод save(..) объекта [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage), чтобы сохранить извлеченное изображение.

Следующий фрагмент кода показывает, как извлечь изображения из PDF файла.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Извлечь конкретное изображение
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Сохранить выходное изображение
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Сохранить обновленный PDF файл
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```