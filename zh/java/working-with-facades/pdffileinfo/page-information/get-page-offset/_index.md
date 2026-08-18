---
title: 获取页面偏移量
linktitle: 获取页面偏移量
type: docs
weight: 20
url: /java/get-page-offset/
description: 了解如何使用 PdfFileInfo 外观检查 Java 中的页面 X 和 Y 偏移量。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 获取 PDF 页面偏移量
Abstract: 了解如何使用 Aspose.PDF for Java 检索页面偏移量。 Java 示例使用 PdfFileInfo 读取第 1 页的 X 和 Y 偏移，并将点值转换为英寸，以便于布局分析。
---
## 获取页面偏移量

当您需要了解页面内容相对于 PDF 原点的定位方式时，请使用此工作流程。

### 步骤

1. 为输入 PDF 创建一个 `PdfFileInfo` 对象。
2. 为目标页面调用`getPageXOffset` 和`getPageYOffset`。
3. 通过除以 `72.0` 将点值转换为英寸。
4. 使用或打印转换后的值。
5. 关闭`PdfFileInfo`实例。

### Java示例

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
