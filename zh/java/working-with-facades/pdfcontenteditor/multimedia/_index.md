---
title: 多媒体
linktitle: 多媒体
type: docs
weight: 70
url: /zh/java/pdfcontenteditor-multimedia/
description: 了解 Aspose.PDF 中 Java PdfContentEditor 外观当前提供的多媒体支持。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Java 中的多媒体注释工作流
Abstract: 本节介绍 Java PdfContentEditor 示例集当前支持的多媒体相关工作流。代码库包含直接的电影注释示例，未支持的音频主题则保留为明确的范围说明。
---
当前的 Java `PdfContentEditorExamples` 类直接支持 `addMovieAnnotation(...)`.

## 添加电影注释

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. 调用 `createMovie(...)` 带有注释矩形、电影文件路径和页码。
3. 保存已更新的 PDF 文档。

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
