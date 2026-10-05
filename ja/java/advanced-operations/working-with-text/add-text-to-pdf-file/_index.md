---
title: "Java での PDFにテキストの追加"
linktitle: "PDFにテキストの追加"
type: docs
weight: 10
url: /ja/java/add-text-to-pdf-file/
description: JavaでPDFドキュメントにテキスト、HTMLフラグメント、リスト、リンク、カスタムフォントを追加する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使ってPDFファイルにテキスト、リンク、HTML、フォントを追加する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントにテキストを追加し、スタイル設定する方法を説明します。シンプルなテキスト挿入、段落レイアウト、ハイパーリンク、右から左へのテキスト、フォントスタイル設定、透明度、ボーダー、HTML および LaTeX フラグメント、グラデーションテキスト、そしてファイルまたはストリームからロードするカスタムフォントについてカバーしています。
---
Aspose.PDF for Java はプレーンテキストの挿入、**高度なレイアウト**、スタイリング、グラデーション、HTML、LaTeX、カスタムフォントをサポートしています。

## シンプルなテキストフラグメントの追加

短いテキスト文字列を固定ページ座標に配置する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. `TextFragment` を作成し、位置を設定してください。
1. それをページに追加して、ドキュメントを保存してください。

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

## 矩形内に段落の追加

大きなテキストブロックを限定された領域内に流し込む必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. ソーステキストを読み込み、構成します `TextParagraph` 長方形と折り返しモード。
1. フラグメントを通じて追加する `TextBuilder` そしてPDFを保存してください。

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

## インデント設定が異なる段落の追加

最初の行とそれ以降の行で異なるインデントルールを使用する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 共有テキストフラグメントを準備し、複数作成します `TextParagraph` オブジェクト。
1. 各段落のインデントを設定し、それらを追加して、文書を保存してください。

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

## 手動改行でテキストの挿入

この例は、テキスト フラグメントが明示的な改行を含む必要がある場合に使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成する `TextFragment` 改行を含み、そのスタイルを設定してください。
1. それを...で追加する `TextParagraph` そしてPDFを保存してください。

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

## 検出された改行の検査

テキストレイアウトと行折り返しに関する通知出力を確認する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、通知ログを有効にしてください。
1. ページにいくつかの長いテキストフラグメントを追加してください。
1. 通知を確認し、ドキュメントを保存してください。

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

## テキストの幅を動的に測定する

レイアウトの決定を行う前に文字や文字列の幅を測定すべき場合は、この例を使用してください。

1. 対象フォントを解決し、作成します `TextState`.
1. 文字を測定し、フォントおよびテキストステート API の結果を比較します。
1. 検証のために不一致を出力してください。

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

## ハイパーリンクセグメント付きのテキストの追加

テキストフラグメントの一部がウェブリンクとして機能する場合に、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. ビルド `TextFragment` いくつかの `TextSegment` オブジェクト。
1. 対象セグメントにハイパーリンクとスタイルを割り当て、ドキュメントを保存してください。

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

## 右から左のテキストの追加

この例は、ドキュメントが右から左へのスクリプトコンテンツを適切に配置して表示する必要がある場合に使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成する `TextFragment` ターゲットのRTLテキストとともに、フォントと配置を設定してください。
1. ページに追加してPDFを保存してください。

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

## スタイル付きテキストと数式のようなセグメントの追加

通常のテキストと下付き文字のようなセグメントが、1つの出力で異なるテキスト状態を使用すべき場合に、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. メインのスタイル付きフラグメントを作成し、ヘルパーセグメントで式を組み立てます。
1. 両方のフラグメントをページに追加し、ドキュメントを保存してください。

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

## 下線付きのテキストの追加

テキストフラグメントに下線スタイルを明示的に適用したい場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. テキストフラグメントを作成し、フォントと下線の状態を設定し、位置を指定してください。
1. それに付け加えて `TextBuilder` そして結果を保存してください。

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

## 色付きのシェイプの上に透明なテキストの追加

テキストを背景グラフィックの上に透明で表示させる必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 背景の形状を描画し、半透明のテキストフラグメントを作成してください。
1. 両方の要素をページに追加し、ドキュメントを保存してください。

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

## 不可視テキストの追加

検索可能または非表示のテキストが可視的なレンダリングなしで存在すべき場合に、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 表示されるテキストフラグメントを追加し、非表示フラグが有効な2番目のフラグメントも追加してください。
1. 文書を保存してください。

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

## 矩形の枠でテキストの追加

テキストを境界矩形と一緒に描画する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. スタイル付きの作成 `TextFragment` テキスト矩形の枠線の描画を有効にしてください。
1. それに付け加えて `TextBuilder` そしてPDFを保存してください。

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

## 取り消し線テキストの追加

テキストが取り消し線の書式を使用すべき場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. ストライクアウトが有効なスタイル付きテキストフラグメントを作成してください。
1. ページに追加して、ドキュメントを保存してください。

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

## テキストに軸方向のグラデーションシェーディングを適用する

テキストが単色ではなく線形グラデーション塗りつぶしを使用すべき場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. テキストフラグメントを作成し、その前景色に軸方向グラデーションを割り当てます。
1. ページに追加してPDFを保存してください。

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

## テキストに放射状グラデーションのシェーディングを適用する

テキストに放射状グラデーション塗りを使用する場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. テキストフラグメントを作成し、その前景色に放射型グラデーションを割り当てます。
1. それをページに追加して、ドキュメントを保存してください。

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

## インラインHTMLスタイルの書式付きテキストの追加

上付き文字および下付き文字の書式をHTMLマークアップで挿入する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成する `HtmlFragment` 必要なインラインマークアップを使用して。
1. ページに追加してPDFを保存してください。

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

## LaTeX テキストフラグメントの追加

数式や TeX 形式のコンテンツを PDF 内にレンダリングする必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成する `TeXFragment` 必要な式を使用して。
1. それをページに追加して、ドキュメントを保存してください。

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

## リッチHTMLフラグメントの追加

ページが見出し、段落、リンクなどの構造化されたHTMLコンテンツをレンダリングする必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. HTMLコンテンツ文字列を準備し、作成 `HtmlFragment`.
1. ページに追加してPDFを保存してください。

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

## 上書きされたテキスト状態を持つHTMLフラグメントの追加

インポートされたHTMLコンテンツが制御されたフォントとカラー設定を継承すべき場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. HTML コンテンツを準備し、作成する `HtmlFragment`.
1. カスタムを割り当てる `TextState`、フラグメントを追加し、ドキュメントを保存してください。

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

## ファイルから読み込んだカスタムフォントの使用

テキストがフォントファイルのパスから直接ロードされたフォントを使用すべき場合は、この例を使用してください。

1. カスタムフォントファイルのパスを解決する。
1. テキストフラグメントを作成し、フォントを通じてロードします `FontRepository.openFont`。
1. フォント設定を適用し、ドキュメントを保存してください。

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

## ストリームからロードしたカスタムフォントの使用

カスタムフォントをストリームから開き、PDF に埋め込む必要がある場合は、この例を使用してください。

1. フォントファイルをストリームとして開き、ロードします `FontRepository`。
1. テキストフラグメントを作成し、埋め込みフォントを割り当てます。
1. フラグメントをページに追加し、ドキュメントを保存してください。

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
