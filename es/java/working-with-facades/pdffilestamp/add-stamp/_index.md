---
title: Agregar sello al PDF
linktitle: Agregar sello al PDF
type: docs
weight: 40
url: /es/java/add-stamp/
description: Aprenda cómo agregar un sello de imagen a las páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar sellos de imagen al PDF en Java
Abstract: Aprenda cómo agregar contenido de sello a documentos PDF con Aspose.PDF for Java usando la fachada PdfFileStamp. El conjunto actual de ejemplos en Java muestra cómo crear un `Stamp`, vincularlo a un archivo de imagen, agregarlo al documento y guardar el PDF con sello.
---
## Agregar sello al PDF

Utilice este flujo de trabajo cuando se deba aplicar un sello basado en imagen al PDF.

### Pasos

1. Crear un `PdfFileStamp` instanciar y enlazar el PDF de origen.
2. Crear un `Stamp` objeto.
3. Vincula el sello a un archivo de imagen con `bindImage`.
4. Agregar el sello al documento con `addStamp`.
5. Guarde la salida y cierre el objeto fachada.

### Ejemplo de Java

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

El actual `PdfFileStampExamples.java` La clase no incluye un ejemplo Java separado para sellos solo de texto, rotación o configuración de opacidad.
