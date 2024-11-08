---
title: ページプロパティの操作
type: docs
weight: 80
url: /ja/net/manipulate-page-properties/
description: このセクションでは、PdfPageEditor クラスを使用して Aspose.PDF Facades でページプロパティを操作する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルからPDFページプロパティを取得する

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) は、PDFファイルの個々のページを操作することができます。 個々のページのプロパティを取得するのに役立ちます。異なるページボックスサイズ、ページの回転、ページのズームなどです。これらのプロパティを取得するためには、[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。その後、さまざまなメソッドを使用してページプロパティを取得することができます。例えば、[GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)、[GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)、[GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) などです。

次のコードスニペットは、既存のPDFファイルからPDFページのプロパティを取得する方法を示しています。




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## 既存のPDFファイルでPDFページプロパティを設定する

ページの回転、ズーム、または原点を設定するには、[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスを使用する必要があります。このクラスは、これらのページプロパティを設定するためのさまざまなメソッドとプロパティを提供します。まず、[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。その後、これらのメソッドとプロパティを使用してページプロパティを設定できます。最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFファイルを保存します。

次のコードスニペットは、既存のPDFファイルでPDFページプロパティを設定する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## 特定のページのPDFファイルの内容をリサイズ

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスの ResizeContents メソッドを使用すると、PDFファイル内のページ内容をリサイズできます。[ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) クラスは、ページをリサイズするために使用するパラメータを指定するために使用されます。例えば、パーセンテージや単位でマージンを指定することができます。すべてのページをリサイズすることも、ResizeContents メソッドを使用してリサイズするページの配列を指定することもできます。

次のコードスニペットは、PDFファイルの特定のページの内容をどのようにリサイズするかを示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}