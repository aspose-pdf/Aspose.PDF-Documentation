---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: Aprenda como salvar documentos PDF em Java em um arquivo, em um fluxo ou como um padrão PDF usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando documentos PDF usando a biblioteca Aspose.PDF em Java
Abstract: Este artigo descreve como salvar documentos PDF em Java usando Aspose.PDF. Abrange salvar em um caminho de arquivo, salvar em um OutputStream e converter um documento antes de salvá-lo como um arquivo padrão PDF/X.
---
Aspose.PDF para Java oferece várias maneiras de salvar um documento, dependendo do destino de destino e dos requisitos de saída.

## Salvar um documento PDF em Java

Você pode salvar um documento:

1. Salve o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) diretamente em um arquivo no disco.
1. Salve o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) em `OutputStream`.
1. Converta o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) e salve-o em um formato padrão como [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Salvar documento em arquivo

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Salvar documento para transmitir

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

## Salvar documento como PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
