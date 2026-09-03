---
title: Agregar fondos PDF en Java
linktitle: Agregar fondos
type: docs
weight: 20
url: /es/java/add-backgrounds/
description: Aprende cómo agregar una imagen de fondo o un color de fondo a páginas PDF en Java usando `BackgroundArtifact` con Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar fondo a PDF con Java
Abstract: Este artículo explica cómo agregar o eliminar fondos de página PDF en Java usando Aspose.PDF. Cubre la incorporación de una imagen de fondo, el ajuste de la opacidad de la imagen, la aplicación de un color de fondo y la eliminación de artefactos de fondo de una página.
---
Los artefactos de fondo le permiten colocar elementos visuales no contenidos detrás del contenido principal de la página sin cambiar el texto lógico del documento.

## Agregar una imagen de fondo a un PDF

Utilice este ejemplo cuando la página deba mostrar una imagen como artefacto de fondo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y la secuencia de entrada de imagen.
1. Crear un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) y asignar el flujo de imagen.
1. Agregar el artefacto a la página de destino y guardar el PDF de salida.

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

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y flujo de imagen.
1. Crear un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), asigna la imagen, y establece la opacidad.
1. Agrega el artefacto a la página y guarda el documento.

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

Utilice este ejemplo cuando la página debe usar un color de fondo sólido en lugar de una imagen.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) y asignar el color de fondo.
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

## Eliminar artefactos de fondo

Utilice este enfoque cuando los artefactos de fondo existentes deban eliminarse de la página.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de la colección de artefactos de la página en orden inverso.
1. Eliminar los artefactos cuyo tipo es paginación y subtipo es fondo, luego guardar el documento.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
