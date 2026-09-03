---
title: Extraer páginas de PDF
linktitle: Extraer páginas de PDF
type: docs
weight: 30
url: /es/java/extract-pages-from-pdf/
description: Extraer páginas seleccionadas de un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer páginas PDF seleccionadas a un nuevo documento con Java
Abstract: Aprenda cómo extraer páginas de un PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor para recopilar números de página específicos y escribirlos en un PDF de salida separado.
---
## Extraer páginas de un PDF

El ejemplo en Java extrae las páginas 1, 4 y 3 en un nuevo documento PDF.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Define los números de página a extraer.
3. Llamar `extract` con el archivo de origen, la matriz de páginas y el archivo de salida.
4. Guarda las páginas extraídas como un nuevo PDF.

### Ejemplo en Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
