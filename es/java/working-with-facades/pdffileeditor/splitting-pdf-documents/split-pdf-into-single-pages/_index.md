---
title: Dividir PDF en páginas individuales
linktitle: Dividir PDF en páginas individuales
type: docs
weight: 30
url: /es/java/split-pdf-into-single-pages/
description: Divida un PDF en archivos de salida de una sola página en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exporte cada página de un PDF a su propio archivo con Java
Abstract: Aprenda cómo dividir un PDF en archivos de una sola página con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para escribir cada página en un PDF de salida individual basado en un patrón de nombre de archivo.
---
## Dividir PDF en páginas individuales

Utilice este flujo de trabajo cuando cada página de origen deba convertirse en su propio archivo PDF.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Prepare un patrón de archivo de salida que incluya un marcador de posición de página, como `%NUM%`.
3. Llamar `splitToPages` con el archivo fuente y el patrón de salida.
4. Guarde los archivos de una sola página generados.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
