---
title: Clase de sello
linktitle: Clase de sello
type: docs
weight: 150
url: /java/stamp-class/
description: Aprenda a trabajar con la clase Stamp en Java para agregar imágenes, PDF y sellos basados ​​en texto a documentos PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos de imagen, PDF y texto a documentos PDF en Java
Abstract: Esta sección explica cómo utilizar la clase Stamp junto con PdfFileStamp en Aspose.PDF para Java para agregar contenido de sello reutilizable a documentos PDF. Los ejemplos actuales de Java cubren sellos de imágenes, sellos de páginas PDF, sellos de texto con un TextState personalizado, sellos específicos de página y sellos de imágenes de fondo con configuraciones de opacidad, tamaño y rotación.
---
La clase Java `StampExamples` demuestra los principales flujos de trabajo de creación de sellos disponibles a través de la API de Fachadas.

## Add an image stamp

Utilice este flujo de trabajo cuando un archivo de imagen deba colocarse en el PDF como un sello.

### Steps

1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.
2. Create a `Stamp` object and bind it to the image file.
3. Establezca el identificador del sello y el origen de la ubicación.
4. Add the stamp to the document.
5. Save the result and close the facade object.

### Java example

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a PDF page as a stamp

Utilice este flujo de trabajo cuando el contenido de otra página PDF deba reutilizarse como contenido de sello.

### Pasos

1. Cree una instancia `PdfFileStamp` y vincule el PDF de destino.
2. Create a `Stamp` object.
3. Bind the stamp to a specific page from another PDF file.
4. Set the target page number and origin for placement.
5. Agregue el sello, guarde el resultado y cierre el objeto de fachada.

### Java example

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a text stamp with TextState

Use this workflow when the stamp should contain styled text rather than an image.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object.
3. Bind a `FormattedText` logo and a custom `TextState` to the stamp.
4. Set the stamp origin and rotation.
5. Add the stamp, save the output, and close the facade object.

### Java example

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a stamp to specific pages

Use this workflow when the stamp should appear only on selected pages instead of the whole document.

### Steps

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Create a `Stamp` object and bind it to an image file.
3. Set the target page list, origin, and image size.
4. Add the stamp to the document.
5. Save the result and close the facade object.

### Ejemplo de Java

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Add a background image stamp

Use this workflow when the stamp should appear behind page content with controlled opacity and rotation.

### Pasos

1. Create a `PdfFileStamp` instance and bind the source PDF.
2. Cree un objeto `Stamp` y vincúlelo al archivo de imagen.
3. Mark the stamp as background content.
4. Configure opacidad, calidad, rotación, tamaño y origen.
5. Add the stamp, save the output, and close the facade object.

### Ejemplo de Java

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
