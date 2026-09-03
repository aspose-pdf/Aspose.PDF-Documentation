---
title: Agregar marcas de imagen al PDF en Java
linktitle: Marcas de imagen en archivo PDF
type: docs
weight: 10
url: /es/java/image-stamps-in-pdf-page/
description: Aprenda a agregar marcas de imagen a las páginas PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar marcas de imagen y fondos de imagen a las páginas PDF con Java
Abstract: Este artículo explica cómo agregar sellos de imagen a archivos PDF usando Aspose.PDF for Java. Cubre los sellos de imagen con posicionamiento, rotación, opacidad y control de calidad, y el uso de una imagen como fondo de una caja flotante.
---
Aspose.PDF for Java admite sellos de imagen como superposiciones y elementos de diseño respaldados por imágenes.

## Agregar un sello de imagen

Utilice este ejemplo cuando una página deba mostrar un sello de imagen con una ubicación personalizada y opacidad.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) y configure su apariencia.
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

## Agregar una marca de imagen con control de calidad

Utilice este ejemplo cuando necesite ajustar la calidad de renderizado del sello de imagen.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) y establezca el valor de calidad.
1. Agregue el sello a la página y guarde el resultado.

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

## Utiliza una imagen como fondo de una caja flotante

Utiliza este ejemplo cuando una imagen debe servir como fondo de un contenedor de diseño con estilo.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y accede a la página objetivo.
1. Crear un [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) con texto y configuraciones de borde.
1. Establezca la imagen de fondo, añada el cuadro a la página y guarde el documento.

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
