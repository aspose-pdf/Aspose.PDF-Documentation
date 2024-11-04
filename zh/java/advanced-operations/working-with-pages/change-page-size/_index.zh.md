---
title: 程序化更改 PDF 页面大小
linktitle: 更改页面大小
type: docs
weight: 50
url: /java/change-page-size/
description: 使用 Java 库从您的 PDF 文件更改页面大小。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更改 PDF 页面大小

Aspose.PDF for Java 允许您在 Java 应用程序中通过简单的代码行更改 PDF 页面大小。本主题解释了如何更新/更改现有 PDF 文件的页面尺寸（大小）。

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) 类包含 SetPageSize(...) 方法，允许您设置页面大小。下面的代码片段通过几个简单的步骤更新页面尺寸：

1. 加载源 PDF 文件。
1. 将页面加载到 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 对象中。
1. 获取指定页面。
1. 调用 SetPageSize(..) 方法来更新其尺寸。

1. 调用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 Save(..) 方法生成具有更新页面尺寸的 PDF 文件。

{{% alert color="primary" %}}

请注意，高度和宽度属性使用点作为基本单位，其中 1 英寸 = 72 点，1 厘米 = 1/2.54 英寸 = 0.3937 英寸 = 28.3 点。

{{% /alert %}}

以下代码片段展示了如何将 PDF 页面尺寸更改为 A4 大小。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // 打开第一个文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // 获取页面集合
        PageCollection pageCollection = pdfDocument.getPages();

        // 获取特定页面
        Page pdfPage = pageCollection.get_Item(1);

        // 设置页面大小为 A4 (11.7 x 8.3 英寸)，在 Aspose.Pdf 中，1 英寸 = 72 点
        // 因此 A4 尺寸的点数为 (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // 保存更新后的文档
        pdfDocument.save(_dataDir);
    }
```


## 获取 PDF 页面大小

您可以使用 Aspose.PDF for Java 读取现有 PDF 文件的页面大小。以下代码示例展示了如何使用 Java 读取 PDF 页面尺寸。

```java
    public static void GetPDFPageSize() {
        
        // 打开第一个文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // 向 PDF 文档添加一个空白页面
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // 获取页面高度和宽度信息
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // 将页面旋转 90 度
        page.setRotate (Rotation.on90);

        // 获取页面高度和宽度信息
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // 保存更新后的文档
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```