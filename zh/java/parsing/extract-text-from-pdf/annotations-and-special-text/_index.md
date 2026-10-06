---
title: 使用 Java 的批注和特殊文本
linktitle: 批注和特殊文本
type: docs
weight: 40
url: /zh/java/annotation-and-special-text/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文档中的印章批注、突出显示的文本以及上标或下标内容中提取文本。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 提取突出显示的文本

遍历页面批注并读取标记的文本 `HighlightAnnotation`。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 遍历 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 目标上的对象 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 检查每个批注是否为 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) 在将其转换为特定批注类之前。
1. 读取每个高亮批注中的标记文本并将其打印到控制台。

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

## 从印章批注中提取文本

读取印章批注的常规外观流并将其传递 `TextAbsorber`。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 遍历 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 目标上的对象 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 过滤批注，仅保留其类型为 `Stamp`。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 并请求 stamp 批注外观字典中的 normal appearance 条目。
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

当需要在每个片段上同时获取提取的文本以及上标或下标标记时，使用 `TextFragmentAbsorber`。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) 用于片段级文本分析。
1. 访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并收集它的 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 对象。
1. 遍历这些片段并从中读取带有上标和下标标志的文本 `fragment.getTextState()`。
1. 将提取的细节写入输出文件。

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
