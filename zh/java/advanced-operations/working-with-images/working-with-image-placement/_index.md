---
title: 使用图像放置
linktitle: 图像放置
type: docs
weight: 50
url: zh/java/working-with-image-placement/
description: 本节介绍使用Java库处理图像放置PDF文件的功能。
lastmod: "2021-06-05"
---

Aspose.PDF for Java 引入了名为 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)、[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) 和 [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) 的类，这些类提供与上面描述的类类似的功能，以获取PDF文档中图像的分辨率和位置。

- ImagePlacementAbsorber 执行图像使用搜索作为 ImagePlacement 对象集合。
- ImagePlacement 提供返回实际图像放置值的成员 Resolution 和 Rectangle。

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
        // 加载源PDF文件
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // 加载第一页的内容
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // 获取图像属性
            System.out.println("图像宽度:" + imagePlacement.getRectangle().getWidth());
            System.out.println("图像高度:" + imagePlacement.getRectangle().getHeight());
            System.out.println("图像 LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("图像 LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("图像水平分辨率:" + imagePlacement.getResolution().getX());
            System.out.println("图像垂直分辨率:" + imagePlacement.getResolution().getY());

            // 获取具有可见尺寸的图像
            // Bitmap scaledImage;
            // 从资源中检索图像
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // 创建具有实际尺寸的位图
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

        // 创建具有透明度的缓冲图像
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // 将图像绘制到缓冲图像上
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // 返回缓冲图像
        return bimage;
    }
}
```