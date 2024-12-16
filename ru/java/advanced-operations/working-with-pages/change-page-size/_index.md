---
title: Изменение размера страницы PDF программно
linktitle: Изменить размер страницы
type: docs
weight: 50
url: /ru/java/change-page-size/
description: Изменение размера страницы в PDF файле с использованием Java библиотеки.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Изменение размера страницы PDF

Aspose.PDF for Java позволяет изменить размер страницы PDF с помощью простых строк кода в ваших Java приложениях. Эта тема объясняет, как обновить/изменить размеры (размер) страницы существующего PDF файла.

Класс [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) содержит метод SetPageSize(...), который позволяет установить размер страницы. Пример кода ниже обновляет размеры страницы в несколько простых шагов:

1. Загрузите исходный PDF файл.
1. Получите страницы в объект [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Получите заданную страницу.
1. Вызовите метод SetPageSize(..) для обновления её размеров.

1. Вызовите метод Save(..) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) для создания PDF-файла с обновленными размерами страницы.

{{% alert color="primary" %}}

Обратите внимание, что свойства высоты и ширины используют точки в качестве основной единицы, где 1 дюйм = 72 точки и 1 см = 1/2.54 дюйма = 0.3937 дюйма = 28.3 точки.

{{% /alert %}}

Следующий фрагмент кода показывает, как изменить размеры страницы PDF на формат A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Открыть первый документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Получить коллекцию страниц
        PageCollection pageCollection = pdfDocument.getPages();

        // Получить конкретную страницу
        Page pdfPage = pageCollection.get_Item(1);

        // Установить размер страницы как A4 (11.7 x 8.3 дюйма), и в Aspose.Pdf, 1 дюйм = 72 точки
        // Таким образом, размеры A4 в точках будут (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Сохранить обновленный документ
        pdfDocument.save(_dataDir);
    }
```


## Получить размер страницы PDF

Вы можете прочитать размер страницы PDF существующего PDF файла, используя Aspose.PDF для Java. Пример кода ниже показывает, как прочитать размеры страницы PDF с использованием Java.

```java
    public static void GetPDFPageSize() {
        
        // Открыть первый документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Добавляет пустую страницу в PDF документ
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Получить информацию о высоте и ширине страницы
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Повернуть страницу на 90 градусов
        page.setRotate (Rotation.on90);

        // Получить информацию о высоте и ширине страницы
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Сохранить обновленный документ
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```