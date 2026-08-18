---
title: 用 Java 提取 PDF 链接
linktitle: 提取链接
type: docs
weight: 30
url: /java/extract-links/
description: 了解如何使用 Java 从 PDF 文档中提取链接注释和超链接。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中提取链接注释和 URI 目标
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中提取链接注释。它展示了如何枚举页面上的链接注释、读取其页面索引和矩形以及从 GoToURIAction 实例中提取 URI 目标。
---
您可以通过迭代页面注释并过滤 `AnnotationType.Link` 来检查 PDF 链接。

## 提取链接注释

当您需要页面上链接注释的位置和页面信息时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代页面注释并过滤链接注释。
1. 读取每个匹配链接的页面索引和矩形。

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## 提取超链接目标

当您需要从 Web 链接注释中读取目标 URI 时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 查找其操作为 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) 的 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 对象。
1. 打印每个超链接的页面索引和 URI 目标。

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
