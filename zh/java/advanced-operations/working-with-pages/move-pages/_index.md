---
title: 移动 PDF 页面
linktitle: 移动页面
type: docs
weight: 20
url: zh/java/move-pages/
description: 尝试使用 Aspose.PDF for Java 将页面移动到 PDF 文件的所需位置或末尾。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将页面从一个 PDF 文档移动到另一个

本主题解释了如何使用 Java 将页面从一个 PDF 文档移动到另一个文档的末尾。
要移动页面，我们应该：

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 使用目标 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 集合中获取页面。
1. 将页面添加到目标文档。
1. 使用 Save 方法保存输出 PDF。
1. 删除源文档中的页面。
1. 使用 Save 方法保存源 PDF。


以下代码片段向您展示如何移动一个页面。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // 保存输出文件
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## 从一个PDF文档移动一批页面到另一个

1. 使用源PDF文件创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类对象。
1. 使用目标PDF文件创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类对象。
1. 定义一个数组，其中包含要移动的页码。

1. 遍历数组循环：
    1. 从 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 集合中获取页面。
    1. 将页面添加到目标文档。
1. 使用 Save 方法保存输出 PDF。
1. 使用数组删除源文档中的页面。
1. 使用 Save 方法保存源 PDF。

以下代码片段展示了如何在 PDF 文件末尾插入一个空白页面。

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // 保存输出文件
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## 在当前 PDF 文档中移动页面到新位置

1. 使用源PDF文件创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类对象。
1. 从[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)集合中获取页面。
1. 将页面添加到新位置（例如末尾）。
1. 删除页面在先前的位置。
1. 使用Save方法保存输出PDF。

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // 保存输出文件
    srcDocument.save(dstFileName);
  }
}
```