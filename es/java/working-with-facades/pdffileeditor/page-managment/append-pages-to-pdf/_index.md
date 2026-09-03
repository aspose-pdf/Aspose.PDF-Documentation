---
title: Agregar páginas al PDF
linktitle: Agregar páginas al PDF
type: docs
weight: 10
url: /es/java/append-pages-to-pdf/
description: Agregar páginas de un PDF a otro en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un rango de páginas de un documento PDF a otro con Java
Abstract: Aprenda cómo agregar páginas a un PDF con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para agregar un rango de páginas seleccionado de otro documento al final del PDF actual.
---
## Agregar páginas a un PDF

El ejemplo en Java agrega la página 1 de un segundo PDF al final del primer documento.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Vincula el PDF de entrada principal pasando su ruta a `append`.
3. Proporcione la lista de archivos fuente secundarios y el rango de páginas a añadir.
4. Guarde el resultado combinado en el archivo de salida.

### Ejemplo Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
