---
title: 替换现有PDF文件中的图像
linktitle: 替换图像
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: 本节介绍如何使用Java库替换现有PDF文件中的图像。
lastmod: "2021-06-05"
---

[XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) 集合的 [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) 方法允许您替换现有PDF文件中的图像。

图像集合可以在页面的资源集合中找到。要替换图像：

1. 使用 Document 对象打开PDF文件。
2. 替换特定图像，使用 Document 对象的 Save 方法保存更新后的PDF文件。

以下代码片段展示了如何在PDF文件中替换图像。

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // 打开文档
        Document pdfDocument = new Document("input.pdf");
        // 替换特定图像
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO 自动生成的 catch 块
            e.printStackTrace();
        }
        // 保存更新后的PDF文件
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```