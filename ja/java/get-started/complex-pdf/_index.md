---
title: 複雑なPDFの作成
linktitle: 複雑なPDFの作成
type: docs
weight: 30
url: /ja/java/complex-pdf-example/
description: Aspose.PDF for Java を使用すると、画像、テキストフラグメント、テーブルを1つのファイルに含む、より複雑な PDF ドキュメントを作成できます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して複雑な PDF を作成する
Abstract: この記事では、Aspose.PDF を使用して Java でより複雑な PDF を作成する方法を示します。例では、画像、書式設定された見出し、説明テキストブロック、およびスタイルが適用されたヘッダーセルと生成されたスケジュール行を持つテーブルを追加し、結果を PDF ドキュメントとして保存します。
---
その [こんにちは世界](/pdf/ja/java/hello-world-example/) この例は最もシンプルな PDF 作成パスをカバーしています。この例はそのワークフローを基に、グラフィック、テキスト、表形式のコンテンツを組み合わせた、よりリッチなドキュメントを作成します。

Java で、より複雑な PDF ドキュメントを作成するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 画像を追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) と `page.addImage(...)` およびターゲット [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. ヘッダーを作成する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) フォント、サイズ、配置、そして [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/)。
1. 2番目を作成 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 説明段落用に。
1. 構築する [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 枠線、パディング、ヘッダーのスタイリング付き。
1. 生成されたスケジュール行を追加する [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 追加する [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) に [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 段落。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

以下の Java コードは次のものに基づいています `GetStartedExamples.java`.

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
