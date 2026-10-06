---
title: 在 Java 中旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 110
url: /zh/java/rotate-pages/
description: 了解如何在 Java 中旋转 PDF 页面并更改页面方向。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 旋转 PDF 页面
Abstract: 本文解释了如何使用 Aspose.PDF for Java 旋转 PDF 页面。示例遍历文档中的所有页面，应用 90 度旋转，并保存更新后的 PDF。
---
当需要跨一个或多个页面更改方向时，请使用页面旋转 API。

## 将所有页面旋转 90 度

当文档中的每一页都应顺时针旋转时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历全部 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 对象并设置旋转值。
1. 保存更新后的 PDF。

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
