---
title: Fusionar archivos PDF en Java
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /java/merge-pdf/
description: Aprenda a fusionar varios archivos PDF en un solo documento en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine páginas PDF usando Java
Abstract: Este artículo explica cómo fusionar dos documentos PDF en Java usando Aspose.PDF. El ejemplo abre dos documentos de origen, agrega las páginas del segundo documento al primero y guarda el resultado combinado como un nuevo archivo PDF.
---
Fusionar archivos PDF es útil cuando necesita combinar documentos relacionados en un solo archivo para distribuirlos, archivarlos o procesarlos.


## 
Ejemplo en vivo



[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación en línea gratuita para probar la fusión de PDF en un navegador.



Este tema muestra cómo fusionar varios archivos PDF en un solo documento en Java:


1. 
Abra ambos documentos fuente con el constructor [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue la colección [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del segundo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) al primero con `document1.getPages().add(document2.getPages())`.

1. 
Guarde el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) combinado en la ruta de salida.


## 
Fusionar dos documentos PDF



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
