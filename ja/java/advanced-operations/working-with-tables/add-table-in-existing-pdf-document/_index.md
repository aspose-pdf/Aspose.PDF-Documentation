---
title: "Java での PDF へのテーブルの追加"
linktitle: テーブルの追加
type: docs
weight: 10
url: /ja/java/adding-tables/
description: "Java で既存の PDF ドキュメントにテーブルを追加し、構成する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントへのテーブルの追加と書式設定"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントにテーブルを追加および構成する方法を説明します。テーブルの作成、罫線、余白、パディング、行および列の結合、AutoFit の動作、セルへの画像挿入、行と列の繰り返し、HTML および LaTeX フラグメント、そして複数ページのレンダリング制御について解説します。
---
Aspose.PDF for Java は、レイアウトおよびコンテンツのカスタマイズが可能な豊富な `Table` API を提供します。

## 基本的なテーブルの作成

シンプルなテーブルで均一な罫線とテキストセルを追加する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、境界線を設定してください。
1. 行とセルを追加し、テーブルをページに添付して、ドキュメントを保存してください。

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 行スパンと列スパンを持つセルの追加

テーブルに行や列をまたがる結合セルが必要な場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、行を追加してください。
1. `ColSpan` と `RowSpan` を対象セルに設定し、PDF を保存してください。

```java
public static void addRowspanOrColspan(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));

        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            row1.getCells().add("Test 1" + cellCount);
        }

        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        Row row4 = table.getRows().add();
        row4.getCells().add("Test 4 1");
        cell = row4.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row4.getCells().add("Test 4 3");
        row4.getCells().add("Test 4 4");

        Row row5 = table.getRows().add();
        row5.getCells().add("Test 5 1");
        row5.getCells().add("Test 5 3");
        row5.getCells().add("Test 5 4");

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## テーブルの罫線とセルのパディングの追加

ボーダー、パディング、およびセルの折り返し動作を設定する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、幅、境界線、パディングを設定してください。
1. 行を追加し、結果の文書を保存してください。

```java
public static void addBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();
        row1.getCells().get_Item(2).getParagraphs().add(new TextFragment("col3 with large text string"));
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## 自動フィットテーブルレイアウトの有効化

テーブルをページの利用可能な幅に自動的に合わせて調整する場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、`ColumnAdjustment.AutoFitToWindow` を設定してください。
1. サンプル行を追加して PDF を保存してください。

