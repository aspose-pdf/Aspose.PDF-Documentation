---
title: 将页面追加到 PDF
linktitle: 将页面追加到 PDF
type: docs
weight: 10
url: /zh/java/append-pages-to-pdf/
description: 使用 PdfFileEditor 类在 Java 中将一个 PDF 的页面追加到另一个 PDF。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将一个 PDF 文档的页面范围追加到另一个文档。
Abstract: 了解如何使用 Aspose.PDF for Java 将页面追加到 PDF。此 Java 示例使用 PdfFileEditor 将另一个文档中选定的页面范围追加到当前 PDF 的末尾。
---
## 将页面追加到 PDF

该 Java 示例将第二个 PDF 的第 1 页追加到第一个文档的末尾。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 通过将其路径传递给来绑定主输入 PDF `append`。
3. 提供次要源文件列表和要追加的页码范围。
4. 将合并结果保存到输出文件。

### Java 示例

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
