---
title: 向 PDF 插入页面
linktitle: 向 PDF 插入页面
type: docs
weight: 40
url: /zh/java/insert-pages-into-pdf/
description: 使用 PdfFileEditor 类在 Java 中将一个 PDF 中选定的页面插入到另一个 PDF 中。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在选定位置插入另一个 PDF 的页面
Abstract: 了解如何使用 Aspose.PDF for Java 向 PDF 插入页面。Java 示例使用 PdfFileEditor 将第二个文档中选定的页面插入目标 PDF 中指定页码之后。
---
## 向 PDF 插入页面

该 Java 示例将在次要文档中的第 1 页和第 2 页插入到目标 PDF 的第 2 页之后。

### 步骤

1. 创建 `PdfFileEditor` 实例。
2. 在目标文档中选择插入位置。
3. 选择要从源文档复制的页码。
4. 调用 `insert` 使用目标文件、插入点、源文件、页面数组以及输出文件。
5. 保存更新后的 PDF。

### Java 示例

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
