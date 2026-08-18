---
title: Добавить номер страницы в PDF
linktitle: Добавить номер страницы в PDF
type: docs
weight: 30
url: /java/page-number/
description: Узнайте, как добавлять номера страниц в PDF-документы на Java с помощью фасада PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление номеров страниц в PDF на Java
Abstract: Узнайте, как добавлять номера страниц в PDF-документы с помощью Aspose.PDF для Java, используя фасад PdfFileStamp. Примеры Java охватывают размещение по умолчанию, явные координаты, выравнивание размещения с полями и вывод в римской нумерации с настраиваемым начальным номером.
---
## Добавьте номер страницы в PDF

Используйте `PdfFileStamp`, когда нумерацию страниц необходимо применить после того, как содержимое PDF уже создано.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Выберите нужную вам стратегию размещения номеров страниц.
3. При необходимости установите стиль нумерации и начальный номер перед штамповкой.
4. Вызовите `addPageNumber` с необходимой перегрузкой.
5. Сохраните вывод и закройте объект фасада.

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
