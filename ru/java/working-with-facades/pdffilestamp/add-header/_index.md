---
title: Добавить заголовок в PDF
linktitle: Добавить заголовок в PDF
type: docs
weight: 20
url: /ru/java/add-header/
description: Узнайте, как добавить текстовые и графические заголовки на страницы PDF в Java с фасадом PdfFileStamp.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить текстовые и графические заголовки в PDF на Java
Abstract: Узнайте, как добавить содержимое заголовка в PDF-документы с помощью Aspose.PDF for Java, используя фасад PdfFileStamp. Примеры на Java охватывают простые текстовые заголовки, графические заголовки, загружаемые из потока, и стилизованные заголовки с явными значениями отступов.
---
## Добавьте заголовок в PDF

Использовать `PdfFileStamp` когда вам нужно повторяющееся содержимое заголовка на каждой странице.

### Шаги

1. Создайте `PdfFileStamp` создайте экземпляр и привяжите исходный PDF.
2. Создайте содержимое заголовка как `FormattedText` или загрузить его из потока изображения.
3. Вызовите соответствующий `addHeader` перегрузка.
4. Сохраните вывод и закройте объект‑фасад.

### Примеры на Java

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

