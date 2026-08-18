---
title: Converta PDF em formatos de imagem em Java
linktitle: Converter PDF em imagens
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: Aprenda como renderizar páginas PDF como arquivos TIFF, BMP, EMF, JPEG, PNG, GIF e SVG em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Converta páginas PDF em TIFF, PNG, JPEG, GIF, BMP, EMF e SVG em Java
Abstract: Este artigo explica como converter arquivos PDF em formatos de imagem comuns com Aspose.PDF para Java. Abrange a exportação TIFF de todo o documento, geração raster por página com dispositivos de imagem, substituição opcional de fonte durante a exportação PNG e saída SVG com `SvgSaveOptions`.
---
Aspose.PDF para Java pode renderizar páginas PDF em formatos de imagem raster e vetorial com opções de dispositivo específicas de formato.

## Converter PDF em BMP

Use este exemplo quando as páginas PDF devem ser renderizadas como imagens BMP.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere `document.getPages()` e chame `device.process(...)` para cada página.
1. Salve as imagens BMP geradas em caminhos de saída numerados.

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

## Converter PDF em EMF

Use este exemplo quando as páginas PDF devem ser exportadas como imagens vetoriais EMF.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para cada página.
1. Salve as saídas EMF em caminhos de arquivo numerados.

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

## Converter PDF em GIF

Use este exemplo quando as páginas PDF devem ser convertidas em imagens GIF.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para renderizar cada página.
1. Salve os arquivos GIF em caminhos de saída numerados.

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

## Converter PDF em JPEG

Use este exemplo quando as páginas PDF devem ser exportadas como imagens JPEG.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para rasterizar cada página para JPEG.
1. Salve os arquivos de saída JPEG em caminhos numerados.

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

## Converter PDF em PNG

Use este exemplo quando páginas PDF devem ser convertidas em imagens PNG.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para cada página do PDF.
1. Salve as saídas PNG em caminhos de arquivo numerados.

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

## Converta PDF em PNG com uma fonte padrão

Use este exemplo quando a renderização precisar usar uma fonte substituta para glifos ausentes.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) com [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Habilite `document.setAbsentFontTryToSubstitute(true)` para que os glifos ausentes possam substituir as fontes durante a renderização.
1. Renderize as páginas e salve os arquivos PNG.

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

## Converter PDF em SVG

Use este exemplo quando páginas PDF devem ser exportadas como gráficos SVG.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) e desative a compactação ZIP quando a saída bruta `.svg` for necessária.
1. Habilite `setTreatTargetFileNameAsDirectory(true)` para que a saída SVG por página possa ser organizada no caminho de destino.
1. Salve a saída SVG.

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

## Converter PDF em TIFF

Use este exemplo quando uma ou mais páginas PDF devem ser exportadas para TIFF.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) e configure compactação, profundidade de cor e comportamento de página em branco.
1. Crie um [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI e as configurações TIFF preparadas.
1. Renderize as páginas e salve a saída TIFF.

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
