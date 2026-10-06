---
title: 使用 Java 的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 20
url: /zh/java/hello-world-example/
description: 此示例演示了如何使用 Aspose.PDF for Java 创建带有样式化 Hello World 文本的简单 PDF 文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Java 的 Hello World 示例
Abstract: 本文提供了 Aspose.PDF for Java 的 Hello World 示例。该示例创建一个新的 PDF 文档，添加一个页面，创建一个具有自定义位置、字体和颜色的 TextFragment，使用 TextBuilder 将文本追加到页面，并将结果保存为 PDF 文件。
---
"Hello World" 示例是了解基本 PDF 创建工作流的最简途径。在本文中，示例创建一个新的 PDF，将样式化的文本片段放置在页面上，并保存输出文件。

Java 示例遵循以下步骤：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个带有文本 `Hello, world!` 的 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 设置 [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/)，并通过片段的 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) 设置字体、字号、背景色和前景色。
1. 为页面创建一个 [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/)。
1. 将 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 追加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 保存 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

以下 Java 代码基于 `GetStartedExamples.java`。

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
