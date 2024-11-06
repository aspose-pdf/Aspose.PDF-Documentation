---
title: 以编程方式旋转PDF页面 
linktitle: 旋转PDF页面
type: docs
weight: 60
url: zh/java/rotate-pages/
description: 使用Java更改页面方向并将页面内容调整到新页面方向。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更改页面方向

本文介绍如何更新或更改现有PDF文件中页面的方向。

Aspose.PDF for Java具有将页面方向从横向更改为纵向，反之亦然的功能。要更改页面方向，请使用以下代码片段设置页面的[MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-)。

您还可以通过使用Rotate()方法设置旋转角度来更改页面方向。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // 我们必须向上移动页面以补偿页面大小的变化
            // // （页面的下边缘是0,0，信息通常从页面顶部放置。因此我们将下边缘向上移动旧高度与新高度之间的差异。
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // 有时我们还需要设置CropBox（如果在原始文件中设置了）
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // 设置页面的旋转角度
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // 保存输出文件
        pdfDocument.save(_dataDir);
    }    
}
```