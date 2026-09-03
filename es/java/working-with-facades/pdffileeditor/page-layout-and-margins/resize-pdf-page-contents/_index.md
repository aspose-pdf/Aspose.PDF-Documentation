---
title: Redimensionar el contenido de la página PDF
linktitle: Redimensionar el contenido de la página PDF
type: docs
weight: 30
url: /es/java/resize-pdf-page-contents/
description: Redimensionar el contenido en páginas PDF seleccionadas en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionar contenidos de página existentes en un documento PDF con Java
Abstract: Aprenda cómo redimensionar contenidos de página con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para apuntar a páginas específicas, aplicar un nuevo ancho y alto de contenido, y detener el flujo de trabajo si la operación de redimensionado falla.
---
## Redimensionar contenidos de página PDF

El ejemplo en Java redimensiona el área de contenido en las páginas 1 y 3 y verifica el valor booleano de retorno.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Elija las páginas cuyo contenido debe redimensionarse.
3. Llamar `resizeContents` con el ancho y la altura objetivo.
4. Verifique el valor de retorno y maneje la falla antes de continuar.
5. Guarde el documento actualizado.

### Ejemplo de Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
