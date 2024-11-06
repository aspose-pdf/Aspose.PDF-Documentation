---
title: 设置默认字体名称
linktitle: 设置默认字体名称
type: docs
weight: 90
url: zh/java/set-default-font-name/
description: 本节介绍如何使用 Aspose.PDF for Java 库设置默认字体名称。
lastmod: "2021-06-05"
---

**Aspose.PDF for Java** API 允许您在文档中字体不可用时设置默认字体名称。您可以使用 [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) 类的 [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) 方法来设置默认字体名称。如果 setDefaultFontName 设置为 null，将使用 **Times New Roman** 字体。

以下代码片段显示了在将 PDF 保存为图像时如何设置默认字体名称：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

public class ExampleSetDefaultFontName {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SetDefaultFontName() {
        
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        FileOutputStream imageStream = null;;
        try {
            imageStream = new FileOutputStream(_dataDir + "SetDefaultFontName.png");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.setDefaultFontName("Arial");
        pngDevice.setRenderingOptions(ro);
        pngDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
    }    
}
```