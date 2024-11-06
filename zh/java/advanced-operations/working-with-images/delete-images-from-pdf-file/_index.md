---
title: 从 PDF 文件中删除图像
linktitle: 删除图像
type: docs
weight: 20
url: zh/java/delete-images-from-pdf-file/
description: 本节解释如何使用 Aspose.PDF for Java 从 PDF 文件中删除图像。
lastmod: "2021-06-05"
---

要从 PDF 文件中删除图像，只需使用 Images 集合的 delete(..) 方法。

1. 创建一个 Document 对象并打开输入 PDF 文件。
1. 从 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 集合中获取包含图像的页面。
1. 图像保存在页面的 [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 集合中的 Images 集合中。
1. 使用 Images 集合的 Delete 方法删除图像。
1. 使用 Document 对象的 Save 方法保存输出。

以下代码片段展示了如何从 PDF 文件中删除图像。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // 创建页码印章
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // 印章是否为背景
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // 设置文本属性
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // 将印章添加到特定页面
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // 保存输出文档
        pdfDocument.save(_dataDir);

    }
}
```