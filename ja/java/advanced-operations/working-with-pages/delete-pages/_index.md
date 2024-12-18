---
title: プログラムでPDFページを削除する
linktitle: PDFページを削除する
type: docs
weight: 40
url: /ja/java/delete-pages/
description: Javaライブラリを使用してPDFファイルからページを削除できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Javaを使用してPDFファイルからページを削除できます。[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)から特定のページを削除するには、単にdelete()メソッドを呼び出し、削除したい特定のページのインデックスを指定します。その後、saveメソッドを呼び出して更新されたPDFファイルを保存します。

## PDFファイルからページを削除する

1. Deleteメソッドを呼び出し、ページのインデックスを指定します
1. Saveメソッドを呼び出して更新されたPDFファイルを保存します
以下のコードスニペットは、Javaを使用してPDFファイルから特定のページを削除する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 特定のページを削除する
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // 更新されたPDFを保存する
    pdfDocument.save(_dataDir);    

  }
```