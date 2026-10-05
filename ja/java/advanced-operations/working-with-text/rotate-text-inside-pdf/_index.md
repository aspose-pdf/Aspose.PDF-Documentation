---
title: "Java での PDFテキストの回転"
linktitle: "PDF内のテキストの回転"
type: docs
weight: 50
url: /ja/java/rotate-text-inside-pdf/
description: JavaでPDFドキュメント内のテキストフラグメントと段落を回転する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFドキュメント内のテキストフラグメントと段落を回転する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメント内のテキストを回転させる方法を説明します。個々のテキストフラグメントの回転、回転した行を含む段落の作成、そしてさまざまなレイアウトシナリオに対応した全文テキスト段落の回転方法を示します。
---
Aspose.PDF for Java を使用すると、個々のテキストフラグメントだけでなく、全文テキスト段落も回転させることができます。

## 個々のテキストフラグメントを回転させる

同じ行にある複数のテキストフラグメントが異なる回転角度を使用すべき場合に、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 必要な回転値を持つテキストフラグメントを作成してください。
1. それらに追加します `TextBuilder` そして結果を保存してください。

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

## テキスト段落内の行を回転させる

段落に通常の行と回転した行の両方を含める必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 作成 `TextParagraph` そして、異なる回転設定を持つテキストフラグメントを追加してください。
1. 段落をページに追加し、ドキュメントを保存してください。

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

## 明示的な位置が指定されていない段落フラグメントを回転させる

通常のページ段落フローを通して回転テキストを追加する必要がある場合は、この例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. 異なる回転値を持つ複数のテキストフラグメントを作成してください。
1. それらをページ段落コレクションに追加し、PDFを保存してください。

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

## 段落全体を回転させる

段落全体のブロックを回転させ、各行が共有スタイルを保持する場合にこの例を使用してください。

1. 新しいPDFドキュメントを作成し、ページを追加してください。
1. いくつか構築する `TextParagraph` 段落レベルの回転を持つオブジェクト。
1. 共有ヘルパーメソッドで行を作成し、追加して、ドキュメントを保存してください。

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
