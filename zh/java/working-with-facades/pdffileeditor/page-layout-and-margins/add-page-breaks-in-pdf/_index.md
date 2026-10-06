---
title: 在 PDF 中添加分页符
linktitle: 在 PDF 中添加分页符
type: docs
weight: 20
url: /zh/java/add-page-breaks-in-pdf/
description: 使用 PdfFileEditor 外观在 Java 中向 PDF 插入分页符。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文档的固定位置插入分页符
Abstract: 了解如何使用 Aspose.PDF for Java 添加分页符。Java 示例使用 PdfFileEditor.PageBreak 在特定垂直位置拆分页面，并将结果保存为新 PDF。
---
## 在 PDF 中添加分页符

当需要在已知的 Y 位置将页面拆分为多个页面时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 构建一个或多个 `PdfFileEditor.PageBreak` 带有页码和断点位置的条目。
3. 将分页符数组传递给 `addPageBreak`.
4. 保存已更新的 PDF 文档。

### Java 示例

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
