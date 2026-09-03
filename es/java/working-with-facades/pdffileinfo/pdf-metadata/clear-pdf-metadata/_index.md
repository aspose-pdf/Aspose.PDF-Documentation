---
title: Borrar metadatos de PDF
linktitle: Borrar metadatos de PDF
type: docs
weight: 10
url: /es/java/clear-pdf-metadata/
description: Aprenda cómo borrar los metadatos de PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Borrado de metadatos de PDF usando Aspose.PDF for Java
Abstract: Aprenda cómo borrar los metadatos de PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para eliminar la información del documento almacenada con `clearInfo()` y luego guarda el PDF limpio en un nuevo archivo.
---
## Borrar metadatos de PDF

Utilice este flujo de trabajo cuando necesite eliminar la información del documento almacenada antes de compartir o archivar un PDF.

### Pasos

1. Crear un `PdfFileInfo` objeto para el PDF de entrada.
2. Llamar `clearInfo()` para eliminar los metadatos del documento.
3. Guarda el resultado en un nuevo archivo con `save()`.
4. Cierra el `PdfFileInfo` instancia.

### Ejemplo de Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
