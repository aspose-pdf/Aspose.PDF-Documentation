---
title: Добавить заголовок в PDF
linktitle: Добавить заголовок в PDF
type: docs
weight: 20
url: /java/add-header/
description: Узнайте, как добавлять заголовки текста и изображений на страницы PDF в Java с помощью фасада PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление заголовков текста и изображений в PDF на Java
Abstract: Узнайте, как добавить содержимое заголовка в PDF-документы с помощью Aspose.PDF для Java, используя фасад PdfFileStamp. Примеры Java охватывают заголовки обычного текста, заголовки изображений, загруженные из потока, а также стилизованные заголовки с явными значениями полей.
---
## Добавьте заголовок в PDF

Используйте `PdfFileStamp`, если вам нужно повторяющееся содержимое заголовка на каждой странице.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте содержимое заголовка как `FormattedText` или загрузите его из потока изображений.
3. Вызовите соответствующую перегрузку `addHeader`.
4. Сохраните вывод и закройте объект фасада.

### Примеры Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
