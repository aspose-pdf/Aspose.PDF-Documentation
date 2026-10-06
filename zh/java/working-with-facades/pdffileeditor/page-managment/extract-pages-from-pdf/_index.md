---
title: 从 PDF 中提取页面
linktitle: 从 PDF 中提取页面
type: docs
weight: 30
url: /zh/java/extract-pages-from-pdf/
description: 在 Java 中使用 PdfFileEditor 类从 PDF 中提取所选页面。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将所选 PDF 页面提取到新文档中
Abstract: 了解如何使用 Aspose.PDF for Java 从 PDF 中提取页面。Java 示例使用 PdfFileEditor 收集特定页码并将其写入单独的输出 PDF。
---
## 从 PDF 中提取页面

该 Java 示例将第 1、4、3 页提取到新的 PDF 文档中。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 定义要提取的页码。
3. 调用 `extract` 使用源文件、页数组和输出文件。
4. 将提取的页面保存为新的 PDF。

### Java 示例

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
