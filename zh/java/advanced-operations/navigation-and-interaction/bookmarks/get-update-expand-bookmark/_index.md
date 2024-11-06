---
title: 获取、更新和展开书签 
linktitle: 获取、更新和展开书签
type: docs
weight: 20
url: zh/java/get-update-and-expand-bookmark/
description: 本文描述了如何在 PDF 文件中使用书签。使用我们的 Java 库，您可以从 PDF 文件中获取书签，获取书签的页码，更新 PDF 文档中的书签，以及在查看文档时展开书签。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取书签

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合包含了 PDF 文件的所有书签。本文解释了如何从 PDF 文件中获取书签，以及如何获取特定书签所在的页面。

要获取书签，遍历 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合，并在 OutlineItemCollection 中获取每个书签。
 OutlineItemCollection提供对所有书签属性的访问。以下代码片段向您展示如何从PDF文件中获取书签。

```java
    public static void GettingBookmarks() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 遍历所有书签
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("标题 :- " + outlineItem.getTitle());
            System.out.println("是否斜体 :- " + outlineItem.getItalic());
            System.out.println("是否加粗 :- " + outlineItem.getBold());
            System.out.println("颜色 :- " + outlineItem.getColor());
        }
    }
```

## 获取书签的页码

一旦您添加了书签，您可以通过获取与书签对象关联的目标页码来找出它位于哪一页。

```java
    public static void GettingBookmarksPageNumber() {
        // 创建PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // 打开PDF文件
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // 提取书签
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("标题 :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("页码 :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("页面动作 :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## 更新 PDF 文档中的书签

要在 PDF 文件中更新书签，首先通过指定书签的索引，从 Document 对象的 OutlineCollection 集合中获取特定的书签。一旦将书签检索到 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 对象中，可以更新其属性，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段展示了如何在 PDF 文档中更新书签。

```java
    public static void UpdateBookmarksInPDFDocument() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 获取书签对象
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // 更新书签对象
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // 将目标页面设置为 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 保存输出
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## 更新 PDF 文档中的子书签

要更新子书签：

1. 通过首先获取父书签，然后使用适当的索引值获取子书签，从 PDF 文件中检索要更新的子书签。
2. 使用 Save 方法保存更新后的 PDF 文件。

{{% alert color="primary" %}}

通过指定书签的索引从 Document 对象的 OutlineCollection 集合中获取书签，然后通过指定父书签的索引获取子书签。

{{% /alert %}}

以下代码片段向您展示如何在 PDF 文档中更新子书签。

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // 打开文档
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 获取书签对象
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // 获取子书签对象
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // 更新书签对象
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // 将目标页面设置为2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 保存输出
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## 查看文档时展开书签

书签保存在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 集合中，它本身位于 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 集合中。然而，我们可能需要在查看 PDF 文件时将所有书签展开。

为了实现这一要求，我们可以将每个大纲/书签项的打开状态设置为 Open。以下代码段向您展示如何在 PDF 文档中将每个书签的打开状态设置为展开。

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // 设置页面查看模式，例如显示缩略图，全屏，显示附件面板
        doc.setPageMode(PageMode.UseOutlines);
        // 打印 PDF 文件中书签的总数
        System.out.println(doc.getOutlines().size());
        // 遍历 PDF 文件的大纲集合中的每个大纲项
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // 设置大纲项的打开状态
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // 保存 PDF 文件
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```