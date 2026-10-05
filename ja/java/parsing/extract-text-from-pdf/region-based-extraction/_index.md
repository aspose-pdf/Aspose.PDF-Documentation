---
title: Java を使用した領域ベース抽出
linktitle: 領域ベース抽出
type: docs
weight: 20
url: /ja/java/region-based-extraction/
description: Aspose.PDF for Java を使用して、PDF ドキュメント内の特定のページ領域からテキストを抽出したり、段落のジオメトリを検査したりする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 矩形ページ領域からテキストの抽出

使用 `TextSearchOptions` と `Rectangle` ページ上の定義された領域に抽出を制限する

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 選択されたページ領域からテキストを取得するために。
1. 作成 [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) 対象に対して [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) そして有効にする `setLimitToPageBounds(true)` 抽出が表示ページボックス内に収まるように。
1. 設定した検索オプションを absorber に適用し、対象を訪問します。 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 抽出されたテキストバッファを出力ファイルに書き込んでください。

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## ジオメトリ情報を含む段落の抽出

使用 `ParagraphAbsorber` 抽出されたテキストとともに、セクション矩形と段落ポリゴンを検査するために。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) 対象にアクセスする [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ページマークアップ情報を構築するために。
1. 最初のページマークアップ結果を読み取り、そのセクションと段落を反復処理してください。
1. 各セクションの矩形、段落のポリゴン、およびそれから再構築された段落テキストを [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 行。
1. ジオメトリと抽出されたテキストの詳細を含む出力レポートを作成してください。
1. 抽出された詳細を出力ファイルに書き込んでください。

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
