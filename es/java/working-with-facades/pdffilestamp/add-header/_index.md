---
title: Agregar encabezado a PDF
linktitle: Agregar encabezado a PDF
type: docs
weight: 20
url: /java/add-header/
description: Aprenda a agregar encabezados de texto e imágenes a páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue encabezados de texto e imágenes a PDF en Java
Abstract: Aprenda a agregar contenido de encabezado a documentos PDF con Aspose.PDF para Java usando la fachada PdfFileStamp. Los ejemplos de Java cubren encabezados de texto sin formato, encabezados de imágenes cargados desde una secuencia y encabezados con estilos con valores de margen explícitos.
---
## Agregar encabezado a PDF



Utilice `PdfFileStamp` cuando necesite contenido de encabezado repetido en cada página.


### 
Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. Cree el contenido del encabezado como `FormattedText` o cárguelo desde una secuencia de imágenes.
3. Llame a la sobrecarga `addHeader` apropiada.

4. Guarde la salida y cierre el objeto de fachada.


### 
Ejemplos de Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
