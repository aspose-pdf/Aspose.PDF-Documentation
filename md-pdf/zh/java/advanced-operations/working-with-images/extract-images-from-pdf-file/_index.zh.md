---
title: 从PDF文件中提取图像
linktitle: 提取图像
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: 本节介绍如何使用Java库从PDF文件中提取图像。
lastmod: "2021-06-05"
---

每个页面都有一个[资源](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)集合，而该集合中包含了图像集合，其中保存了页面中的所有图像。 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage)对象可以获取图像集合中的指定图像。

要从页面中提取图像：

从图像集合中使用图像索引获取图像。
使用[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage)对象的save(..)方法保存提取的图像。

以下代码片段向您展示如何从PDF文件中提取图像。

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // 提取特定图像
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // 保存输出图像
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // 保存更新的PDF文件
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```