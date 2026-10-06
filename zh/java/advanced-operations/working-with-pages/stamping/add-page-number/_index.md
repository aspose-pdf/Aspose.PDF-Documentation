---
title: 在 Java 中为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 30
url: /zh/java/add-page-number/
description: 了解如何在 Java 中向 PDF 文档添加页码印章。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 向 PDF 文件添加页码印章
Abstract: 本文说明了如何使用 Aspose.PDF for Java 添加页码印章。它涵盖了使用自定义字体样式的标准页码以及可配置起始编号的罗马数字页码。
---
## 添加页码印章

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 对象。
1. 配置所需的印章放置和编号选项。
1. 设置所需的文本格式选项，包括 [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) 和 [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 将已配置的 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 添加到目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
