---
title: PDFからテーブルデータを抽出する
linktitle: テーブルデータを抽出
type: docs
weight: 40
url: ja/php-java/extract-data-from-table-in-pdf/
description: Aspose.PDF for PHPを使用してPDFから表形式のデータを抽出する方法を学ぶ
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## プログラムでPDFからテーブルを抽出する

PDFからテーブルを抽出することは、テーブルがさまざまな方法で作成されている可能性があるため、簡単な作業ではありません。

Aspose.PDF for PHP via Javaには、テーブルを簡単に取得するためのツールがあります。テーブルデータを抽出するには、次の手順を実行する必要があります。

1. PDFドキュメントを開く - [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document)オブジェクトをインスタンス化します。
1. ドキュメントからテーブルを抽出するために、TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber)オブジェクトを作成します。
1. ドキュメントの各ページを反復処理します。

1. 分析するページを決定し、目的のページに[visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)を適用します。表形式のデータがスキャンされ、結果は[AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable)のリストに保存されます。このリストは[getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを通じて取得できます。
1. データを取得するには、`TableList`を反復処理し、[absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow)のリストと吸収されたセルのリストを処理します。最初のリストには[getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--)メソッドを呼び出すことでアクセスでき、2番目には[getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--)メソッドを呼び出すことでアクセスできます。

1. 各[AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell)には[TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection)が含まれています。それを自分の目的に応じて処理することができます。

以下の例は、すべてのページからのテーブル抽出を示しています:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();

for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // 行内の各セルを反復処理します。
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // セル内の各テキストフラグメントを反復処理します。
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // テキストフラグメント内の各セグメントを反復処理します。
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// テーブルデータを出力ファイルに保存します。
file_put_contents($outputFile, $responseData);

// PDFドキュメントを閉じます。
$document->close();
```


## PDFからテーブルデータを抽出してCSVファイルに保存

次の例は、テーブルを抽出してCSVファイルとして保存する方法を示しています。
PDFをExcelスプレッドシートに変換する方法については、[PDFをExcelに変換](/pdf/php-java/convert-pdf-to-excel/)の記事を参照してください。

```php

    // Documentクラスを使用して入力PDFドキュメントを読み込みます。
    $document = new Document($inputFile);

    // 保存オプションを指定するためにExcelSaveOptionsクラスのインスタンスを作成します。
    $saveOption = new ExcelSaveOptions();

    // 出力形式をCSVに設定します。
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // 指定された保存オプションを使用して、PDFドキュメントをExcelファイルとして保存します。
    $document->save($outputFile, $saveOption);
```