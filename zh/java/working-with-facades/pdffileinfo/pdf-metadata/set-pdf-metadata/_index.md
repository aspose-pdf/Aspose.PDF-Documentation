---
title: 设置 PDF 元数据
linktitle: 设置 PDF 元数据
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: 了解如何使用 PdfFileInfo 外观更新 Java 中的 PDF 元数据。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 更新 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 更新 PDF 元数据。 Java 示例使用 PdfFileInfo 设置标准元数据字段（例如主题、标题、关键字和创建者），添加自定义元数据条目，并将结果保存到新的 PDF。
---
## 设置 PDF 元数据

当您需要在保存 PDF 之前规范或丰富文档信息时，请使用此工作流程。

### 步骤

1. 为源 PDF 创建一个 `PdfFileInfo` 对象。
2. 设置要更新的标准元数据字段。
3. 使用`setMetaInfo` 添加任何自定义元数据。
4. 使用`save()` 保存更新的文档。
5. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
