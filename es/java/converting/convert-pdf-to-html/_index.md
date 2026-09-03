---
title: Convertir PDF a HTML en Java
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /es/java/convert-pdf-to-html/
lastmod: "2026-09-03"
description: Aprenda cómo convertir PDF a HTML en Java con Aspose.PDF, incluyendo salida de varias páginas, carpetas externas de imágenes, manejo de SVG y renderizado en capas de HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a HTML en Java
Abstract: Este artículo explica cómo convertir archivos PDF a HTML usando Aspose.PDF for Java. Cubre la exportación básica a HTML junto con opciones para carpetas de imágenes, división de páginas, salida SVG, gráficos SVG comprimidos, fondos de página PNG, marcado solo del cuerpo, renderizado de texto transparente y conversión de capa de documento.
---
Aspose.PDF for Java admite la exportación a HTML con opciones para imágenes, SVG, división de páginas, transparencia y renderizado de capas. Utilice [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para controlar cómo se escriben las páginas PDF, los recursos y el marcado en la salida HTML.

## Convertir PDF a HTML

Utilice este ejemplo cuando se deba exportar un PDF a un documento HTML estándar.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear predeterminado [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para la serialización HTML estándar.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que el contenido de la página PDF se exporta como marcado HTML.
1. Guarda la salida HTML generada.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML y almacenar imágenes por separado

Utilice este ejemplo cuando las imágenes extraídas deben guardarse como archivos separados durante la exportación a HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establecer `setSpecialFolderForAllImages(...)` a un directorio de salida de imágenes dedicado.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto, las imágenes ráster se emiten como archivos de recursos separados en lugar de salida solo en línea.
1. Guarda la salida HTML junto con los activos de imagen generados.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML multipágina

Utilice este ejemplo cuando cada página PDF deba representarse por separado en la salida HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilitar `setSplitIntoPages(true)`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que cada página PDF se escribe como una salida HTML separada.
1. Guarda los archivos HTML generados.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML y almacenar SVG por separado

Utiliza este ejemplo cuando el contenido vectorial debe emitirse como recursos SVG separados.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establecer `setSpecialFolderForSvgImages(...)` a un directorio de recursos SVG externo.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que los gráficos vectoriales se almacenan fuera del archivo HTML principal.
1. Guarda la salida HTML y los recursos SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML con SVG comprimido

Utilice este ejemplo cuando la salida SVG deba optimizarse durante la exportación HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y configure una carpeta dedicada para los recursos SVG.
1. Habilitar `setCompressSvgGraphicsIfAny(true)` por lo que los recursos SVG se comprimen durante la exportación.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarda los archivos HTML convertidos.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML con fondos de página PNG

Utilice este ejemplo cuando los fondos de página deben renderizarse como imágenes PNG en la salida HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establezca el modo de guardado de imágenes raster a fondos de página PNG.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto, el contenido de fondo de la página se emite como capas HTML respaldadas por PNG.
1. Guarda la salida HTML convertida.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a contenido del cuerpo HTML únicamente

Utilice este ejemplo cuando solo se necesite el marcado del cuerpo en lugar de una estructura completa de documento HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establecer el modo de generación de marcado a `WriteOnlyBodyContent`.
1. Mantener `setSplitIntoPages(true)` habilitado cuando la salida solo del cuerpo aún debe estar separada por páginas.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarde la salida HTML.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML con renderizado de texto transparente

Utilice este ejemplo cuando se deba preservar el texto transparente en la exportación HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilitar la preservación de texto transparente y sombreado.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que la apariencia del texto relacionada con la transparencia se retiene en el resultado HTML.
1. Guarda la salida HTML convertida.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a HTML con renderizado de capa del documento

Utilice este ejemplo cuando la visibilidad de capas del PDF deba reflejarse en el resultado HTML.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilitar `setConvertMarkedContentToLayers(true)`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` Por lo tanto, el contenido marcado del PDF se asigna a capas HTML.
1. Guarde los archivos HTML exportados.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