```java
public static void autoFit(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## テーブルセルへの画像の追加

テーブルがセルの1つにラスター画像コンテンツを表示する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、テキストと画像のセルを含む行を追加してください。
1. [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) のサイズを設定し、ドキュメントを保存してください。

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");

        Row row = table.getRows().add();
        row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
        Image image = new Image();
        image.setFile(imageFile.toString());
        image.setFixWidth(50);
        image.setFixHeight(50);
        row.getCells().add().getParagraphs().add(image);

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## テーブルセル内に SVG 画像の追加

テーブルが SVG ファイルを行ごとにレンダリングする必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、SVG ファイルを反復処理してください。
1. 画像ごとに 1 行を追加し、SVG を [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) に設定して、PDF を保存してください。

```java
public static void addSvgImage(List<Path> imageFiles, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");
        for (Path imageFile : imageFiles) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
            Image image = new Image();
            image.setFileType(ImageFileType.Svg);
            image.setFile(imageFile.toString());
            image.setFixWidth(50);
            image.setFixHeight(50);
            row.getCells().add().getParagraphs().add(image);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## HTML フラグメントをテーブルセルに追加

テーブルの内容にインライン HTML 書式を含める必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、境界線を設定してください。
1. [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) オブジェクトをセルに追加し、ドキュメントを保存してください。

```java
public static void addHtmlFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <strong>(" + rowCount + ", 1)</strong>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + rowCount + ", 2)</span>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + rowCount + ", 3)</span>"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## テーブルセルに LaTeX フラグメントの追加

テーブルの内容に TeX または LaTeX 式をレンダリングする必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. ボーダー付きの [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成してください。
1. [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) オブジェクトをセルに配置し、出力ファイルを保存してください。

```java
public static void addLatexFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\mathbf{(" + rowCount + ", 1)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\textcolor{red}{(" + rowCount + ", 2)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\underline{(" + rowCount + ", 3)}$"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## テーブルの新しいページに強制的への配置

大きなテーブルの後、2番目のテーブルを別のページで開始する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページ設定を構成してください。
1. 最初の大きな [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を構築し、それをページに追加してください。
1. 2番目のテーブルを作成し、`InNewPage` を設定して、ドキュメントを保存してください。

```java
public static void addTableOnNewPage(Path outputFile) {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(37);
        document.getPageInfo().getMargin().setRight(37);
        document.getPageInfo().getMargin().setTop(37);
        document.getPageInfo().getMargin().setBottom(37);
        document.getPageInfo().setLandscape(true);

        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("50 100");
        for (int i = 1; i < 121; i++) {
            Row row = table.getRows().add();
            row.setFixedRowHeight(15);
            row.getCells().add().getParagraphs().add(new TextFragment("Content 1"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 2"));
        }
        page.getParagraphs().add(table);

        Table table1 = new Table();
        table1.setColumnWidths("100 100");
        for (int i = 1; i < 11; i++) {
            Row row = table1.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment("Content 3"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 4"));
        }
        table1.setInNewPage(true);
        page.getParagraphs().add(table1);
        document.save(outputFile.toString());
    }
}
```

## 繰り返し列を含む縦方向に分割されたテーブルの作成

幅広いテーブルを縦方向に続け、キー列を繰り返す場合はこの例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、繰り返し列で垂直ブレークを設定してください。
1. ヘッダーとデータ行を追加し、ドキュメントを保存してください。

```java
public static void addTableHideBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));
        table.setRepeatingColumnsCount(2);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        Cell cell = row.getCells().add("header 1");
        cell.setColSpan(2);
        cell.setBackgroundColor(Color.getLightGray());
        row.getCells().add("header 3");
        Cell cell2 = row.getCells().add("header 4");
        cell2.setColSpan(2);
        cell2.setBackgroundColor(Color.getLightBlue());
        row.getCells().add("header 6");
        Cell cell3 = row.getCells().add("header 7");
        cell3.setColSpan(2);
        cell3.setBackgroundColor(Color.getLightGreen());
        Cell cell4 = row.getCells().add("header 9");
        cell4.setColSpan(3);
        cell4.setBackgroundColor(Color.getLightCoral());
        for (int i = 12; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 0; rowCounter < 3; rowCounter++) {
            Row row1 = table.getRows().add();
            for (int i = 1; i < 18; i++) {
                row1.getCells().add("col " + rowCounter + ", " + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 枠線とパディングの例の再利用

マージンとパディングのシナリオで共有ボーダーの例に委任すべき場合は、このヘルパーを使用してください。

1. 既存のテーブルのボーダーとパディングのメソッドを呼び出してください。
1. コードを重複させずに、同じテーブルレイアウトロジックを再利用してください。

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## 角が丸いテーブルの作成

テーブルが標準の長方形の枠ではなく、角が丸いスタイルを使用すべき場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、丸みを帯びた枠線設定を構成してください。
1. テーブルに行を追加し、PDF を保存してください。

```java
public static void createTableWithRoundCorner(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        BorderInfo borderInfo = new BorderInfo(BorderSide.All);
        borderInfo.setRoundedBorderRadius(15);
        table.setCornerStyle(BorderCornerStyle.Round);
        table.setBorder(borderInfo);
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 繰り返しヘッダー行の追加

マルチページテーブルでヘッダー行を各続きページに繰り返す必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. 垂直方向に分割される [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、繰り返し行数とスタイルを設定してください。
1. ヘッダー行とデータ行を追加し、ドキュメントを保存してください。

```java
public static void addRepeatingRows(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setRepeatingRowsCount(2);
        TextState textState = new TextState();
        textState.setFontSize(12);
        textState.setFont(FontRepository.findFont("TimesNewRoman"));
        textState.setForegroundColor(Color.getRed());
        table.setRepeatingRowsStyle(textState);
        table.setColumnWidths("100 100 100");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getBlack()));

        Row headerRow1 = table.getRows().add();
        headerRow1.getCells().add("Header 1-1");
        headerRow1.getCells().add("Header 1-2");
        headerRow1.getCells().add("Header 1-3");
        for (Cell cell : headerRow1.getCells()) {
            cell.setBackgroundColor(Color.getLightGray());
        }
        Row headerRow2 = table.getRows().add();
        headerRow2.getCells().add("Header 2-1");
        headerRow2.getCells().add("Header 2-2");
        headerRow2.getCells().add("Header 2-3");
        for (Cell cell : headerRow2.getCells()) {
            cell.setBackgroundColor(Color.getLightBlue());
        }
        for (int i = 1; i < 101; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Data " + i + "-1");
            row.getCells().add("Data " + i + "-2");
            row.getCells().add("Data " + i + "-3");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 幅の広いテーブルに繰り返し列の追加

テーブルが同じページ内で垂直に分割され、最初の列が繰り返される必要がある場合に、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページサイズを設定してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、繰り返し列と自動調整動作を設定してください。
1. ヘッダーとデータ行を追加し、PDF を保存してください。

```java
public static void addRepeatingColumns(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(PageSize.getA5().getHeight(), PageSize.getA5().getWidth());
        BorderInfo border = new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray());
        Table table = new Table();
        table.setBroken(TableBroken.VerticalInSamePage);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
        table.setRepeatingColumnsCount(5);
        table.setBorder(border);
        table.setDefaultCellBorder(border);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        for (int i = 1; i < 6; i++) {
            Cell cell = row.getCells().add("header " + i);
            cell.setBackgroundColor(Color.getLightGray());
        }
        for (int i = 6; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 1; rowCounter < 6; rowCounter++) {
            row = table.getRows().add();
            for (int i = 1; i < 6; i++) {
                Cell cell = row.getCells().add("cell " + rowCounter + "," + i);
                cell.setBackgroundColor(Color.getLightGray());
            }
            for (int i = 6; i < 18; i++) {
                row.getCells().add("cell " + rowCounter + "," + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## テーブルの行の間に改ページの挿入

特定のテーブル行が新しいページで開始される必要がある場合に、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) を作成し、多くの行を追加してください。
1. 選択した行に `InNewPage` を設定し、ドキュメントを保存してください。

```java
public static void insertPageBreak(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setColumnWidths("100 100");
        for (int counter = 0; counter < 201; counter++) {
            Row row = new Row();
            table.getRows().add(row);
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            if (counter % 10 == 0 && counter != 0) {
                row.setInNewPage(true);
            }
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## テーブルセル内のテキストを回転させる

セルのテキストを異なる回転角度で表示する必要がある場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、複数のセルを含む行を追加してください。
1. 回転させた [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) オブジェクトを作成し、セルに追加して PDF を保存してください。

```java
public static void rotatedTextTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        Row row = table.getRows().add();
        row.setMinRowHeight(200);
        for (int cellCount = 0; cellCount < 4; cellCount++) {
            Cell cell = row.getCells().add();
            TextFragment textFragment = new TextFragment("Cell 1 " + (cellCount - 1));
            textFragment.getTextState().setRotation(90 * cellCount);
            textFragment.setHorizontalAlignment(HorizontalAlignment.Center);
            cell.getParagraphs().add(textFragment);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
