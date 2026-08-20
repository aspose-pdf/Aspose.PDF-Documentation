---
title: Agregar pie de página a PDF
linktitle: Agregar pie de página a PDF
type: docs
weight: 10
url: /java/add-footer/
description: Aprenda a agregar pies de página de texto e imágenes a páginas PDF en Java con la fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue pies de página de texto e imágenes a PDF en Java
Abstract: Aprenda a agregar contenido de pie de página a documentos PDF con Aspose.PDF para Java usando la fachada PdfFileStamp. Los ejemplos de Java cubren pies de página de texto sin formato, pies de página de imágenes cargados desde una secuencia y pies de página de texto con márgenes izquierdo, derecho e inferior explícitos.
---
## Agregar pie de página a PDF



Utilice `PdfFileStamp` cuando necesite contenido de pie de página repetido en cada página de un documento.


### 
Pasos


1. 
Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. 
Cree el contenido del pie de página como `FormattedText` o como una secuencia de imágenes.
3. Llame a la sobrecarga `addFooter` apropiada.

4. 
Guarde el archivo actualizado y cierre el objeto de fachada.


### 
Ejemplos de Java

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
