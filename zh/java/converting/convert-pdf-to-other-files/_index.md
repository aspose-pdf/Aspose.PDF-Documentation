---
title: 在 Java 中将 PDF 转换为 EPUB、文本、XPS 等格式
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/java/convert-pdf-to-other-files/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 PDF 文件转换为 EPUB、LaTeX、Markdown、文本、XPS 和 MobiXML。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF 转换为其他格式
Abstract: 本文解释了如何使用 Aspose.PDF for Java 将 PDF 文件转换为 EPUB、TeX、Markdown、文本、XPS 和 MobiXML 格式，并在需要时使用特定于格式的保存选项。
---
Aspose.PDF for Java 可以将 PDF 文档导出为文本、电子书、打印和标记导向的输出格式。

## 将 PDF 转换为 EPUB

当需要将 PDF 文档导出为 EPUB 电子书格式时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) 并将识别模式设置为 `Flow`.
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容被导出为可重新流式的 EPUB 标记。
1. 保存已转换的 EPUB 文件。

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

当需要将 PDF 内容导出为 TeX 标记时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) 用于 TeX 序列化。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容被输出为 TeX 标记。
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

当需要将 PDF 文档导出为文本文件时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) 从 PDF 页面提取文本内容。
1. 调用 `device.process(document.getPages().get_Item(1), outputFile.toString())` 将第一页写成纯文本。
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

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) 并启用嵌入的 TrueType 字体。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 被序列化为 XPS，并嵌入了字体资源。
1. 保存已转换的 XPS 文件。

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

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) 并配置图像资源目录以及 HTML 图像标签输出。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容以 Markdown 形式输出，并使用外部图像资源。
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

当需要将 PDF 内容导出为兼容 Mobi 的 XML 时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 选择 [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` 作为目标序列化格式。
1. 调用 `document.save(outputFile.toString(), SaveFormat.MobiXml)` 因此，PDF 导出为兼容 Mobi 的 XML。
1. 保存已转换的文件。

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
