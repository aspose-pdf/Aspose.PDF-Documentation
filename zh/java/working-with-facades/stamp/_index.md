---
title: 邮票类别
linktitle: 邮票类别
type: docs
weight: 150
url: /java/stamp-class/
description: 了解如何使用 Java 中的 Stamp 类向 PDF 文档添加图像、PDF 和基于文本的图章。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将图像、PDF 和文本标记添加到 PDF 文档
Abstract: 本节介绍如何在 Aspose.PDF for Java 中使用 Stamp 类和 PdfFileStamp 来将可重用的图章内容添加到 PDF 文档中。当前的 Java 示例涵盖图像图章、PDF 页面图章、具有自定义 TextState 的文本图章、特定于页面的图章以及具有不透明度、大小和旋转设置的背景图像图章。
---
Java `StampExamples` 类演示了通过 Facades API 可用的主要图章构建工作流程。

## 添加图像印记

当应将图像文件作为图章放置在 PDF 上时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 设置图章标识符和放置原点。
4. 将图章添加到文档中。
5. 保存结果并关闭外观对象。

### Java示例

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

## 添加 PDF 页面作为图章

当其他 PDF 页面的内容应重新用作图章内容时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定目标PDF。
2. 创建一个 `Stamp` 对象。
3. 将图章绑定到另一个 PDF 文件的特定页面。
4. 设置放置的目标页码和原点。
5. 添加图章，保存输出，然后关闭外观对象。

### Java示例

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

## 使用 TextState 添加文本标记

当图章应包含样式文本而不是图像时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 创建一个 `Stamp` 对象。
3. 将`FormattedText` 徽标和自定义`TextState` 绑定到图章。
4. 设置图章原点和旋转。
5. 添加图章，保存输出，然后关闭外观对象。

### Java示例

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

## 为特定页面添加图章

当图章应仅出现在选定页面而不是整个文档上时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 设置目标页面列表、原点和图像尺寸。
4. 将图章添加到文档中。
5. 保存结果并关闭外观对象。

### Java示例

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

## 添加背景图像印记

当图章应以受控的不透明度和旋转显示在页面内容后面时，请使用此工作流程。

### 步骤

1. 创建`PdfFileStamp`实例并绑定源PDF。
2. 创建一个 `Stamp` 对象并将其绑定到图像文件。
3. 将图章标记为背景内容。
4. 配置不透明度、质量、旋转、大小和原点。
5. 添加图章，保存输出，然后关闭外观对象。

### Java示例

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
