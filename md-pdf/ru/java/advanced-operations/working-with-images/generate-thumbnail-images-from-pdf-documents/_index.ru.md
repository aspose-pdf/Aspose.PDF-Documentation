---
title: Генерация миниатюр изображений из PDF документов
linktitle: Генерация миниатюр изображений
type: docs
weight: 100
url: /java/generate-thumbnail-images-from-pdf-documents/
description: В этом разделе описывается, как создать миниатюры изображений из PDF документов с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
---

## Подход Aspose.PDF для Java

Aspose.PDF для Java предоставляет широкую поддержку для работы с PDF документами. Он также поддерживает возможность конвертации страниц PDF документов в различные форматы изображений. Описанную выше функциональность можно легко реализовать с использованием Aspose.PDF для Java.

Aspose.PDF имеет явные преимущества:

- Вам не нужно устанавливать Adobe Acrobat на свою систему для работы с PDF файлами.
- Использование Aspose.PDF для Java проще и легче для понимания по сравнению с автоматизацией Acrobat.

Если нам нужно конвертировать страницы PDF в JPEG, пространство имен [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) предоставляет класс с именем [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) для рендеринга страниц PDF в изображения JPEG.
 Пожалуйста, ознакомьтесь со следующим фрагментом кода.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // Получить имена всех PDF файлов в определенной директории
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Ошибка при чтении директории
        }

        // Перебрать все файлы в массиве
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Открыть документ
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Создать объект разрешения
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Конвертировать определенную страницу и сохранить изображение в поток
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Закрыть поток
                imageStream.close();
            }
        }

    }
}
```