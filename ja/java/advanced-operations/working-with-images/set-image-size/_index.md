---
title: 画像サイズの設定
linktitle: 画像サイズの設定
type: docs
weight: 80
url: ja/java/set-image-size/
description: このセクションでは、Javaライブラリを使用してPDFファイルの画像サイズを設定する方法について説明します。
lastmod: "2021-06-05"
---

PDFファイルに追加される画像のサイズを設定することができます。サイズを設定するには、com.aspose.pdf.Imageクラスの[setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-)メソッドと[setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-)メソッドを使用します。

次のコードスニペットは、画像のサイズを設定する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Documentオブジェクトをインスタンス化
        Document doc = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = doc.getPages().add();
        // 画像インスタンスを作成
        Image img = new Image();
        // ポイントで画像の幅と高さを設定
        img.setFixWidth (100);
        img.setFixHeight (100);
        // 画像タイプをSVGに設定
        img.setFileType (ImageFileType.Svg);
        // ソースファイルのパス
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // ページプロパティを設定
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // 結果として得られるPDFファイルを保存
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```