---
title: PDFにページを追加 
linktitle: ページを追加
type: docs
weight: 10
url: /java/add-pages/
description: この記事では、PDFファイルの希望する場所にページを挿入（追加）する方法を教えます。Javaライブラリを使用して、PDFファイルからページを移動、削除（削除）する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルにページを追加または挿入

Aspose.PDF for Javaを使用すると、ファイル内の任意の場所にPDFドキュメントにページを挿入したり、PDFファイルの末尾にページを追加したりできます。空白ページを挿入したい場所をinsertメソッドに渡す必要があります。このセクションでは、Aspose.PDF for Javaを使用してPDFにページを追加する方法を示します。

### 希望の場所にPDFファイルに空白ページを挿入

次のコードスニペットは、PDFファイルに空白ページを挿入する方法を示しています。

1. 入力PDFファイルを指定して[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。

1. 指定されたインデックスで[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection)コレクションのInsertメソッドを呼び出します。
1. Saveメソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // ページを追加
        document.getPages().add();

        // PDFに空のページを挿入
        document.getPages().insert(2);

        // 更新されたPDFを保存
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

上記の例では、デフォルトのパラメータで空のページを追加しました。ドキュメント内の他のページと同じサイズにする必要がある場合は、数行のコードを追加する必要があります。

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // ページを追加
        Page page1 = document.getPages().add();

        // PDFに空のページを挿入
        Page page2 = document.getPages().insert(2);

        // ページ1からページパラメータをコピー
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // 更新されたPDFを保存
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### PDFファイルの最後に空白ページを追加する

時々、ドキュメントが空白ページで終わることを確認したい場合があります。このトピックでは、PDFドキュメントの最後に空白ページを挿入する方法を説明します。

PDFファイルの最後に空白ページを挿入するには：

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。
1. パラメータなしで[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection)コレクションのAddメソッドを呼び出します。
1. Saveメソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの最後に空白ページを挿入する方法を示しています。

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // ページを追加
        document.getPages().add();

        // PDFファイルの最後に空白ページを挿入
        document.getPages().add();

        // 更新されたPDFを保存
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```