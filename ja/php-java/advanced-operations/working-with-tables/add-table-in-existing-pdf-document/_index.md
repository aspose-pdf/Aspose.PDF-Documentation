---
title: PDFにテーブルを作成または追加する
linktitle: テーブルを作成または追加する
type: docs
weight: 10
url: ja/php-java/add-table-in-existing-pdf-document/
description: PDFドキュメントにテーブルを作成または追加し、セルスタイルを適用し、ページ上でテーブルを分割し、行と列をカスタマイズする方法を学びます。
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFドキュメントにテーブルを追加する

Aspose.PDF for PHPを使用して既存のPDFファイルにテーブルを追加するには、以下の手順を実行します。

1. ソースファイルを読み込む。
1. テーブルを初期化する
1. テーブルの枠線の色をLightGrayに設定する
1. テーブルセルの枠線を設定する
1. 10行を追加するループを作成する
1. 入力ドキュメントの最初のページにテーブルオブジェクトを追加する
1. ファイルを保存する。

以下のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);        
    // Tableの新しいインスタンスを初期化する
    $table = new Table();
    $colors= new Color();
    // テーブルの枠線の色をLightGrayに設定する
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // テーブルセルの枠線を設定する
    $table->setDefaultCellBorder($borderInfo);
    // 10行を追加するループを作成する
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // テーブルに行を追加する
        $row = $table->getRows()->add();
        // テーブルセルを追加する
        $row->getCells()->add("列 (" . $row_count . ", 1)");
        $row->getCells()->add("列 (" . $row_count . ", 2)");
        $row->getCells()->add("列 (" . $row_count . ", 3)");
    }
    // 入力ドキュメントの最初のページにテーブルオブジェクトを追加する
    $document->getPages()->add()->getParagraphs()->add($table);

    // 結果のPDFドキュメントを保存する。    
    $document->save($outputFile);
    $document->close();
```