---
title: Eliminar metadatos de PDF
linktitle: Eliminar metadatos de PDF
type: docs
weight: 10
url: /es/java/clear-pdf-metadata/
description: Aprende cómo eliminar los metadatos de PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar metadatos de PDF usando Aspose.PDF for Java
Abstract: Aprende cómo eliminar los metadatos de PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para eliminar la información del documento almacenada con `clearInfo()` y luego guarda el PDF limpiado en un nuevo archivo.
---
## Eliminar metadatos de PDF

Utiliza este flujo de trabajo cuando necesites eliminar la información del documento almacenada antes de compartir o archivar un PDF.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de entrada.
2. Llame `clearInfo()` para eliminar los metadatos del documento.
3. Guarde el resultado en un nuevo archivo con `save()`.
4. Cierre la instancia de `PdfFileInfo`.

### Ejemplo en Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
