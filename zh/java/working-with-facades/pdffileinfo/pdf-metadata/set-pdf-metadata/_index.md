---
title: 设置 PDF 元数据
linktitle: 设置 PDF 元数据
type: docs
weight: 50
url: /zh/java/set-pdf-metadata/
description: 了解如何使用 PdfFileInfo 外观在 Java 中更新 PDF 元数据。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 更新 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 更新 PDF 元数据。Java 示例使用 PdfFileInfo 设置标准元数据字段，如 subject、title、keywords、creator，添加自定义元数据条目，并将结果保存为新的 PDF。
---
## 设置 PDF 元数据

当需要在保存 PDF 前对文档信息进行标准化或丰富时，请使用此 Workflow。

### 步骤

1. 创建一个 `PdfFileInfo` 源 PDF 的对象。
2. 设置您想要更新的标准元数据字段。
3. 使用以下方式添加任何自定义元数据 `setMetaInfo`.
4. 使用以下方式保存已更新的文档 `save()`.
5. 关闭 `PdfFileInfo` 实例。

### Java 示例

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
