---
title: 拆分 PDF 页面
type: docs
weight: 60
url: zh/net/split-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 拆分 PDF 页面。
lastmod: "2021-06-05"
draft: false
---

## 从第一页开始使用文件路径拆分 PDF 页面

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类的 [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 方法允许您从第一页开始到指定页码结束拆分 PDF 文件。如果您想从磁盘操作 PDF 文件，可以将输入和输出 PDF 文件的文件路径传递给此方法。以下代码片段向您展示了如何使用文件路径从第一页开始拆分 PDF 页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## 从第一页开始使用文件流拆分 PDF 页面

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 方法属于 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类，允许您从第一页开始并在指定的页码结束拆分 PDF 文件。如果您想从流中操作 PDF 文件，可以将输入和输出 PDF 流传递给此方法。以下代码片段向您展示了如何使用文件流拆分 PDF 页。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## 使用文件路径批量拆分 PDF 页

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) 方法属于 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类，允许您将 PDF 文件拆分成多组页面。 在这个例子中，我们需要两组页面（1, 2）和（5, 6）。如果您想从磁盘访问PDF文件，您需要将输入PDF作为文件路径传递。此方法返回一个MemoryStream数组。您可以遍历此数组并将各个页面集保存为单独的文件。以下代码片段展示了如何使用文件路径批量拆分PDF页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## 使用流批量拆分PDF页面

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您将PDF文件拆分为多组页面。 在这个例子中，我们需要两组页面 (1, 2) 和 (5, 6)。您可以传递一个流给这个方法，而不是从磁盘访问文件。这个方法返回一个 MemoryStream 数组。您可以遍历这个数组，并将每组页面另存为单独的文件。以下代码片段向您展示如何使用流批量拆分 PDF 页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## 使用文件路径拆分 PDF 页面到终点

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 方法属于 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类，允许您从指定的页码开始拆分 PDF 直到 PDF 文件的结尾，并将其另存为一个新的 PDF。 为了实现这一点，使用文件路径，您需要传递输入和输出文件路径以及需要开始拆分的页码。输出的PDF将被保存到磁盘。以下代码片段向您展示如何使用文件路径拆分PDF页面到末尾。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## 使用流拆分PDF页面到末尾

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您从指定的页码开始拆分PDF到PDF文件的末尾并将其保存为一个新的PDF。 为了做到这一点，使用流，您需要传递输入和输出流以及需要开始拆分的页码。输出的 PDF 将保存到输出流。下面的代码片段向您展示如何使用流拆分 PDF 页。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## 使用文件路径将 PDF 拆分为单个页面

{{% alert color="primary" %}}

您可以尝试拆分 PDF 文档并在此链接在线查看结果：

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

为了将 PDF 文件拆分为单个页面，您需要将 PDF 作为文件路径传递给 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 方法。 此方法将返回一个包含 PDF 文件各个页面的 MemoryStream 数组。您可以遍历此 MemoryStream 数组，并将各个页面作为单独的 PDF 文件保存在磁盘上。以下代码片段向您展示了如何使用文件路径将 PDF 拆分为单个页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## 使用流将 PDF 拆分为单个页面

为了将 PDF 文件拆分为单个页面，您需要将 PDF 作为流传递给 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 方法。 该方法将返回一个包含 PDF 文件各个页面的 MemoryStream 数组。您可以遍历这个 MemoryStream 数组，将各个页面单独保存为磁盘上的 PDF 文件，或者您可以将这些单独的页面保存在内存流中，以便在应用程序中稍后使用。以下代码片段向您展示如何使用流将 PDF 拆分为单个页面。