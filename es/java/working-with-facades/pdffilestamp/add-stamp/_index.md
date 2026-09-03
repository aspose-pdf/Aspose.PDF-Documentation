---
title: Agregar sello a PDF
linktitle: Agregar sello a PDF
type: docs
weight: 40
url: /java/add-stamp/
description: Aprenda a agregar un sello de imagen a páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar sellos de imágenes a PDF en Java
Abstract: Aprenda a agregar contenido de sello a documentos PDF con Aspose.PDF para Java usando la fachada PdfFileStamp. El conjunto de ejemplos de Java actual muestra cómo crear un `Stamp`, vincularlo a un archivo de imagen, agregarlo al documento y guardar el PDF estampado.
---
## Agregar sello a PDF



Utilice este flujo de trabajo cuando deba aplicarse un sello basado en imágenes al PDF.


### 
Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. Cree un objeto `Stamp`.
3. Vincule el sello a un archivo de imagen con `bindImage`.

4. Agregue el sello al documento con `addStamp`.

5. Guarde la salida y cierre el objeto de fachada.


### 
Ejemplo de Java


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


La clase `PdfFileStampExamples.java` actual no incluye una muestra Java separada para sellos de solo texto, rotación u configuración de opacidad.
