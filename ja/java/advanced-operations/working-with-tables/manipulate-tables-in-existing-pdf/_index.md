---
title: "既存のPDFドキュメント内のテーブルの操作"
linktitle: "テーブルの操作"
type: docs
weight: 40
url: /ja/java/manipulating-tables/
description: Javaを使用して既存のPDFドキュメント内のテーブルを検査および変更する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで既存のPDFテーブルを検査および変更する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに既に存在するテーブルを操作する方法を説明します。TableAbsorber を使用したテーブルの検索、セル内テキストの更新、検出されたテーブルを新しい Table オブジェクトに置き換える方法を取り上げます。
---
使用 `TableAbsorber` 既存のテーブルを検索し、その内容を更新する必要がある場合。

## テーブルセル内のテキストの置換

検出されたセル内のテキストを、テーブル全体を再構築せずに更新する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、次のページにアクセスします [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)。
1. 対象のテーブルとセルのテキストフラグメントが存在することを検証してください。
1. セルのテキストを置換し、更新されたドキュメントを保存してください。

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## 検出されたテーブルを新しいテーブルに置き換える

元のテーブルを新しく作成したテーブルで完全に置き換える必要がある場合は、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、ページ上のテーブルを検出してください。
1. 新しいものを作成する [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 望ましい構造で。
1. 吸収されたテーブルを置き換えて、出力 PDF を保存してください。

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
