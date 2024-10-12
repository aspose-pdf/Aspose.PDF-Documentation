---
title: 添加和删除书签
linktitle: 添加和删除书签
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: 本主题解释如何使用C++库向PDF文档添加书签。您还可以从PDF文档中删除所有或特定书签。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 向PDF文档添加书签

书签保存在文档对象的[OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/)集合中，该集合本身位于[OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/)集合中。

要向PDF添加书签：

1. 使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)对象打开PDF文档。
1. 创建一个书签并定义其属性。
1. 将[OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/)集合添加到Outlines集合中。

以下代码片段向您展示如何在PDF文档中添加书签。

```cpp
void AddBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");

// 创建书签对象

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// 设置目标页码

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

// 在文档的大纲集合中添加书签。

pdfDocument->get_Outlines()->Add(pdfOutline);

// 保存更新后的文档

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## 向PDF文档添加子书签

书签可以嵌套，表示与父书签和子书签的层次关系。 这篇文章解释了如何向 PDF 添加子书签，即二级书签。

要向 PDF 文件添加子书签，首先添加一个父书签：

1. 打开一个文档。
2. 向 [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) 添加书签，定义其属性。
3. 将 OutlineItemCollection 添加到 Document 对象的 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 集合中。

子书签的创建方式与上文解释的父书签相同，但被添加到父书签的 Outlines 集合中。

以下代码片段展示了如何向 PDF 文档中添加子书签。

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// 创建一个父书签对象

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// 创建一个子书签对象

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// 在父书签的集合中添加子书签

pdfOutline->Add(pdfChildOutline);

// 在文档的书签集合中添加父书签。

pdfDocument->get_Outlines()->Add(pdfOutline);


// 保存输出

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## 删除 PDF 文档中的所有书签

PDF 中的所有书签都保存在 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 集合中。本文解释了如何从 PDF 文件中删除所有书签。

要删除 PDF 文件中的所有书签：

1. 调用 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 集合的 Delete 方法。
2. 使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 对象的 Save 方法保存修改后的文件。

以下代码片段显示了如何从 PDF 文档中删除所有书签。

```cpp
void DeleteAllBookmarksFromPDFDocument() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");

// 删除所有书签

pdfDocument->get_Outlines()->Delete();

// 保存更新后的文件

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```

## 删除 PDF 文档中特定的书签

[从PDF文档中删除所有附件](https://docs.aspose.com/pdf/cpp/working-with-attachments/) 显示了如何从PDF文件中删除所有附件。也可以仅删除特定附件。

要从PDF文件中删除特定书签：

1. 将书签的标题作为参数传递给 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 集合的 Delete 方法。
1. 然后使用 Document 对象的 Save 方法保存更新后的文件。

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 类提供了 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 集合。[Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) 方法会删除传递给该方法的标题的任何书签。

以下代码片段展示了如何从PDF文档中删除特定书签。

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// 按标题删除特定大纲

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// 保存更新后的文件

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```