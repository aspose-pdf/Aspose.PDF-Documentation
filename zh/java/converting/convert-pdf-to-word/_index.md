---
title: 在 Java 中将 PDF 转换为 Word
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/java/convert-pdf-to-word/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 PDF 文件转换为 DOC 和 DOCX，以便更轻松地编辑和重复使用文档。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF 转换为 Word
Abstract: 本文说明了如何使用 Aspose.PDF for Java 将 PDF 文件转换为 Microsoft Word 格式。它涵盖了 DOC 输出、DOCX 输出、增强流式 DOCX 转换、保留换行符、项目符号识别以及通过 `DocSaveOptions` 对图像分辨率的控制。
---
Aspose.PDF for Java 可以将 PDF 文档导出为 Microsoft Word 格式，并提供不同的识别和布局选项。使用 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 用于控制 PDF 文本、列表和图像如何映射到 Word 输出中。

## 将 PDF 转换为 DOC

当需要将 PDF 文档导出为传统 DOC 格式时使用此示例。代码创建 `DocSaveOptions`，设置格式为 `Doc`，并将选项传递给共享的保存方法。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 并将格式设置为 `Doc`.
1. 调用 `document.save(outputFile.toString(), saveOptions)` 所以 PDF 被导出为 Microsoft Word 的二进制文档格式。
1. 保存已转换的 DOC 文件。

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 DOCX

当需要将 PDF 文档导出为 DOCX 文件时，请使用此示例。DOCX 是大多数新文字处理工作流的首选格式，因为它被广泛支持且更易于编辑。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 并将格式设置为 `DocX`.
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容被导出为 Office Open XML Word 文档。
1. 保存生成的 DOCX 文件。

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 DOCX，并增强流式识别

当 Word 导出应更倾向于流式可编辑内容而非固定视觉布局时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 对于 `DocX` 输出。
1. 启用 `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` 因此，转换器在生成 DOCX 时使用增强的流识别。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存转换后的 DOCX 输出。

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 DOCX 并保留换行

当需要在 Word 输出中保留源 PDF 的换行符时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 对于 `DocX` 导出.
1. 启用 `setAddReturnToLineEnd(true)` 因此在转换过程中会保留显式换行。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存 DOCX 文件。

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 DOCX，识别项目符号

当需要识别并保留来源 PDF 的列表项目符号为 Word 中的列表结构时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 对于 `DocX` 导出.
1. 启用 `setRecognizeBullets(true)` 因此，类似列表的 PDF 内容在转换过程中被识别为项目符号列表。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存 DOCX 文件。

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 DOCX 并自定义图像分辨率

在转换过程中需要控制生成的 DOCX 中图像保真度时，请使用此示例。

1. 在 a 中打开源 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 对于 `DocX` 导出.
1. 设置 `setImageResolutionX(300)` 和 `setImageResolutionY(300)` 因此，光栅内容会在请求的分辨率下生成。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存 DOCX 输出。

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
