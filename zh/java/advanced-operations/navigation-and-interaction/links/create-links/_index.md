---
title: 用 Java 创建 PDF 链接
linktitle: 创建链接
type: docs
weight: 10
url: /java/create-links/
description: 了解如何使用 Java 创建内部、外部和远程 PDF 链接。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中创建链接注释
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建链接注释。它涵盖启动操作、远程文档导航、文档内页面导航以及通过将操作附加到 LinkAnnotation 对象的基于 URI 的 Web 链接。
---
Aspose.PDF for Java 使用 `LinkAnnotation` 和操作对象来定义链接行为。

## 创建启动操作链接

当链接注释应启动外部文件或目标时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并选择目标页面。
1. 创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 并配置其边框和颜色。
1. 分配 [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) 并保存文档。

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 创建远程跳转链接

当链接应打开另一个 PDF 文档中的页面时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 在目标页面上创建 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)。
1. 分配 [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) 并保存输出文件。

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 创建内部跳转链接

当链接应导航到同一 PDF 文档内的另一个页面时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 并配置其外观。
1. 将 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) 分配给目标页面并保存文档。

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 创建 URI 链接

当链接应通过 URI 操作打开 Web 资源时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 在页面上创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)。
1. 分配 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) 并保存输出文件。

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
