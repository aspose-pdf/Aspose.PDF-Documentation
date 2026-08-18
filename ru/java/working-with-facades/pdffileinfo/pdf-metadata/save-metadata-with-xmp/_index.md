---
title: Сохранение метаданных с помощью XMP
linktitle: Сохранение метаданных с помощью XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: Узнайте, как сохранить метаданные PDF с помощью XMP на Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение метаданных PDF с помощью XMP с использованием Aspose.PDF для Java
Abstract: Узнайте, как сохранить метаданные PDF с помощью XMP, используя Aspose.PDF для Java. Пример Java обновляет основные поля метаданных с помощью PdfFileInfo и записывает их обратно с помощью `saveNewInfoWithXmp()`, поэтому выходной документ сохраняет информацию в форме XMP.
---
## Сохраняйте метаданные с помощью XMP

Используйте этот рабочий процесс, если вам нужно сохранить обновленную информацию о документе в формате XMP.

### Шаги

1. Создайте объект `PdfFileInfo` для исходного PDF-файла.
2. Задайте поля метаданных, которые вы хотите обновить, например тему, заголовок, ключевые слова и создателя.
3. Вызовите `saveNewInfoWithXmp()`, указав путь к выходному файлу.
4. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
