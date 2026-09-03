---
title: Convertir formatos de imagen a PDF en Java
linktitle: Convertir imágenes a PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: Aprenda a convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR y otros formatos de imagen a PDF en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir imágenes a PDF en Java
Abstract: Este artículo explica cómo convertir múltiples formatos de imagen a PDF usando Aspose.PDF para Java. Cubre la colocación directa de imágenes en una nueva página PDF, así como opciones de carga específicas del tipo de archivo para entradas CGM, SVG y CDR.
---
Aspose.PDF para Java puede convertir muchos formatos de imágenes rasterizadas y vectoriales en documentos PDF.


## 
Convertir BMP a PDF



Utilice este ejemplo cuando deba colocar una imagen BMP en un documento PDF.


1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para contener el PDF de salida.

1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque el BMP con `page.addImage(...)`.
1. Defina el rectángulo de la imagen de destino con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que el contenido rasterizado llene el área de la página PDF.

1. Guarde el archivo PDF de salida.


```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 
Convertir CGM a PDF



Utilice este ejemplo cuando un archivo de gráficos CGM deba convertirse a PDF.


1. Abra la fuente CGM pasando la ruta del archivo y [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) al constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deje que Aspose.PDF interprete el flujo de gráficos CGM durante la carga del documento.

1. Guarde el PDF convertido en la ruta de salida de destino.


```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir DICOM a PDF



Utilice este ejemplo cuando una imagen DICOM médica deba incluirse en un documento PDF.


1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para la salida PDF.
1. Cree un objeto [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), establezca su [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) en `Dicom` y asigne la ruta del archivo fuente.

1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y agregue la imagen DICOM a la colección de párrafos de la página.

1. Guarde el resultado como PDF.


```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta EMF a PDF con carga directa de documentos



Utilice este ejemplo cuando un archivo EMF deba convertirse a PDF a través de la ruta de carga principal de EMF.

1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío y abra la fuente EMF como una secuencia binaria.

1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y borre sus márgenes para que la obra de arte de EMF pueda ocupar el área completa de la página.

1. Cree un [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), vincule la secuencia EMF y agréguelo a la colección de párrafos de la página.

1. Guarde el archivo PDF de salida.


```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta EMF a PDF con un flujo de trabajo alternativo

Utilice este ejemplo cuando el contenido EMF deba convertirse utilizando una configuración alternativa o un flujo de composición de página.


1. Cargue la fuente EMF con Aspose.Imaging y renderícela en una secuencia PNG en memoria antes de colocar el PDF.

1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío y agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Cree un [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) a partir del flujo de bytes intermedio y agréguelo a la página.

1. Guarde el PDF convertido.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir GIF a PDF



Utilice este ejemplo cuando deba agregar una imagen GIF a una página PDF.


1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para la salida PDF.

1. Agrega un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloca el GIF con `page.addImage(...)`.

1. Defina los límites de ubicación con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que la imagen llene el área de la página.
1. Guarde el PDF de salida.


```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir JPEG a PDF



Utilice este ejemplo cuando una imagen JPEG deba convertirse en un PDF de una página.


1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para el PDF de salida.

1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e inserte la imagen JPEG con `page.addImage(...)`.
1. Utilice [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para controlar cómo se asigna la imagen rasterizada a las coordenadas de la página.

1. Guarde el archivo PDF generado.


```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PNG a PDF



Utilice este ejemplo cuando una imagen PNG deba incluirse en un documento PDF.


1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para la salida de la conversión.
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque la imagen PNG con `page.addImage(...)`.

1. Utilice [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para ajustar el tamaño de la imagen al lienzo de la página.

1. Guarde el archivo de salida.


```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir SVG a PDF



Utilice este ejemplo cuando las ilustraciones SVG deban representarse dentro de un documento PDF.

1. Abra la fuente SVG pasando la ruta del archivo y [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) al constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Deje que Aspose.PDF analice el marcado SVG y cree el modelo de gráficos PDF correspondiente durante la carga.

1. Guarde la salida del PDF en la ruta del archivo de destino.


```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir TIFF a PDF



Utilice este ejemplo cuando deba convertir una imagen TIFF a PDF.

1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vacío para la salida PDF.

1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque la imagen TIFF con `page.addImage(...)`.

1. Defina el área de ubicación con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que el contenido TIFF se asigne a las coordenadas de la página.

1. Guarde el resultado como PDF.


```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir CDR a PDF

Utilice este ejemplo cuando deba convertir un archivo CDR de CorelDRAW a PDF.


1. Abra la fuente del CDR pasando la ruta del archivo y [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) al constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Deje que Aspose.PDF cargue el contenido de CorelDRAW en el modelo de documento PDF.

1. Guarde el archivo PDF convertido en la ruta de salida solicitada.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
