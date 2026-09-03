---
title: Convertir formatos de imagen a PDF en Java
linktitle: Convertir imágenes a PDF
type: docs
weight: 60
url: /es/java/convert-images-format-to-pdf/
lastmod: "2026-09-03"
description: Aprenda cómo convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR y otros formatos de imagen a PDF en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir imágenes a PDF en Java
Abstract: Este artículo explica cómo convertir varios formatos de imagen a PDF usando Aspose.PDF for Java. Cubre la colocación directa de imágenes en una nueva página PDF, así como opciones de carga específicas por tipo de archivo para entradas CGM, SVG y CDR.
---
Aspose.PDF for Java puede convertir muchos formatos de imagen raster y vectorial en documentos PDF.

## Convertir BMP a PDF

Utilice este ejemplo cuando una imagen BMP deba insertarse en un documento PDF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para contener el PDF de salida.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque el BMP con `page.addImage(...)`.
1. Defina el rectángulo de imagen de destino con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) de modo que el contenido rasterizado llena el área de la página PDF.
1. Guarda el archivo PDF de salida.

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

## Convertir CGM a PDF

Utilice este ejemplo cuando se deba convertir un archivo de gráficos CGM a PDF.

1. Abre el origen CGM pasando la ruta del archivo y [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF interprete la secuencia de gráficos CGM durante la carga del documento.
1. Guarde el PDF convertido en la ruta de salida objetivo.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir DICOM a PDF

Utilice este ejemplo cuando una imagen médica DICOM deba incorporarse en un documento PDF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para la salida PDF.
1. Crear un [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) objeto, establezca su [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) a `Dicom`, y asigna la ruta del archivo fuente.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y añada la imagen DICOM a la colección de párrafos de la página.
1. Guarda el resultado como PDF.

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

## Convertir EMF a PDF con carga directa del documento

Utilice este ejemplo cuando un archivo EMF deba convertirse a PDF a través de la ruta principal de carga de EMF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra la fuente EMF como una secuencia binaria.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y elimine sus márgenes para que la obra de arte EMF pueda ocupar toda el área de la página.
1. Crear un [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), vincula el flujo EMF a él, y añádelo a la colección de párrafos de la página.
1. Guarda el archivo PDF de salida.

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

## Convertir EMF a PDF con un flujo de trabajo alternativo

Utilice este ejemplo cuando el contenido EMF deba convertirse utilizando una configuración alternativa o un flujo de composición de página.

1. Cargue la fuente EMF con Aspose.Imaging y conviértala en un flujo PNG en memoria antes de la colocación en PDF.
1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añadir un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crear un [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) del flujo intermedio de bytes y añádelo a la página.
1. Guarda el PDF convertido.

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

Utilice este ejemplo cuando se deba agregar una imagen GIF a una página PDF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para la salida PDF.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloca el GIF con `page.addImage(...)`.
1. Definir los límites de ubicación con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que la imagen llene el área de la página.
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

## Convertir JPEG a PDF

Utilice este ejemplo cuando una imagen JPEG deba convertirse en un PDF de una página.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para el PDF de salida.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e inserte la imagen JPEG con `page.addImage(...)`.
1. Usar [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para controlar cómo se asigna la imagen raster a las coordenadas de la página.
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

## Convertir PNG a PDF

Utilice este ejemplo cuando una imagen PNG deba envolverse en un documento PDF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para la salida de conversión.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque la imagen PNG en él con `page.addImage(...)`.
1. Usar [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para dimensionar la imagen respecto al lienzo de la página.
1. Guardar el archivo de salida.

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

## Convertir SVG a PDF

Utilice este ejemplo cuando el arte SVG deba renderizarse dentro de un documento PDF.

1. Abra la fuente SVG pasando la ruta del archivo y [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF analice el marcado SVG y cree el modelo gráfico PDF correspondiente durante la carga.
1. Guarda la salida PDF en la ruta de archivo de destino.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir TIFF a PDF

Utilice este ejemplo cuando una imagen TIFF deba convertirse en PDF.

1. Crear un vacío [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para la salida PDF.
1. Agregar un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y coloque la imagen TIFF con `page.addImage(...)`.
1. Define el área de colocación con [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) por lo que el contenido TIFF se asigna a las coordenadas de la página.
1. Guarda el resultado como PDF.

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

## Convertir CDR a PDF

Utilice este ejemplo cuando se deba convertir un archivo CorelDRAW CDR a PDF.

1. Abra la fuente CDR pasando la ruta del archivo y [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF cargue el contenido de CorelDRAW en el modelo de documento PDF.
1. Guarde el archivo PDF convertido en la ruta de salida solicitada.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
