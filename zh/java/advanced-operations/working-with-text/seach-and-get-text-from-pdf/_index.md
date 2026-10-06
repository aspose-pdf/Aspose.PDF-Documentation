---
title: 在 Java 中搜索并提取 PDF 文本
linktitle: 搜索并获取文本
type: docs
weight: 60
url: /zh/java/search-and-get-text-from-pdf/
description: 了解如何在 Java 中搜索、检查并提取 PDF 文档中的文本。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中搜索 PDF 文本并检查提取的片段
Abstract: 本文说明了如何使用 Aspose.PDF for Java 对 PDF 文档进行搜索和提取文本。它涵盖了 TextAbsorber 和 TextFragmentAbsorber，包括基于区域的提取、特定页面的搜索、正则表达式和短语匹配、超链接插入、样式文本检查以及片段高亮显示。
---
Aspose.PDF for Java 支持原始文本提取和片段级搜索，涉及坐标、样式和正则表达式匹配。

## 使用 TextAbsorber 提取所有页面的文本

当您需要从选定文档区域跨所有页面提取纯文本时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建 `TextExtractionOptions` 以及基于区域的 `TextSearchOptions`。
1. 运行 `TextAbsorber` 在所有页面上提取文本并输出。

```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## 使用 TextAbsorber 提取单页文本

当纯文本提取应限制为单页时，请使用此示例。

1. 打开源 PDF 文档。
1. 使用目标区域配置文本提取和搜索选项。
1. 运行 `TextAbsorber` 在选定的页面上并输出结果。

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## 检查文档中的所有文本片段

当您需要文本内容以及字体、位置和颜色元数据时，请使用此示例。

1. 打开源 PDF 文档。
1. 运行 `TextFragmentAbsorber` 跨所有页面。
1. 遍历片段并输出它们的元数据。

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## 在特定页面上搜索一个短语

当目标词应仅在选定页面上找到时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建 `TextFragmentAbsorber` 带有目标短语。
1. 访问所选页面并输出匹配的片段位置。

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 在页面之间继续顺序搜索

当您想在从一个页面搜索移动到下一个页面搜索时复用同一个吸收器，请使用此示例。

1. 打开源 PDF 文档并创建可重用的吸收器。
1. 搜索第一页并检查结果。
1. 继续搜索其他页面并查看更新的匹配项。

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## 在选定的矩形内搜索短语

在短语匹配应仅限于单页的某个区域时，使用此示例。

1. 打开源 PDF 文档。
1. 创建 `TextFragmentAbsorber` 使用目标短语和基于矩形的 `TextSearchOptions`。
1. 访问页面并输出匹配的片段位置。

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 使用正则表达式搜索文本

当匹配应该通过正则表达式模式而不是固定短语来查找时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建一个支持正则表达式的 `TextFragmentAbsorber`。
1. 访问目标页面并输出匹配的片段。

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 通过正则表达式模式搜索短语列表

当需要在一次运行中找到多个目标短语时，请使用此示例。

1. 打开源 PDF 文档。
1. 创建一个正则表达式模式数组并将其传递给 `TextFragmentAbsorber`。
1. 访问文档并检查分组的正则表达式结果。

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## 查找文本并将其转换为超链接

当匹配的词需要突出显示并转换为可点击的链接时，请使用此示例。

1. 打开源 PDF 文档。
1. 在启用正则表达式搜索的情况下搜索目标词。
1. 更新文本样式，附加超链接，并保存修改后的 PDF。

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## 按样式特征搜索文本

当您需要根据格式（如粗体或不可见文本）检查片段时，请使用此示例。

1. 打开源 PDF 文档。
1. 运行 `TextFragmentAbsorber` 在目标页面上。
1. 检查每个片段样式并输出匹配的条目。

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## 在已呈现的页面预览中突出显示搜索结果

当文本匹配需要与渲染的页面图像关联以进行视觉检查时，请使用此示例。

1. 创建具有所需分辨率的 PNG 设备。
1. 使用...搜索每页 `TextFragmentAbsorber` 并将页面渲染为图像流。
1. 写入页面预览图像并输出片段坐标以供检查。

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
