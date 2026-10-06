---
title: Converter PDF para formatos de imagem em Java
linktitle: Converter PDF para imagens
type: docs
weight: 70
url: /pt/java/convert-pdf-to-images-format/
lastmod: "2026-10-06"
description: Aprenda como renderizar páginas PDF como arquivos TIFF, BMP, EMF, JPEG, PNG, GIF e SVG em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Converter páginas PDF para TIFF, PNG, JPEG, GIF, BMP, EMF e SVG em Java
Abstract: Este artigo explica como converter arquivos PDF para formatos de imagem comuns com Aspose.PDF for Java. Ele cobre exportação de TIFF em todo o documento, geração raster por página com dispositivos de imagem, substituição opcional de fontes durante a exportação PNG e saída SVG com `SvgSaveOptions`.
---
Aspose.PDF for Java pode renderizar páginas PDF em formatos de imagem raster e vetor com opções de dispositivo específicas do formato.

## Converter PDF para BMP

Use este exemplo quando as páginas PDF devem ser renderizadas como imagens BMP.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere através de `document.getPages()` e chame `device.process(...)` para cada página.
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

## Converter PDF para EMF

Use este exemplo quando as páginas PDF devem ser exportadas como imagens vetoriais EMF.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
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

## Converter PDF para GIF

Use este exemplo quando as páginas do PDF devem ser convertidas em imagens GIF.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
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

## Converter PDF para JPEG

Use este exemplo quando as páginas PDF devem ser exportadas como imagens JPEG.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para rasterizar cada página em JPEG.
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

## Converter PDF para PNG

Use este exemplo quando as páginas de PDF devem ser convertidas em imagens PNG.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Itere pelas páginas e chame `device.process(...)` para cada página PDF.
1. Salve as saídas PNG em caminhos de arquivos numerados.

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

## Converter PDF para PNG com fallback de fonte padrão

Use este exemplo quando a renderização deve usar uma fonte de fallback para glifos ausentes.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) com um [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Ative `document.setAbsentFontTryToSubstitute(true)` para que glifos ausentes possam recorrer a fontes substitutas durante a renderização.
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

## Converter PDF para SVG

Use este exemplo quando as páginas PDF devem ser exportadas como gráficos SVG.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) e desative a compressão ZIP quando bruto `.svg` a saída é necessária.
1. Ative `setTreatTargetFileNameAsDirectory(true)` para que a saída SVG por página possa ser organizada no caminho de destino.
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

## Converter PDF para TIFF

Use este exemplo quando uma ou mais páginas PDF devem ser exportadas para TIFF.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) e configure a compressão, a profundidade de cor e o comportamento de páginas em branco.
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
