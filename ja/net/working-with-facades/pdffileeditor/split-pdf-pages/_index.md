---
title: PDFページの分割
type: docs
weight: 60
url: /ja/net/split-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを分割する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## ファイルパスを使用して最初からPDFページを分割する

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor)クラスの[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1)メソッドを使用すると、PDFファイルを最初のページから指定されたページ番号まで分割できます。ディスクからPDFファイルを操作したい場合は、このメソッドに入力および出力PDFファイルのファイルパスを渡すことができます。以下のコードスニペットは、ファイルパスを使用して最初からPDFページを分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## ファイルストリームを使用して最初からPDFページを分割する

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) クラスのメソッドで、PDF ファイルを最初のページから指定したページ番号まで分割することができます。ストリームから PDF ファイルを操作したい場合は、このメソッドに入力および出力の PDF ストリームを渡すことができます。以下のコードスニペットは、ファイルストリームを使用して最初から PDF ページを分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## ファイルパスを使用して PDF ページを一括分割

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) クラスのメソッドで、PDF ファイルを複数のページセットに分割することができます。 この例では、2セットのページ (1, 2) および (5, 6) を必要とします。ディスクからPDFファイルにアクセスしたい場合は、入力PDFをファイルパスとして渡す必要があります。このメソッドはMemoryStreamの配列を返します。この配列をループして、個別のページセットを別々のファイルとして保存できます。以下のコードスニペットは、ファイルパスを使用してPDFページを分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## ストリームを使用してPDFページを一括で分割

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスの [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) メソッドを使用すると、PDFファイルを複数のページセットに分割できます。 この例では、2組のページセット（1, 2）と（5, 6）が必要です。このメソッドにストリームを渡すことで、ディスクからファイルにアクセスする代わりに使用できます。このメソッドは、MemoryStreamの配列を返します。この配列をループして、個々のページセットを別々のファイルとして保存できます。以下のコードスニペットは、ストリームを使用してPDFページを一括に分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## ファイルパスを使用してPDFページを最後まで分割

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスの [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) メソッドを使用すると、指定したページ番号からPDFファイルの末尾までを分割し、新しいPDFとして保存できます。 この作業を行うには、ファイルパスを使用して、入力および出力ファイルパスと、分割を開始するページ番号を指定する必要があります。出力されたPDFはディスクに保存されます。次のコードスニペットは、ファイルパスを使用してPDFページを最後まで分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## ストリームを使用してPDFページを最後まで分割する

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスの [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) メソッドを使用すると、指定したページ番号からPDFファイルの最後までPDFを分割し、新しいPDFとして保存することができます。 この作業を行うには、ストリームを使用して、分割を開始するページ番号とともに入力ストリームと出力ストリームを渡す必要があります。出力PDFは出力ストリームに保存されます。以下のコードスニペットは、ストリームを使用してPDFページを最後まで分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## ファイルパスを使用してPDFを個々のページに分割

{{% alert color="primary" %}}

PDFドキュメントを分割し、結果をオンラインで確認するには、次のリンクをご利用ください：

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

PDFファイルを個々のページに分割するには、PDFをファイルパスとして [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) メソッドに渡す必要があります。 このメソッドは、PDFファイルの各ページを含むMemoryStreamの配列を返します。このMemoryStreamの配列をループして、個別のページをディスク上の個別のPDFファイルとして保存できます。以下のコードスニペットは、ファイルパスを使用してPDFを個別のページに分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## ストリームを使用してPDFを個別のページに分割

PDFファイルを個別のページに分割するには、PDFをストリームとして[SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index)メソッドに渡す必要があります。 このメソッドは、PDFファイルの個々のページを含むMemoryStreamの配列を返します。このMemoryStreamの配列をループして、ディスク上に個々のPDFファイルとして個々のページを保存することもできますし、アプリケーションで後で使用するためにメモリストリーム内に保持することもできます。以下のコードスニペットは、ストリームを使用してPDFを個々のページに分割する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}