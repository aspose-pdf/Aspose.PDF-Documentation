---
title: Fusionar archivos PDF en Java
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /es/java/merge-pdf/
description: Aprenda cómo fusionar varios archivos PDF en un solo documento en Java usando Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar páginas PDF usando Java
Abstract: Este artículo explica cómo fusionar dos documentos PDF en Java usando Aspose.PDF. El ejemplo abre dos documentos de origen, agrega las páginas del segundo documento al primero y guarda el resultado fusionado como un nuevo archivo PDF.
---
Fusionar archivos PDF es útil cuando necesita combinar documentos relacionados en un solo archivo para distribución, archivado o procesamiento.

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación gratuita en línea para probar la fusión de PDF en un navegador.

Este tema muestra cómo combinar varios archivos PDF en un solo documento en Java:

1. Abra ambos documentos de origen con el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Agregue la colección [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del segundo [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) al primero con `document1.getPages().add(document2.getPages())`.
1. Guarde el fusionado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a la ruta de salida.

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
