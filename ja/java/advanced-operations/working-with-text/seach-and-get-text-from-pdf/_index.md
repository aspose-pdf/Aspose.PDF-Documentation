---
title: "Java で PDF テキストを検索および抽出"
linktitle: テキストを検索して取得
type: docs
weight: 60
url: /ja/java/search-and-get-text-from-pdf/
description: "Java で PDF ドキュメントからテキストを検索・検査・抽出する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF テキストを検索し、抽出されたフラグメントの検査"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントからテキストを検索および抽出する方法を説明します。TextAbsorber および TextFragmentAbsorber を取り上げ、領域ベースの抽出、ページ単位の検索、正規表現およびフレーズマッチ、ハイパーリンクの挿入、スタイル化テキストの検査、フラグメントのハイライトを含みます。"
---
Aspose.PDF for Java は、座標、スタイル、および正規表現マッチングを使用した生テキスト抽出およびフラグメントレベルの検索をサポートしています。

## TextAbsorber を使用したすべてのページからテキストの抽出

すべてのページで選択した文書領域からプレーンな抽出テキストが必要な場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextExtractionOptions` および地域ベースの `TextSearchOptions` を作成してください。
1. `TextAbsorber` をすべてのページで実行し、抽出されたテキストを出力してください。

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

## TextAbsorber を使用した 1 ページからのテキスト抽出

プレーンテキスト抽出を 1 ページに制限すべき場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 対象領域でテキスト抽出および検索オプションを構成してください。
1. `TextAbsorber` を選択したページで実行し、結果を出力してください。

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

## ドキュメント内のすべてのテキストフラグメントの検査

フォント、位置、カラーのメタデータとともにテキストコンテンツが必要な場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を全ページにわたって実行してください。
1. フラグメントを反復処理し、それらのメタデータを出力してください。

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

## 特定のページでフレーズの検索

対象の単語が選択したページのみで見つかる必要がある場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 対象のフレーズを指定して `TextFragmentAbsorber` を作成してください。
1. 選択したページを検索し、一致するフラグメントの位置を出力してください。

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

## ページをまたぐシーケンシャル検索の継続

この例は、ページ検索を次へ移動しながら 1 つの absorber を再利用したい場合に使用してください。

1. ソース PDF ドキュメントを開き、再利用可能な absorber を作成してください。
1. 最初のページを検索し、結果を検査してください。
1. 追加ページの検索を続行し、更新された一致結果を確認してください。

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

## 選択した長方形内でフレーズを検索

フレーズマッチングを1ページの領域に限定すべき場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. `TextFragmentAbsorber` を、対象フレーズと矩形ベースの `TextSearchOptions` を指定して作成してください。
1. ページを訪問し、一致したフラグメントの位置を出力してください。

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

## 正規表現でテキストを検索

正規表現パターンで一致を検索すべき場合、固定フレーズではなくこの例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 正規表現対応の `TextFragmentAbsorber` を作成してください。
1. 対象ページを訪問し、一致するフラグメントを出力してください。

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

## 正規表現パターンでフレーズのリストの検索

複数の対象フレーズを一度に検索する必要がある場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 正規表現パターンの配列を作成し、それを `TextFragmentAbsorber` に渡してください。
1. ドキュメントを開き、グループ化された正規表現の結果を確認してください。

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

## テキストを検索してハイパーリンクに変換

一致した単語をハイライトし、クリック可能なリンクに変換する場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 正規表現検索を有効にして対象語を検索してください。
1. テキストのスタイルを更新し、ハイパーリンクを添付して、変更された PDF を保存してください。

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

## スタイル特性でテキストを検索

太字や不可視テキストなどの書式に基づいてフラグメントを検査する必要がある場合は、この例を使用してください。

1. ソース PDF ドキュメントを開いてください。
1. 対象ページ上で `TextFragmentAbsorber` を実行してください。
1. 各フラグメントスタイルをチェックし、一致するエントリを出力してください。

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

## レンダリングされたページプレビューでの検索結果のハイライト

テキストの一致をレンダリングされたページ画像と関連付けて視覚的に検査する必要がある場合は、この例をご使用ください。

1. 必要な解像度で PNG デバイスを作成してください。
1. 各ページを `TextFragmentAbsorber` で検索し、ページを画像ストリームにレンダリングしてください。
1. ページプレビュー画像を書き出し、検査のためにフラグメント座標を出力してください。

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
