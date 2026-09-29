---
title: Agregar sello al PDF
linktitle: Agregar sello al PDF
type: docs
weight: 40
url: /es/java/add-stamp/
description: Aprenda c\u00f3mo agregar un sello de imagen a las p\u00e1ginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar sellos de imagen al PDF en Java
Abstract: Aprenda c\u00f3mo agregar contenido de sello a documentos PDF con Aspose.PDF for Java usando la fachada PdfFileStamp. El conjunto actual de ejemplos en Java muestra c\u00f3mo crear un `Stamp`, vincularlo a un archivo de imagen, agregarlo al documento y guardar el PDF sellado.
---
## Agregar sello al PDF

Utilice este flujo de trabajo cuando se deba aplicar un sello basado en una imagen al PDF.

### Pasos

1. Cree una instancia de `PdfFileStamp` y vincule el PDF de origen.
2. Cree un objeto `Stamp`.
3. Vincule el sello a un archivo de imagen con `bindImage`.
4. Agregue el sello al documento con `addStamp`.
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
