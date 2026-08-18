---
title: 使用 Java 将 PDF 转换为 EPUB、文本、XPS 等
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 PDF 文件转换为 Java 中的 EPUB、LaTeX、Markdown、文本、XPS 和 MobiXML。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在Java中将PDF转换为其他格式
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 PDF 文件转换为 EPUB、TeX、Markdown、文本、XPS 和 MobiXML 格式，并在需要时使用特定于格式的保存选项。
---
Aspose.PDF for Java 可以将 PDF 文档导出为文本、电子书、打印和面向标记的输出格式。

## 将 PDF 转换为 EPUB

当 PDF 文档应导出为 EPUB 电子书格式时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/)并将识别模式设置为`Flow`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容导出为可重排的 EPUB 标记。
1. 保存转换后的 EPUB 文件。

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 将 PDF 转换为 TeX

当 PDF 内容应导出为 TeX 标记时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) 用于 TeX 序列化。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容作为 TeX 标记发出。
1. 保存生成的 TeX 文件。

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为纯文本

当应将 PDF 文档导出为文本文件时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) 以从 PDF 页面中提取文本内容。
1. 调用 `device.process(document.getPages().get_Item(1), outputFile.toString())` 将第一页写入纯文本。
1. 保存文本输出文件。

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 XPS

当需要将 PDF 文档转换为 XPS 格式时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) 并启用嵌入的 TrueType 字体。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 序列化为带有嵌入字体资源的 XPS。
1. 保存转换后的 XPS 文件。

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 Markdown

当 PDF 内容应导出为 Markdown 时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) 并配置图像资源目录以及 HTML 图像标签输出。
1. 调用 `document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容以带有外部图像资源的 Markdown 形式发出。
1. 保存生成的 Markdown 文件。

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 Mobi XML

当 PDF 内容应导出为与 Mobi 兼容的 XML 时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 选择 [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` 作为目标序列化格式。
1. 调用`document.save(outputFile.toString(), SaveFormat.MobiXml)`，以便将 PDF 导出为与 Mobi 兼容的 XML。
1. 保存转换后的文件。

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
