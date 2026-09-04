---
title: Установить метаданные PDF
linktitle: Установить метаданные PDF
type: docs
weight: 50
url: /ru/java/set-pdf-metadata/
description: Узнайте, как обновлять метаданные PDF в Java с помощью фасада PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновление метаданных PDF с использованием Aspose.PDF for Java
Abstract: Узнайте, как обновлять метаданные PDF с помощью Aspose.PDF for Java. Пример на Java использует PdfFileInfo для установки стандартных полей метаданных, таких как subject, title, keywords и creator, добавляет пользовательскую запись метаданных и сохраняет результат в новый PDF.
---
## Установите метаданные PDF

Используйте этот рабочий процесс, когда необходимо нормализовать или обогатить информацию о документе перед сохранением PDF.

### Шаги

1. Создайте `PdfFileInfo` объект для исходного PDF.
2. Установите стандартные поля метаданных, которые вы хотите обновить.
3. Добавьте любые пользовательские метаданные с `setMetaInfo`.
4. Сохраните обновлённый документ с `save()`.
5. Закройте `PdfFileInfo` экземпляр.

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


