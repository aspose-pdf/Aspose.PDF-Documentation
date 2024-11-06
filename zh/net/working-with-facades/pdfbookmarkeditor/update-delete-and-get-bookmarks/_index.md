---
title: 更新、删除和获取书签
type: docs
weight: 30
url: zh/net/update-delete-and-get-bookmarks/
description: 本节解释如何使用 Aspose.PDF Facades 更新、删除和获取书签。
lastmod: "2021-06-05"
draft: false
---

## 更新 PDF 文件中的现有书签

为了更新 PDF 文件中的现有书签，您需要使用 [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 方法。 此方法需要两个参数：源标题（要修改的书签标题）、目标标题（要替换的标题）。您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，您需要调用 [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 方法，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF。以下代码片段展示了如何修改 PDF 文件中的现有书签。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## 删除 PDF 文件中的所有书签

您可以使用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法删除 PDF 文件中的所有书签，无需任何参数。 首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，您需要调用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段向您展示了如何从 PDF 文件中删除所有书签。

## 从 PDF 文件中删除特定书签

为了删除特定书签，您需要使用字符串（标题）参数调用 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 方法。 The *title* here represents the bookmark to be deleted from the PDF. Create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method and then save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to delete a particular bookmark from a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## 从PDF文档外观获取书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类提供了在现有PDF文件中操作书签的功能。 它提供了各种属性来获取/设置有关书签的信息。以下代码片段显示了如何获取与 PDF 文件中每个书签相关的信息。

## 从现有 PDF 文件中提取书签

[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法允许您从 PDF 文件中提取书签。 为了提取书签，您需要创建 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定 PDF 文件。 在此之后，你需要调用 [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法。 [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 方法返回 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index) 对象。然后，你可以遍历这些书签并获取单个 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象。最后，使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新的 PDF 文件。以下代码片段向你展示了如何将书签导出到 XML 文件中。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}