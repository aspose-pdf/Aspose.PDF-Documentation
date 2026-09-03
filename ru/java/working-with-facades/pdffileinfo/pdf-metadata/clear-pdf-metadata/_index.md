---
title: Очистить метаданные PDF
linktitle: Очистить метаданные PDF
type: docs
weight: 10
url: /ru/java/clear-pdf-metadata/
description: Узнайте, как очистить метаданные PDF в Java с помощью фасада PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Очистка метаданных PDF с помощью Aspose.PDF for Java
Abstract: Узнайте, как очистить метаданные PDF с помощью Aspose.PDF for Java. Пример на Java использует PdfFileInfo для удаления сохранённой информации о документе с помощью `clearInfo()`, а затем сохраняет очищенный PDF в новый файл.
---
## Очистите метаданные PDF

Используйте этот рабочий процесс, когда необходимо удалить сохранённую информацию о документе перед передачей или архивированием PDF.

### Шаги

1. Создайте `PdfFileInfo` объект для входного PDF.
2. Вызовите `clearInfo()` удалить метаданные документа.
3. Сохраните результат в новый файл с `save()`.
4. Закройте `PdfFileInfo` экземпляр.

### Пример на Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```


