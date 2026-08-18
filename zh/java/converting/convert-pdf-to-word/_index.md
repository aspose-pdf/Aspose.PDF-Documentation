---
title: 在 Java 中将 PDF 转换为 Word
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 PDF 文件转换为 Java 中的 DOC 和 DOCX，以便更轻松地编辑和重复使用文档。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何用 Java 将 PDF 转换为 Word
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 PDF 文件转换为 Microsoft Word 格式。它涵盖 DOC 输出、DOCX 输出、增强流 DOCX 转换、保留换行符、项目符号识别以及通过`DocSaveOptions` 进行图像分辨率控制。
---
Aspose.PDF for Java 可以将 PDF 文档导出为具有不同识别和布局选项的 Microsoft Word 格式。使用 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) 控制 PDF 文本、列表和图像如何映射到 Word 输出。

## 将 PDF 转换为 DOC

当 PDF 文档应导出为旧版 DOC 格式时，请使用此示例。该代码创建`DocSaveOptions`，将格式设置为`Doc`，并将选项传递给共享保存方法。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)并将格式设置为`Doc`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 导出为 Microsoft Word 二进制文档格式。
1. 保存转换后的 DOC 文件。

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

当应将 PDF 文档导出为 DOCX 文件时，请使用此示例。 DOCX 是大多数新文字处理工作流程的首选格式，因为它受到广泛支持并且更易于编辑。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)并将格式设置为`DocX`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容导出为 Office Open XML Word 文档。
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

## 通过增强的流程识别将 PDF 转换为 DOCX

当 Word 导出应支持流动的可编辑内容而不是固定的视觉布局时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `DocX` 输出创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)。
1. 启用`setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)`，以便转换器在 DOCX 生成期间使用增强的流识别。
1. 调用`document.save(outputFile.toString(), saveOptions)`并保存转换后的DOCX输出。

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

## 将 PDF 转换为 DOCX 并保留换行符

当源 PDF 中的行结尾应保留在 Word 输出中时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `DocX` 导出创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)。
1. 启用`setAddReturnToLineEnd(true)`，以便在转换期间保留显式换行符。
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

## 使用项目符号识别将 PDF 转换为 DOCX

当源 PDF 中的列表项目符号应在 Word 中识别并保留为列表结构时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `DocX` 导出创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)。
1. 启用`setRecognizeBullets(true)`，以便列表式 PDF 内容在转换过程中被识别为项目符号列表。
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

## 使用自定义图像分辨率将 PDF 转换为 DOCX

当在转换过程中应控制生成的 DOCX 内的图像保真度时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `DocX` 导出创建 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/)。
1. 设置`setImageResolutionX(300)` 和`setImageResolutionY(300)`，以便以请求的分辨率生成光栅内容。
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
