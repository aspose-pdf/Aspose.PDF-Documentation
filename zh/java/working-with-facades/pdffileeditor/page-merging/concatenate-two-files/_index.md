---
title: 合并两个 PDF 文件
linktitle: 合并两个 PDF 文件
type: docs
weight: 60
url: /zh/java/concatenate-two-files/
description: 在 Java 中使用 PdfFileEditor 外观将两个 PDF 文件合并为一个文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将两个 PDF 文件合并为单个输出文档
Abstract: 了解如何使用 Aspose.PDF for Java 合并两个 PDF 文件。Java 示例使用 PdfFileEditor 和基于数组的 `concatenate` 重载，将两个源文档合并为一个输出 PDF。
---
## 合并两个 PDF 文件

本文直接映射到 `mergePdfDocuments` 示例在 `PdfFileEditorExamples.java`.

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 将两个输入文件路径作为字符串数组传递。
3. 呼叫 `concatenate` 使用数组和输出文件路径。
4. 保存合并后的 PDF。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
