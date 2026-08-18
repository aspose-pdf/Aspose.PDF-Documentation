---
title: 获取 PDF 版本
linktitle: 获取 PDF 版本
type: docs
weight: 20
url: /java/get-pdf-version/
description: 了解如何使用 PdfFileInfo 外观在 Java 中检索 PDF 文档的版本。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 检索 PDF 版本
Abstract: 了解如何使用 Aspose.PDF for Java 检索 PDF 版本。 Java 示例创建一个 PdfFileInfo 对象，使用 `getPdfVersion()` 读取版本字符串，打印结果，然后关闭文件信息对象。
---
## 获取 PDF 版本

当您需要检查文件兼容性或通过特定于版本的处理逻辑路由文档时，请使用此工作流程。

### 步骤

1. 为 PDF 文件创建 `PdfFileInfo` 对象。
2. 调用`getPdfVersion()`来检索报告的版本。
3. 使用或打印版本值。
4. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
