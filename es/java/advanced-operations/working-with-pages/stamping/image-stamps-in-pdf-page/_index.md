---
title: Agregar sellos de imagen a PDF en Java
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Aprenda a agregar sellos de imágenes a páginas PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos de imágenes y fondos de imágenes a páginas PDF con Java
Abstract: Este artículo explica cómo agregar sellos de imágenes a archivos PDF usando Aspose.PDF para Java. Cubre sellos de imágenes con posicionamiento, rotación, opacidad y control de calidad, y el uso de una imagen como fondo de un cuadro flotante.
---
Aspose.PDF para Java admite sellos de imágenes como superposiciones y elementos de diseño respaldados por imágenes.


## 
Agregar un sello de imagen



Utilice este ejemplo cuando una página deba mostrar un sello de imagen con ubicación y opacidad personalizadas.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) y configure su apariencia.
1. Agregue el sello a la página y guarde el documento.


```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Añadir un sello de imagen con control de calidad.



Utilice este ejemplo cuando necesite ajustar la calidad de representación del sello de imagen.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) y establezca el valor de calidad.
1. Añade el sello a la página y guarda el resultado.


```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Utilice una imagen como fondo de cuadro flotante



Utilice este ejemplo cuando una imagen deba servir como fondo de un contenedor de diseño con estilo.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y acceda a la página de destino.

1. 
Cree un [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) con configuración de texto y borde.
1. Configure la imagen de fondo, agregue el cuadro a la página y guarde el documento.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
