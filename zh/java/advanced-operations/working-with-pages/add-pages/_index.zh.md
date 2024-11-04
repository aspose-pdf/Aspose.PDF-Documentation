---  
title: 在 PDF 中添加页面  
linktitle: 添加页面  
type: docs  
weight: 10  
url: /java/add-pages/  
description: 本文介绍如何在 PDF 文件的指定位置插入（添加）页面。了解如何使用 Java 库移动、删除（删除）PDF 文件中的页面。  
lastmod: "2021-06-05"  
sitemap:  
changefreq: "weekly"  
priority: 0.7  
---

## 在 PDF 文件中添加或插入页面

Aspose.PDF for Java 允许您在文件中的任何位置插入页面到 PDF 文档中，也可以在 PDF 文件的末尾添加页面。您需要将要插入空白页面的位置传递给插入方法。  
本节介绍如何使用 Aspose.PDF for Java 向 PDF 添加页面。

### 在期望的位置插入空白页面到 PDF 文件中

以下代码片段展示了如何将空白页面插入到 PDF 文件中：

1. 使用输入 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。

1. 调用 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 集合的 Insert 方法，并指定索引。
1. 使用 Save 方法保存输出的 PDF。

下面的代码片段展示了如何在 PDF 文件中插入一页。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // 添加页面
        document.getPages().add();

        // 在 PDF 中插入空白页面
        document.getPages().insert(2);

        // 保存更新后的 PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

在上面的示例中，我们添加了具有默认参数的空白页面。如果您需要将页面大小设置为与文档中的另一页面相同，您应该添加几行代码：

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // 添加页面
        Page page1 = document.getPages().add();

        // 在 PDF 中插入空白页面
        Page page2 = document.getPages().insert(2);

        // 从页面1复制页面参数
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // 保存更新后的 PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### 在 PDF 文件末尾添加空白页

有时，您需要确保文档以空白页结尾。本主题解释了如何在 PDF 文档的末尾插入一个空白页。

要在 PDF 文件末尾插入一个空白页：

1. 使用输入 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
2. 调用 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 集合的 Add 方法，不带任何参数。
3. 使用 Save 方法保存输出 PDF。

以下代码片段展示了如何在 PDF 文件的末尾插入一个空白页。

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // 添加页面
        document.getPages().add();

        // 在 PDF 文件末尾插入一个空白页
        document.getPages().add();

        // 保存更新后的 PDF
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```