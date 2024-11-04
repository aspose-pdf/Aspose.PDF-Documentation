---
title: PDFドキュメントから画像を検索して取得する
linktitle: 画像を検索して取得する
type: docs
weight: 60
url: /java/search-and-get-images-from-pdf-document/
description: このセクションでは、Aspose.PDF for Javaライブラリを使用してPDFドキュメントから画像を検索して取得する方法を説明します。
lastmod: "2021-06-05"
---

[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber)を使用すると、PDFドキュメント内のすべてのページの画像を検索できます。

ドキュメント全体で画像を検索するには：

1. [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection)コレクションのAcceptメソッドを呼び出します。Acceptメソッドは[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber)オブジェクトをパラメーターとして受け取ります。これにより、[ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)オブジェクトのコレクションが返されます。
1. ImagePlacementsオブジェクトをループして、そのプロパティ（画像、寸法、解像度など）を取得します。

以下のコードスニペットは、ドキュメント内のすべての画像を検索する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // ドキュメントを開く
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // 画像配置検索を行うためのImagePlacementAbsorberオブジェクトを作成
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // すべてのページに対してアブソーバーを受け入れる
        doc.getPages().accept(abs);

        // すべてのImagePlacementをループし、画像とImagePlacementのプロパティを取得
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // ImagePlacementオブジェクトを使用して画像を取得
            // XImage image = imagePlacement.getImage();

            // すべての配置の画像配置プロパティを表示
            System.out.println("image width:" + imagePlacement.getRectangle().getWidth());
            System.out.println("image height:" + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution:" + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution:" + imagePlacement.getResolution().getY());
        }

    }
}
```

To get an image from an individual page, use the following code:

個別のページから画像を取得するには、次のコードを使用します。

```java
doc.getPages().get_Item(1).accept(abs)
```