---
title: Agregar saltos de página en PDF
linktitle: Agregar saltos de página en PDF
type: docs
weight: 20
url: /es/java/add-page-breaks-in-pdf/
description: Insertar saltos de página en un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insertar saltos de página en posiciones fijas en un documento PDF con Java
Abstract: Aprenda cómo agregar saltos de página con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor.PageBreak para dividir una página en una posición vertical específica y guardar el resultado como un nuevo PDF.
---
## Agregar saltos de página en un PDF

Utilice este flujo de trabajo cuando una página necesite dividirse en varias páginas en una posición Y conocida.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Construir uno o más `PdfFileEditor.PageBreak` entradas con el número de página y la posición de salto.
3. Pasar el arreglo de salto de página a `addPageBreak`.
4. Guarda el documento PDF actualizado.

### Ejemplo de Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
