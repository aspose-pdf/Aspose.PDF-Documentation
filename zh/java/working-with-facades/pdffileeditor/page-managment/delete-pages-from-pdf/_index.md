---
title: 从 PDF 中删除页面
linktitle: 从 PDF 中删除页面
type: docs
weight: 20
url: /zh/java/delete-pages-from-pdf/
description: 在 Java 中使用 PdfFileEditor 门面从 PDF 删除选定页面。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文档中删除特定页面
Abstract: 了解如何使用 Aspose.PDF for Java 删除 PDF 页面。该 Java 示例使用 PdfFileEditor 删除指定的页面编号，并将剩余页面保存为新文档。
---
## 删除 PDF 页面

此 Java 示例从源文档中删除第 2 页和第 4 页。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 构建一个包含要删除的页码的数组。
3. 调用 `delete` 使用输入文件、页面数组和输出文件。
4. 保存生成的 PDF。

### Java 示例

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
