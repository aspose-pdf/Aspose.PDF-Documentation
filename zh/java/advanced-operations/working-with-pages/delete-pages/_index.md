---
title: 使用编程方式删除 PDF 页面 
linktitle: 删除 PDF 页面
type: docs
weight: 40
url: /zh/java/delete-pages/
description: 您可以使用 Java 库从 PDF 文件中删除页面。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用 Aspose.PDF for Java 从 PDF 文件中删除页面。要从 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 中删除特定页面，只需调用 delete() 方法并指定要删除的特定页面的索引。然后调用 save 方法以保存更新后的 PDF 文件。

## 从 PDF 文件中删除页面

1. 调用 Delete 方法并指定页面的索引
1. 调用 Save 方法以保存更新后的 PDF 文件

以下代码片段展示了如何使用 Java 从 PDF 文件中删除特定页面。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 删除特定页面
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // 保存更新后的 PDF
    pdfDocument.save(_dataDir);    

  }
```