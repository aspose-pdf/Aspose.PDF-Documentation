---
title: Преобразование PDF в PDF/A, PDF/E и PDF/X на Java
linktitle: Преобразование PDF в PDF/A, PDF/E и PDF/X
type: docs
weight: 120
url: /ru/java/convert-pdf-to-pdf_x/
lastmod: "2026-09-16"
description: Узнайте, как преобразовать файлы PDF в PDF/A, PDF/E и PDF/X на Java с помощью Aspose.PDF для архивных, инженерных, обеспечивающих доступность и печатных рабочих процессов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в форматы PDF/x
Abstract: В этой статье объясняется, как проверять и конвертировать документы PDF в форматы PDF/A, PDF/E и PDF/X с использованием Aspose.PDF for Java. Описываются генерация логов, сохранение вложений для PDF/A-3, замена отсутствующих шрифтов, автоматическая разметка тегов, настройка профиля ICC и параметры намерения вывода.
---
Aspose.PDF for Java может проверять и конвертировать стандартные файлы PDF в архивные и ориентированные на обмен стандарты PDF.

## Преобразование PDF в PDF/A

Используйте этот пример, когда стандартный PDF должен быть преобразован в архивный документ, соответствующий PDF/A.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `document.convert(...)` с [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` и [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Запишите журнал проверки в сопутствующий XML‑файл, чтобы проблемы соответствия фиксировались во время конвертации.
1. Сохраните проверенный файл PDF/A.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Преобразование PDF в PDF/E

Используйте этот пример, когда PDF нужно преобразовать в инженерный стандарт PDF/E.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` и укажите нужный путь к файлу журнала.
1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `document.convert(options)`, при этом преобразование соответствия выполняется с подготовленным объектом параметров.
1. Сохраните полученный соответствующий требованиям PDF-файл.

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

## Преобразование PDF в PDF/X

Используйте этот пример, когда PDF необходимо преобразовать в ориентированный на печать стандарт PDF/X.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` и укажите нужный путь к файлу журнала.
1. Настройте [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/), например `FOGRA39`, при этом профиль цвета для печати встраивается в настройки конвертации.
1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и вызовите `document.convert(options)`.
1. Сохраните преобразованный файл PDF/X.

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
