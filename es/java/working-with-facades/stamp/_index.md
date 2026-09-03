---
title: Clase de sello
linktitle: Clase de sello
type: docs
weight: 150
url: /java/stamp-class/
description: Aprenda a trabajar con la clase Stamp en Java para agregar imágenes, PDF y sellos basados en texto a documentos PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos de imagen, PDF y texto a documentos PDF en Java
Abstract: Esta sección explica cómo utilizar la clase Stamp junto con PdfFileStamp en Aspose.PDF para Java para agregar contenido de sello reutilizable a documentos PDF. Los ejemplos actuales de Java cubren sellos de imágenes, sellos de páginas PDF, sellos de texto con un TextState personalizado, sellos específicos de página y sellos de imágenes de fondo con configuraciones de opacidad, tamaño y rotación.
---
La clase Java `StampExamples` demuestra los principales flujos de trabajo de creación de sellos disponibles a través de la API de Fachadas.


## 
Agregar un sello de imagen



Utilice este flujo de trabajo cuando un archivo de imagen deba colocarse en el PDF como un sello.


### 
Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.
2. Cree un objeto `Stamp` y vincúlelo al archivo de imagen.

3. Establezca el identificador del sello y el origen de la ubicación.

4. Añade el sello al documento.

5. Guarde el resultado y cierre el objeto de fachada.


### 
Ejemplo de Java

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



Utilice este flujo de trabajo cuando el contenido de otra página PDF deba reutilizarse como contenido de sello.


### 
Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de destino.

2. Cree un objeto `Stamp`.
3. Vincula el sello a una página específica de otro archivo PDF.

4. Establezca el número de página de destino y el origen de la ubicación.

5. Agregue el sello, guarde el resultado y cierre el objeto de fachada.


### 
Ejemplo de Java


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

## 
Agregar un sello de texto con TextState

Utilice este flujo de trabajo cuando el sello deba contener texto con estilo en lugar de una imagen.


### 
Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. Cree un objeto `Stamp`.

3. Vincula un logotipo `FormattedText` y un `TextState` personalizado al sello.
4. Establezca el origen y la rotación del sello.

5. Agregue el sello, guarde el resultado y cierre el objeto de fachada.


### 
Ejemplo de Java


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

## 
Agregar un sello a páginas específicas



Utilice este flujo de trabajo cuando el sello deba aparecer solo en páginas seleccionadas en lugar de en todo el documento.

### Pasos


1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. Cree un objeto `Stamp` y vincúlelo a un archivo de imagen.

3. Establezca la lista de páginas de destino, el origen y el tamaño de la imagen.

4. Añade el sello al documento.
5. Guarde el resultado y cierre el objeto de fachada.


### 
Ejemplo de Java


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

## 
Agregar un sello de imagen de fondo



Utilice este flujo de trabajo cuando el sello deba aparecer detrás del contenido de la página con opacidad y rotación controladas.


### 
Pasos

1. Cree una instancia `PdfFileStamp` y vincule el PDF de origen.

2. Cree un objeto `Stamp` y vincúlelo al archivo de imagen.

3. Marque el sello como contenido de fondo.

4. Configure opacidad, calidad, rotación, tamaño y origen.

5. Agregue el sello, guarde el resultado y cierre el objeto de fachada.

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
