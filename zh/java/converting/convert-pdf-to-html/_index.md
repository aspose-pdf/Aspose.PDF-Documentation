---
title: 在 Java 中将 PDF 转换为 HTML
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 转换为 HTML，包括多页输出、外部图像文件夹、SVG 处理和分层 HTML 渲染。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF 转换为 HTML
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 PDF 文件转换为 HTML。它涵盖基本的 HTML 导出以及图像文件夹、页面分割、SVG 输出、压缩 SVG 图形、PNG 页面背景、仅正文标记、透明文本渲染和文档层转换的选项。
---
Aspose.PDF for Java 支持 HTML 导出，并提供图像、SVG、页面分割、透明度和图层渲染选项。使用 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 控制如何将 PDF 页面、资源和标记写入 HTML 输出。

## 将 PDF 转换为 HTML

当应将 PDF 导出为标准 HTML 文档时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为标准 HTML 序列化创建默认的 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 页面内容导出为 HTML 标记。
1. 保存生成的 HTML 输出。

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 HTML 并单独存储图像

当在 HTML 导出期间提取的图像应写入单独的文件时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)并将`setSpecialFolderForAllImages(...)`设置为专用图像输出目录。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将光栅图像作为单独的资源文件发出，而不是仅内联输出。
1. 将 HTML 输出与生成的图像资源一起保存。

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

## 将 PDF 转换为多页 HTML

当每个 PDF 页面应在 HTML 输出中单独表示时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用 `setSplitIntoPages(true)`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将每个 PDF 页面写入单独的 HTML 输出。
1. 保存生成的 HTML 文件。

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

## 将 PDF 转换为 HTML 并单独存储 SVG

当矢量内容应作为单独的 SVG 资源发出时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并将 `setSpecialFolderForSvgImages(...)` 设置为外部 SVG 资源目录。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便矢量图形存储在主 HTML 文件之外。
1. 保存 HTML 输出和 SVG 资源。

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

## 使用压缩的 SVG 将 PDF 转换为 HTML

当应在 HTML 导出期间优化 SVG 输出时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并为 SVG 资源配置专用文件夹。
1. 启用`setCompressSvgGraphicsIfAny(true)`，以便在导出期间压缩 SVG 资源。
1. 调用`document.save(outputFile.toString(), saveOptions)`并保存转换后的HTML文件。

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

## 将 PDF 转换为带有 PNG 页面背景的 HTML

当页面背景应在 HTML 输出中呈现为 PNG 图像时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)并将光栅图像保存模式设置为PNG页面背景。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便页面背景内容作为 PNG 支持的 HTML 层发出。
1. 保存转换后的 HTML 输出。

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

## 仅将 PDF 转换为 HTML 正文内容

当仅需要正文标记而不是完整的 HTML 文档 shell 时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/)并将标记生成模式设置为`WriteOnlyBodyContent`。
1. 当仅正文输出仍应以页面分隔时，请保持 `setSplitIntoPages(true)` 启用。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存 HTML 输出。

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

## 通过透明文本渲染将 PDF 转换为 HTML

当应在 HTML 导出中保留透明文本时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用透明和阴影文本保留。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便在 HTML 结果中保留与透明度相关的文本外观。
1. 保存转换后的 HTML 输出。

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

## 通过文档层渲染将 PDF 转换为 HTML

当 PDF 图层可见性应反映在 HTML 结果中时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用 `setConvertMarkedContentToLayers(true)`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，将标记的PDF内容映射到HTML层。
1. 保存导出的 HTML 文件。

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
