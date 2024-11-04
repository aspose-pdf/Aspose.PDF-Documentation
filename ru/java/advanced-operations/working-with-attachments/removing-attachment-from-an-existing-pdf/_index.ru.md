---
title: Удаление вложения из существующего PDF 
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF-документов. Используйте Java PDF API для удаления вложений в PDF-файлах с помощью библиотеки Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF может удалять вложения из PDF-файлов. Вложения PDF-документа хранятся в коллекции EmbeddedFiles объекта Document.

Вложения PDF-документа хранятся в коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Чтобы удалить все вложения, связанные с PDF-файлом:

1. Вызовите метод delete(..) коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. Сохраните обновленный файл, используя метод save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как удалить все вложения из PDF-документа.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Открыть документ
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Удалить все вложения
  pdfDocument.getEmbeddedFiles().delete();
  // Сохранить обновленный файл
  pdfDocument.save("output.pdf");

    }
```