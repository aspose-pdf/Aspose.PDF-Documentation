---
title: Convertir PDF a formatos de imagen en Java
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/java/convert-pdf-to-images-format/
lastmod: "2026-09-03"
description: Aprenda cómo renderizar páginas PDF como archivos TIFF, BMP, EMF, JPEG, PNG, GIF y SVG en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Convierta páginas PDF a TIFF, PNG, JPEG, GIF, BMP, EMF y SVG en Java.
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de imagen comunes con Aspose.PDF for Java. Cubre la exportación de TIFF a nivel de documento, la generación de ráster por página con dispositivos de imagen, la sustitución opcional de fuentes durante la exportación a PNG y la salida SVG con `SvgSaveOptions`.
---
Aspose.PDF for Java puede renderizar páginas PDF a formatos de imagen rasterizados y vectoriales con opciones de dispositivo específicas del formato.

## Convertir PDF a BMP

Utilice este ejemplo cuando las páginas PDF deban renderizarse como imágenes BMP.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Iterar a través de `document.getPages()` y llamar `device.process(...)` para cada página.
1. Guarda las imágenes BMP generadas en rutas de salida numeradas.

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

## Convertir PDF a EMF

Utilice este ejemplo cuando las páginas PDF deben exportarse como imágenes vectoriales EMF.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Iterar a través de las páginas y llamar `device.process(...)` para cada página.
1. Guarde las salidas EMF en rutas de archivo numeradas.

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

## Convertir PDF a GIF

Utilice este ejemplo cuando las páginas PDF deban convertirse en imágenes GIF.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Iterar a través de las páginas y llamar `device.process(...)` para renderizar cada página.
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

## Convertir PDF a JPEG

Utilice este ejemplo cuando las páginas PDF deban exportarse como imágenes JPEG.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Iterar a través de las páginas y llamar `device.process(...)` rasterizar cada página a JPEG.
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

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Iterar a través de las páginas y llamar `device.process(...)` para cada página PDF.
1. Guarde las salidas PNG en rutas de archivo numeradas.

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

## Convertir PDF a PNG con una fuente predeterminada de respaldo

Utilice este ejemplo cuando la renderización debe usar una fuente de respaldo para los glifos que faltan.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Habilitar `document.setAbsentFontTryToSubstitute(true)` para que los glifos faltantes puedan recurrir a fuentes de sustitución durante el renderizado.
1. Renderiza las páginas y guarda los archivos PNG.

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

## Convertir PDF a SVG

Utilice este ejemplo cuando las páginas PDF deban exportarse como gráficos SVG.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) y desactivar la compresión ZIP cuando sea en bruto `.svg` Se requiere salida.
1. Habilitar `setTreatTargetFileNameAsDirectory(true)` de modo que la salida SVG por página pueda organizarse bajo la ruta de destino.
1. Guardar la salida SVG.

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

## Convertir PDF a TIFF

Utilice este ejemplo cuando una o más páginas PDF deban exportarse a TIFF.

1. Abre el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) y configure la compresión, la profundidad de color y el comportamiento de páginas en blanco.
1. Crear un [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) con un [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI y los ajustes de TIFF preparados.
1. Renderiza las páginas y guarda la salida TIFF.

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
