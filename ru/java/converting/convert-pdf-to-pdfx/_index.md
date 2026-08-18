---
title: Преобразование PDF в PDF/A, PDF/E и PDF/X в Java
linktitle: Конвертируйте PDF в PDF/A, PDF/E и PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать PDF-файлы в PDF/A, PDF/E и PDF/X на Java с помощью Aspose.PDF для рабочих процессов архивирования, проектирования, обеспечения доступности и печати.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в форматы PDF/x
Abstract: В этой статье объясняется, как проверять и конвертировать PDF-документы в форматы PDF/A, PDF/E и PDF/X с помощью Aspose.PDF для Java. Он охватывает создание журналов, сохранение вложений для PDF/A-3, замену отсутствующих шрифтов, автоматическую пометку, настройку профиля ICC и настройки способа вывода.
---
Aspose.PDF для Java может проверять и преобразовывать стандартные PDF-файлы в стандарты PDF для архивирования и обмена.

## Конвертировать PDF в PDF/A

Используйте этот пример, когда стандартный PDF-файл необходимо преобразовать в архивный документ, совместимый с PDF/A.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвоните `document.convert(...)` с помощью [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` и [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Запишите журнал проверки в дополнительный XML-файл, чтобы во время преобразования фиксировались проблемы соответствия.
1. Сохраните проверенный вывод PDF/A.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Конвертировать PDF в PDF/E

Используйте этот пример, когда PDF-файл необходимо преобразовать в инженерно-ориентированный стандарт PDF/E.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` и желаемый путь к файлу журнала.
1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `document.convert(options)`, чтобы выполнить преобразование соответствия с подготовленным объектом параметров.
1. Сохраните полученный совместимый PDF-файл.

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## Конвертировать PDF в PDF/X

Используйте этот пример, когда PDF-файл необходимо преобразовать в ориентированный на печать стандарт PDF/X.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` и желаемый путь к файлу журнала.
1. Настройте [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/), например `FOGRA39`, чтобы целевой цветовой профиль печати был встроен в настройки преобразования.
1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и вызовите `document.convert(options)`.
1. Сохраните преобразованный вывод PDF/X.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
