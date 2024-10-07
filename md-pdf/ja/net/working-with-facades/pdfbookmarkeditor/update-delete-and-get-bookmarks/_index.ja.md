---
title: Update, Delete and Get Bookmarks
type: docs
weight: 30
url: /net/update-delete-and-get-bookmarks/
description: このセクションでは、Aspose.PDF Facadesを使用してブックマークを更新、削除、および取得する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイル内の既存のブックマークを更新する

PDFファイル内の既存のブックマークを更新するには、[ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks)メソッドを使用する必要があります。 このメソッドは2つの引数を取ります：ソースタイトル（変更するブックマークのタイトル）、デスティネーションタイトル（置き換えるタイトル）。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) メソッドを呼び出し、続いて [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFを保存します。以下のコードスニペットは、PDFファイル内の既存のブックマークを変更する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## PDFファイルからすべてのブックマークを削除

[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) メソッドを使用して、任意のパラメータなしでPDFファイルからすべてのブックマークを削除できます。 最初に、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新された PDF ファイルを保存する必要があります。次のコードスニペットは、PDF ファイルからすべてのブックマークを削除する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## PDFファイルから特定のブックマークを削除する

特定のブックマークを削除するには、文字列（タイトル）パラメーターを使用して [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) メソッドを呼び出す必要があります。 *title* は、PDF から削除されるブックマークを表しています。[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力 PDF ファイルをバインドします。その後、[DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) メソッドを呼び出し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新された PDF ファイルを保存します。以下のコードスニペットは、特定のブックマークを PDF ファイルから削除する方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## PDF ドキュメントのファサードからブックマークを取得

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) クラスは、既存の PDF ファイル内のブックマークを操作する機能を提供します。 それはブックマークに関する情報を取得/設定するためのさまざまなプロパティを提供します。次のコードスニペットは、PDFファイル内の各ブックマークに関連する情報を取得する方法を示しています。

## 既存のPDFファイルからブックマークを抽出する

[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) メソッドは、PDFファイルからブックマークを抽出することを可能にします。 In order to extract the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method.

ブックマークを抽出するためには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用してPDFファイルをバインドする必要があります。 その後、[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) メソッドを呼び出す必要があります。[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) メソッドは [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index) オブジェクトを返します。その後、これらのブックマークをループして、個々の [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) オブジェクトを取得できます。最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、ブックマークをXMLファイルにエクスポートする方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}