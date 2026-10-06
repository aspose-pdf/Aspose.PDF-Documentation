---
title: 使用 XMP 保存元数据
linktitle: 使用 XMP 保存元数据
type: docs
weight: 30
url: /zh/java/save-metadata-with-xmp/
description: 了解如何在 Java 中使用 PdfFileInfo 外观通过 XMP 保存 PDF 元数据。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 通过 XMP 保存 PDF 元数据
Abstract: 了解如何使用 Aspose.PDF for Java 通过 XMP 保存 PDF 元数据。该 Java 示例使用 PdfFileInfo 更新核心元数据字段，并使用 `saveNewInfoWithXmp()` 将其写回，从而使输出文档以 XMP 形式存储信息。
---
## 使用 XMP 保存元数据

当您需要将更新后的文档信息存储为 XMP 格式时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileInfo` 源 PDF 的对象。
2. 设置要更新的元数据字段，例如主题、标题、关键字和创建者。
3. 调用 `saveNewInfoWithXmp()` 使用输出文件路径。
4. 关闭 `PdfFileInfo` 实例.

### Java 示例

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
