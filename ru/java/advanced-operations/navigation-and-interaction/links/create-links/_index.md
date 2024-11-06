---
title: Создание ссылок в PDF файле
linktitle: Создание ссылок
type: docs
weight: 10
url: ru/java/create-links/
description: Этот раздел объясняет, как создавать ссылки в вашем PDF документе с помощью Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Создание ссылок

Aspose.PDF для Java позволяет добавить ссылку на внешний PDF файл, чтобы можно было связать несколько документов вместе. Добавляя ссылку на приложение в документ, можно связывать приложения с документом. Это полезно, когда вы хотите, чтобы читатели совершили определенное действие в определенной точке учебника, например, или чтобы создать документ с богатым функционалом. Чтобы создать ссылку на приложение:

1. [Создайте объект Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Получите [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), на которую хотите добавить ссылку.

1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) с использованием объектов [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) и [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Установите атрибуты ссылки, используя объект [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Также установите для объекта [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) и вызовите метод setAction(..).
1. При создании объекта [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) укажите приложение, которое вы хотите запустить.
1. Добавьте ссылку в коллекцию [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) объекта Page.
1. Наконец, сохраните обновленный PDF, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как создать ссылку на приложение в PDF-файле.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Открыть документ
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Создать ссылку
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Сохранить обновленный документ
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Создание ссылки на PDF-документ в PDF-файле

Aspose.PDF для Java позволяет добавлять ссылку на внешний PDF-файл, чтобы вы могли связывать несколько документов вместе.
 Для создания ссылки на PDF документ:

1. Сначала создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Затем получите конкретную [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), к которой вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) с использованием объектов [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) и [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Установите атрибуты ссылки с помощью объекта [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Вызовите метод setAction(..) и передайте объект [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. При создании объекта [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction), укажите PDF файл, который должен открыться, а также номер страницы, на которой он должен открыться.
1. Добавьте ссылку в коллекцию [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) объекта Page.
1. Наконец, сохраните обновленный PDF, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как создать ссылку на документ PDF в файле PDF.

```java
    public static void CreatePDFDocumentLink() {

        // Открыть документ
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Создать ссылку
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Сохранить обновленный документ
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```