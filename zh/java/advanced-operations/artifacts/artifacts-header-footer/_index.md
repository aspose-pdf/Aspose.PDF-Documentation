---
title: 使用 Java 管理 PDF 页眉和页脚
linktitle: 管理 PDF 页眉和页脚
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文档中添加和删除页眉和页脚工件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Java 添加、自定义和删除 PDF 页眉和页脚
Abstract: 本文介绍如何使用 Aspose.PDF for Java 管理 PDF 文档中的页眉和页脚工件。它涵盖了创建具有自定义文本状态和对齐方式的可重用`HeaderArtifact` 和`FooterArtifact` 对象、将它们添加到页面以及删除现有的页眉和页脚工件。
---
页眉和页脚工件是非内容分页元素，通常用于重复标签、页面标识符和布局框架。

## 创建标头工件

当您需要具有一致文本样式和对齐方式的可重用标题工件时，请使用此帮助程序。

1. 创建一个 [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/)。
1. 设置其文本、字体设置和前景色。
1. 配置水平对齐并返回工件。

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

该帮助器创建一个可重用的页脚工件，其样式模式与页眉工件相同。

1. 创建一个 [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/)。
1. 设置其文本、文本状态和前景色。
1. 配置对齐并返回工件。

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

## 添加标题工件

当页面应显示可重用的标头工件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 通过辅助方法创建标头工件。
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

## 添加页脚神器

当页面应显示具有可重用格式的页脚工件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
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

## 删除页眉和页脚工件

当应从页面中删除现有的页眉和页脚工件时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 以相反的顺序迭代页面工件集合。
1. 删除子类型为页眉或页脚的分页工件，然后保存文档。

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
