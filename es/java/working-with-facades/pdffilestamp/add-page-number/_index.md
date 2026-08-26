---
title: Agregar número de página a PDF
linktitle: Agregar número de página a PDF
type: docs
weight: 30
url: /java/page-number/
description: Aprenda a agregar números de página a documentos PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar números de página a PDF en Java
Abstract: Aprenda a agregar números de página a documentos PDF con Aspose.PDF para Java usando la fachada PdfFileStamp. Los ejemplos de Java cubren la ubicación predeterminada, las coordenadas explícitas, la ubicación alineada con márgenes y la salida de numeración romana con un número inicial personalizado.
---
## Agregar número de página a PDF

Utilice `PdfFileStamp` cuando se deba aplicar la numeración de páginas después de que ya se haya creado el contenido del PDF.

### Pasos

1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.
2. Elija la estrategia de ubicación de números de página que necesita.
3. Optionally set numbering style and starting number before stamping.
4. Llame a `addPageNumber` con la sobrecarga requerida.
5. Save the output and close the facade object.

### Ejemplos de Java

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
