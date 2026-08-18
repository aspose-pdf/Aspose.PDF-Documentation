---
title: 使用 Java 的标记注释
linktitle: 标记注释
type: docs
weight: 30
url: /java/markup-annotations/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文档中添加、检查和删除突出显示、下划线、波浪线和删除线注释。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 处理 PDF 文件中的标记注释。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建、检查和删除 PDF 文档中的文本标记注释。它涵盖了基于存储库 Java 示例的突出显示、下划线、波浪线和删除线注释。
---
本节中的标记注释工作流程重点关注注释样式注释、插入符号标记和分组替换审阅场景。

## 添加文字注释

当您需要在页面上放置带有弹出元数据的便签样式文本注释时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) 并配置其标题、内容、图标和弹出窗口。
1. 将注释添加到页面并保存文档。

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 获取文本注释

此示例扫描页面并打印每个文本注释的矩形。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面上的注释。
1. 按 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` 过滤注释并打印其矩形。

```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 删除文字注释

当应从文档中删除现有文本注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` 类型的注释。
1. 删除收集的注释并保存输出文件。

```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
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

## 添加插入符号注释

当您需要使用插入符号样式的审阅注释来标记插入的文本时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. Create a [CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) and configure its popup and appearance.
1. 将注释添加到页面并保存文档。

```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 获取插入符号注释

此示例读取现有插入符号注释并打印它们的位置。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代页面注释。
1. 按 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` 过滤注释并打印其矩形。

```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## 删除插入符号注释

当应从页面中删除插入符号注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集类型为 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` 的注释。
1. 删除收集的注释并保存输出文档。

```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 添加分组替换注释

此示例将脱字号注释与删除线注释相结合，以表示替换样式的审阅注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建插入符号注释和相关的 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/)。
1. 通过`setInReplyTo`和`setReplyType`链接注释，然后保存文档。

```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 分组替换注释

此示例检测参与分组替换工作流程的删除线注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面注释并选择删除线注释。
1. 检查回复关系并打印匹配注释的矩形。

```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## 删除分组替换注释

当应从页面中删除替换审阅删除线注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集代表替换标记的删除线注释。
1. 删除收集的注释并保存更新的文档。

```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 相关注释主题

- [文字注释](/pdf/java/text-based-annotations/)
- [交互式注释](/pdf/java/interactive-annotations/)
- [形状注释](/pdf/java/shape-annotations/)
- [媒体注释](/pdf/java/media-annotations/)
- [安全注释](/pdf/java/security-annotations/)
- [水印注释](/pdf/java/watermark-annotations/)
