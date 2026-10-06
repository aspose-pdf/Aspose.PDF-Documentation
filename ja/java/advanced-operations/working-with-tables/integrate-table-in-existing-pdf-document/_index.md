---
title: "Java での PDF テーブルとデータソースの統合"
linktitle: "テーブルの統合"
type: docs
weight: 30
url: /ja/java/integrate-table/
description: "Java で、CSV ファイルなどの構造化データソースと PDF テーブルを統合する方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での構造化データを使用した PDF テーブルの構築"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF テーブルを外部データと統合する方法を説明します。CSV データの読み取り、特定の列の選択、解析された行からスタイル付き Table オブジェクトの構築、および結果を PDF ドキュメントにレンダリングする手順をカバーしています。"
---
この Java の例では、外部のデータフレームライブラリに依存せずに CSV データから PDF テーブルを構築します。

## CSV 行を使用したテーブルの構築

選択した CSV 列をスタイル付き PDF テーブルに変換する必要がある場合は、この例を使用してください。

1. [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) オブジェクトを作成し、その境界線を設定してください。
1. CSV のヘッダー行から必要な列インデックスを検出してください。
1. ヘッダー行と要求されたデータ行数を追加して、テーブルを返してください。

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## CSV データから PDF の作成

CSV 入力を PDF テーブル文書としてレンダリングする必要がある場合は、この例を使用してください。

1. 入力ファイルから CSV 行を読み取ってください。
1. コンソールで解析された行のサブセットをプレビューしてください。
1. PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、生成されたテーブルを追加して、出力ファイルを保存してください。

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## 名前で CSV 列インデックスを見つける

特定の名前付き列を CSV ヘッダー行で見つける必要がある場合は、このヘルパーを使用してください。

1. 要求された列名を反復処理してください。
1. ヘッダー行で一致するインデックスを検索してください。
1. 収集された列位置を返してください。

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## ファイルから CSV 行を読み取る

テーブル生成前に CSV ソースをメモリにロードする必要がある場合は、このヘルパーを使用してください。

1. 入力ファイルからすべての行を読み取ってください。
1. CSV パーサーヘルパーで各行を分割してください。
1. 収集した行の値を返してください。

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## CSV の 1 行の値への分割

CSV 行に引用符で囲まれた値やエスケープされた引用符文字が含まれる可能性がある場合は、このヘルパーを使用してください。

1. 行の文字を順に走査してください。
1. パーサーが現在引用テキスト内にいるかどうかを追跡してください。
1. 最終的な値リストを構築し、配列として返してください。

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
