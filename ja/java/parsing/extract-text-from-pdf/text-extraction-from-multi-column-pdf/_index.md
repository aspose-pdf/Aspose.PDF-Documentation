---
title: マルチカラムPDFからのテキスト抽出の改善
linktitle: マルチカラムPDFからのテキスト抽出
type: docs
weight: 30
url: /ja/java/text-extraction-from-multi-column-pdf/
description: Aspose.PDF for Java を使用して、マルチカラムPDFレイアウトからのテキスト抽出を改善するテクニックを学びましょう。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
マルチカラムレイアウトは、読み順と抽出品質を向上させるために、追加の処理が必要になることがよくあります。

## フォントサイズを縮小した後にテキストの抽出

この手法はテキストフラグメントのフォントサイズを更新し、調整されたドキュメントをメモリに保存し、そして変換された結果からテキストを抽出します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) すべてのドキュメントページを訪問して収集する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) オブジェクト。
1. フラグメントを反復処理し、要求された比率でそれぞれのフォントサイズを縮小し、抽出前に密な列レイアウトを正規化できるようにしてください。
1. 調整されたものを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) メモリ内バイトストリームに。
1. 2番目を再度開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そのメモリ バッファから。
1. 作成 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)、変換されたドキュメントのすべてのページを訪問し、抽出されたテキストを出力ファイルに書き込んでください。

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## スケールファクターでテキストの抽出

使用 `TextExtractionOptions` 純粋なフォーマットモードで、列が多いレイアウトのスケール係数を調整します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) フルドキュメント抽出のために。
1. 作成 [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) 純粋なフォーマットモードで、レイアウトに敏感な抽出動作が使用されます。
1. ページを訪問する前に、スケールファクターを設定し、抽出オプションをアブソーバーに適用してください。
1. すべてのドキュメントページを訪問し、抽出されたテキストを出力ファイルに書き込みます。

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
