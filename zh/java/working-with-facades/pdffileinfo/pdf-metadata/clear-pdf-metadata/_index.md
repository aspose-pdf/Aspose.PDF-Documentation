---
title: 清除 PDF 元数据
linktitle: 清除 PDF 元数据
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: 了解如何使用 PdfFileInfo 外观在 Java 中清除 PDF 元数据。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 清除 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 清除 PDF 元数据。 Java 示例使用 PdfFileInfo 通过 `clearInfo()` 删除存储的文档信息，然后将清理后的 PDF 保存到新文件中。
---
## 清除 PDF 元数据

当您需要在共享或存档 PDF 之前删除存储的文档信息时，请使用此工作流程。

### 步骤

1. 为输入 PDF 创建一个 `PdfFileInfo` 对象。
2. 调用 `clearInfo()` 以删除文档元数据。
3. 使用`save()` 将结果保存到新文件。
4. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
