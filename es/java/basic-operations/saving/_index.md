---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/java/save-pdf-document/
description: Aprenda cómo guardar documentos PDF en Java a un archivo, a un flujo o como un estándar PDF usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardando documentos PDF usando la biblioteca Aspose.PDF en Java
Abstract: Este artículo describe cómo guardar documentos PDF en Java usando Aspose.PDF. Cubre guardar en una ruta de archivo, guardar en un OutputStream y convertir un documento antes de guardarlo como un archivo estándar PDF/X.
---
Aspose.PDF for Java ofrece varias formas de guardar un documento dependiendo del destino objetivo y los requisitos de salida.

## Guardar un documento PDF en Java

Puede guardar un documento:

1. Guardar el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directamente a un archivo en el disco.
1. Guardar el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a un `OutputStream`.
1. Convertir el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) y guardarlo en un formato estándar como [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Guardar documento en archivo

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Guardar documento en flujo

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

## Guardar documento como PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
