---
title: JavaでPDFテキストをフォーマットする
linktitle: PDF内のテキスト書式設定
type: docs
weight: 70
url: /ja/java/text-formatting-inside-pdf/
description: JavaでPDFドキュメント内のテキストを、間隔、ノート、リスト、マルチカラムレイアウト、スタイリングオプションを使用してフォーマットする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFファイル内のテキストをフォーマットおよびスタイル設定する。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメント内のテキストを書式設定する方法を説明します。行間、文字間、箇条書きおよび番号付きリスト、脚注と文末脚注、インライン段落コンテンツ、マルチカラムレイアウト、強制ページ改ページ、カスタムタブストップについてカバーしています。
---
Aspose.PDF for Java は、間隔、リスト、注釈、インラインレイアウト、およびマルチカラム構成のためのテキスト書式設定コントロールを提供します。

## シンプルな行間の設定

段落テキストで固定行間の値を使用すべき場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. ソーステキストをロードまたは準備し、作成します `TextFragment`。
1. 行間を設定し、フラグメントをページに追加して、ドキュメントを保存してください。

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

## カスタムフォントを使用した行間モードの比較

同じフォントで異なる書式モードの行間をテストする際は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. カスタムフォントを読み込み、異なる行間モードを持つ2つのフラグメントを準備してください。
1. 両方のフラグメントをページに追加し、PDFを保存してください。

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

## テキストフラグメントで文字間隔の設定

文字間隔の値が異なる同じテキストを表示する場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. ヘルパーメソッドを使用して、複数の間隔値に対してテキストフラグメントを構築してください。
1. フラグメントをページに追加して、ドキュメントを保存してください。

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

## テキスト段落内の文字間隔の設定

文字間隔をバウンドされたテキスト段落内に適用すべき場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 作成する `TextParagraph` ターゲット矩形と折り返しオプションを使用して。
1. スタイルされたテキストフラグメントを追加し、PDFを保存してください。

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

## HTMLで箇条書きリストの作成

HTMLマークアップから順不同リストの書式を生成する必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. HTMLリスト文字列を作成してください。
1. それを…として追加 `HtmlFragment` そしてドキュメントを保存してください。

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

## HTMLで番号付きリストの作成

HTMLマークアップから順序付きリストのフォーマットを生成すべき場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 順序付きHTMLリストの文字列を作成してください。
1. それを…として追加 `HtmlFragment` そしてドキュメントを保存してください。

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

## LaTeXで箇条書きリストの作成

箇条書きの書式設定を TeX マークアップからレンダリングする必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. TeXリスト文字列を用意する `itemize` 環境。
1. それを...として追加 `TeXFragment` そしてPDFを保存してください。

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

## LaTeXで番号付きリストの作成

この例は、順序付きリストの書式設定をTeXマークアップからレンダリングする必要がある場合に使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. TeXリスト文字列を用意する `enumerate` 環境。
1. それを...として追加 `TeXFragment` そしてPDFを保存してください。

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

## テキスト段落を使用した箇条書きリストの作成

プレーンテキストフラグメントから手動の箇条書きリストを作成する必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 構築する `TextParagraph` そして、箇条書きプレフィックス付きのフラグメントを追加してください。
1. 段落をページに追加し、ドキュメントを保存してください。

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

## テキスト段落を含む番号付きリストの作成

プレーンテキストのフラグメントから手動の番号付きリストを作成する必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 構築する `TextParagraph` そして、番号付きのフラグメントを追加してください。
1. 段落をページに追加し、ドキュメントを保存してください。

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

## 基本的な脚注の追加

テキストフラグメントがシンプルな脚注を参照すべき場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. メインのテキストフラグメントを作成し、割り当てます `Note` 脚注として。
1. インライン継続テキストを追加して、ドキュメントを保存してください。

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

## カスタムテキストスタイルで脚注の追加

脚注の内容が独自のフォント、サイズ、カラー設定を使用すべき場合に、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. メインテキストフラグメントを作成し、スタイル付きの脚注を設定してください。
1. ノートを添付してPDFを保存してください。

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

## カスタムマーカー テキストを使用した脚注の追加

目に見える脚注マーカーをカスタムテキストに置き換える必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 脚注をメインテキストフラグメントに割り当て、マーカーテキストを上書きしてください。
1. 残りのコンテンツを追加して、ドキュメントを保存してください。

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

## 脚注の区切り線をカスタマイズする

脚注とページコンテンツを分離する線を明示的にスタイル指定する必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. ページノートのラインスタイルを設定します `GraphInfo`。
1. 脚注付きのテキストフラグメントを追加し、ドキュメントを保存してください。

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

## 画像とテーブルの内容を含む脚注の追加

脚注自体に画像、テキスト、テーブルなどのリッチコンテンツを含める必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 構築する `Note` 画像、インラインテキスト、およびテーブルを含むオブジェクト。
1. それをメインのテキストフラグメントに添付し、ドキュメントを保存してください。

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

## エンドノートの追加

テキスト フラグメントがページ脚注ではなくエンドノート コンテンツを参照すべき場合に、この例を使用します。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. メインテキストフラグメントに文末脚注を割り当て、補足の本文を追加してください。
1. 生成されたエンドノートの内容で文書を保存してください。

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

## カスタムマーカー文字列でエンドノートの追加

エンドノートマーカーがカスタムの表示ラベルを使用すべき場合に、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. メインテキストフラグメントに対してエンドノートを割り当て、そのマーカーテキストを上書きしてください。
1. 残りの文書テキストを追加して、PDFを保存してください。

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

## テーブルの内容を新しいページに強制的に配置する

この例は、書式設定されたコンテンツを明示的に新しいページで開始する必要がある場合に使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. テーブルを作成し、その行を埋めます。
1. テーブルを新しいページで開始するように設定し、ドキュメントを保存してください。

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

## 1つの段落フロー内にインラインコンテンツを混在させる

テキストと画像が同じ段落のフロー内で続くべき場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 最初のテキストフラグメントを追加し、次にインライン画像を、そして別のインラインテキストフラグメントを追加してください。
1. 任意の次の単独段落を追加し、ドキュメントを保存してください。

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

## マルチカラムテキストレイアウトの作成

記事スタイルのテキストを複数列に流す必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページ余白を設定してください。
1. 見出しコンテンツを追加し、マルチカラムを作成する `FloatingBox`。
1. テキストを入力し、最終的な PDF を保存します。

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

## カスタムタブストップを使用した整列したテキストの作成

テキストをタブストップ位置を使用してシンプルな表のように揃える必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. タブストップを、配置とリーダー設定で構成してください。
1. それらのタブストップを使用するテキストフラグメントを作成し、文書を保存してください。

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
