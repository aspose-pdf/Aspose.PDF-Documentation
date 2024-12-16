---
title: 获取、更新和扩展书签
linktitle: 获取、更新和扩展书签
type: docs
weight: 20
url: /zh/cpp/get-update-and-expand-bookmark/
description: Aspose.PDF for C++ 库允许您在 PDF 文件中获取和更新。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取书签

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 集合包含了 PDF 文件的所有书签。本文解释了如何从 PDF 文件中获取书签，以及如何获取特定书签所在的页面。

要获取书签，请遍历 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 集合，并在 OutlineItemCollection 中获取每个书签。 The OutlineItemCollection 提供对所有书签属性的访问。以下代码片段显示了如何从 PDF 文件中获取书签。

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 遍历所有书签

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"标题 :- " + outlineItem->get_Title());


Console::WriteLine(u"是否斜体 :- " + outlineItem->get_Italic());


Console::WriteLine(u"是否加粗 :- " + outlineItem->get_Bold());


Console::WriteLine(u"颜色 :- {0}", outlineItem->get_Color());

}
}
```

## 获取书签的页码

一旦添加了书签，就可以通过获取与书签对象关联的目标页码来找出它所在的页面。

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 创建 PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// 打开 PDF 文件

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// 提取书签

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"标题 :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"页码 :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"页面动作 :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## 更新 PDF 文档中的书签

要更新 PDF 文件中的书签，首先通过指定书签的索引从 Document 对象的 OutlineColletion 集合中获取特定的书签。 一旦将书签检索到 [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) 对象中，就可以更新其属性，然后使用 Save 方法保存更新的 PDF 文件。 以下代码片段展示了如何在 PDF 文档中更新书签。

```cpp
void UpdateBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 获取书签对象

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// 更新书签对象

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// 将目标页面设置为 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 保存输出

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## 更新 PDF 文档中的子书签

要更新子书签：

1. 通过首先获取父书签，然后使用适当的索引值获取子书签，从 PDF 文件中检索要更新的子书签。
2. 使用 Save 方法保存更新后的 PDF 文件。

{{% alert color="primary" %}}

通过指定书签的索引，从 Document 对象的 OutlineCollection 集合中获取书签，然后通过指定此父书签的索引获取子书签。

{{% /alert %}}

以下代码片段向您展示如何更新 PDF 文档中的子书签。

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 获取书签对象

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// 获取子书签对象

auto childOutline = pdfOutline->idx_get(1);


// 更新书签对象

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// 将目标页面设置为 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 保存输出

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## 查看文档时展开书签

书签保存在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) 集合中，后者又在 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 集合中。然而，我们可能有一个需求，即在查看 PDF 文件时将所有书签展开。

为了实现此需求，我们可以将每个大纲/书签项的打开状态设置为 Open。下面的代码片段展示了如何在 PDF 文档中将每个书签的打开状态设置为展开。

```cpp
void ExpandedBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 设置页面查看模式，例如显示缩略图、全屏、显示附件面板

doc->set_PageMode(PageMode::UseOutlines);

// 打印 PDF 文件中书签的总数

Console::WriteLine(doc->get_Outlines()->get_Count());

// 遍历 PDF 文件书签集合中的每个大纲项

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {

// 设置大纲项的打开状态

doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// 保存 PDF 文件

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```