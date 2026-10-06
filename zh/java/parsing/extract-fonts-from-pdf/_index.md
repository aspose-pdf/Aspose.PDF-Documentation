---
title: 通过 Java 从 PDF 提取字体
linktitle: 从 PDF 提取字体
type: docs
weight: 30
url: /zh/java/extract-fonts-from-pdf/
description: 使用 Aspose.PDF for Java 检查并提取 PDF 文档中使用的字体。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Java 从 PDF 提取字体
Abstract: 本文说明了如何使用 Aspose.PDF for Java 检查 PDF 文档中使用的字体。它展示了如何打开 PDF，调用 `getFontUtilities().getAllFonts()`，并遍历得到的字体对象以读取它们的名称。
---
当您需要审计文档排版、检查嵌入资源或在转换或归档工作流之前验证字体使用情况时，请使用字体提取。

1. 在 a 中打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 调用 `document.getFontUtilities().getAllFonts()` 收集每个 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 由文档引用的资源。
1. 遍历已提取的 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 对象，并从字体元数据中读取每个字体名称。
1. 打印字体名称，以便对文档排版进行审计或导出。

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
