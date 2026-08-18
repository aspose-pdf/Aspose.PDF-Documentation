---
title: 用 Java 格式化 PDF 文本
linktitle: PDF 中的文本格式
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: 了解如何使用 Java 中的间距、注释、列表、多列布局和样式选项来格式化 PDF 文档中的文本。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 设置 PDF 文件内文本的格式和样式
Abstract: 本文介绍如何使用 Aspose.PDF for Java 格式化 PDF 文档中的文本。它涵盖行间距、字符间距、项目符号和编号列表、脚注和尾注、内联段落内容、多列布局、强制分页符和自定义制表位。
---
Aspose.PDF for Java 提供了用于间距、列表、注释、内联布局和多列组合的文本格式控件。

## 设置简单行距

当段落文本应使用固定行距值时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 加载或准备源文本并创建`TextFragment`。
1. 设置行距，将片段添加到页面，然后保存文档。

```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## 将行距模式与自定义字体进行比较

当应使用同一字体的不同格式模式测试行间距时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 加载自定义字体并准备两个具有不同行距模式的片段。
1. 将两个片段添加到页面并保存 PDF。

```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## 使用文本片段设置字符间距

当相同的文本应以不同的字符间距值显示时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用辅助方法针对多个间距值构建文本片段。
1. 将片段添加到页面并保存文档。

```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## 设置文本段落内的字符间距

当应在有界文本段落内应用字符间距时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个带有目标矩形和环绕选项的`TextParagraph`。
1. 附加样式文本片段并保存 PDF。

```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 使用 HTML 创建项目符号列表

当应从 HTML 标记生成无序列表格式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建 HTML 列表字符串。
1. 将其添加为 `HtmlFragment` 并保存文档。

```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 使用 HTML 创建编号列表

当应从 HTML 标记生成有序列表格式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建有序的 HTML 列表字符串。
1. 将其添加为 `HtmlFragment` 并保存文档。

```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 使用 LaTeX 创建项目符号列表

当应从 TeX 标记呈现无序列表格式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用 `itemize` 环境准备 TeX 列表字符串。
1. 将其添加为 `TeXFragment` 并保存 PDF。

```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 使用 LaTeX 创建编号列表

当应从 TeX 标记呈现有序列表格式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用 `enumerate` 环境准备 TeX 列表字符串。
1. 将其添加为 `TeXFragment` 并保存 PDF。

```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 创建包含文本段落的项目符号列表

当应从纯文本片段构建手动项目符号列表时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建 `TextParagraph` 并附加以项目符号为前缀的片段。
1. 将段落添加到页面并保存文档。

```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 创建包含文本段落的编号列表

当应从纯文本片段构建手动编号列表时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建一个 `TextParagraph` 并附加编号的片段。
1. 将段落添加到页面并保存文档。

```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 添加基本​​脚注

当文本片段应引用简单的脚注时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建主文本片段并指定 `Note` 作为脚注。
1. 添加任何内联延续文本并保存文档。

```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## 添加具有自定义文本样式的脚注

当脚注内容应使用自己的字体、大小和颜色设置时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建主要文本片段并配置样式脚注注释。
1. 附上注释并保存 PDF。

```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 添加带有自定义标记文本的脚注

当可见脚注标记应替换为自定义文本时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 将脚注分配给主要文本片段并覆盖其标记文本。
1. 添加剩余内容并保存文档。

```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## 自定义脚注分隔线

当应明确设置脚注与页面内容分隔线的样式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 通过`GraphInfo`配置页面注释线条样式。
1. 添加带有脚注的文本片段并保存文档。

```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 添加包含图像和表格内容的脚注

当脚注本身应包含丰富的内容（例如图像、文本和表格）时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用图像、内联文本和表格构建 `Note` 对象。
1. 将其附加到主要文本片段并保存文档。

```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## 添加尾注

当文本片段应引用尾注内容而不是页面脚注时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 为主要文本片段分配尾注并添加支持正文文本。
1. 使用生成的尾注内容保存文档。

```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## 添加带有自定义标记文本的尾注

当尾注标记应使用自定义可见标签时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 将尾注分配给主要文本片段并覆盖其标记文本。
1. 添加剩余的文档文本并保存 PDF。

```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## 将表格内容强制放到新页面上

当格式化内容应明确从新页面开始时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 构建一个表并填充其行。
1. 将表格设置为从新页面开始并保存文档。

```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 在一个段落流中混合内联内容

当文本和图像应在同一段落流内继续时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 添加第一个文本片段，然后添加内嵌图像，然后添加另一个内嵌文本片段。
1. 添加以下任何独立段落并保存文档。

```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## 创建多列文本布局

当文章样式文本应流经多列时，请使用此示例。

1. 创建新的 PDF 文档并配置页边距。
1. 添加标题内容并创建多列`FloatingBox`。
1. 填写文本并保存最终的 PDF。

```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## 创建带有自定义制表位的对齐文本

当文本需要使用制表位位置像简单表格一样对齐时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 使用对齐和引线设置配置制表位。
1. 创建使用这些制表位的文本片段并保存文档。

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
