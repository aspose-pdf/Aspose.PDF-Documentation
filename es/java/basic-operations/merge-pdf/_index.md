---
title: Combinar archivos PDF en Java
linktitle: Combinar archivos PDF
type: docs
weight: 50
url: /es/java/merge-pdf/
description: Aprenda cómo combinar varios archivos PDF en un solo documento en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar páginas PDF usando Java
Abstract: Este artículo explica cómo combinar dos documentos PDF en Java usando Aspose.PDF. El ejemplo abre dos documentos fuente, agrega las páginas del segundo documento al primero y guarda el resultado combinado como un nuevo archivo PDF.
---
Combinar archivos PDF es útil cuando necesita juntar documentos relacionados en un único archivo para distribución, archivado o procesamiento.

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación en línea gratuita para probar la fusión de PDF en un navegador.

Este tema muestra cómo combinar varios archivos PDF en un solo documento en Java:

1. Abra ambos documentos de origen con el [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Añadir el [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) colección del segundo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) al primero con `document1.getPages().add(document2.getPages())`.
1. Guardar el fusionado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a la ruta de salida.

## Combinar dos documentos PDF

El siguiente ejemplo de Java se basa en `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
