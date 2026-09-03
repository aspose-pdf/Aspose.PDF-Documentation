---
title: Convertir PDF a formatos de imagen en Java
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: Aprenda a renderizar páginas PDF como archivos TIFF, BMP, EMF, JPEG, PNG, GIF y SVG en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Convierta páginas PDF a TIFF, PNG, JPEG, GIF, BMP, EMF y SVG en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de imagen comunes con Aspose.PDF para Java. Cubre la exportación TIFF de todo el documento, la generación de ráster por página con dispositivos de imagen, la sustitución de fuentes opcional durante la exportación PNG y la salida SVG con `SvgSaveOptions`.
---
Aspose.PDF para Java puede representar páginas PDF en formatos de imágenes rasterizadas y vectoriales con opciones de dispositivo específicas del formato.


## 
Convertir PDF a BMP



Utilice este ejemplo cuando las páginas PDF deban representarse como imágenes BMP.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Repita `document.getPages()` y llame a `device.process(...)` para cada página.

1. Guarde las imágenes BMP generadas en rutas de salida numeradas.


```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## 
Convertir PDF a EMF



Utilice este ejemplo cuando las páginas PDF deban exportarse como imágenes vectoriales EMF.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. Recorra las páginas y llame a `device.process(...)` para cada página.

1. Guarde las salidas de EMF en rutas de archivos numeradas.


```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir PDF a GIF



Utilice este ejemplo cuando las páginas PDF deban convertirse en imágenes GIF.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. Repita las páginas y llame a `device.process(...)` para representar cada página.

1. Guarde los archivos GIF en rutas de salida numeradas.


```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir PDF a JPEG

Utilice este ejemplo cuando las páginas PDF deban exportarse como imágenes JPEG.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. Repita las páginas y llame a `device.process(...)` para rasterizar cada página a JPEG.

1. Guarde los archivos de salida JPEG en rutas numeradas.

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Convertir PDF a PNG



Utilice este ejemplo cuando las páginas PDF deban convertirse en imágenes PNG.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. Recorra las páginas y llame a `device.process(...)` para cada página PDF.
1. Guarde las salidas PNG en rutas de archivos numeradas.


```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convierta PDF a PNG con una fuente alternativa predeterminada



Utilice este ejemplo cuando la renderización deba utilizar una fuente alternativa para los glifos faltantes.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Habilite `document.setAbsentFontTryToSubstitute(true)` para que los glifos faltantes puedan recurrir a fuentes sustitutas durante el renderizado.

1. Renderice las páginas y guarde los archivos PNG.


```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir PDF a SVG



Utilice este ejemplo cuando las páginas PDF deban exportarse como gráficos SVG.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) y desactive la compresión ZIP cuando se requiera salida `.svg` sin formato.

1. Habilite `setTreatTargetFileNameAsDirectory(true)` para que la salida SVG por página se pueda organizar en la ruta de destino.

1. Guarde la salida SVG.


```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir PDF a TIFF



Utilice este ejemplo cuando una o más páginas PDF deban exportarse a TIFF.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) y configure la compresión, la profundidad del color y el comportamiento de página en blanco.

1. Cree un [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI y la configuración TIFF preparada.

1. Renderice las páginas y guarde la salida TIFF.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
