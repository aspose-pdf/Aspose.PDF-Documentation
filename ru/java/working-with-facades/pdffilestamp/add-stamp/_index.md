---
title: Добавление штампа в PDF
linktitle: Добавление штампа в PDF
type: docs
weight: 40
url: /ru/java/add-stamp/
description: Узнайте, как добавить штамп‑изображение на страницы PDF в Java с помощью фасада PdfFileStamp.
lastmod: "2026-09-17"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить штампы‑изображения в PDF на Java
Abstract: Узнайте, как добавить содержимое штампа в PDF‑документы с помощью Aspose.PDF for Java, используя фасад PdfFileStamp. Текущий набор примеров на Java показывает, как создать `Stamp`, привязать его к файлу изображения, добавить в документ и сохранить штампованный PDF.
---
## Добавление штампа в PDF

Используйте этот процесс, когда необходимо применить штамп на основе изображения к PDF.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF.
2. Создайте объект `Stamp`.
3. Привяжите штамп к файлу изображения с помощью `bindImage`.
4. Добавьте штамп к документу с `addStamp`.
5. Сохраните результат и закройте объект фасада.

### Пример на Java

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

Текущий класс `PdfFileStampExamples.java` не включает отдельный пример на Java для штампов только с текстом, вращения или настройки непрозрачности.


