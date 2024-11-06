---
title: 添加和删除书签 
linktitle: 添加和删除书签
type: docs
weight: 10
url: zh/java/add-and-delete-bookmark/
description: 您可以使用 Java 向 PDF 文档添加书签。可以从 PDF 文档中删除所有或特定书签。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 向 PDF 文档添加书签

书签存储在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 集合中，该集合本身位于 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合中。

要向 PDF 添加书签：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象打开 PDF 文档。
1. 创建书签并定义其属性。
1. 将 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 集合添加到 Outlines 集合中。

以下代码片段展示了如何在 PDF 文档中添加书签。

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // 创建一个书签对象
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("测试大纲");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 设置目标页码
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 在文档的大纲集合中添加一个书签。
        pdfDocument.getOutlines().add(pdfOutline);

        // 保存更新的文档
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## 向 PDF 文档添加子书签

书签可以嵌套，表示与父书签和子书签的层次关系。本文解释了如何向 PDF 添加子书签，即二级书签。

要向 PDF 文件添加子书签，首先添加一个父书签：

1. 打开文档。
2. 向 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 添加书签，定义其属性。
3. 将 OutlineItemCollection 添加到 Document 对象的 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合中。

子书签的创建方式与上述父书签相同，但被添加到父书签的 Outlines 集合中。

以下代码片段显示了如何向 PDF 文档添加子书签。

```java
    public static void AddChildBookmark() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // 创建父书签对象
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 创建子书签对象
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // 在父书签的集合中添加子书签
        pdfOutline.add(pdfChildOutline);
        // 在文档的书签集合中添加父书签。
        pdfDocument.getOutlines().add(pdfOutline);

        // 保存输出
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## 从 PDF 文档中删除所有书签

PDF 中的所有书签都保存在 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合中。本文解释如何从 PDF 文件中删除所有书签。

要从 PDF 文件中删除所有书签：

1. 调用 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合的 Delete 方法。
1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Save 方法保存修改后的文件。

以下代码片段演示了如何从 PDF 文档中删除所有书签。

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // 删除所有书签
        pdfDocument.getOutlines().delete();

        // 保存更新后的文件
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## 从 PDF 文档中删除特定书签

[从 PDF 文档中删除所有附件](https://docs.aspose.com/pdf/java/working-with-attachments/) 显示了如何从 PDF 文件中删除所有附件。也可以仅删除特定附件。

要从 PDF 文件中删除特定书签：

1. 将书签的标题作为参数传递给 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合的 [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) 方法。
2. 然后使用 Document 对象的 Save 方法保存更新后的文件。

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类提供了 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合。[Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) 方法会删除传递给该方法的标题的任何书签。

以下代码片段展示了如何从 PDF 文档中删除特定书签。

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // 通过标题删除特定大纲
        pdfDocument.getOutlines().delete("Child Outline");

        // 保存更新后的文件
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```