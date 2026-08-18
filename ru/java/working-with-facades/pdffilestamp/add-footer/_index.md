---
title: Добавить нижний колонтитул в PDF
linktitle: Добавить нижний колонтитул в PDF
type: docs
weight: 10
url: /java/add-footer/
description: Узнайте, как добавлять нижние колонтитулы с текстом и изображениями на страницы PDF в Java с помощью фасада PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление нижних колонтитулов текста и изображений в PDF на Java
Abstract: Узнайте, как добавить содержимое нижнего колонтитула в PDF-документы с помощью Aspose.PDF для Java, используя фасад PdfFileStamp. Примеры Java охватывают нижние колонтитулы в виде простого текста, нижние колонтитулы изображений, загруженные из потока, а также текстовые нижние колонтитулы с явными левыми, правыми и нижними полями.
---
## Добавьте нижний колонтитул в PDF

Используйте `PdfFileStamp`, если вам нужно повторяющееся содержимое нижнего колонтитула на каждой странице документа.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте содержимое нижнего колонтитула либо в виде `FormattedText`, либо в виде потока изображений.
3. Вызовите соответствующую перегрузку `addFooter`.
4. Сохраните обновленный файл и закройте объект фасада.

### Примеры Java

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
