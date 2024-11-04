---
title: PDFページの移動
linktitle: ページの移動
type: docs
weight: 20
url: /java/move-pages/
description: Aspose.PDF for Javaを使用して、PDFファイルの希望する位置または末尾にページを移動してみてください。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 一つのPDFドキュメントから別のドキュメントへのページの移動

このトピックでは、Javaを使用して一つのPDFドキュメントから別のドキュメントの末尾にページを移動する方法を説明します。
ページを移動するには、以下を行う必要があります：

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. 目的のPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)コレクションからページを取得します。
1. ページを目的のドキュメントに追加します。
1. Saveメソッドを使用して出力PDFを保存します。
1. ソースドキュメントでページを削除します。
1. Saveメソッドを使用してソースPDFを保存します。

次のコードスニペットは、1ページを移動する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // 出力ファイルを保存
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## 複数のページを1つのPDFドキュメントから別のPDFドキュメントに移動

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. 目的のPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. 移動するページ番号を含む配列を定義します。

1. 配列をループで実行します:
    1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) コレクションからページを取得します。
    1. ページを宛先ドキュメントに追加します。
1. Save メソッドを使用して出力 PDF を保存します。
1. 配列を使用してソースドキュメント内のページを削除します。
1. Save メソッドを使用してソース PDF を保存します。

以下のコードスニペットは、PDF ファイルの最後に空のページを挿入する方法を示しています。

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // 出力ファイルを保存
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## 現在の PDF ドキュメント内の新しい場所にページを移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)コレクションからページを取得します。
1. 新しい場所（例えば末尾）にページを追加します。
1. 前の場所のページを削除します。
1. Saveメソッドを使用して出力PDFを保存します。

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // 出力ファイルを保存
    srcDocument.save(dstFileName);
  }
}
```