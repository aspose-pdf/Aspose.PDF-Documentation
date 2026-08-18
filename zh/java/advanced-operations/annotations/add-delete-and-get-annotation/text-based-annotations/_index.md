---
title: 使用 Java 基于文本的注释
linktitle: 文本注释
type: docs
weight: 10
url: /java/text-based-annotations/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文档中添加、检查和删除文本、自由文本和删除线注释。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 处理文本 PDF 注释。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建、读取和删除 PDF 文档中基于文本的注释。它涵盖了基于 Java 示例实现的文本注释、自由文本注释和删除线注释。
---
本节中基于文本的注释工作流程涵盖自由文本、突出显示、删除线、波浪线和下划线方案。

## 添加、获取和删除自由文本注释

当您需要放置可编辑文本注释、检查它们或从页面中删除它们时，请使用这些示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 在页面上创建、查找或收集 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) 对象。
1. 添加或删除注释时保存更新的文档。

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加、获取和删除突出显示注释

这些示例展示了如何创建突出显示标记、检查现有突出显示注释以及删除它们。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用页面上的 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) 对象。
1. 添加或删除注释后保存文档。

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加、获取和删除删除线注释

当您需要在文本范围内使用审阅式删除线标记时，请使用这些示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建、检查或收集 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) 对象。
1. 应用更改后保存文档。

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加、获取和删除波浪形注释

这些示例使用波浪形标记，用于在审阅期间强调文本。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建、检查或收集 [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) 对象。
1. 添加或删除注释后保存文档。

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加、获取和删除下划线注释

当应通过注释 API 对文本添加下划线、检查或删除时，请使用这些示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用页面上的 [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) 对象。
1. 添加或删除注释后保存文档。

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加带有四点的下划线注释

此示例通过从矩形派生的四点明确定义下划线区域。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) 并计算其四边形点。
1. 将注释添加到页面并保存文档。

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 从下划线注释中获取标记文本

这些示例读取与下划线注释关联的文本内容，作为完整字符串或单个片段。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面上的下划线注释。
1. 读取`getMarkedText()` 或`getMarkedTextFragments()` 并打印结果。

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## 按标题删除下划线注释

当应根据元数据有选择地删除下划线注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 按标题过滤下划线注释。
1. 删除匹配的注释并保存更新的文档。

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加并展平下划线注释

此示例添加下划线注释并立即将其展平为静态页面内容。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 向页面添加[下划线注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/)。
1. 对注释调用 `flatten()` 并保存输出文件。

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## 相关注释主题

- [交互式注释](/pdf/java/interactive-annotations/)
- [标记注释](/pdf/java/markup-annotations/)
- [安全注释](/pdf/java/security-annotations/)
- [形状注释](/pdf/java/shape-annotations/)
- [水印注释](/pdf/java/watermark-annotations/)
- [导入和导出注释](/pdf/java/import-export-annotations/)
