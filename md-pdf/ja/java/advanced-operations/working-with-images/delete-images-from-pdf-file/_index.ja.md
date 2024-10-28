---
title: PDFファイルから画像を削除
linktitle: 画像を削除
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFファイルから画像を削除する方法を説明します。
lastmod: "2021-06-05"
---

PDFファイルから画像を削除するには、Imagesコレクションのdelete(..)メソッドを使用します。

1. Documentオブジェクトを作成し、入力PDFファイルを開きます。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトの[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)コレクションから画像を保持しているページを取得します。
1. 画像は、ページの[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)コレクションにあるImagesコレクションに保持されています。
1. ImagesコレクションのDeleteメソッドを使用して画像を削除します。
1. DocumentオブジェクトのSaveメソッドを使用して出力を保存します。

以下のコードスニペットは、PDFファイルから画像を削除する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // ページ番号スタンプを作成
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // スタンプが背景かどうか
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // テキストプロパティを設定
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // 特定のページにスタンプを追加
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir);

    }
}
```