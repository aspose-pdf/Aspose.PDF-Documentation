---
title: 使用 Java 替换 PDF 中的文本
linktitle: 替换 PDF 中的文本
type: docs
weight: 40
url: /zh/java/replace-text-in-pdf/
description: 了解如何使用 Java 替换、重新排列和删除 PDF 文档中的文本。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7

TechArticle: true
AlternativeHeadline: 使用 Java 替换、删除并调整 PDF 中的文本内容
Abstract: 本文说明了使用 Aspose.PDF for Java 在 PDF 文档中进行文本替换的工作流。内容包括跨所有页面替换文本、将替换限制在选定区域、调整替换布局、使用基于正则表达式的匹配、替换字体、删除所有文本以及清除隐藏文本。
aliases:
    - "/zh/java/replace-text-in-a-pdf-document/"
---

Aspose.PDF for Java 提供了简单替换和布局感知替换功能，通过 `TextFragmentAbsorber` 并替换选项。

## 在所有页面上替换文本

当需要在整个文档中替换相同短语时使用此示例。

1. 打开源 PDF 文档。
1. 在所有页面中搜索目标短语 `TextFragmentAbsorber`.
1. 替换匹配的文本并保存更新后的 PDF。

```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## 在特定页面区域替换文本

当替换应限制在单页的选定矩形时使用此示例。

1. 打开源 PDF 文档。
1. 配置 `TextSearchOptions` 带有页面边界和目标矩形。
1. 在该区域内替换匹配的文本并保存文档。

```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## 在偏移的矩形内替换文本并调整间距

当替换文本应保留在页面上并调整间距，但字体大小保持不变时，请使用此示例。

1. 打开源 PDF 并从目标页收集文本片段。
1. 修改替换矩形并选择 `AdjustSpaceWidth` 行为。
1. 设置新文本并保存文档。

```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 在更大的段落矩形内替换文本

当替换文本应扩展到更大的页面区域时，请使用此示例。

1. 打开源 PDF 并从目标页面获取第一个文本片段。
1. 从页面媒体盒构建一个更大的替换矩形。
1. 应用替换选项并保存 PDF。

```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 替换文本并缩放字体以填满矩形

使用此示例，当替换文本需要放大以填满目标区域时。

1. 打开源 PDF 并访问目标文本片段。
1. 定义一个替换矩形并启用 `ScaleToFill` 字体调整。
1. 设置新文本并保存更新后的文档。

```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 替换文本并缩小以适应

当替换文本必须保持在原始文本矩形内部时，请使用此示例。

1. 打开源 PDF 并选择目标片段。
1. 重用当前片段矩形并启用 `ShrinkToFit`.
1. 替换文本并保存文档。

```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 使用正则表达式替换文本

当匹配的文本应通过正则表达式模式查找并在替换过程中重新设置样式时，请使用此示例。

1. 打开源 PDF 文档。
1. 使用正则表达式搜索页面 `TextFragmentAbsorber`.
1. 替换每个匹配项，更新其文字样式，并保存结果。

```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## 替换占位符文本并让页面重新排列

当占位符必须被更长的真实值替换且需要保持页面布局时，请使用此示例。

1. 打开源 PDF 并搜索占位符文本。
1. 分配替换文本并更新其字体设置。
1. 保存文档以重新计算布局。

```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## 将一种字体替换为另一种字体

使用此示例在文本使用特定嵌入式字体时需要切换到另一种字体。

1. 打开源 PDF 并收集所有文本片段。
1. 检查每个片段的字体名称并替换为目标字体。
1. 保存更新后的 PDF。

```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 替换字体并删除未使用的字体资源

当文档在替换字体后需要清理时，请使用此示例。

1. 打开源PDF并进行配置 `TextEditOptions` 删除未使用的字体。
1. 吸收文本片段并指定替换字体。
1. 保存优化后的文档。

```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## 删除文档中的所有文本

当必须从每页删除所有文本内容时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建一个 `TextFragmentAbsorber` 并调用 `removeAllText(document)`.
1. 保存已清理的 PDF。

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## 从单页中删除所有文本

当仅需要从特定页面删除所有文本时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建一个 `TextFragmentAbsorber` 并从目标页面删除文本。
1. 保存更新后的文档。

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## 从选定矩形中删除文本

当只需要在选定的页面区域内删除文本时使用此示例。

1. 打开源 PDF 文档。
1. 创建一个 `TextFragmentAbsorber` 并定义要清除的矩形。
1. 从该区域删除文本并保存文档。

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## 删除隐藏文本

当需要从 PDF 中剥离不可见文本片段时，请使用此示例。

1. 打开源 PDF，并吸收所有文本片段。
1. 检查每个片段是否为不可见文本状态。
1. 清除隐藏文本并保存文档。

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
