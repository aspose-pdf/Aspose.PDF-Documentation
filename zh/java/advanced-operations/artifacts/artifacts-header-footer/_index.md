---
title: 在 Java 中添加 PDF 页眉和页脚
linktitle: 添加页眉和页脚
type: docs
weight: 70
url: /zh/java/artifacts-header-footer/
description: 创建样式化的页眉和页脚工件，并将其添加到 Java 中的 PDF 页面。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中添加页眉和页脚
Abstract: 创建样式化的页眉和页脚工件，并将其添加到 Java 中的 PDF 页面。
---
页眉和页脚人工制品是非内容的分页元素，常用于重复标签、页码标识和布局框架。

## 创建页眉人工制品

当您需要具有一致文本样式和对齐方式的可重用页眉人工制品时，请使用此助手。

1. 创建一个 [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/)。
1. 设置其文本、字体设置和前景色。
1. 配置水平对齐并返回该工件。

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 创建页脚工件

此帮助程序创建一个可重复使用的页脚工件，其样式模式与页眉工件相同。

1. 创建一个 [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/)。
1. 设置其文本、文本状态和前景颜色。
1. 设置对齐方式并返回工件。

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 添加页眉工件

当页面需要显示可重用的页眉工件时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 通过辅助方法创建页眉工件。
1. 将工件添加到页面并保存输出文件。

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## 添加页脚工件

当页面需要显示具有可重用格式的页脚工件时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 通过辅助方法创建页脚工件。
1. 将工件添加到页面并保存输出文件。

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [删除页眉和页脚](/pdf/zh/java/remove-headers-footers/)
- [在 Java 中使用 PDF 制品](/pdf/zh/java/artifacts/)
