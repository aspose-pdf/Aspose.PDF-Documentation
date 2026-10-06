---
title: 将 PDF 拆分为单页
linktitle: 将 PDF 拆分为单页
type: docs
weight: 30
url: /zh/java/split-pdf-into-single-pages/
description: 使用 PdfFileEditor 类在 Java 中将 PDF 拆分为单页输出文件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将 PDF 的每页导出为自己的文件
Abstract: 了解如何使用 Aspose.PDF for Java 将 PDF 拆分为单页文件。Java 示例使用 PdfFileEditor 根据文件名模式将每页写入单独的输出 PDF。
---
## 将 PDF 拆分为单页

当每个源页面必须成为单独的 PDF 文件时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 准备一个包含页面占位符的输出文件模式，例如 `%NUM%`。
3. 调用 `splitToPages` 使用源文件和输出模式。
4. 保存生成的单页文件。

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
