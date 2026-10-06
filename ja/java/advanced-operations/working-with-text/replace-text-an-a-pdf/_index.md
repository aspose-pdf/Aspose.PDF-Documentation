---
title: "Java での PDF のテキストの置換"
linktitle: "PDF のテキストの置換"
type: docs
weight: 40
url: /ja/java/replace-text-in-pdf/
description: "Java を使用して、PDF ドキュメント内のテキストを置換、再配置、削除する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: "Java を使用して PDF のテキストコンテンツの置換、削除、調整"
Abstract: "この記事では、Aspose.PDF for Java を使用した PDF ドキュメントのテキスト置換ワークフローについて説明します。すべてのページでテキストを置換する方法、選択した領域に置換を限定する方法、置換レイアウトの調整、正規表現ベースのマッチングの使用、フォントの置換、すべてのテキストの削除、および非表示テキストの削除についてカバーしています。"
---
Aspose.PDF for Java は、`TextFragmentAbsorber` および置換オプションを通じて、シンプルな置換とレイアウト認識置換機能の両方を提供します。

## すべてのページのテキストを置き換える

同じフレーズを文書全体で置き換える必要がある場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を使用して、すべてのページで対象フレーズを検索してください。
1. 一致したテキストを置き換えて、更新された PDF を保存してください。

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

## 特定のページ領域のテキストの置換

この例は、置換が 1 ページの選択した矩形に限定される場合に使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextSearchOptions` を設定し、ページ境界と対象矩形を指定してください。
1. その領域内の一致したテキストを置換し、ドキュメントを保存してください。

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

## シフトされた矩形内のテキストを置換し、間隔の調整

置換テキストをページ上に残し、間隔を調整するがフォントサイズは変更しない場合は、この例を使用してください。

1. ソース PDF を開き、対象ページからテキストフラグメントを収集してください。
1. 置換矩形を変更し、`AdjustSpaceWidth` 行動を選択してください。
1. 新しいテキストを設定し、ドキュメントを保存してください。

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

## 大きな段落矩形の内部のテキストの置換

置換テキストがより大きなページ領域に拡張されるべき場合は、この例を使用してください。

1. ソース PDF を開き、対象ページから最初のテキスト フラグメントを取得してください。
1. ページのメディアボックスから、より大きな置換矩形を構築してください。
1. 置換オプションを適用し、PDF を保存してください。

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

## テキストを置き換え、フォントを拡大して矩形を埋める

置換テキストを拡大してターゲット領域を埋める必要がある場合は、この例を使用してください。

1. ソース PDF を開き、対象のテキストフラグメントにアクセスしてください。
1. 置換矩形を定義し、`ScaleToFill` フォント調整を有効にしてください。
1. 新しいテキストを設定し、更新されたドキュメントを保存してください。

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

## テキストの置換と縮小によるフィット

置換テキストを元のテキスト矩形の内部に保つ必要がある場合は、この例を使用してください。

1. ソース PDF を開き、対象フラグメントを選択してください。
1. 現在のフラグメント矩形を再利用し、`ShrinkToFit` を有効にしてください。
1. テキストを置き換え、ドキュメントを保存してください。

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

## 正規表現によるテキスト置換

この例は、マッチしたテキストを正規表現パターンで見つけ、置換時に再スタイルする必要がある場合に使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 正規表現対応の `TextFragmentAbsorber` を使用してページを検索してください。
1. 各一致項目を置換し、テキストスタイルを更新して、結果を保存してください。

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

## プレースホルダーのテキストを置き換えてページを再配置

ページレイアウトを保持しながら、プレースホルダーを実際の長い値に置き換える必要がある場合は、この例を使用してください。

1. ソース PDF を開き、プレースホルダー テキストを検索してください。
1. 置換テキストを割り当て、そのフォント設定を更新してください。
1. レイアウトが再計算されるように文書を保存してください。

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

## フォントを別のフォントに置き換える

特定の埋め込みフォントを使用しているテキストを別のフォントに切り替える必要がある場合は、この例をご利用ください。

1. ソース PDF を開き、すべてのテキストフラグメントを収集してください。
1. 各フラグメントのフォント名を確認し、対象のフォントを置き換えてください。
1. 更新された PDF を保存してください。

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

## フォントの置き換えと未使用フォントリソースの削除

フォント置換後に文書をクリーンアップする必要がある場合は、この例を使用してください。

1. ソース PDF を開き、`TextEditOptions` を設定して未使用のフォントを削除してください。
1. テキストフラグメントを吸収し、置換フォントを割り当ててください。
1. 最適化されたドキュメントを保存してください。

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

## 文書からすべてのテキストの削除

すべてのページからすべてのテキストコンテンツを削除する必要がある場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を作成し、`removeAllText(document)` を呼び出してください。
1. クリーンアップされた PDF を保存してください。

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## 1 ページからすべてのテキストの削除

この例は、特定のページからのみすべてのテキストを削除する場合に使用します。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を作成し、対象ページからテキストを削除してください。
1. 更新されたドキュメントを保存してください。

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## 選択した矩形からテキストの削除

テキストを選択したページ領域内でのみ削除する場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を作成し、クリアする矩形を定義してください。
1. その領域のテキストを削除し、文書を保存してください。

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## 隠しテキストの削除

この例は、不可視のテキストフラグメントを PDF から削除する必要がある場合に使用してください。

1. ソース PDF を開き、すべてのテキストフラグメントを吸収してください。
1. 各フラグメントの不可視テキスト状態を確認してください。
1. 非表示テキストをクリアし、ドキュメントを保存してください。

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
