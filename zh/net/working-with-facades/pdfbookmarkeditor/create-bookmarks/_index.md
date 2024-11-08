---
title: Create Bookmarks
type: docs
weight: 10
url: /zh/net/create-bookmarks/
description: 本节解释如何使用 Aspose.PDF Facades 中的 PdfBookmarEditor 类为 PDF 文件创建书签。
lastmod: "2021-06-05"
draft: false
---

## Create Bookmarks of All Pages

为了创建所有页面的书签，您需要使用[CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)方法且无需任何参数。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)类允许您为 PDF 文件的所有页面创建书签。 首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF。然后，您需要调用 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出 PDF 文件。以下代码片段向您展示了如何创建书签。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## 创建具有属性的所有页面的书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类允许您为 PDF 文件的所有页面创建书签并指定属性（颜色、加粗、斜体）。 您可以借助 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法来实现这一点。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF。然后，您需要调用 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出的 PDF 文件。以下代码片段向您展示了如何为所有页面创建带有属性的书签。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## 为特定页面创建书签

您可以使用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法在现有 PDF 文件中为特定页面创建书签。 此方法接受两个参数：书签标题和页码。首先，您需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。然后，您需要调用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出的 PDF 文件。以下代码片段向您展示了如何创建特定页面的书签。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## 创建一系列页面的书签

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类允许您创建一系列页面的书签。 你可以使用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，带有两个参数：书签列表（书签标题的列表）和页面列表（要书签的页面列表）。首先，你需要创建一个 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。然后，你必须调用 [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 方法，并使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存输出的 PDF。以下代码片段向你展示了如何创建一系列页面的书签。




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## 在现有 PDF 文件中添加书签

您可以使用 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类在现有 PDF 文件中添加书签。为了创建书签，您需要创建 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象并设置书签的必要属性。之后，您需要将 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 对象传递给 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor) 类的 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 方法。最后，您需要使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段展示了如何在现有 PDF 文件中添加书签。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## 在现有 PDF 文件中添加子书签

您可以使用 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 类在现有 PDF 文件中添加子书签。 为了添加子书签，您需要创建[书签](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark)对象。 你可以将单个[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark)对象添加到[Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks)对象中。 你还需要创建一个[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark)对象，并将其[ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem)属性设置为[Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks)对象。然后，你需要将这个带有[ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem)的[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark)对象传递给[CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2)方法。最后，你需要使用[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)类的[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)方法保存更新后的PDF。以下代码片段展示了如何在现有PDF文件中添加子书签。
## 另请参见

尝试比较并找到适合您的书签使用方式。让我们学习[在 PDF 中使用书签](/pdf/zh/net/bookmarks/)部分。