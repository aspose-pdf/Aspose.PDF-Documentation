---
title: Guarde el documento PDF mediante programación
linktitle: Guardar PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: Aprenda a guardar documentos PDF en Java en un archivo, en una secuencia o como un PDF estándar usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardar documentos PDF usando la biblioteca Aspose.PDF en Java
Abstract: Este artículo describe cómo guardar documentos PDF en Java usando Aspose.PDF. Cubre guardar en una ruta de archivo, guardar en OutputStream y convertir un documento antes de guardarlo como un archivo estándar PDF/X.
---
Aspose.PDF para Java proporciona varias formas de guardar un documento según el destino de destino y los requisitos de salida.


## 
Guardar un documento PDF en Java



Puedes guardar un documento:


1. Guarde el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directamente en un archivo en el disco.

1. Guarde el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) en un `OutputStream`.
1. Convierta el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) y guárdelo en un formato estándar como [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).


## 
Guardar documento en archivo


```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## 
Guardar documento para transmitir


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

## 
Guardar documento como PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
