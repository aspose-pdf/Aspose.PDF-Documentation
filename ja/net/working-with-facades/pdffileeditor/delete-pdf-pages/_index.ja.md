---
title: PDFページの削除
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを削除する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

ディスク上にあるPDFファイルから複数のページを削除したい場合は、[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) メソッドのオーバーロードを使用できます。このメソッドは次の3つのパラメータを取ります：入力ファイルパス、削除するページ番号の配列、出力PDFファイルパス。2番目のパラメータは、削除する必要のあるすべてのページを表す整数の配列です。指定されたページは入力ファイルから削除され、その結果が出力ファイルとして保存されます。以下のコードスニペットは、ファイルパスを使用してPDFページを削除する方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## ストリームを使用してPDFページを削除する

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスに属し、入力 PDF ファイルからページを削除するためのオーバーロードを提供します。このオーバーロードは、入力ファイルと出力ファイルの両方がストリームにある場合に使用します。このオーバーロードは、以下の3つのパラメーターを取ります: 入力ストリーム、削除するPDFページの整数配列、および出力ストリーム。以下のコードスニペットは、ストリームを使用してPDFページを削除する方法を示しています。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}