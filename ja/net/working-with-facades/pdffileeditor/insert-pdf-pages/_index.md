---
title: PDFページの挿入
type: docs
weight: 50
url: /ja/net/insert-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを挿入する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## ファイルパスを使用して2つの数値の間にPDFページを挿入する

特定のページ範囲を、あるPDFから別のPDFに[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドを使用して挿入できます。 そのためには、ページを挿入したい入力PDFファイル、挿入のためにページを取るポートファイル、ページを挿入する場所、および入力PDFファイルに挿入する必要があるポートファイルのページの範囲が必要です。この範囲は、開始ページと終了ページのパラメータで指定されます。最後に、指定された範囲のページが入力ファイルに挿入された状態で出力PDFファイルが保存されます。次のコードスニペットは、ファイルストリームを使用して、2つの数値の間にPDFページを挿入する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## ファイルパスを使用してPDFページの配列を挿入

特定のページを別のPDFファイルに挿入したい場合は、ページの整数配列を必要とする[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドのオーバーロードを使用できます。 この配列では、入力PDFファイルに挿入したい特定のページを指定できます。そのためには、ページを挿入したい入力PDFファイル、挿入のためにページを取得するポートファイル、ページを挿入する場所、そして入力PDFファイルに挿入する必要があるポートファイルのページの整数配列が必要です。この配列には、入力PDFファイルに挿入することに興味のある特定のページのリストが含まれています。最後に、指定されたページ配列が挿入された出力PDFファイルが保存されます。
次のコードスニペットは、ファイルパスを使用してPDFページの配列を挿入する方法を示しています。

## ストリームを使用して2つの数字の間にPDFページを挿入する

ストリームを使用してページ範囲を挿入したい場合は、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドの適切なオーバーロードを使用するだけです。 そのためには、ページを挿入したい入力PDFストリーム、挿入するためにページを取得するポートストリーム、ページを挿入する場所、および入力PDFストリームに挿入する必要のあるポートストリームのページ範囲が必要です。この範囲は、開始ページと終了ページのパラメータで指定されます。最後に、指定された範囲のページが入力ストリームに挿入された状態で出力PDFストリームが保存されます。以下のコードスニペットは、ストリームを使用して2つの番号の間にPDFページを挿入する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbersUsingStreams-InsertPagesBetweenNumbersUsingStreams.cs" >}}

## ストリームを使用してPDFページの配列を挿入する

ストリームを使用して、ページの整数配列を必要とするInsertメソッドの適切なオーバーロードを使用することで、ページの配列を別のPDFファイルに挿入することもできます。 この配列では、入力PDFストリームに挿入したい特定のページを指定できます。そのためには、ページを挿入したい入力PDFストリーム、挿入のためにページを取り出すポートストリーム、ページを挿入する場所、入力PDFファイルに挿入しなければならないポートストリームからのページの整数配列が必要です。この配列には、入力PDFストリームに挿入することに興味のある特定のページのリストが含まれています。最終的に、指定されたページの配列が挿入された出力PDFストリームが保存されます。以下のコードスニペットは、ストリームを使用してPDFページの配列を挿入する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesUsingStreams-InsertPagesUsingStreams.cs" >}}