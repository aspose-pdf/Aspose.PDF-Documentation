---
title: 操作页面属性
type: docs
weight: 80
url: /net/manipulate-page-properties/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfPageEditor 类操作页面属性。
lastmod: "2021-06-05"
draft: false
---

## 从现有 PDF 文件获取 PDF 页面属性

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 允许您处理 PDF 文件的单个页面。 它帮助您获取单个页面的属性，如不同的页面框大小、页面旋转、页面缩放等。为了获取这些属性，您需要创建一个[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor)对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)方法绑定输入的PDF文件。之后，您可以使用不同的方法获取页面属性，如[GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)，[GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)，[GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize)等。

以下代码片段向您展示如何从现有的PDF文件中获取PDF页面属性。




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## 设置现有 PDF 文件的 PDF 页面属性

为了设置页面属性如页面旋转、缩放或原点，你需要使用 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类。该类提供了不同的方法和属性来设置这些页面属性。首先，你需要创建一个 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，你可以使用这些方法和属性来设置页面属性。最后，使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。

以下代码片段向你展示了如何在现有 PDF 文件中设置 PDF 页面属性。




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## 调整 PDF 文件中特定页面的内容大小

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类的 ResizeContents 方法允许您调整 PDF 文件中页面内容的大小。[ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) 类用于指定调整页面大小的参数，例如百分比或单位等的边距。您可以调整所有页面的大小，或者使用 ResizeContents 方法指定要调整大小的页面数组。

以下代码片段显示了如何调整 PDF 文件中特定页面的内容大小。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}