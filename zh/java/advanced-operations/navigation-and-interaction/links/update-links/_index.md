---
title: 在 Java 中更新 PDF 链接
linktitle: 更新链接
type: docs
weight: 20
url: /zh/java/update-links/
description: 了解如何在 Java 中更新 PDF 链接的外观和目标。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 更新 PDF 文件中链接批注的外观和网页目标
Abstract: 本文展示了如何使用 Aspose.PDF for Java 更新现有的链接批注。示例演示了更改链接覆盖的文本颜色、更新链接批注的颜色以及替换网页链接的目标 URI。
---
可以通过在页面上找到链接批注并更新其外观或操作来编辑现有链接。

## 更新链接文本颜色

当链接批注覆盖的文本区域需要重新着色时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 查找链接批注，并从每个批注区域构建文本搜索矩形。
1. 重新着色匹配的文本片段并保存文档。

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

当需要更改现有链接批注的可见颜色时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面批注并进行过滤以获取 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 对象。
1. 更新链接批注颜色并保存文档。

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

## 更新网页链接目标

当现有网页链接应指向新的 URI 时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 查找操作类型为 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) 的链接批注。
1. 替换 URI 并保存更新后的文档。

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
