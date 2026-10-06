---
title: 调整 PDF 页面内容
linktitle: 调整 PDF 页面内容
type: docs
weight: 30
url: /zh/java/resize-pdf-page-contents/
description: 使用 PdfFileEditor 门面在 Java 中调整所选 PDF 页面上的内容大小。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 调整 PDF 文档中已有页面内容的大小
Abstract: 了解如何使用 Aspose.PDF for Java 调整页面内容。此 Java 示例使用 PdfFileEditor 定位特定页面，应用新的内容宽度和高度，并在调整操作失败时终止工作流。
---
## 调整 PDF 页面内容

Java 示例调整第 1 页和第 3 页的内容区域，并检查布尔返回值。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 选择要调整其内容大小的页面。
3. 调用 `resizeContents` 使用目标宽度和高度。
4. 检查返回值，并在继续之前处理失败情况。
5. 保存已更新的文档。

### Java 示例

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
