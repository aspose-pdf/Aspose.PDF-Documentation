---
title: Разделение PDF программно
linktitle: Разделение PDF файлов
type: docs
weight: 60
url: /java/split-document/
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших Java приложениях.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Вы можете разделить PDF файлы, используя Aspose.PDF, и получить результаты онлайн по этой ссылке: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Эта тема показывает, как разделить страницы PDF с помощью Aspose.PDF для Java на отдельные PDF файлы в ваших Java приложениях. Чтобы разделить страницы PDF на файлы с одной страницей, используя Java, можно следовать следующим шагам:

1. Переберите страницы PDF документа через коллекцию [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Для каждой итерации создайте новый объект Document и добавьте отдельный объект [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) в пустой документ.
1. Сохраните новый PDF, используя метод Save.

Следующий фрагмент кода на Java показывает, как разделить страницы PDF на отдельные PDF-файлы.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Перебрать все страницы
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```