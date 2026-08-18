---
title: 使用 Java 将文本添加到 PDF
linktitle: 添加文本到 PDF
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: 了解如何使用 Java 将文本、HTML 片段、列表、链接和自定义字体添加到 PDF 文档。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将文本、链接、HTML 和字体添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 在 PDF 文档中添加文本并设置文本样式。它涵盖简单的文本插入、段落布局、超链接、从右到左的文本、字体样式、透明度、边框、HTML 和 LaTeX 片段、渐变文本以及从文件或流加载的自定义字体。
---
Aspose.PDF for Java 支持纯文本插入、高级布局、样式、渐变、HTML、LaTeX 和自定义字体。

## 添加简单的文本片段

当应将短文本字符串放置在固定页面坐标处时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个`TextFragment`并设置其位置。
1. 将其添加到页面并保存文档。

```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## 在矩形内添加一个段落

当较大的文本块应在有界区域内流动时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 加载源文本并配置`TextParagraph`矩形和换行模式。
1. 通过`TextBuilder` 附加片段并保存 PDF。

```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 添加具有不同缩进设置的段落

当第一行和后续行应使用不同的缩进规则时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 准备共享文本片段并创建多个`TextParagraph`对象。
1. 为每个段落配置缩进，附加它们，然后保存文档。

```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## 插入带有手动换行符的文本

当一个文本片段应包含显式新行时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个包含换行符的`TextFragment`并配置其样式。
1. 通过 `TextParagraph` 附加它并保存 PDF。

```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 检查检测到的换行符

当您需要查看与文本布局和换行相关的通知输出时，请使用此示例。

1. 创建新的 PDF 文档并启用通知日志记录。
1. 向页面添加几个长文本片段。
1. 检查通知并保存文档。

```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## 动态测量文本宽度

当应在做出布局决策之前测量字符和字符串宽度时，请使用此示例。

1. 解析目标字体并创建`TextState`。
1. 测量字符并比较字体和文本状态 API 的结果。
1. 输出任何不匹配的情况以进行验证。

```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## 添加带有超链接段的文本

当文本片段的一部分应充当 Web 链接时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用多个`TextSegment` 对象构建`TextFragment`。
1. 为译文句段指定超链接和样式，然后保存文档。

```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 添加从右到左的文本

当文档必须以正确的对齐方式显示从右到左的脚本内容时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用目标 RTL 文本创建 `TextFragment` 并配置其字体和对齐方式。
1. 将其添加到页面并保存 PDF。

```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加样式文本和类似公式的段

当常规文本和类似下标的段应在一个输出中使用不同的文本状态时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建主要样式片段并使用辅助片段组成公式。
1. 将两个片段添加到页面并保存文档。

```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## 添加下划线文本

当文本片段应该明显使用下划线样式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建文本片段，配置其字体和下划线状态，并设置其位置。
1. 添加 `TextBuilder` 并保存结果。

```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## 在彩色形状上添加透明文本

当文本应以透明方式显示在背景图形上方时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 绘制背景形状并创建半透明文本片段。
1. 将两个元素添加到页面并保存文档。

```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## Add invisible text

当可搜索或隐藏文本应该存在而无需可见渲染时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 添加一个可见文本片段和第二个启用不可见标志的片段。
1. 保存文档。

```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 添加带有矩形边框的文本

当文本应与其边框一起绘制时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个样式化的`TextFragment`并启用文本矩形边框的绘制。
1. 添加 `TextBuilder` 并保存 PDF。

```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 添加删除线文本

当文本应使用删除线格式时使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建启用删除线的样式化文本片段。
1. 将其附加到页面并保存文档。

```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 将轴向渐变阴影应用于文本

当文本应使用线性渐变填充而不是纯色时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建文本片段并为其前景色指定轴向渐变。
1. 将其添加到页面并保存 PDF。

```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 将径向渐变阴影应用于文本

当文本应使用径向渐变填充时使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建文本片段并为其前景色指定径向渐变。
1. 将其添加到页面并保存文档。

```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加内联 HTML 样式格式的文本

当应通过 HTML 标记插入上标和下标格式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用所需的内联标记创建`HtmlFragment`。
1. 将其添加到页面并保存 PDF。

```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加 LaTeX 文本片段

当需要在 PDF 中呈现数学或 TeX 格式的内容时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用所需的表达式创建 `TeXFragment`。
1. 将其添加到页面并保存文档。

```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加丰富的 HTML 片段

当页面应呈现结构化 HTML 内容（例如标题、段落和链接）时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 准备 HTML 内容字符串并创建 `HtmlFragment`。
1. 将其添加到页面并保存 PDF。

```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加具有覆盖文本状态的 HTML 片段

当导入的 HTML 内容应继承受控字体和颜色设置时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 准备 HTML 内容并创建 `HtmlFragment`。
1. 分配自定义`TextState`，添加片段，然后保存文档。

```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 使用从文件加载的自定义字体

当文本应使用直接从字体文件路径加载的字体时，请使用此示例。

1. 解析自定义字体文件路径。
1. 创建文本片段并通过`FontRepository.openFont`加载字体。
1. 应用字体设置并保存文档。

```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 使用从流加载的自定义字体

当应从流中打开自定义字体并将其嵌入 PDF 中时，请使用此示例。

1. 以流的形式打开字体文件并使用 `FontRepository` 加载它。
1. 创建文本片段并指定嵌入字体。
1. 将片段添加到页面并保存文档。

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
