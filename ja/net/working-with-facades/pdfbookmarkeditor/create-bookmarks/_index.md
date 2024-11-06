---
title: ブックマークを作成
type: docs
weight: 10
url: ja/net/create-bookmarks/
description: このセクションでは、Aspose.PDF Facades を使用して PdfBookmarEditor クラスで PDF ファイルにブックマークを作成する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## すべてのページのブックマークを作成

すべてのページのブックマークを作成するには、パラメータなしで [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドを使用する必要があります。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスを使用すると、PDF ファイルのすべてのページにブックマークを作成できます。 最初に、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFをバインドする必要があります。その後、[CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して出力PDFファイルを保存する必要があります。次のコードスニペットは、ブックマークを作成する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## すべてのページにプロパティを持つブックマークを作成する

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスを使用すると、PDFファイルのすべてのページのブックマークを作成し、プロパティ（色、太字、斜体）を指定することができます。 以下の方法を使用して、それを行うことができます。[CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドの助けを借りて。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFをバインドする必要があります。その後、[CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して出力PDFファイルを保存します。次のコードスニペットは、プロパティを持つすべてのページのブックマークを作成する方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## 特定のページのブックマークを作成

[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) メソッドを使用して、既存のPDFファイル内の特定のページのブックマークを作成できます。 このメソッドは、2つの引数を取ります: ブックマークのタイトルとページ番号。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。次に、[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して出力PDFファイルを保存する必要があります。次のコードスニペットは、特定のページのブックマークを作成する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## ページ範囲のブックマークを作成する

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスは、ページ範囲のブックマークを作成することを可能にします。 あなたは[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを、2つのパラメーターを使って利用できます。ブックマークリスト（ブックマークタイトルのリスト）とページリスト（ブックマークを作成するページのリスト）です。まず、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1)メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使って出力PDFを保存しなければなりません。次のコードスニペットは、ページ範囲のブックマークを作成する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## 既存のPDFファイルにブックマークを追加

既存のPDFファイルにブックマークを追加するには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスを使用します。ブックマークを作成するためには、[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクトを作成し、ブックマークの必要な属性を設定する必要があります。その後、[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクトを [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスの [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドに渡す必要があります。最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、既存のPDFファイルにブックマークを追加する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## 既存のPDFファイルに子ブックマークを追加

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスを使用して、既存のPDFファイルに子ブックマークを追加できます。 In order to add child bookmarks, you need to create [ブックマーク](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクト。 You can add individual [ブックマーク](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [ブックマーク](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. ドキュメントの翻訳: 

[Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクトを作成し、その [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) プロパティを [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) オブジェクトに設定する必要があります。その後、この [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクトを [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) と共に [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) メソッドに渡す必要があります。最後に、更新されたPDFを [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスの [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して保存します。以下のコードスニペットは、既存のPDFファイルに子ブックマークを追加する方法を示しています。




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
## See also

自分に合ったブックマークの使い方を見つけてみてください。[PDFでのブックマークの操作](/pdf/net/bookmarks/)セクションを学びましょう。