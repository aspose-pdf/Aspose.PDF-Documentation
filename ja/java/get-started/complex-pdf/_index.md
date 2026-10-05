---
title: "複雑な PDF の作成"
linktitle: "複雑な PDF の作成"
type: docs
weight: 30
url: /ja/java/complex-pdf-example/
description: "Aspose.PDF for Java を使用すると、画像、テキストフラグメント、テーブルを 1 つのファイルに含む、より複雑な PDF ドキュメントを作成できます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した複雑な PDF の作成"
Abstract: この記事では、Aspose.PDF を使用して Java でより複雑な PDF を作成する方法を示します。例では、画像、書式設定された見出し、説明テキストブロック、およびスタイルが適用されたヘッダーセルと生成されたスケジュール行を持つテーブルを追加し、結果を PDF ドキュメントとして保存します。
---
[Hello World の例](/pdf/ja/java/hello-world-example/) では、最もシンプルな PDF 作成手順を説明しています。この例では、そのワークフローを基に、グラフィックス、テキスト、表形式のコンテンツを組み合わせた、より複雑なドキュメントを作成します。

Java で、より複雑な PDF ドキュメントを作成するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. `page.addImage(...)` と対象領域を定義する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を使用して、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に画像を追加してください。
1. 見出し用の [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成し、フォント、サイズ、配置、および [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/) を設定してください。
1. 説明段落用に 2 つ目の [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成してください。
1. 枠線、パディング、およびヘッダーのスタイルを設定した [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成してください。
1. 生成したスケジュール行を [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) に追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) の段落コレクションに追加してください。
1. 出力 PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

次の Java コードは `GetStartedExamples.java` に基づいています。

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

同じ例では、ヘッダーの書式設定と生成された出発時刻を使用してスケジュールテーブルを準備するヘルパーメソッドを使用します。

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
