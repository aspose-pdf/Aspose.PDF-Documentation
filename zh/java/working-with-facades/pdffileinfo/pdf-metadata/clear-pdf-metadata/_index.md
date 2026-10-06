---
title: 清除 PDF 元数据
linktitle: 清除 PDF 元数据
type: docs
weight: 10
url: /zh/java/clear-pdf-metadata/
description: 了解如何使用 PdfFileInfo 外观在 Java 中清除 PDF 元数据。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 清除 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 清除 PDF 元数据。该 Java 示例使用 PdfFileInfo 通过 `clearInfo()` 删除已存储的文档信息，然后将清理后的 PDF 保存为新文件。
---
## 清除 PDF 元数据

当您需要在共享或存档 PDF 之前移除已存储的文档信息时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileInfo` 用于输入 PDF 的对象。
2. 调用 `clearInfo()` 删除文档元数据。
3. 将结果保存到一个新文件中，使用 `save()`.
4. 关闭 `PdfFileInfo` 实例。

### Java 示例

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
