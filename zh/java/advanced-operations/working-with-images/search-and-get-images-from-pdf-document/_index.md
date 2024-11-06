---
title: 从 PDF 文档中搜索和获取图像
linktitle: 搜索和获取图像
type: docs
weight: 60
url: zh/java/search-and-get-images-from-pdf-document/
description: 本节解释如何使用 Aspose.PDF for Java 库从 PDF 文档中搜索和获取图像。
lastmod: "2021-06-05"
---

[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) 允许您在 PDF 文档的所有页面中搜索图像。

要在整个文档中搜索图像：

1. 调用 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 集合的 Accept 方法。Accept 方法接受一个 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) 对象作为参数。这将返回一个 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement) 对象的集合。
2. 遍历 ImagePlacements 对象并获取其属性（图像、尺寸、分辨率等）。

以下代码片段显示如何在文档中搜索其所有图像。

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // 打开文档
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // 创建 ImagePlacementAbsorber 对象以执行图像位置搜索
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // 接受所有页面的吸收器
        doc.getPages().accept(abs);

        // 遍历所有 ImagePlacements，获取图像和 ImagePlacement 属性
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // 使用 ImagePlacement 对象获取图像
            // XImage image = imagePlacement.getImage();

            // 显示所有位置的图像位置属性
            System.out.println("图像宽度:" + imagePlacement.getRectangle().getWidth());
            System.out.println("图像高度:" + imagePlacement.getRectangle().getHeight());
            System.out.println("图像 LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("图像 LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("图像水平分辨率:" + imagePlacement.getResolution().getX());
            System.out.println("图像垂直分辨率:" + imagePlacement.getResolution().getY());
        }

    }
}
```

要从单个页面获取图像，请使用以下代码：

```java
doc.getPages().get_Item(1).accept(abs)
```