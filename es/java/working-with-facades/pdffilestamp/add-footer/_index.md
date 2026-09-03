---
title: Agregar pie de página al PDF
linktitle: Agregar pie de página al PDF
type: docs
weight: 10
url: /es/java/add-footer/
description: Aprenda cómo agregar pies de página de texto e imagen a páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar pies de página de texto e imagen al PDF en Java
Abstract: Aprenda cómo agregar contenido de pie de página a documentos PDF con Aspose.PDF for Java usando la fachada PdfFileStamp. Los ejemplos en Java cubren pies de página de texto simple, pies de página de imagen cargados desde un flujo y pies de página de texto con márgenes explícitos izquierdo, derecho e inferior.
---
## Agregar pie de página al PDF

Usar `PdfFileStamp` cuando necesitas contenido de pie de página repetido en cada página de un documento.

### Pasos

1. Crear un `PdfFileStamp` instancia y vincula el PDF de origen.
2. Construya el contenido del pie de página como cualquiera de `FormattedText` o un flujo de imagen.
3. Llame al apropiado `addFooter` sobrecargar.
4. Guarde el archivo actualizado y cierre el objeto fachada.

### Ejemplos de Java

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
