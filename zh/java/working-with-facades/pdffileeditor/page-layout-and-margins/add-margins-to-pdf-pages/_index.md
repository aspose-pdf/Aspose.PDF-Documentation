---
title: 为 PDF 页面添加边距
linktitle: 为 PDF 页面添加边距
type: docs
weight: 10
url: /zh/java/add-margins-to-pdf-pages/
description: 使用 PdfFileEditor 类在 Java 中为选定的 PDF 页面添加边距。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 为 PDF 文档的特定页面添加边距
Abstract: 了解如何使用 Aspose.PDF for Java 为选定页面添加边距。该 Java 示例使用 PdfFileEditor 定位各个页面号，并应用相等的上、下、左、右边距值。
---
## 为 PDF 页面添加边距

该 Java 示例在源文档的第 1 页和第 3 页添加了 36 点的边距。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 选择应添加新页边距的页码。
3. 调用 `addMargins` 使用输入文件、输出文件、页列表和边距值。
4. 保存已更新的 PDF。

### Java 示例

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
