---
title: 为PDF添加背景
linktitle: 添加背景
type: docs
weight: 110
url: /zh/java/add-backgrounds/
descriptions: 使用Java为您的PDF文件添加背景图像。使用BackgroundArtifact对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

背景图像可用于为文档添加水印或其他细微设计。在Aspose.PDF for Java中，每个PDF文档是一个页面集合，每个页面包含一个工件集合。[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact)类可用于为页面对象添加背景图像。

以下代码片段展示了如何使用Java中的BackgroundArtifact对象将背景图像添加到PDF页面。

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // 对于完整的示例和数据文件，请访问
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // 创建一个新的Document对象
        Document doc = new Document();
        // 向文档对象添加一个新页面
        Page page = doc.getPages().add();
        // 创建BackgroundArtifact对象
        BackgroundArtifact background = new BackgroundArtifact();
        // 为backgroundartifact对象指定图像
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // 将backgroundartifact添加到页面的工件集合中
        page.getArtifacts().add(background);
        // 保存文档
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```