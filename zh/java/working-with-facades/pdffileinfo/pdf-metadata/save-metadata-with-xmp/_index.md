---
title: 使用 XMP 保存元数据
linktitle: 使用 XMP 保存元数据
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: 了解如何通过 PdfFileInfo 外观在 Java 中使用 XMP 保存 PDF 元数据。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 通过 XMP 保存 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 通过 XMP 保存 PDF 元数据。 Java 示例使用 PdfFileInfo 更新核心元数据字段，并使用 `saveNewInfoWithXmp()` 将其写回，以便输出文档以 XMP 形式存储信息。
---
## 使用 XMP 保存元数据

当您需要以 XMP 格式存储更新的文档信息时，请使用此工作流程。

### 步骤

1. 为源 PDF 创建一个 `PdfFileInfo` 对象。
2. 设置要更新的元数据字段，例如主题、标题、关键字和创建者。
3. 使用输出文件路径调用`saveNewInfoWithXmp()`。
4. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
