---
title: 在 Java 中将图像格式转换为 PDF
linktitle: 将图像转换为 PDF
type: docs
weight: 60
url: /zh/java/convert-images-format-to-pdf/
lastmod: "2026-10-06"
description: 了解如何使用 Aspose.PDF 在 Java 中将 BMP、CGM、DICOM、PNG、TIFF、EMF、SVG、CDR 等图像格式转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在 Java 中将图像转换为 PDF
Abstract: 本文说明如何使用 Aspose.PDF for Java 将多种图像格式转换为 PDF。它涵盖了将图像直接放置到新 PDF 页面以及针对 CGM、SVG 和 CDR 输入的特定文件类型加载选项。
---
Aspose.PDF for Java 可以将多种光栅和矢量图像格式转换为 PDF 文档。

## 将 BMP 转换为 PDF

当需要将 BMP 图像放入 PDF 文档时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于保存输出 PDF。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 BMP 放置在 `page.addImage(...)`。
1. 使用以下方式定义目标图像矩形 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 因此光栅内容填满 PDF 页面区域。
1. 保存输出 PDF 文件。

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 将 CGM 转换为 PDF

当需要将 CGM 图形文件转换为 PDF 时，请使用此示例。

1. 通过传递文件路径打开 CGM 源并 [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 在文档加载期间解释 CGM 图形流。
1. 将转换后的 PDF 保存到目标输出路径。

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 DICOM 转换为 PDF

当需要将医学 DICOM 图像包装成 PDF 文档时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于 PDF 输出。
1. 创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 对象，设置它的 [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) 到 `Dicom`，并指定源文件路径。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 DICOM 图像追加到页面段落集合中。
1. 将结果保存为 PDF。

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 EMF 转换为 PDF，直接加载文档

当需要通过主要的 EMF 加载路径将 EMF 文件转换为 PDF 时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并将 EMF 源以二进制流打开。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并清除其边距，使 EMF 艺术作品能够占据整个页面区域。
1. 创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), 将 EMF 流绑定到它，并将其添加到页面段落集合中。
1. 保存输出 PDF 文件。

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用替代工作流将 EMF 转换为 PDF

当需要使用替代设置或页面组合流程转换 EMF 内容时，请使用此示例。

1. 使用 Aspose.Imaging 加载 EMF 源文件，并在 PDF 放置之前将其渲染为内存中的 PNG 流。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 从中间字节流中提取并将其添加到页面。
1. 保存已转换的 PDF。

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 GIF 转换为 PDF

在需要将 GIF 图像添加到 PDF 页面时使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于 PDF 输出。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 GIF 放置在 `page.addImage(...)`。
1. 使用以下方式定义放置边界 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 所以图像填满页面区域。
1. 保存输出的 PDF。

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 JPEG 转换为 PDF

当需要将 JPEG 图像转换为单页 PDF 时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于输出 PDF。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并插入 JPEG 图像 `page.addImage(...)`。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 控制光栅图像如何映射到页面坐标。
1. 保存生成的 PDF 文件。

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PNG 转换为 PDF

使用此示例将 PNG 图像包装成 PDF 文档。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于转换输出。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 PNG 图像放置在其上 `page.addImage(...)`。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 根据页面画布对图像进行尺寸调整。
1. 保存输出文件。

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 SVG 转换为 PDF

当需要在 PDF 文档中渲染 SVG 艺术作品时，请使用此示例。

1. 通过传递文件路径打开 SVG 源并 [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 在加载时解析 SVG 标记并创建相应的 PDF 图形模型。
1. 将 PDF 输出保存到目标文件路径。

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 TIFF 转换为 PDF

当需要将 TIFF 图像转换为 PDF 时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 用于 PDF 输出。
1. 添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 TIFF 图像放置在 `page.addImage(...)`。
1. 定义放置区域的方式 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 因此，TIFF 内容映射到页面坐标。
1. 将结果保存为 PDF。

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 CDR 转换为 PDF

当需要将 CorelDRAW CDR 文件转换为 PDF 时，请使用此示例。

1. 通过传递文件路径打开 CDR 源并 [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 将 CorelDRAW 内容加载到 PDF 文档模型中。
1. 将已转换的 PDF 文件保存到请求的输出路径。

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
