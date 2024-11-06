---
title: 画像配置の操作
linktitle: 画像配置
type: docs
weight: 50
url: ja/java/working-with-image-placement/
description: このセクションでは、Javaライブラリを使用してPDFファイルの画像配置を操作する機能について説明します。
lastmod: "2021-06-05"
---

Aspose.PDF for Javaは、PDFドキュメント内の画像の解像度と位置を取得するための同様の機能を提供する、[ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)、[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber)、および[ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection)というクラスを導入しました。

- ImagePlacementAbsorberは、ImagePlacementオブジェクトのコレクションとして画像使用検索を実行します。
- ImagePlacementは、実際の画像配置の値を返すメンバーResolutionとRectangleを提供します。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // ソースPDFファイルを読み込む
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // 最初のページの内容を読み込む
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // 画像のプロパティを取得
            System.out.println("画像の幅:" + imagePlacement.getRectangle().getWidth());
            System.out.println("画像の高さ:" + imagePlacement.getRectangle().getHeight());
            System.out.println("画像のLLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("画像のLLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("画像の水平解像度:" + imagePlacement.getResolution().getX());
            System.out.println("画像の垂直解像度:" + imagePlacement.getResolution().getY());

            // 可視の寸法で画像を取得
            // Bitmap scaledImage;
            // リソースから画像を取得
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // 実際の寸法でビットマップを作成
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // 透過性を持つバッファードイメージを作成
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // バッファードイメージに画像を描画
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // バッファードイメージを返す
        return bimage;
    }
}
```