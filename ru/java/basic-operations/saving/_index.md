---
title: Сохранение PDF‑документа программно
linktitle: Сохранение PDF
type: docs
weight: 30
url: /ru/java/save-pdf-document/
description: Узнайте, как сохранять PDF‑документы в Java в файл, в поток или в соответствии со стандартом PDF, используя Aspose.PDF.
lastmod: "2026-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение PDF‑документов с использованием библиотеки Aspose.PDF в Java
Abstract: В этой статье описывается, как сохранять PDF‑документы в Java с использованием Aspose.PDF. Рассматривается сохранение в путь к файлу, сохранение в OutputStream и преобразование документа перед сохранением его как файл стандарта PDF/X.
---
Aspose.PDF for Java предоставляет несколько способов сохранения документа в зависимости от целевого назначения и требований к выводу.

## Сохранение PDF‑документа в Java

Выберите подходящий способ сохранения документа:

1. Сохраните [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) непосредственно в файл на диске.
1. Сохраните [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в поток `OutputStream`.
1. Преобразуйте документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с помощью [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) и сохраните его в формате, указанном в [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Сохранение документа в файл

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Сохранение документа в поток

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

## Сохранение документа как PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```


