---
title: PDFページサイズをプログラムで変更する
linktitle: ページサイズを変更
type: docs
weight: 50
url: /java/change-page-size/
description: Javaライブラリを使用してPDFファイルのページサイズを変更します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFページサイズを変更する

Aspose.PDF for Javaを使用すると、Javaアプリケーションで簡単なコード行でPDFページサイズを変更できます。このトピックでは、既存のPDFファイルのページの寸法（サイズ）を更新/変更する方法を説明します。

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) クラスには、ページサイズを設定できるSetPageSize(...)メソッドがあります。以下のコードスニペットは、簡単なステップでページの寸法を更新します：

1. ソースPDFファイルをロードします。
1. ページを[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)オブジェクトに取得します。
1. 指定されたページを取得します。
1. SetPageSize(..)メソッドを呼び出して、寸法を更新します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスの Save(..) メソッドを呼び出して、ページ寸法が更新されたPDFファイルを生成します。

{{% alert color="primary" %}}

高さと幅のプロパティは基本単位としてポイントを使用します。1インチ = 72ポイント、1cm = 1/2.54インチ = 0.3937インチ = 28.3ポイントです。

{{% /alert %}}

次のコードスニペットは、PDFページの寸法をA4サイズに変更する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // ドキュメントディレクトリへのパス
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // 最初のドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // ページコレクションを取得
        PageCollection pageCollection = pdfDocument.getPages();

        // 特定のページを取得
        Page pdfPage = pageCollection.get_Item(1);

        // ページサイズをA4（11.7 x 8.3インチ）に設定し、Aspose.Pdfでは1インチ = 72ポイント
        // したがって、ポイントでのA4の寸法は (842.4, 597.6) になります
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }
```


## PDFページサイズを取得する

Aspose.PDF for Javaを使用して、既存のPDFファイルのページサイズを読み取ることができます。以下のコードサンプルは、Javaを使用してPDFページの寸法を読み取る方法を示しています。

```java
    public static void GetPDFPageSize() {
        
        // 最初のドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // PDFドキュメントに空白ページを追加する
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // ページの高さと幅の情報を取得する
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // ページを90度回転する
        page.setRotate (Rotation.on90);

        // ページの高さと幅の情報を取得する
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // 更新されたドキュメントを保存する
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```