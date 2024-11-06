---
title: 既存のPDFファイル内の画像を置き換える
linktitle: 画像を置き換える
type: docs
weight: 70
url: ja/java/replace-image-in-existing-pdf-file/
description: このセクションでは、Javaライブラリを使用して既存のPDFファイル内の画像を置き換える方法について説明します。
lastmod: "2021-06-05"
---

[XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) コレクションの [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) メソッドを使用すると、既存のPDFファイル内の画像を置き換えることができます。

画像コレクションは、ページのリソースコレクション内にあります。画像を置き換えるには：

1. Documentオブジェクトを使用してPDFファイルを開きます。
2. 特定の画像を置き換え、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、PDFファイル内の画像を置き換える方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // ドキュメントを開く
        Document pdfDocument = new Document("input.pdf");
        // 特定の画像を置き換える
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO 自動生成されたキャッチブロック
            e.printStackTrace();
        }
        // 更新されたPDFファイルを保存する
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```