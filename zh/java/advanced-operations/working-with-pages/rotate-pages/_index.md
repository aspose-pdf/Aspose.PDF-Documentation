---
title: 在 Java 中旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 110
url: /java/rotate-pages/
description: 了解如何在 Java 中旋转 PDF 页面和更改页面方向。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 旋转 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF for Java 旋转 PDF 页面。该示例迭代文档中的所有页面，应用 90 度旋转，并保存更新的 PDF。
---
当您需要更改一页或多页的方向时，请使用页面旋转 API。

## 将所有页面旋转 90 度

当文档中的每一页都应顺时针旋转时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代所有 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 对象并设置旋转值。
1. 保存更新的 PDF。

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
