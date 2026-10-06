---
title: 获取页面信息
linktitle: 获取页面信息
type: docs
weight: 10
url: /zh/java/get-page-info/
description: 了解如何在 Java 中使用 PdfFileInfo 类检查页面宽度、高度和旋转。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 获取 PDF 页面信息
Abstract: 了解如何使用 Aspose.PDF for Java 检索页面信息。Java 示例使用 PdfFileInfo 读取第 1 页的宽度、高度和旋转，以便在进一步处理之前检查其布局。
---
## 获取页面信息

此示例读取第 1 页的主要几何属性。

### 步骤

1. 创建一个 `PdfFileInfo` 源 PDF 的对象。
2. 调用 `getPageWidth`, `getPageHeight`，并且 `getPageRotation` 对于您想检查的页面。
3. 使用或打印返回的值。
4. 关闭 `PdfFileInfo` 实例。

### Java 示例

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
