---
title: 在 Java 中将图像格式转换为 PDF
linktitle: 将图像转换为 PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 BMP、CGM、DICOM、PNG、TIFF、EMF、SVG、CDR 和其他图像格式转换为 Java 中的 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何用 Java 将图像转换为 PDF
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将多种图像格式转换为 PDF。它涵盖了将图像直接放置到新 PDF 页面中以及用于 CGM、SVG 和 CDR 输入的特定于文件类型的加载选项。
---
Aspose.PDF for Java 可以将许多光栅和矢量图像格式转换为 PDF 文档。

## 将 BMP 转换为 PDF

当应将 BMP 图像放入 PDF 文档中时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 来保存输出 PDF。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 BMP 与`page.addImage(...)` 一起放置。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 定义目标图像矩形，以便光栅内容填充 PDF 页面区域。
1. 保存输出的 PDF 文件。

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

当应将 CGM 图形文件转换为 PDF 时，请使用此示例。

1. 通过将文件路径和 [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 CGM 源。
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

当应将医学 DICOM 图像包装到 PDF 文档中时，请使用此示例。

1. 为 PDF 输出创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 对象，将其 [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) 设置为`Dicom`，并指定源文件路径。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 DICOM 图像附加到页面段落集合中。
1. 将结果另存为 PDF。

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

## 通过直接加载文档将 EMF 转换为 PDF

当应通过主 EMF 加载路径将 EMF 文件转换为 PDF 时，请使用此示例。

1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并以二进制流形式打开 EMF 源。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并清除其边距，以便 EMF 图稿可以占据整个页面区域。
1. 创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)，将 EMF 流绑定到它，并将其添加到页面段落集合中。
1. 保存输出的 PDF 文件。

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

## 使用替代工作流程将 EMF 转换为 PDF

当应使用替代设置或页面合成流程转换 EMF 内容时，请使用此示例。

1. 使用 Aspose.Imaging 加载 EMF 源，并在 PDF 放置之前将其渲染为内存中的 PNG 流。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 从中间字节流创建一个 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 并将其添加到页面中。
1. 保存转换后的 PDF。

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

当应将 GIF 图像添加到 PDF 页面时，请使用此示例。

1. 为 PDF 输出创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 GIF 与 `page.addImage(...)` 放在一起。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 定义放置边界，以便图像填充页面区域。
1. 保存输出 PDF。

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

当需要将 JPEG 图像转换为一页 PDF 时，请使用此示例。

1. 为输出 PDF 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并使用 `page.addImage(...)` 插入 JPEG 图像。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 控制光栅图像映射到页面坐标的方式。
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

当应将 PNG 图像封装到 PDF 文档中时，请使用此示例。

1. 为转换输出创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并使用 `page.addImage(...)` 将 PNG 图像放在其上。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 根据页面画布调整图像大小。
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

当应在 PDF 文档内渲染 SVG 图稿时，请使用此示例。

1. 通过将文件路径和 [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 SVG 源。
1. 让 Aspose.PDF 解析 SVG 标记并在加载期间创建相应的 PDF 图形模型。
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

当 TIFF 图像应转换为 PDF 时，请使用此示例。

1. 为 PDF 输出创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并将 TIFF 图像与`page.addImage(...)` 一起放置。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 定义放置区域，以便 TIFF 内容映射到页面坐标。
1. 将结果另存为 PDF。

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

1. 通过将文件路径和 [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 CDR 源。
1. 让 Aspose.PDF 将 CorelDRAW 内容加载到 PDF 文档模型中。
1. 将转换后的 PDF 文件保存到请求的输出路径。

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
