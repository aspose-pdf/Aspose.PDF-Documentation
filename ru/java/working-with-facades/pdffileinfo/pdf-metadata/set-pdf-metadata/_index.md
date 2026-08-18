---
title: Установить метаданные PDF
linktitle: Установить метаданные PDF
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: Узнайте, как обновить метаданные PDF в Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновление метаданных PDF с помощью Aspose.PDF для Java
Abstract: Узнайте, как обновить метаданные PDF с помощью Aspose.PDF для Java. В примере Java используется PdfFileInfo для установки стандартных полей метаданных, таких как тема, заголовок, ключевые слова и создатель, добавляется пользовательская запись метаданных и сохраняется результат в новый PDF-файл.
---
## Установите метаданные PDF

Используйте этот рабочий процесс, когда вам нужно нормализовать или дополнить информацию о документе перед сохранением PDF-файла.

### Шаги

1. Создайте объект `PdfFileInfo` для исходного PDF-файла.
2. Установите стандартные поля метаданных, которые вы хотите обновить.
3. Добавьте любые пользовательские метаданные с помощью `setMetaInfo`.
4. Сохраните обновленный документ с помощью `save()`.
5. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
