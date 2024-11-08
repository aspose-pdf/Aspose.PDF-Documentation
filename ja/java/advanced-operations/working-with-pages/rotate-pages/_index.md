---
title: プログラムでPDFページを回転 
linktitle: PDFページを回転
type: docs
weight: 60
url: /ja/java/rotate-pages/
description: Javaを使用してページの向きを変更し、新しいページの向きにページ内容を合わせる。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ページの向きを変更

この記事では、既存のPDFファイルのページの向きを更新または変更する方法について説明します。

Aspose.PDF for Javaは、ページの向きを横から縦に、またはその逆に変更する機能を持っています。ページの向きを変更するには、次のコードスニペットを使用してページの[MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-)を設定します。

Rotate()メソッドを使用して回転角度を設定することで、ページの向きを変更することもできます。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // ページサイズの変更を補うためにページを上に移動する必要があります
            // // （ページの下部は0,0であり、情報は通常ページの上部から配置されます。
            // //  そのため、古い高さと新しい高さの差で下の縁を上に移動します）
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // 元のファイルで設定されていれば、CropBoxも設定する必要があります
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // ページの回転角度を設定
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // 出力ファイルを保存
        pdfDocument.save(_dataDir);
    }    
}
```