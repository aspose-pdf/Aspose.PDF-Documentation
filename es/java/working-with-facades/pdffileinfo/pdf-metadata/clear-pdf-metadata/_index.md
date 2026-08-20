---
title: Borrar metadatos PDF
linktitle: Borrar metadatos PDF
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: Aprenda a borrar metadatos de PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Borrar metadatos de PDF usando Aspose.PDF para Java
Abstract: Aprenda a borrar metadatos de PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileInfo para eliminar la información del documento almacenado con `clearInfo()` y luego guarda el PDF limpio en un archivo nuevo.
---
## Borrar metadatos PDF



Utilice este flujo de trabajo cuando necesite eliminar información del documento almacenado antes de compartir o archivar un PDF.


### 
Pasos


1. 
Cree un objeto `PdfFileInfo` para el PDF de entrada.

2. 
Llame a `clearInfo()` para eliminar los metadatos del documento.
3. Guarde el resultado en un archivo nuevo con `save()`.

4. 
Cierre la instancia `PdfFileInfo`.


### 
Ejemplo de Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
