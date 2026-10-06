---
title: マルチカラムPDFからのテキスト抽出の改善
linktitle: マルチカラムPDFからのテキスト抽出
type: docs
weight: 30
url: /ja/java/text-extraction-from-multi-column-pdf/
description: Aspose.PDF for Java を使用して、マルチカラムPDFレイアウトからのテキスト抽出を改善するテクニックを学びましょう。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
マルチカラムレイアウトは、読み順と抽出品質を向上させるために、追加の処理が必要になることがよくあります。

## フォントサイズを縮小した後のテキストの抽出

この手法は、テキストフラグメントのフォントサイズを更新し、調整されたドキュメントをメモリに保存した後、変換された結果からテキストを抽出します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) を作成し、すべてのドキュメントページを訪問して [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) オブジェクトを収集してください。
1. フラグメントを反復処理し、要求された比率で各フォントサイズを縮小してください。これにより、抽出前に密な列レイアウトを正規化できます。
1. 調整された [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) をメモリ内バイトストリームに保存してください。
1. そのメモリバッファから、2番目の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を再度開いてください。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) を作成し、変換されたドキュメントのすべてのページを訪問して、抽出されたテキストを出力ファイルに書き込んでください。

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

`TextExtractionOptions` を純粋なフォーマットモードで使用し、列が多いレイアウトのスケール係数を調整してください。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) を全ドキュメント抽出用に作成してください。
1. [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) を純粋なフォーマットモードで作成し、レイアウトに敏感な抽出動作が使用されるようにしてください。
1. ページを訪問する前に、スケールファクターを設定し、抽出オプションをアブソーバーに適用してください。
1. すべてのドキュメントページを訪問し、抽出されたテキストを出力ファイルに書き込んでください。

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
