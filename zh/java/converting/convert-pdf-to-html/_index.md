---
title: 在 Java 中将 PDF 转换为 HTML
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: /zh/java/convert-pdf-to-html/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 PDF 转换为 HTML，包括多页输出、外部图像文件夹、SVG 处理以及分层 HTML 渲染。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF 转换为 HTML
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 将 PDF 文件转换为 HTML。它涵盖了基本的 HTML 导出以及图像文件夹、页面拆分、SVG 输出、压缩的 SVG 图形、PNG 页面背景、仅正文标记、透明文本渲染和文档层转换等选项。
---
Aspose.PDF for Java 支持 HTML 导出，具有图像、SVG、页面拆分、透明度和图层渲染的选项。使用 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 控制 PDF 页面、资源和标记写入 HTML 输出的方式。

## 将 PDF 转换为 HTML

当需要将 PDF 导出为标准 HTML 文档时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建默认 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 用于标准 HTML 序列化。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 页面内容被导出为 HTML 标记。
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

在 HTML 导出期间，如果提取的图像应写入为单独的文件，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并设置 `setSpecialFolderForAllImages(...)` 到专用的图像输出目录。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，栅格图像会作为单独的资源文件输出，而不是仅内联输出。
1. 将 HTML 输出连同生成的图像资源一起保存。

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

当每个 PDF 页面应在 HTML 输出中单独呈现时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用 `setSplitIntoPages(true)`.
1. 调用 `document.save(outputFile.toString(), saveOptions)` 所以每个 PDF 页面都会被写成单独的 HTML 输出。
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

## 将 PDF 转换为 HTML 并将 SVG 单独存储

当向量内容应作为单独的 SVG 资源输出时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并设置 `setSpecialFolderForSvgImages(...)` 到外部 SVG 资源目录。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，矢量图形存储在主 HTML 文件之外。
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

## 将 PDF 转换为带有压缩 SVG 的 HTML

在 HTML 导出时应优化 SVG 输出，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并为 SVG 资源配置专用文件夹。
1. 启用 `setCompressSvgGraphicsIfAny(true)` 因此，在导出过程中 SVG 资产会被压缩。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存转换后的 HTML 文件。

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

## 将 PDF 转换为带 PNG 页面背景的 HTML

当页面背景应在 HTML 输出中渲染为 PNG 图像时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并将光栅图像保存模式设置为 PNG 页面背景。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，页面背景内容会以 PNG 支持的 HTML 层形式输出。
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

当只需要正文标记而不是完整的 HTML 文档外壳时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并将标记生成模式设置为 `WriteOnlyBodyContent`.
1. 保持 `setSplitIntoPages(true)` 启用时，即使仅输出正文也应保持分页。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存HTML输出。

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

## 将 PDF 转换为 HTML，使用透明文本渲染

在需要在 HTML 导出中保留透明文本时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用透明和带阴影文本的保留。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，透明度相关的文本外观在HTML结果中得以保留。
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

## 将 PDF 转换为带有文档层渲染的 HTML

当 PDF 图层可见性应在 HTML 结果中反映时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 并启用 `setConvertMarkedContentToLayers(true)`.
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此标记的 PDF 内容被映射到 HTML 层。
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
