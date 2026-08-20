---
title: Agregar saltos de página en PDF
linktitle: Agregar saltos de página en PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: Inserte saltos de página en un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insertar saltos de página en posiciones fijas en un documento PDF con Java
Abstract: Aprenda a agregar saltos de página con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor.PageBreak para dividir una página en una posición vertical específica y guardar el resultado como un nuevo PDF.
---
## Agregar saltos de página en un PDF



Utilice este flujo de trabajo cuando sea necesario dividir una página en varias páginas en una posición Y conocida.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Cree una o más entradas `PdfFileEditor.PageBreak` con el número de página y la posición de ruptura.
3. Pase la matriz de salto de página a `addPageBreak`.

4. 
Guarde el documento PDF actualizado.


### 
Ejemplo de Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
