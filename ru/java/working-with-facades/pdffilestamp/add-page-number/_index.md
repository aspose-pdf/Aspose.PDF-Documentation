---
title: Добавить номер страницы в PDF
linktitle: Добавить номер страницы в PDF
type: docs
weight: 30
url: /ru/java/page-number/
description: Узнайте, как добавить номера страниц в PDF-документы на Java с фасадом PdfFileStamp.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить номера страниц в PDF на Java
Abstract: Узнайте, как добавить номера страниц в PDF-документы с помощью Aspose.PDF for Java, используя фасад PdfFileStamp. Примеры на Java охватывают размещение по умолчанию, явные координаты, выравненное размещение с полями и вывод римскими цифрами с пользовательским начальным номером.
---
## Добавьте номер страницы в PDF

Использовать `PdfFileStamp` когда нумерацию страниц необходимо применить после того, как содержимое PDF уже создано

### Шаги

1. Создайте `PdfFileStamp` экземпляр и привязать исходный PDF.
2. Выберите стратегию размещения номера страницы, которая вам нужна.
3. При необходимости задайте стиль нумерации и начальный номер перед нанесением штампа.
4. Вызов `addPageNumber` с требуемой перегрузкой.
5. Сохраните результат и закройте фасадный объект.

### Примеры Java

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

