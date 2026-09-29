---
title: Agregar número de página a PDF
linktitle: Agregar número de página a PDF
type: docs
weight: 30
url: /es/java/page-number/
description: Aprenda cómo agregar números de página a documentos PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar números de página a PDF en Java
Abstract: Aprenda cómo agregar números de página a documentos PDF con Aspose.PDF for Java utilizando la fachada PdfFileStamp. Los ejemplos en Java cubren la ubicación predeterminada, coordenadas explícitas, colocación alineada con márgenes y salida en numeración romana con un número inicial personalizado.
---
## Agregar número de página a PDF

Utilice `PdfFileStamp` cuando la numeración de páginas debe aplicarse después de que el contenido del PDF ya ha sido creado.

### Pasos

1. Cree un `PdfFileStamp` instanciar y enlace el PDF de origen.
2. Seleccione la estrategia de ubicación de número de página que necesite.
3. Opcionalmente establezca el estilo de numeración y el número inicial antes de estampar.
4. Llame `addPageNumber` con la sobrecarga requerida.
5. Guarde la salida y cierre el objeto fachada.

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
