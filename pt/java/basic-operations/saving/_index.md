---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/java/save-pdf-document/
description: Aprenda como salvar documentos PDF em Java para um arquivo, para um fluxo ou como um padrão PDF usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando documentos PDF usando a biblioteca Aspose.PDF em Java
Abstract: Este artigo descreve como salvar documentos PDF em Java usando Aspose.PDF. Ele aborda salvar em um caminho de arquivo, salvar em um OutputStream e converter um documento antes de salvá‑lo como um arquivo padrão PDF/X.
---
Aspose.PDF for Java fornece várias maneiras de salvar um documento, dependendo do destino e dos requisitos de saída.

## Salvar um documento PDF em Java

Você pode salvar um documento:

1. Salve o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) diretamente em um arquivo no disco.
1. Salve o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para um `OutputStream`.
1. Converta o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) e salve-o em um formato padrão, como [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Salvar documento em arquivo

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Salvar documento em stream

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
