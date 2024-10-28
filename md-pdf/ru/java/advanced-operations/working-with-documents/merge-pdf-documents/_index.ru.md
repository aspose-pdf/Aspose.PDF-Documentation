---
title: Объединение PDF программно
linktitle: Объединение PDF файлов
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Эта страница объясняет, как объединить PDF-документы в один PDF-файл с помощью Java.
lastmod: "2021-06-05"
---

Теперь объединение PDF-файлов — одна из самых востребованных задач.
Эта статья показывает, как объединить несколько PDF-файлов в один PDF-документ с использованием Aspose.PDF для Java. Пример написан на Java, но API можно использовать и в других языках программирования. PDF-файлы объединяются так, что первый присоединяется в конце другого документа.

## Объединение PDF файлов с использованием Java

{{% alert color="primary" %}}

Вы можете объединить PDF-файлы, используя Aspose.PDF, и получить результаты онлайн по этой ссылке: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Чтобы объединить два PDF-файла:

1. Создайте два объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), каждый из которых содержит один из входных PDF-файлов.

1. Затем вызовите метод Add коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) для объекта Document, в который вы хотите добавить другой файл PDF.
1. Передайте коллекцию PageCollection второго объекта Document методу Add первой коллекции PageCollection.
1. Наконец, сохраните выходной PDF-файл, используя метод Save.

Следующий фрагмент кода показывает, как объединить PDF-файлы с помощью Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // Путь к каталогу с документами.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Открыть первый документ
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Открыть второй документ
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Добавить страницы второго документа к первому
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Сохранить объединенный выходной файл
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```