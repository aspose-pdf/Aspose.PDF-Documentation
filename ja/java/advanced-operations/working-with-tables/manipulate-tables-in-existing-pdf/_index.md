---
title: 既存のPDFでテーブルを操作する
linktitle: テーブルを操作する
type: docs
weight: 30
url: ja/java/manipulate-tables-in-existing-pdf/
description: 既存のPDFファイルのテーブルを操作し、Aspose.PDF for Javaを使用してPDFドキュメント内の古いテーブルを新しいものに置き換えます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFでテーブルを操作する

Aspose.PDF for Javaによってサポートされている最初期の機能の1つは、テーブルを操作する機能であり、最初から生成されたPDFファイルや既存のPDFファイルにテーブルを追加するための優れたサポートを提供します。
 You also get the capability to Integrate Table with Database (DOM) to create dynamic tables based on database contents. In this new release, we have implemented new feature of searching and parsing simple tables that already exist on page of PDF document. A new class named **Aspose.PDF.Text.TableAbsorber** provides these capabilities. The usage of TableAbsorber is very much similar to existing TextFragmentAbsorber class.

以下のコードスニペットは、特定のテーブルセル内のコンテンツを更新する手順を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // 既存のPDFファイルを読み込む
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // テーブルを見つけるためのTableAbsorberオブジェクトを作成する
        TableAbsorber absorber = new TableAbsorber();

        // 最初のページにアブソーバーを訪問
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // ページ上の最初のテーブルにアクセスし、その最初のセルとその中のテキストフラグメントを取得する
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // セル内の最初のテキストフラグメントのテキストを変更する
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## PDFドキュメント内の古いテーブルを新しいテーブルに置き換える

特定のテーブルを見つけて希望のものと置き換える必要がある場合、[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) クラスの Replace() メソッドを使用してそれを行うことができます。

次の例は、PDFドキュメント内のテーブルを置き換える機能を示しています。

```java
public static void ReplaceOldTableWithNew() {

        // 既存のPDFドキュメントを読み込む
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // テーブルを見つけるためのTableAbsorberオブジェクトを作成
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // 吸収器で最初のページを訪問
        absorber.visit(page);

        // ページ上の最初のテーブルを取得
        AbsorbedTable table = absorber.getTableList().get(0);

        // 新しいテーブルを作成
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // 古いテーブルを新しいものに置き換える
        absorber.replace(page, table, newTable);

        // ドキュメントを保存
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```