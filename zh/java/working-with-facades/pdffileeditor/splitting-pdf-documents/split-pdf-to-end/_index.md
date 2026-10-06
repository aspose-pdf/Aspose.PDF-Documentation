---
title: 将 PDF 拆分至末尾
linktitle: 将 PDF 拆分至末尾
type: docs
weight: 40
url: /zh/java/split-pdf-to-end/
description: 在 Java 中使用 PdfFileEditor 类将 PDF 从选定页面拆分至结束。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 提取 PDF 从起始页至结束的页面。
Abstract: 了解如何使用 Aspose.PDF for Java 将 PDF 拆分至结束。此 Java 示例使用 PdfFileEditor 提取从第 2 页开始直至源文档结束的所有页面。
---
## 将 PDF 拆分至末尾

此 Java 示例提取从第 2 页开始的所有页面。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 调用 `splitToEnd` 使用源文件、起始页码和输出文件。
3. 保存生成的 PDF 文档。

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
