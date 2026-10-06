---
title: 获取页面偏移
linktitle: 获取页面偏移
type: docs
weight: 20
url: /zh/java/get-page-offset/
description: 了解如何使用 PdfFileInfo 类在 Java 中检查页面的 X 和 Y 偏移。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 获取 PDF 页面偏移
Abstract: 了解如何使用 Aspose.PDF for Java 检索页面偏移。Java 示例使用 PdfFileInfo 读取第 1 页的 X 和 Y 偏移，并将点值转换为英寸，以便更容易进行布局分析。
---
## 获取页面偏移

在需要了解页面内容相对于 PDF 原点的定位方式时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileInfo` 输入 PDF 的对象。
2. 呼叫 `getPageXOffset` 和 `getPageYOffset` 对于目标页面。
3. 通过除以将点值转换为英寸 `72.0`。
4. 使用或打印转换后的值。
5. 关闭 `PdfFileInfo` 实例。

### Java 示例

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
