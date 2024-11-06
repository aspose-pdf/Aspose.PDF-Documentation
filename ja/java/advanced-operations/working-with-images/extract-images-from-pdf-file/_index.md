---
title: PDFファイルから画像を抽出する
linktitle: 画像を抽出する
type: docs
weight: 30
url: ja/java/extract-images-from-pdf-file/
description: このセクションでは、Javaライブラリを使用してPDFファイルから画像を抽出する方法を示します。
lastmod: "2021-06-05"
---

各ページには[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)コレクションがあり、これにはページ内のすべての画像が保持されているImagesコレクションがあります。[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage)オブジェクトは、Imagesコレクション内の特定の画像を取得します。

ページから画像を抽出するには:

Imagesコレクションから画像インデックスを使用して画像を取得します。
[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage)オブジェクトのsave(..)メソッドを使用して抽出した画像を保存します。

次のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // 特定の画像を抽出する
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // 出力画像を保存する
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // 更新されたPDFファイルを保存する
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```