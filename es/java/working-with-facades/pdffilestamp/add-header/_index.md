---
title: Agregar encabezado a PDF
linktitle: Agregar encabezado a PDF
type: docs
weight: 20
url: /es/java/add-header/
description: Aprenda cómo agregar encabezados de texto e imagen a páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar encabezados de texto e imagen a PDF en Java
Abstract: Aprenda cómo agregar contenido de encabezado a documentos PDF con Aspose.PDF for Java usando la fachada PdfFileStamp. Los ejemplos en Java cubren encabezados de texto sin formato, encabezados de imagen cargados desde un flujo y encabezados con estilo con valores de margen explícitos.
---
## Agregar encabezado a PDF

Usar `PdfFileStamp` cuando necesitas contenido de encabezado repetido en cada página.

### Pasos

1. Crear un `PdfFileStamp` instanciar y enlazar el PDF de origen.
2. Construir el contenido del encabezado como `FormattedText` o cárgalo desde un flujo de imagen.
3. Llama al apropiado `addHeader` sobrecargar.
4. Guarde la salida y cierre el objeto fachada.

### Ejemplos de Java

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
