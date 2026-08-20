---
title: Конвертировать PDF в PDF/A, PDF/E и PDF/X на Java
linktitle: Конвертировать PDF в PDF/A, PDF/E и PDF/X
type: docs
weight: 120
url: /ru/java/convert-pdf-to-pdf_x/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать PDF‑файлы в PDF/A, PDF/E и PDF/X на Java с помощью Aspose.PDF для архивных, инженерных, доступных и печатных рабочих процессов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в форматы PDF/x
Abstract: В этой статье объясняется, как проверять и конвертировать PDF‑документы в форматы PDF/A, PDF/E и PDF/X с использованием Aspose.PDF for Java. Описывается генерация журналов, сохранение вложений для PDF/A‑3, замена отсутствующих шрифтов, автоматическая разметка, настройка ICC‑профиля и параметры намерения вывода.
---
Aspose.PDF for Java может проверять и конвертировать стандартные PDF‑файлы в архивные и ориентированные на обмен стандарты PDF.

## Конвертировать PDF в PDF/A

Используйте этот пример, когда стандартный PDF необходимо конвертировать в архивный документ, соответствующий требованиям PDF/A.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляре.
1. Вызовите `document.convert(...)` с [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` и [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Запишите журнал валидации в вспомогательный XML‑файл, чтобы проблемы соответствия фиксировались во время конвертации.
1. Сохраните проверенный вывод PDF/A.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Преобразуйте PDF в PDF/E

Используйте этот пример, когда PDF должен быть преобразован в ориентированный на инженерию стандарт PDF/E.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` и желаемый путь к файлу журнала.
1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляре.
1. Вызовите `document.convert(options)` поэтому преобразование соответствия выполняется с подготовленным объектом параметров.
1. Сохраните полученный соответствующий PDF-файл.

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

Используйте этот пример, когда PDF должен быть преобразован в ориентированный на печать стандарт PDF/X.

1. Создайте [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) для [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` и желаемый путь к файлу журнала.
1. Настройте [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) например `FOGRA39` поэтому профиль цветового пространства печати встраивается в настройки конверсии.
1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) создать экземпляр и вызвать `document.convert(options)`.
1. Сохраните преобразованный PDF/X вывод.

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


