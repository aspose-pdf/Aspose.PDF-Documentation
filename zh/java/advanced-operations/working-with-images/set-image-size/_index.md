---
title: 设置图像大小
linktitle: 设置图像大小
type: docs
weight: 80
url: /zh/java/set-image-size/
description: 本节介绍如何使用 Java 库设置 PDF 文件中的图像大小。
lastmod: "2021-06-05"
---

可以设置添加到 PDF 文件中的图像的大小。为了设置大小，可以使用 com.aspose.pdf.Image 类的 [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) 和 [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) 方法。

下面的代码片段演示了如何设置图像的大小：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // 实例化 Document 对象
        Document doc = new Document();
        // 向 PDF 文件的页面集合添加页面
        Page page = doc.getPages().add();
        // 创建图像实例
        Image img = new Image();
        // 以点为单位设置图像的宽度和高度
        img.setFixWidth (100);
        img.setFixHeight (100);
        // 将图像类型设置为 SVG
        img.setFileType (ImageFileType.Svg);
        // 源文件路径
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // 设置页面属性
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // 保存生成的 PDF 文件
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```