---
title: Agregar marcas de agua a PDF en Java
linktitle: Agregar marca de agua
type: docs
weight: 30
url: /java/add-watermarks/
description: Aprenda a agregar, extraer y eliminar artefactos de marcas de agua en archivos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar una marca de agua a un PDF con Java
Abstract: Este artículo explica cómo agregar, inspeccionar y eliminar artefactos de marcas de agua en documentos PDF usando Aspose.PDF para Java. Cubre la creación de una marca de agua de texto con configuraciones de alineación, rotación, opacidad y fondo, la inspección de artefactos de marca de agua en una página y su eliminación.
---
Los artefactos de marca de agua le permiten colocar marcas visuales persistentes en una página sin mezclarlas con el contenido del documento principal.


## 
Extraiga artefactos de marcas de agua de un PDF



Utilice este ejemplo cuando necesite inspeccionar artefactos de marcas de agua existentes y leer su texto o posición.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de la colección de artefactos de la página de destino.
1. Filtre artefactos de paginación de marcas de agua e imprima su texto y rectángulos.


```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 
Agregar un artefacto de marca de agua



Utilice este ejemplo cuando la página deba mostrar una marca de agua de texto centrada con rotación, opacidad y ubicación de fondo personalizadas.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) y configure el estado del texto y los ajustes de ubicación.
1. Agregue la marca de agua a la página y guarde el archivo de salida.


```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar artefactos de marca de agua



Utilice este enfoque cuando los artefactos de marcas de agua existentes deban eliminarse de la página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de la colección de artefactos de la página en orden inverso.
1. Elimine los artefactos de paginación cuyo subtipo sea marca de agua y luego guarde el documento.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
