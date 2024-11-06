---
title: 删除 PDF 页面
type: docs
weight: 70
url: zh/net/delete-pdf-pages/
description: 本节介绍如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 删除 PDF 页面。
lastmod: "2021-06-05"
draft: false
---

如果您想从磁盘上的 PDF 文件中删除一些页面，您可以使用 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 方法的重载，该方法接受以下三个参数：输入文件路径、要删除的页码数组和输出 PDF 文件路径。第二个参数是一个整数数组，表示需要删除的所有页面。指定的页面将从输入文件中删除，并将结果保存为输出文件。下面的代码片段向您展示了如何使用文件路径删除 PDF 页面。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## 使用流删除 PDF 页面

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 方法属于 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类，也提供了一个重载，允许您从输入的 PDF 文件中删除页面，而输入和输出文件都在流中。此重载需要以下三个参数：输入流、要删除的 PDF 页面的整数数组和输出流。以下代码片段向您展示如何使用流删除 PDF 页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}