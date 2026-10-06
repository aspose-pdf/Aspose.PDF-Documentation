---
title: PdfViewer 类
linktitle: PdfViewer 类
type: docs
weight: 135
url: /zh/java/pdfviewer-class/
description: 了解如何在 Java 中使用 PdfViewer 外观来解码 PDF 页面并检查与查看器相关的设置。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfViewer 在 Java 中解码 PDF 页面并检查查看器数据
Abstract: 本节阐述了如何在 Aspose.PDF for Java 中使用 PdfViewer 外观进行页面解码和查看器相关的检查任务。当前的 Java 示例包括将所有页面渲染为图像、解码特定页面，以及检查页面计数、坐标类型、分辨率和绑定的查看器设置。
---
Java `PdfViewerExamples` 类演示了通过 Facades API 可用的主要查看器工作流。

## 解码所有 PDF 页面

当源 PDF 的每一页都应渲染为图像时，请使用此工作流。

### 步骤

1. 创建并配置一个 `PdfViewer` 实例。
2. 将源 PDF 与 `bindPdf`.
3. 调用 `decodeAllPages()` 将文档渲染为 `BufferedImage` 数组。
4. 将每个解码后的页面保存为输出图像文件。
5. 关闭已绑定的 PDF 文件。

### Java 示例

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## 解码特定的 PDF 页面

当仅需要将单页渲染为图像时，请使用此工作流。

### 步骤

1. 创建并配置一个 `PdfViewer` 实例。
2. 绑定源 PDF。
3. 调用 `decodePage()` 对于您想要渲染的页面。
4. 将解码后的页面保存为输出图像文件。
5. 关闭查看器。

### Java 示例

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## 检查 PDF 元数据

在渲染或打印之前需要获取与查看器相关的文档信息时，请使用此工作流。

### 步骤

1. 创建并配置一个 `PdfViewer` 实例。
2. 绑定源 PDF。
3. 读取页数、坐标类型和渲染分辨率。
4. 使用或打印检索到的值。
5. 关闭已绑定的 PDF 文件。

### Java 示例

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## 检查已绑定的查看器设置

在绑定 PDF 后需要确认或调整查看器行为时，请使用此工作流。

### 步骤

1. 创建并配置一个 `PdfViewer` 实例。
2. 绑定源 PDF。
3. 设置查看器选项，例如自动调整大小、自动旋转和打印对话框可见性。
4. 读取活动查看器设置和页数。
5. 关闭查看器。

### Java 示例

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
