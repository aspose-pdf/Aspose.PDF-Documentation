---
title: Dividir PDF al final
linktitle: Dividir PDF al final
type: docs
weight: 40
url: /es/java/split-pdf-to-end/
description: Dividir un PDF desde una página seleccionada hasta el final en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer páginas desde un punto de inicio hasta el final de un PDF con Java
Abstract: Aprende cómo dividir un PDF hasta el final con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor para extraer todas las páginas a partir de la página 2 hasta el final del documento de origen.
---
## Dividir PDF al final

El ejemplo en Java extrae todas las páginas a partir de la página 2.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Llamar `splitToEnd` con el archivo fuente, el número de página inicial y el archivo de salida.
3. Guarde el documento PDF resultante.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
