---
title: Clase Stamp
linktitle: Clase Stamp
type: docs
weight: 150
url: /es/java/stamp-class/
description: Aprenda cómo trabajar con la clase Stamp en Java para agregar sellos basados en imágenes, PDF y texto a documentos PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos de imagen, PDF y texto a documentos PDF en Java
Abstract: Esta sección explica cómo usar la clase Stamp junto con PdfFileStamp en Aspose.PDF for Java para agregar contenido de sello reutilizable a documentos PDF. Los ejemplos actuales en Java cubren sellos de imagen, sellos de página PDF, sellos de texto con un TextState personalizado, sellos específicos por página y sellos de imagen de fondo con configuraciones de opacidad, tamaño y rotación.
---
El Java `StampExamples` La clase demuestra los principales flujos de trabajo de creación de sellos disponibles a través de la Facades API.

## Agregar un sello de imagen

Utilice este flujo de trabajo cuando un archivo de imagen debe colocarse en el PDF como sello.

### Pasos

1. Crear un `PdfFileStamp` instancia y vincula el PDF de origen.
2. Crear un `Stamp` objeto y enlazarlo al archivo de imagen.
3. Establezca el identificador del sello y el origen de colocación.
4. Añada el sello al documento.
5. Guarde el resultado y cierre el objeto fachada.

### Ejemplo de Java

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

## Agregar una página PDF como sello

Utilice este workflow cuando el contenido de otra página PDF deba reutilizarse como contenido de sello.

### Pasos

1. Crear un `PdfFileStamp` instancia y enlaza el PDF de destino.
2. Crear un `Stamp` objeto.
3. Vincule el sello a una página específica de otro archivo PDF.
4. Establezca el número de página de destino y el origen para la ubicación.
5. Agregue el sello, guarde la salida y cierre el objeto fachada.

### Ejemplo de Java

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

## Agregar un sello de texto con TextState

Utilice este flujo de trabajo cuando el sello debe contener texto con estilo en lugar de una imagen.

### Pasos

1. Crear un `PdfFileStamp` instancia y vincula el PDF de origen.
2. Crear un `Stamp` objeto.
3. Vincular un `FormattedText` logo y un personalizado `TextState` al sello.
4. Establece el origen y la rotación del sello.
5. Agregue el sello, guarde la salida y cierre el objeto fachada.

### Ejemplo de Java

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

## Agregar una marca a páginas específicas

Utilice este flujo de trabajo cuando el sello debe aparecer solo en páginas seleccionadas en lugar de en todo el documento.

### Pasos

1. Crear un `PdfFileStamp` instancia y vincula el PDF de origen.
2. Crear un `Stamp` objeto y enlazarlo a un archivo de imagen.
3. Establezca la lista de páginas de destino, el origen y el tamaño de la imagen.
4. Añada el sello al documento.
5. Guarde el resultado y cierre el objeto fachada.

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

## Agregar una marca de imagen de fondo

Utilice este flujo de trabajo cuando el sello debe aparecer detrás del contenido de la página con opacidad y rotación controladas.

### Pasos

1. Crear un `PdfFileStamp` instancia y vincula el PDF de origen.
2. Crear un `Stamp` objeto y enlazarlo al archivo de imagen.
3. Marque el sello como contenido de fondo.
4. Configure la opacidad, la calidad, la rotación, el tamaño y el origen.
5. Agregue el sello, guarde la salida y cierre el objeto fachada.

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
