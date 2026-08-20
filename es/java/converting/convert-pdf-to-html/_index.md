---
title: Convertir PDF a HTML en Java
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: Aprenda cómo convertir PDF a HTML en Java con Aspose.PDF, incluida la salida de varias páginas, carpetas de imágenes externas, manejo de SVG y representación HTML en capas.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a HTML en Java
Abstract: Este artículo explica cómo convertir archivos PDF a HTML usando Aspose.PDF para Java. Cubre la exportación HTML básica junto con opciones para carpetas de imágenes, división de páginas, salida SVG, gráficos SVG comprimidos, fondos de páginas PNG, marcado solo del cuerpo, representación de texto transparente y conversión de capas de documentos.
---
Aspose.PDF para Java admite la exportación HTML con opciones para imágenes, SVG, división de páginas, transparencia y representación de capas. Utilice [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) para controlar cómo se escriben las páginas PDF, los recursos y el marcado en la salida HTML.


## 
Convertir PDF a HTML



Utilice este ejemplo cuando deba exportar un PDF a un documento HTML estándar.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree el [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) predeterminado para la serialización HTML estándar.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido de la página PDF se exporte como formato HTML.

1. 
Guarde la salida HTML generada.


```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta PDF a HTML y almacene imágenes por separado



Utilice este ejemplo cuando las imágenes extraídas deban escribirse como archivos separados durante la exportación HTML.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establezca `setSpecialFolderForAllImages(...)` en un directorio de salida de imagen dedicado.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que las imágenes rasterizadas se emitan como archivos de recursos separados en lugar de una salida solo en línea.

1. 
Guarde la salida HTML junto con los recursos de imagen generados.


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

## 
Convertir PDF a HTML de varias páginas



Utilice este ejemplo cuando cada página PDF deba representarse por separado en la salida HTML.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilite `setSplitIntoPages(true)`.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que cada página PDF se escriba como una salida HTML independiente.

1. 
Guarde los archivos HTML generados.


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

## 
Convierta PDF a HTML y almacene SVG por separado

Utilice este ejemplo cuando el contenido vectorial deba emitirse como recursos SVG separados.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establezca `setSpecialFolderForSvgImages(...)` en un directorio de recursos SVG externo.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que los gráficos vectoriales se almacenen fuera del archivo HTML principal.

1. 
Guarde la salida HTML y los recursos SVG.

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

## Convierta PDF a HTML con SVG comprimido



Utilice este ejemplo cuando la salida SVG deba optimizarse durante la exportación HTML.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y configure una carpeta dedicada para los recursos SVG.

1. 
Habilite `setCompressSvgGraphicsIfAny(true)` para que los activos SVG se compriman durante la exportación.
1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde los archivos HTML convertidos.


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

## 
Convierta PDF a HTML con fondos de página PNG



Utilice este ejemplo cuando los fondos de la página deban representarse como imágenes PNG en la salida HTML.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y configure el modo de guardado de imágenes rasterizadas en fondos de página PNG.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido de fondo de la página se emita como capas HTML respaldadas por PNG.

1. 
Guarde la salida HTML convertida.


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

## 
Convierta PDF a contenido del cuerpo HTML únicamente



Utilice este ejemplo cuando solo se necesite el marcado del cuerpo en lugar de un documento HTML completo.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y establezca el modo de generación de marcado en `WriteOnlyBodyContent`.

1. 
Mantenga `setSplitIntoPages(true)` habilitado cuando la salida solo del cuerpo aún deba estar separada por páginas.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` y guarde el resultado HTML.


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

## 
Convierta PDF a HTML con representación de texto transparente



Utilice este ejemplo cuando deba conservarse el texto transparente en la exportación HTML.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilite la preservación de texto transparente y sombreado.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que la apariencia del texto relacionado con la transparencia se conserve en el resultado HTML.

1. 
Guarde la salida HTML convertida.


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

## 
Convierta PDF a HTML con renderizado de capas de documentos

Utilice este ejemplo cuando la visibilidad de la capa PDF deba reflejarse en el resultado HTML.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) y habilite `setConvertMarkedContentToLayers(true)`.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido PDF marcado se asigne a capas HTML.

1. 
Guarde los archivos HTML exportados.

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
