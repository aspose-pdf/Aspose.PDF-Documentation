---
title: 在 Java 中旋转 PDF 文本
linktitle: 旋转 PDF 内的文本
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: 了解如何使用 Java 旋转 PDF 文档中的文本片段和段落。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 旋转 PDF 文档中的文本片段和段落
Abstract: 本文介绍如何使用 Aspose.PDF for Java 旋转 PDF 文档中的文本。它展示了如何旋转单个文本片段、构建包含旋转行的段落以及针对不同的布局场景旋转完整的文本段落。
---
Aspose.PDF for Java 允许您旋转单个文本片段以及整个文本段落。

## 旋转各个文本片段

当同一行上的多个文本片段应使用不同的旋转角度时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建具有所需旋转值的文本片段。
1. 用 `TextBuilder` 附加它们并保存结果。

```java
public static void rotateTextInsidePdf1(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           TextFragment textFragment1 = new TextFragment("main text");
           textFragment1.setPosition(new Position(100, 600));
           textFragment1.getTextState().setFontSize(12);
           textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

           TextFragment textFragment2 = new TextFragment("rotated text");
           textFragment2.setPosition(new Position(200, 600));
           textFragment2.getTextState().setFontSize(12);
           textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment2.getTextState().setRotation(45);

           TextFragment textFragment3 = new TextFragment("rotated text");
           textFragment3.setPosition(new Position(300, 600));
           textFragment3.getTextState().setFontSize(12);
           textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment3.getTextState().setRotation(90);

           TextBuilder builder = new TextBuilder(page);
           builder.appendText(textFragment1);
           builder.appendText(textFragment2);
           builder.appendText(textFragment3);

           document.save(outputFile.toString());
       }
   }
```

## 旋转文本段落内的行

当段落应同时包含普通行和旋转行时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建 `TextParagraph` 并附加具有不同旋转设置的文本片段。
1. 将段落添加到页面并保存文档。

```java
public static void rotateTextInsidePdf2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));

        TextFragment textFragment1 = new TextFragment("rotated text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setRotation(45);

        TextFragment textFragment2 = new TextFragment("main text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment3 = new TextFragment("another rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(-45);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 旋转没有明确位置的段落片段

当应通过正常页面段落流添加旋转文本时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建多个具有不同旋转值的文本片段。
1. 将它们添加到页面段落集合并保存 PDF。

```java
public static void rotateTextInsidePdf3(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(315);

        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(270);

        page.getParagraphs().add(textFragment1);
        page.getParagraphs().add(textFragment2);
        page.getParagraphs().add(textFragment3);

        document.save(outputFile.toString());
    }
}
```

## 旋转完整段落

当整个段落块应该旋转而每行保持共享样式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建多个带有段落级旋转的 `TextParagraph` 对象。
1. 使用共享帮助器方法创建行，附加它们，然后保存文档。

```java
public static void rotateTextInsidePdf4(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        for (int i = 0; i < 4; i++) {
            TextParagraph paragraph = new TextParagraph();
            paragraph.setPosition(new Position(200, 600));
            paragraph.setRotation(i * 90 + 45);

            TextFragment textFragment1 = rotatedLine("Paragraph Text", false);
            TextFragment textFragment2 = rotatedLine("Second line of text", false);
            TextFragment textFragment3 = rotatedLine("And some more text...", true);

            paragraph.appendLine(textFragment1);
            paragraph.appendLine(textFragment2);
            paragraph.appendLine(textFragment3);

            TextBuilder builder = new TextBuilder(page);
            builder.appendParagraph(paragraph);
        }

        document.save(outputFile.toString());
    }
}

private static TextFragment rotatedLine(String text, boolean underline) {
    TextFragment fragment = new TextFragment(text);
    fragment.getTextState().setFontSize(12);
    fragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    fragment.getTextState().setBackgroundColor(Color.getLightGray());
    fragment.getTextState().setForegroundColor(Color.getBlue());
    fragment.getTextState().setUnderline(underline);
    return fragment;
}
```
