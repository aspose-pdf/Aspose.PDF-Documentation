---
title: Java を使用した基本テキスト抽出
linktitle: 基本テキスト抽出
type: docs
weight: 10
url: /ja/java/basic-text-extraction/
description: Aspose.PDF を使用して、Java で PDF ドキュメントからすべてのページ、特定のページ、または段落構造ごとにテキストを抽出する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
基本テキスト抽出は、Java で PDF コンテンツを読み取る出発点です。Aspose.PDF は 2 つの一般的なアプローチを提供します:

- 使用 `TextAbsorber` ドキュメントやページからプレーンテキストの結果が必要な場合。
- 使用 `ParagraphAbsorber` ページ、セクション、段落、行、そしてフラグメントのグループ化を保持する必要がある場合。

PDF ページはワードプロセッシング文書のようにテキストを保存しないため、抽出された順序はページのコンテンツストリームとレイアウトに依存します。領域別抽出、ジオメトリの詳細、マルチカラムレイアウト、注釈、ハイライトテキスト、または上付き・下付き文字の検出については、このセクションの関連抽出記事を参照してください。

## すべてのページからテキストの抽出

使用 `TextAbsorber` ドキュメント全体からフラットなテキストストリームを収集し、ファイルに書き込む。これは、読み取り可能なテキストコンテンツだけが必要で、段落の境界や座標が不要な場合に最も簡単なオプションです。

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成する [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 文書全体のテキストを蓄積するために。
1. 呼び出す `document.getPages().accept(textAbsorber)` それで、すべて [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 吸収器によって訪問されます。
1. 抽出されたテキストバッファを出力ファイルに書き込んでください。

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 特定のページからテキストの抽出

必要なページにのみアブゾーバーを適用します。ページ番号は `Document` ページコレクションは1ベースですので `get_Item(1)` 最初のページを読み取ります。

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成する [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 単一ページ抽出用。
1. 呼び出す `accept(textAbsorber)` ターゲット上 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ページ番号で選択されます。
1. 抽出されたテキストバッファを出力ファイルに書き込んでください。

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 段落構造でテキストの抽出

使用 `ParagraphAbsorber` 単一のプレーンテキストストリームではなく構造的なグルーピングが必要な場合。セクション、段落、行、そしてページマークアップを返します。 `TextFragment` オブジェクトは、出力がテキストの論理ブロックを保持しなければならない場合に便利です。

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) を作成し、ドキュメント全体を訪れてページマークアップ結果を構築してください。
1. ページのマークアップ、セクション、段落、行、そして [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) アブサーバーが公開するオブジェクト。
1. 構造的なグルーピングが保持されるように、ページ、セクション、段落の番号付けを明示的に行って出力テキストを構築してください。
1. 抽出された段落テキストを出力ファイルに書き込んでください。

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
