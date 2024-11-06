---
title: 添加和删除书签
type: docs
weight: 10
url: zh/cpp/add-and-delete-bookmarks/
---

## <ins>**添加书签**
PdfBookmarkEditor 类允许您在 PDF 文档中添加书签。该类提供的 CreateBookmarkOfPage 方法，使您能够创建书签，该书签将定位到指定的页码。以下代码片段演示了 Aspose.PDF for C++ API 的此功能：

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**在现有文档中添加子书签**
您可以使用 **PdfBookmarkEditor** 类在现有 PDF 文件中添加子书签。 为了添加子书签，您需要创建**Bookmarks**和*Bookmark*对象。您可以将单个**Bookmark**对象添加到**Bookmarks**对象中。您还需要创建一个**Bookmark**对象，并将其**ChildItem**属性设置为**Bookmarks**对象。然后，您需要将带有**ChildItem**的这个**Bookmark**对象传递给**CreateBookmarks**方法。最后，您需要使用**PdfBookmarkEditor**类的**Save**方法保存更新后的PDF。以下代码段展示了如何在现有PDF文件中添加子书签。

## <ins>**删除PDF文件中的所有书签**
您可以使用不带任何参数的**DeleteBookmarks**方法删除PDF文件中的所有书签。 首先，您需要创建一个 **PdfBookmarkEditor** 类的对象，并使用 **BindPdf** 方法绑定输入的 PDF 文件。之后，您需要调用 **DeleteBookmarks** 方法，然后使用 **Save** 方法保存更新后的 PDF 文件。以下代码片段向您展示了如何从 PDF 文件中删除所有书签。

## <ins>**从 PDF 文件中删除特定书签**
为了删除特定书签，您需要使用字符串（标题）参数调用 **DeleteBookmarks** 方法。这里的 **title** 代表要从 PDF 中删除的书签。创建一个 **PdfBookmarkEditor** 类的对象，并使用 **BindPdf** 方法绑定输入的 PDF 文件。之后，调用 **DeleteBookmarks** 方法，然后使用 **Save** 方法保存更新后的 PDF 文件。以下代码片段向您展示了如何从 PDF 文件中删除特定书签。