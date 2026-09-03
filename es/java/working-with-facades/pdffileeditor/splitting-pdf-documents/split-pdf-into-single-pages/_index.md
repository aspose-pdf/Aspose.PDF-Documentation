---
title: Dividir PDF en páginas individuales
linktitle: Dividir PDF en páginas individuales
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: Divida un PDF en archivos de salida de una sola página en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exporta cada página de un PDF a su propio archivo con Java
Abstract: Aprenda a dividir un PDF en archivos de una sola página con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para escribir cada página en un PDF de salida individual según un patrón de nombre de archivo.
---
## Dividir PDF en páginas individuales



Utilice este flujo de trabajo cuando cada página de origen deba convertirse en su propio archivo PDF.


### 
Pasos


1. Cree una instancia `PdfFileEditor`.

2. Prepare un patrón de archivo de salida que incluya un marcador de posición de página como `%NUM%`.
3. Llame a `splitToPages` con el archivo fuente y el patrón de salida.

4. Guarde los archivos de una sola página generados.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
