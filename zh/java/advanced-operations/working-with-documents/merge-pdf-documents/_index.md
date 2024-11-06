---
title: 以编程方式合并PDF
linktitle: 合并PDF文件
type: docs
weight: 50
url: zh/java/merge-pdf-documents/
description: 本页面解释如何使用Java将多个PDF文档合并为一个PDF文件。
lastmod: "2021-06-05"
---

现在，合并PDF文件是最需求的任务之一。
本文展示了如何使用Aspose.PDF for Java将多个PDF文件合并为一个PDF文档。示例使用Java编写，但API可以用于其他编程语言。PDF文件的合并方式是将第一个文件连接到另一个文档的末尾。

## 使用Java合并PDF文件

{{% alert color="primary" %}}

您可以使用Aspose.PDF合并PDF文件，并在此链接在线获取结果：[products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

要连接两个PDF文件：

1. 创建两个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)对象，每个对象包含一个输入的PDF文件。

1. 然后调用您想要添加其他PDF文件的Document对象的[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)集合的Add方法。
1. 将第二个Document对象的PageCollection集合传递给第一个PageCollection集合的Add方法。
1. 最后，使用Save方法保存输出PDF文件。

以下代码片段展示了如何使用Java连接PDF文件。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // 打开第一个文档
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // 打开第二个文档
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // 将第二个文档的页面添加到第一个文档
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // 保存连接后的输出文件
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```