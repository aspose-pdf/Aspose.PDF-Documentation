---
title: Agregar fondos PDF en Java
linktitle: Agregar fondos
type: docs
weight: 20
url: /es/java/add-backgrounds/
description: Agregar fondos de imagen y de color sólido a las páginas PDF en Java y ajustar la opacidad de la imagen.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar fondos en Java
Abstract: Agregar fondos de imagen y de color sólido a las páginas PDF en Java y ajustar la opacidad de la imagen.
---
Los artefactos de fondo le permiten colocar elementos visuales que no son contenido detrás del contenido principal de la página sin cambiar el texto lógico del documento.

## Agregar una imagen de fondo a un PDF

Utilice este ejemplo cuando la página debe mostrar una imagen como un artefacto de fondo.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra el flujo de imagen.
1. Cree un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) y asigne el flujo de imagen.
1. Agregue el artefacto a la página de destino y guarde el PDF de salida.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Agregar una imagen de fondo con opacidad

Este ejemplo coloca una imagen de fondo semitransparente detrás del contenido de la página.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra el flujo de imagen.
1. Cree un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), asigne la imagen, y establezca la opacidad.
1. Agregue el artefacto a la página y guarde el documento.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Agregar un color de fondo a un PDF

Utilice este ejemplo cuando la página deba usar un color de fondo sólido en lugar de una imagen.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) y asigne el color de fondo.
1. Agregue el artefacto a la página y guarde el archivo de salida.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Temas relacionados

- [Eliminar fondos](/pdf/es/java/remove-backgrounds/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
