---
title: Merge PDF Files in Java
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf/
description: Learn how to merge multiple PDF files into a single document in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine PDF pages using Java
Abstract: Este artículo explica cómo fusionar dos documentos PDF en Java usando Aspose.PDF. El ejemplo abre dos documentos de origen, agrega las páginas del segundo documento al primero y guarda el resultado combinado como un nuevo archivo PDF.
---
Merging PDF files is useful when you need to combine related documents into a single file for distribution, archiving, or processing.

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación en línea gratuita para probar la fusión de PDF en un navegador.

Este tema muestra cómo fusionar varios archivos PDF en un solo documento en Java:

1. Abra ambos documentos fuente con el constructor [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Append the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) collection from the second [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) to the first one with `document1.getPages().add(document2.getPages())`.
1. Save the merged [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) to the output path.

## Merge two PDF documents

The following Java example is based on `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
