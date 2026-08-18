---
title: 将 PDF 拆分为结尾
linktitle: 将 PDF 拆分为结尾
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: 使用 PdfFileEditor 外观在 Java 中将 PDF 从选定的页面拆分到末尾。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 的起始点到结尾提取页面
Abstract: 了解如何使用 Aspose.PDF for Java 将 PDF 拆分到最后。 Java 示例使用 PdfFileEditor 提取从第 2 页开始到源文档末尾的所有页面。
---
## 将 PDF 拆分为结尾

Java 示例提取从第 2 页开始的所有页面。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 使用源文件、起始页码和输出文件调用 `splitToEnd`。
3. 保存生成的 PDF 文档。

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
