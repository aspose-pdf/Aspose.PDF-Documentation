---
title: 使用 Java 将页码添加到 PDF
linktitle: 添加页码
type: docs
weight: 30
url: /java/add-page-number/
description: 了解如何使用 Java 将页码标记添加到 PDF 文档。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将页码标记添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 添加页码标记。它涵盖具有自定义字体样式的标准页码和具有可配置起始编号的罗马数字编号。
---
## 添加页码戳

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 对象。
1. 配置所需的图章放置和编号选项。
1. 设置所需的文本格式选项，包括[FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/)和[颜色](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 将配置的 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 添加到目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
