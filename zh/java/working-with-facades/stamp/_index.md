---
title: Stamp 类
linktitle: Stamp 类
type: docs
weight: 150
url: /zh/java/stamp-class/
description: 了解如何在 Java 中使用 Stamp 类向 PDF 文档添加图像、PDF 和基于文本的印章。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 文档添加图像、PDF 和文本印章
Abstract: 本节解释了如何在 Aspose.PDF for Java 中将 Stamp 类与 PdfFileStamp 结合使用，以向 PDF 文档添加可重用的印章内容。目前的 Java 示例涵盖了图像印章、PDF 页面印章、带自定义 TextState 的文本印章、特定页面印章以及具有不透明度、尺寸和旋转设置的背景图像印章。
---
Java `StampExamples` 类演示了通过 Facades API 可用的主要印章构建工作流。

## 添加图像印章

当需要将图像文件作为印章放置在 PDF 上时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 设置印章标识符和放置原点。
4. 将印章添加到文档中。
5. 保存结果并关闭外观对象。

### Java 示例

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 将 PDF 页面添加为印章

当需要将另一个 PDF 页面中的内容重新用作印章内容时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定目标 PDF。
2. 创建一个 `Stamp` 对象。
3. 将印章绑定到另一个 PDF 文件的特定页面。
4. 设置目标页码和放置原点。
5. 添加标签，保存输出，并关闭 facade 对象。

### Java 示例

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 添加带有 TextState 的文本印章

当印章应包含样式化文本而不是图像时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 创建一个 `Stamp` 对象。
3. 绑定一个 `FormattedText` 徽标和自定义 `TextState` 到印章。
4. 设置印章的原点和旋转角度。
5. 添加标签，保存输出，并关闭 facade 对象。

### Java 示例

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 在特定页面添加印章

当需要印章仅出现在选定页面而不是整个文档时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 设置目标页面列表、原点和图像大小。
4. 将印章添加到文档中。
5. 保存结果并关闭外观对象。

### Java 示例

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 添加背景图像印章

当需要将印章显示在页面内容之后，并且需要控制不透明度和旋转时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileStamp` 实例并绑定源 PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 将印章标记为背景内容。
4. 配置不透明度、质量、旋转、大小和原点。
5. 添加标签，保存输出，并关闭 facade 对象。

### Java 示例

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
