---
title: 程序化分割PDF
linktitle: 分割PDF文件
type: docs
weight: 60
url: /java/split-document/
description: 本主题介绍如何在Java应用程序中将PDF页面拆分为单独的PDF文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

您可以使用Aspose.PDF分割PDF文件，并在此链接在线获取结果：[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

本主题介绍如何使用Java中的Aspose.PDF将PDF页面拆分为单独的PDF文件。在Java中将PDF页面拆分为单页PDF文件，可以按照以下步骤进行：

1. 通过[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)集合循环遍历PDF文档的页面。

1. 对于每次迭代，创建一个新的 Document 对象并将单个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象添加到空文档中。
1. 使用 Save 方法保存新的 PDF。

以下 Java 代码片段向您展示了如何将 PDF 页面拆分为单个 PDF 文件。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // 遍历所有页面
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```