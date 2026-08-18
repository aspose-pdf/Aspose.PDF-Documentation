---
title: 使用 Java 的注释和特殊文本
linktitle: 注释和特殊文本
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文档中的图章注释、突出显示文本以及上标或下标内容中提取文本。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 提取突出显示的文本

迭代页面注释并从`HighlightAnnotation`读取标记文本。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 迭代目标 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 上的 [注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 对象。
1. 在将每个注释转换为类型化注释类之前，检查每个注释是否是 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/)。
1. 读取每个突出显示注释中的标记文本并将其打印到控制台。

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## 从图章注释中提取文本

从标记注释中读取正常外观流并将其传递给`TextAbsorber`。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 迭代目标 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 上的 [注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 对象。
1. 将注释过滤为类型为`Stamp`的注释。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 并从图章注释外观字典中请求正常外观条目。
1. 访问外观 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 并打印提取的文本。

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## 提取上标和下标文本详细信息

当您需要提取的文本以及每个片段上的上标或下标标志时，请使用`TextFragmentAbsorber`。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建一个 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) 用于片段级文本分析。
1. 访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并收集其 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 对象。
1. 迭代这些片段并从 `fragment.getTextState()` 读取文本以及上标和下标标志。
1. 将提取的详细信息写入输出文件。

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
