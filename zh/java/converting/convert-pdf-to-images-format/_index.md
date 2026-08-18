---
title: 在 Java 中将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 页面渲染为 TIFF、BMP、EMF、JPEG、PNG、GIF 和 SVG 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 在 Java 中将 PDF 页面转换为 TIFF、PNG、JPEG、GIF、BMP、EMF 和 SVG
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 PDF 文件转换为常见图像格式。它涵盖文档范围的 TIFF 导出、使用图像设备的每页光栅生成、PNG 导出期间的可选字体替换以及使用 `SvgSaveOptions` 的 SVG 输出。
---
Aspose.PDF for Java 可以使用特定于格式的设备选项将 PDF 页面渲染为光栅和矢量图像格式。

## 将 PDF 转换为 BMP

当 PDF 页面应呈现为 BMP 图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 迭代`document.getPages()`并为每个页面调用`device.process(...)`。
1. 将生成的 BMP 图像保存到编号的输出路径。

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

## 将 PDF 转换为 EMF

当 PDF 页面应导出为 EMF 矢量图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 遍历页面并为每个页面调用`device.process(...)`。
1. 将 EMF 输出保存到编号的文件路径。

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

## 将 PDF 转换为 GIF

当 PDF 页面需要转换为 GIF 图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 遍历页面并调用`device.process(...)`来渲染每个页面。
1. 将 GIF 文件保存到编号的输出路径。

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

## 将 PDF 转换为 JPEG

当 PDF 页面应导出为 JPEG 图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 遍历页面并调用 `device.process(...)` 将每个页面光栅化为 JPEG。
1. 将 JPEG 输出文件保存到编号路径。

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

## 将 PDF 转换为 PNG

当 PDF 页面需要转换为 PNG 图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 遍历页面并为每个 PDF 页面调用 `device.process(...)`。
1. 将 PNG 输出保存到编号的文件路径。

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

## 使用默认字体后备将 PDF 转换为 PNG

当渲染应该使用后备字体来弥补缺失的字形时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)，其 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 为 300 DPI。
1. 启用`document.setAbsentFontTryToSubstitute(true)`，以便在渲染期间丢失的字形可以回退到替换字体。
1. 渲染页面并保存 PNG 文件。

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

## 将 PDF 转换为 SVG

当 PDF 页面应导出为 SVG 图形时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 当需要原始 `.svg` 输出时，创建 [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) 并禁用 ZIP 压缩。
1. 启用`setTreatTargetFileNameAsDirectory(true)`，以便可以在目标路径下组织每页 SVG 输出。
1. 保存 SVG 输出。

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

## 将 PDF 转换为 TIFF

当应将一个或多个 PDF 页面导出为 TIFF 时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) 并配置压缩、颜色深度和空白页行为。
1. 使用 300 DPI 的 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 和准备好的 TIFF 设置创建 [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/)。
1. 渲染页面并保存 TIFF 输出。

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
