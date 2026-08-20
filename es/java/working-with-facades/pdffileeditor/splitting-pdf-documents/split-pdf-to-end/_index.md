---
title: Dividir PDF para finalizar
linktitle: Dividir PDF para finalizar
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: Divida un PDF desde una página elegida hasta el final en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga páginas desde el punto inicial hasta el final de un PDF con Java
Abstract: Aprenda a dividir un PDF hasta el final con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para extraer todas las páginas desde la página 2 hasta el final del documento fuente.
---
## Dividir PDF para finalizar



El ejemplo de Java extrae todas las páginas a partir de la página 2.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Llame a `splitToEnd` con el archivo fuente, el número de página inicial y el archivo de salida.
3. Guarde el documento PDF resultante.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
