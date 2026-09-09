---
title: Сохранить метаданные с помощью XMP
linktitle: Сохранить метаданные с помощью XMP
type: docs
weight: 30
url: /ru/java/save-metadata-with-xmp/
description: Узнайте, как сохранить метаданные PDF с помощью XMP в Java, используя фасад PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение метаданных PDF с помощью XMP с использованием Aspose.PDF for Java
Abstract: Узнайте, как сохранить метаданные PDF с помощью XMP, используя Aspose.PDF for Java. Пример на Java обновляет основные поля метаданных с помощью PdfFileInfo и записывает их обратно, используя `saveNewInfoWithXmp()`, так что выходной документ сохраняет информацию в формате XMP.
---
## Сохраните метаданные с помощью XMP

Используйте этот рабочий процесс, когда необходимо, чтобы обновлённая информация о документе сохранялась в формате XMP.

### Шаги

1. Создайте `PdfFileInfo` объект для исходного PDF.
2. Установите поля метаданных, которые вы хотите обновить, такие как тема, заголовок, ключевые слова и создатель.
3. Вызовите `saveNewInfoWithXmp()` с путем к выходному файлу.
4. Закройте `PdfFileInfo` экземпляр.

### Пример на Java

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


