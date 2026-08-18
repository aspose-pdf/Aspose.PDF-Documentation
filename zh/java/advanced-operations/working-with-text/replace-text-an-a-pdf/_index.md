---
title: 使用 Java 替换 PDF 中的文本
linktitle: 替换 PDF 中的文本
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: 了解如何使用 Java 替换、重新排列和删除 PDF 文档中的文本。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: 使用 Java 替换、删除和调整 PDF 中的文本内容
Abstract: 本文介绍使用 Aspose.PDF for Java 在 PDF 文档中进行文本替换的工作流程。它涵盖了替换所有页面上的文本、限制替换到选定区域、调整替换布局、使用基于正则表达式的匹配、替换字体、删除所有文本以及删除隐藏文本。
---
Aspose.PDF for Java 通过 `TextFragmentAbsorber` 和替换选项提供简单替换和布局感知替换功能。

## 替换所有页面上的文本

当需要在整个文档中替换相同的短语时，请使用此示例。

1. 打开源 PDF 文档。
1. 使用`TextFragmentAbsorber` 在所有页面中搜索目标短语。
1. 替换匹配的文本并保存更新的 PDF。

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

## 替换特定页面区域中的文本

当替换应仅限于一页上选定的矩形时，请使用此示例。

1. 打开源 PDF 文档。
1. 使用页面边界和目标矩形配置`TextSearchOptions`。
1. 替换该区域内的匹配文本并保存文档。

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

## 替换文本并调整移动矩形内的间距

当替换文本应保留在页面上并调整间距但字体大小应保持不变时，请使用此示例。

1. 打开源 PDF 并从目标页面收集文本片段。
1. 修改替换矩形并选择`AdjustSpaceWidth` 行为。
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

## 替换较大段落矩形内的文本

当替换文本应扩展到更大的页面区域时，请使用此示例。

1. 打开源 PDF 并从目标页面获取第一个文本片段。
1. 从页面媒体框构建一个更大的替换矩形。
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

## 替换文本并缩放字体以填充矩形

当替换文本需要放大以填充目标区域时，请使用此示例。

1. 打开源 PDF 并访问目标文本片段。
1. 定义替换矩形并启用`ScaleToFill`字体调整。
1. 设置新文本并保存更新的文档。

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

## 替换文本并将其缩小以适合

当替换文本必须保留在原始文本矩形内时，请使用此示例。

1. 打开源 PDF 并选择目标片段。
1. 重用当前片段矩形并启用`ShrinkToFit`。
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

## 用正则表达式替换文本

当应该通过正则表达式模式找到匹配的文本并在替换期间重新设置样式时，请使用此示例。

1. 打开源 PDF 文档。
1. 使用启用正则表达式的 `TextFragmentAbsorber` 搜索页面。
1. 替换每个匹配项，更新其文本样式，然后保存结果。

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

当占位符必须替换为更长的实际值同时保留页面布局时，请使用此示例。

1. 打开源 PDF 并搜索占位符文本。
1. 指定替换文本并更新其字体设置。
1. 保存文档以便重新计算布局。

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

当使用特定嵌入字体的文本应切换为另一种字体时，请使用此示例。

1. 打开源 PDF 并收集所有文本片段。
1. 检查每个片段的字体名称并替换目标字体。
1. 保存更新的 PDF。

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

当字体替换后应清理文档时，请使用此示例。

1. 打开源 PDF 并配置 `TextEditOptions` 以删除未使用的字体。
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

当必须从每个页面删除所有文本内容时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建`TextFragmentAbsorber`并调用`removeAllText(document)`。
1. 保存清理后的 PDF。

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## 删除一页中的所有文本

当仅应从特定页面删除所有文本时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建 `TextFragmentAbsorber` 并从目标页面中删除文本。
1. 保存更新的文档。

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## 从选定的矩形中删除文本

当仅应删除所选页面区域内的文本时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建一个 `TextFragmentAbsorber` 并定义要清理的矩形。
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

当应从 PDF 中删除不可见的文本片段时，请使用此示例。

1. 打开源 PDF 并吸收所有文本片段。
1. 检查每个片段的不可见文本状态。
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
