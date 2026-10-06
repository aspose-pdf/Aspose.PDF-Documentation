---
title: 在 Java 中将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /zh/java/convert-pdf-to-images-format/
lastmod: "2026-10-06"
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 页面渲染为 TIFF、BMP、EMF、JPEG、PNG、GIF 和 SVG 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 在 Java 中将 PDF 页面转换为 TIFF、PNG、JPEG、GIF、BMP、EMF 和 SVG。
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 将 PDF 文件转换为常见图像格式。它涵盖了全局的 TIFF 导出、使用图像设备的逐页光栅生成、PNG 导出时的可选字体替换，以及使用 `SvgSaveOptions` 的 SVG 输出。
---
Aspose.PDF for Java 可以将 PDF 页面渲染为栅格和矢量图像格式，并提供特定格式的设备选项。

## 将 PDF 转换为 BMP

当需要将 PDF 页面渲染为 BMP 图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 遍历 `document.getPages()` 并调用 `device.process(...)` 对于每页。
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

当需要将 PDF 页面导出为 EMF 矢量图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 遍历页面并调用 `device.process(...)` 对于每页。
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

当需要将 PDF 页面转换为 GIF 图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 遍历页面并调用 `device.process(...)` 渲染每页。
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

当需要将 PDF 页面导出为 JPEG 图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 遍历页面并调用 `device.process(...)` 将每页栅格化为 JPEG。
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

当需要将 PDF 页面转换为 PNG 图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 遍历页面并调用 `device.process(...)` 对于每个 PDF 页面。
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

## 将 PDF 转换为 PNG，使用默认字体回退

在渲染时，如果缺少字形需要使用回退字体，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI 的。
1. 启用 `document.setAbsentFontTryToSubstitute(true)` 因此，在渲染时缺失的字形可以回退到替代字体。
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

当需要将 PDF 页面导出为 SVG 图形时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) 并在 raw 时禁用 ZIP 压缩 `.svg` 需要输出。
1. 启用 `setTreatTargetFileNameAsDirectory(true)` 所以，每页的 SVG 输出可以组织在目标路径下。
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

当需要将一个或多个 PDF 页面导出为 TIFF 时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) 并配置压缩、颜色深度和空白页行为。
1. 创建一个 [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) 带有一个 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 分辨率为 300 DPI，且已准备好的 TIFF 设置。
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
