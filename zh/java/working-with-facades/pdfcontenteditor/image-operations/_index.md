---
title: 图像操作
linktitle: 图像操作
type: docs
weight: 50
url: /zh/java/pdfcontenteditor-image-operations/
description: 了解在 Aspose.PDF 中 PdfContentEditor 类提供的当前 Java 图像操作覆盖范围。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 的 Java 图像编辑工作流
Abstract: 本节介绍 Java PdfContentEditor 示例集当前支持的与图像相关的工作流。代码库包含一个直接的替换图像示例，而不支持的图像删除主题则以明确的范围说明保留。
---
当前的 Java `PdfContentEditorExamples` 类直接支持 `replaceImage(...)`。

## 替换图像

1. 将源 PDF 绑定到 `PdfContentEditor` 立面。
2. 调用 `replaceImage(...)` 带有页码、图像索引和替换图像路径。
3. 保存更新后的 PDF 文档。

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
