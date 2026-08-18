---
title: Сохранить PDF-документ программно
linktitle: Сохранить PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: Узнайте, как сохранять PDF-документы на Java в файл, в поток или в формате PDF с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение PDF-документов с использованием библиотеки Aspose.PDF в Java
Abstract: В этой статье описывается, как сохранить документы PDF в Java с помощью Aspose.PDF. Он охватывает сохранение в пути к файлу, сохранение в OutputStream и преобразование документа перед сохранением его в стандартный файл PDF/X.
---
Aspose.PDF для Java предоставляет несколько способов сохранить документ в зависимости от целевого назначения и требований к выводу.

## Сохранение PDF-документа в Java

Вы можете сохранить документ:

1. Сохраните [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) непосредственно в файл на диске.
1. Сохраните [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в `OutputStream`.
1. Преобразуйте [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с помощью [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) и сохраните его в стандартном формате, например [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Сохраните документ в файл

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Сохраните документ для потоковой передачи

```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## Сохраните документ как PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
