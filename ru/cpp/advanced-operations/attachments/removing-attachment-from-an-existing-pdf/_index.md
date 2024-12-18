---
title: Удаление вложений из PDF
linktitle: Удаление вложений из существующего PDF
type: docs
weight: 30
url: /ru/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF для C++ может удалять вложения из ваших PDF-документов. Используйте C++ PDF API для удаления вложений в PDF-файлах с помощью библиотеки Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF может удалять вложения из PDF-файлов. Вложения PDF-документа хранятся в коллекции EmbeddedFiles объекта Document.

Чтобы удалить все вложения, связанные с PDF-файлом:

1. Вызовите метод [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
2. Сохраните обновленный файл, используя метод Save объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Следующий фрагмент кода показывает, как удалить вложения из PDF-документа.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Открыть документ
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Удалить все вложения
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Сохранить обновленный файл
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```