---
title: 既存のPDFからテーブルを削除
linktitle: テーブルを削除
type: docs
weight: 40
url: /java/remove-tables-from-existing-pdf/
description: Aspose.PDF for Javaを使用すると、PDFドキュメントからテーブルおよび複数のテーブルを削除できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF for Javaは、PDFドキュメントを最初から生成する際に、PDFドキュメント内にテーブルを挿入/作成する機能を提供します。また、任意の既存のPDFドキュメントにテーブルオブジェクトを追加することもできます。しかし、既存のPDFに含まれるテーブルセルの内容を更新できる[既存PDFのテーブルを操作する](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/)必要があるかもしれません。しかし、既存のPDFドキュメントからテーブルオブジェクトを削除する必要が生じることがあります。

{{% /alert %}}

テーブルを削除するには、既存のPDFのテーブルを取得するために[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber)クラスを使用し、次に[Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-)メソッドを呼び出す必要があります。

## PDFドキュメントからテーブルを削除する

既存の[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber)クラスに新しい関数、すなわちRemove()を追加して、PDFドキュメントからテーブルを削除できるようにしました。アブソーバーがページ上のテーブルを正常に見つけると、それを削除することが可能になります。以下のコードスニペットを確認して、PDFドキュメントからテーブルを削除する方法を示します:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // 既存のPDFドキュメントを読み込む
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // テーブルを見つけるためにTableAbsorberオブジェクトを作成する
        TableAbsorber absorber = new TableAbsorber();

        // アブソーバーで最初のページを訪問する
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // ページ上の最初のテーブルを取得する
        AbsorbedTable table = absorber.getTableList().get(0);

        // テーブルを削除する
        absorber.remove(table);

        // PDFを保存する
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## PDFドキュメントから複数のテーブルを削除する

PDFドキュメントには複数のテーブルが含まれる場合があり、それらを削除する必要が生じることがあります。PDFドキュメントから複数のテーブルを削除するには、次のコードスニペットを使用してください。

```java
    public static void RemoveMultipleTable() {
        // 既存のPDFドキュメントをロード
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // テーブルを見つけるためのTableAbsorberオブジェクトを作成
        TableAbsorber absorber = new TableAbsorber();

        // 2ページ目をアブソーバーで訪問
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // コレクションのコピーをループしてテーブルを削除
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // ドキュメントを保存
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```