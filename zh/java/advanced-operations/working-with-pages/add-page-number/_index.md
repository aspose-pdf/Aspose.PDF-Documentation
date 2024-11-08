---
title: 为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 100
url: /zh/java/add-page-number/
description: Aspose.PDF for Java 允许您使用 PageNumber Stamp 类向 PDF 文件添加页码印章。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

所有文档都必须包含页码。页码使读者更容易找到文档的不同部分。
**Aspose.PDF for Java** 允许您使用 PageNumberStamp 添加页码。

{{% alert color="primary" %}}

在线试用。您可以在此链接 [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number) 上在线查看 Aspose.PDF 转换的质量和结果。

{{% /alert %}}

您可以使用 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 类在 PDF 文档中添加页码印章。
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 类提供了创建基于页码的印章的方法，例如格式、边距、对齐、起始号码等。为了添加页码印章，您需要创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个具有所需属性的 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 对象。之后，您可以调用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类的 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.Page#addStamp-com.aspose.pdf.Stamp-) 方法在 PDF 文件中添加印章。您还可以设置页码印章的字体属性。

以下代码片段展示了如何在 PDF 文件中添加页码。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

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