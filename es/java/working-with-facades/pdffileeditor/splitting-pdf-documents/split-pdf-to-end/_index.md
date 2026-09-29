---
title: Dividir PDF hasta el final
linktitle: Dividir PDF hasta el final
type: docs
weight: 40
url: /es/java/split-pdf-to-end/
description: Dividir un PDF desde una página elegida hasta el final en Java con la fachada PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer páginas desde un punto de inicio hasta el final de un PDF con Java
Abstract: Aprenda cómo dividir un PDF hasta el final con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor para extraer todas las páginas a partir de la página 2 hasta el final del documento de origen.
---
## Dividir PDF hasta el final

El ejemplo en Java extrae todas las páginas a partir de la página 2.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Llame `splitToEnd` con el archivo fuente, número de página inicial y archivo de salida.
3. Guarde el documento PDF resultante.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
