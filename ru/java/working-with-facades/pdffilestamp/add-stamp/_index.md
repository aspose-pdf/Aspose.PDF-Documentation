---
title: Добавить штамп в PDF
linktitle: Добавить штамп в PDF
type: docs
weight: 40
url: /java/add-stamp/
description: Узнайте, как добавить штамп изображения на страницы PDF в Java с помощью фасада PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление штампов изображений в PDF на Java
Abstract: Узнайте, как добавить содержимое штампа в PDF-документы с помощью Aspose.PDF для Java, используя фасад PdfFileStamp. Текущий набор примеров Java показывает, как создать `Stamp`, связать его с файлом изображения, добавить в документ и сохранить PDF-файл с отметкой.
---
## Добавьте штамп в PDF

Используйте этот рабочий процесс, если к PDF-файлу необходимо применить штамп на основе изображения.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте объект `Stamp`.
3. Привяжите штамп к файлу изображения с помощью `bindImage`.
4. Добавьте штамп в документ с помощью `addStamp`.
5. Сохраните вывод и закройте объект фасада.

### Пример Java

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

Текущий класс `PdfFileStampExamples.java` не включает отдельный пример Java для текстовых штампов, поворота или конфигурации непрозрачности.
