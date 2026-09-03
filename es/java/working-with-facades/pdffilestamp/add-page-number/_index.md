---
title: Agregar número de página al PDF
linktitle: Agregar número de página al PDF
type: docs
weight: 30
url: /es/java/page-number/
description: Aprenda cómo agregar números de página a documentos PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar números de página al PDF en Java
Abstract: Aprenda cómo agregar números de página a documentos PDF con Aspose.PDF for Java utilizando la fachada PdfFileStamp. Los ejemplos en Java cubren la colocación predeterminada, coordenadas explícitas, colocación alineada con márgenes y salida en numeración romana con un número de inicio personalizado.
---
## Agregar número de página al PDF

Usar `PdfFileStamp` cuando la numeración de página debe aplicarse después de que el contenido del PDF ya ha sido creado.

### Pasos

1. Crear un `PdfFileStamp` instancia y enlaza el PDF de origen.
2. Elige la estrategia de ubicación de números de página que necesites.
3. Opcionalmente, establece el estilo de numeración y el número inicial antes de aplicar el sello.
4. Llamar `addPageNumber` con la sobrecarga requerida.
5. Guarda la salida y cierra el objeto fachada.

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
