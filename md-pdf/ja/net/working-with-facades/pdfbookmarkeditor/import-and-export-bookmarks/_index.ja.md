---
title: ブックマークのインポートとエクスポート
type: docs
weight: 20
url: /net/import-and-export-bookmarks/
description: このセクションでは、Aspose.PDF Facadesを使用してブックマークをインポートおよびエクスポートする方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルにXMLからブックマークをインポートする

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) メソッドを使用すると、XMLファイルからPDFファイルにブックマークをインポートできます。 ブックマークをインポートするためには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用してPDFファイルをバインドする必要があります。その後、[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1)メソッドを呼び出します。最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、XMLファイルからブックマークをインポートする方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## 既存のPDFファイルからXMLにブックマークをエクスポートする

ExportBookmarksToXmlメソッドは、PDFファイルからXMLファイルにブックマークをエクスポートすることを可能にします。

ブックマークをエクスポートするには:

1. Create a PdfBookmarkEditor オブジェクトを作成し、BindPdf メソッドを使用して PDF ファイルをバインドします。
1. ExportBookmarksToXml メソッドを呼び出します。
1. Save メソッドを使用して更新された PDF ファイルを保存します。

次のコードスニペットは、ブックマークを XML ファイルにエクスポートする方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}