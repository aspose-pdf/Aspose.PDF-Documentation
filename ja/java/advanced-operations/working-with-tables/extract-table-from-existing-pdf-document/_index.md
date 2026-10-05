---
title: "Java での PDF からテーブルの抽出"
linktitle: "テーブルの抽出"
type: docs
weight: 20
url: /ja/java/extracting-table/
description: "Java で既存の PDF ドキュメントからテーブルデータを抽出する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルからテーブルデータの抽出"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF 文書からテーブルを抽出する方法を説明します。TableAbsorber を使用してページ単位でテーブルを検出し、行とセルを反復処理し、セルのテキストを取得して下流の処理に利用する方法を示します。
---
既存の PDF でテーブル構造を検出し、その内容を読み取る必要がある場合は、`TableAbsorber` を使用してください。

## 検出されたテーブルからテキストの抽出

各ページでテーブルを検出し、セルのテキストを収集する必要がある場合は、この例をご使用ください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 各ページに [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) を適用してください。
1. 吸収されたテーブル、行、セルを反復処理し、抽出されたテキストを出力してください。

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
