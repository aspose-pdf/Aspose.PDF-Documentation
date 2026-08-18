---
title: 通过 Java 从 PDF 中提取字体
linktitle: 从 PDF 中提取字体
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: 使用 Aspose.PDF for Java 检查和提取 PDF 文档中使用的字体。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Java 从 PDF 中提取字体
Abstract: 本文介绍如何使用 Aspose.PDF for Java 检查 PDF 文档中使用的字体。它展示了如何打开 PDF、调用 `getFontUtilities().getAllFonts()` 以及迭代生成的字体对象以读取其名称。
---
当您需要在转换或归档工作流程之前审核文档排版、检查嵌入资源或验证字体使用情况时，请使用字体提取。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 调用`document.getFontUtilities().getAllFonts()`来收集文档引用的每个[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/)资源。
1. 迭代提取的 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 对象并从字体元数据中读取每个字体名称。
1. 打印字体名称，以便可以审核或导出文档排版。

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
