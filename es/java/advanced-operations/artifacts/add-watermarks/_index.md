---
title: Agregar marcas de agua a PDF en Java
linktitle: Agregar marcas de agua
type: docs
weight: 30
url: /es/java/add-watermarks/
description: Agregar artefactos de marcas de agua de texto con estilo a páginas PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar marcas de agua en Java
Abstract: Agregar artefactos de marcas de agua de texto con estilo a páginas PDF en Java.
---
Los artefactos de marcas de agua le permiten colocar marcas visuales persistentes en una página sin mezclararlas con el contenido principal del documento.

## Agregar un artefacto de marca de agua

Utilice este ejemplo cuando la página debe mostrar una marca de agua de texto centrada con rotación personalizada, opacidad y ubicación de fondo.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) y configure su estado de texto y la configuración de ubicación.
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

## Temas relacionados

- [Extraer detalles de marca de agua](/pdf/es/java/extract-watermarks/)
- [Eliminar marcas de agua](/pdf/es/java/remove-watermarks/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
