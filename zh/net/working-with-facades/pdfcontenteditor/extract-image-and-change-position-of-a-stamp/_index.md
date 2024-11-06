---
title: 提取图像并更改印章位置
type: docs
weight: 30
url: zh/net/extract-image-and-change-position-of-a-stamp/
description: 本节介绍如何使用 Aspose.PDF Facades 提取图像和更改印章位置。
lastmod: "2021-06-05"
draft: false
---

## 从图像印章中提取图像

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类允许您从 PDF 文件中的印章提取图像。 首先，您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。然后，调用 [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) 方法以获取 PDF 文件特定页面上的 StampInfo 对象数组。接下来，您可以使用 StampInfo.Image 属性从 StampInfo 获取图像。一旦获取了图像，您可以保存图像或处理图像的不同属性。以下代码片段展示了如何从图像印章中提取图像。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## 更改 PDF 文件中印章的位置

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类允许您更改 PDF 文件中印章的位置。 首先，您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。之后，调用 [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) 方法，使用印章索引和新位置在 PDF 文件的特定页面上移动印章。然后，您可以使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的文件。以下代码段展示了如何在特定页面移动印章。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

此外，您还可以使用 [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) 方法通过使用 StampId 移动特定印章。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}