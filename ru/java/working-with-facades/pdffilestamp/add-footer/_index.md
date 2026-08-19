---
title: Добавить нижний колонтитул в PDF
linktitle: Добавить нижний колонтитул в PDF
type: docs
weight: 10
url: /ru/java/add-footer/
description: Узнайте, как добавить текстовые и графические нижние колонтитулы на страницы PDF в Java с помощью фасада PdfFileStamp.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте текстовые и графические нижние колонтитулы в PDF на Java
Abstract: Узнайте, как добавить содержимое нижних колонтитулов в PDF‑документы с помощью Aspose.PDF for Java, используя фасад PdfFileStamp. В примерах на Java рассматриваются простые текстовые нижние колонтитулы, графические нижние колонтитулы, загружаемые из потока, и текстовые нижние колонтитулы с явно указанными левыми, правыми и нижними полями.
---
## Добавьте нижний колонтитул в PDF

Использовать `PdfFileStamp` когда вам нужно повторяющееся содержимое нижнего колонтитула на каждой странице документа.

### Шаги

1. Создайте `PdfFileStamp` создать экземпляр и привязать исходный PDF.
2. Сформируйте содержимое нижнего колонтитула как `FormattedText` или поток изображения.
3. Вызовите соответствующий `addFooter` перегрузка.
4. Сохраните обновлённый файл и закройте объект фасада.

### Примеры на Java

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

