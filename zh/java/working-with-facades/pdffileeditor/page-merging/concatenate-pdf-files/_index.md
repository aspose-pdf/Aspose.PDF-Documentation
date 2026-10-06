---
title: 合并多个 PDF 文件
linktitle: 合并多个 PDF 文件
type: docs
weight: 20
url: /zh/java/concatenate-pdf-files/
description: 在 Java 中使用基于数组的 PdfFileEditor concatenate 工作流合并 PDF 文件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将多个 PDF 文件合并为一个文档
Abstract: 了解如何使用 Aspose.PDF for Java 合并 PDF 文件。仓库示例使用基于数组的 `concatenate` 重载，传入两个输入；同一工作流可以扩展到更长的文件列表，因为该方法接受字符串数组形式的源路径。
---
## 合并 PDF 文件

Java 示例通过将两个文件传递给基于数组的方式来合并它们。 `concatenate` 过载。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 构建一个包含输入 PDF 路径的字符串数组。
3. 调用 `concatenate` 使用输入数组和输出文件路径。
4. 保存合并后的文档。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

要合并超过两个文件，请扩展传递给的字符串数组 `concatenate`.
