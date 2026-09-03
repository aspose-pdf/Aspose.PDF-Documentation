---
title: Extraer páginas de PDF
linktitle: Extraer páginas de PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Extraiga páginas seleccionadas de un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga páginas PDF seleccionadas en un nuevo documento con Java
Abstract: Aprenda a extraer páginas de un PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para recopilar números de página específicos y escribirlos en un PDF de salida independiente.
---
## Extraer páginas de un PDF



El ejemplo de Java extrae las páginas 1, 4 y 3 en un nuevo documento PDF.


### 
Pasos


1. Cree una instancia `PdfFileEditor`.

2. Defina los números de página a extraer.
3. Llame a `extract` con el archivo fuente, la matriz de páginas y el archivo de salida.

4. Guarde las páginas extraídas como un nuevo PDF.


### 
Ejemplo de Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
