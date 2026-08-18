---
title: Очистить метаданные PDF
linktitle: Очистить метаданные PDF
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: Узнайте, как очистить метаданные PDF в Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Очистка метаданных PDF с помощью Aspose.PDF для Java
Abstract: Узнайте, как очистить метаданные PDF с помощью Aspose.PDF для Java. В примере Java используется PdfFileInfo для удаления сохраненной информации о документе с помощью `clearInfo()`, а затем сохраняется очищенный PDF-файл в новый файл.
---
## Очистить метаданные PDF

Используйте этот рабочий процесс, если вам нужно удалить сохраненную информацию о документе перед отправкой или архивированием PDF-файла.

### Шаги

1. Создайте объект `PdfFileInfo` для входного PDF-файла.
2. Позвоните `clearInfo()`, чтобы удалить метаданные документа.
3. Сохраните результат в новый файл с помощью `save()`.
4. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
