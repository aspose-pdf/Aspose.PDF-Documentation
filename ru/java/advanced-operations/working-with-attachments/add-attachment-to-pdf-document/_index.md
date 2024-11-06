---
title: Добавление вложения в PDF документ 
linktitle: Добавление вложения в PDF документ 
type: docs
weight: 10
url: ru/java/add-attachment-to-pdf-document/
description: На этой странице описывается, как добавить вложение в PDF файл с помощью Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вложения могут содержать широкий спектр информации и могут быть различных типов файлов. В этой статье объясняется, как добавить вложение в PDF файл.

1. Создайте объект [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), содержащий файл, который вы хотите прикрепить, и описание файла.

1. Добавьте объект [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) в коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с помощью метода [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) содержит все вложения, добавленные в файл PDF.

Следующий фрагмент кода показывает, как добавить вложение в PDF-документ.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Настроить новый файл, который будет добавлен как вложение
        FileSpecification fileSpecification = new FileSpecification("sample.txt", "Пример текстового файла");
        // Добавить вложение в коллекцию вложений документа
        pdfDocument.getEmbeddedFiles().add(fileSpecification);
        // Сохранить обновленный документ
        pdfDocument.save("output.pdf");
    }
}
```