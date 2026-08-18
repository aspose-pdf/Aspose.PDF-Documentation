---
title: 用 Java 更新 PDF 链接
linktitle: 更新链接
type: docs
weight: 20
url: /java/update-links/
description: 了解如何在 Java 中更新 PDF 链接外观和目标。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 更新 PDF 文件中的链接注释外观和 Web 目标
Abstract: 本文介绍如何使用 Aspose.PDF for Java 更新现有链接注释。这些示例演示了如何更改链接所覆盖的文本颜色、更新链接注释颜色以及替换 Web 链接的目标 URI。
---
可以通过查找页面上的链接注释并更新其外观或操作来编辑现有链接。

## 更新链接文本颜色

当链接注释覆盖的文本区域应重新着色时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 查找链接注释并从每个注释区域构建文本搜索矩形。
1. 对匹配的文本片段重新着色并保存文档。

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 更新链接边框颜色

当应更改现有链接注释的可见颜色时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代页面注释并过滤 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 对象。
1. 更新链接注释颜色并保存文档。

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 更新网络链接目标

当现有 Web 链接应指向新 URI 时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 查找操作为 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) 的链接注释。
1. 替换 URI 并保存更新的文档。

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
