---
title: Agregar imagen a PDF usando Java
linktitle: Agregar imagen
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Aprenda a agregar imágenes a archivos PDF existentes en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregue imágenes a archivos PDF existentes con Java
Abstract: Este artículo muestra cómo agregar imágenes a documentos PDF usando Aspose.PDF para Java. Cubre la colocación de una imagen en coordenadas fijas, la adición de imágenes a través de operadores de página de bajo nivel, la configuración de texto alternativo para accesibilidad y la incrustación de datos de imagen con compresión Flate.
---
Aspose.PDF para Java admite tanto la colocación de imágenes de alto nivel como el dibujo basado en operadores de bajo nivel.


## 
Agregar una imagen con coordenadas de página



Utilice este ejemplo cuando necesite colocar una imagen en una posición fija en una página PDF.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue una página.

1. 
Llame a `page.addImage()` con la ruta de la imagen de origen y el rectángulo de destino.
1. Guarde el archivo PDF generado.


```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una imagen con operadores de página



Utilice este ejemplo cuando necesite un control de bajo nivel sobre la ubicación y el escalado de las imágenes mediante operadores de página.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra la secuencia de imágenes de origen.

1. 
Agregue la imagen a los recursos de la página y calcule el rectángulo de destino.
1. Escriba los operadores gráficos necesarios y guarde el documento.


```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## 
Agregar una imagen y establecer texto alternativo



Utilice este ejemplo cuando la imagen deba incluir metadatos de accesibilidad para lectores de pantalla.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue la imagen a la página.

1. 
Obtenga la [XImage] (https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) insertada de los recursos de la página.
1. Establezca el texto alternativo y guarde el PDF.


```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una imagen con compresión Flate



Utilice este ejemplo cuando desee incrustar datos de imagen mediante la compresión Flate.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra la secuencia de imágenes.

1. 
Agregue la imagen a los recursos de la página con `ImageFilterType.Flate`.
1. Dibuja la imagen a través de operadores de página y guarda el resultado.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
