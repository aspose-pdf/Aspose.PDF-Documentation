---
title: Convert PDF File
type: docs
weight: 30
url: /zh/net/convert-pdf-file/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfConverter 类转换 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

## 将 PDF 页面转换为不同的图像格式（Facades）

为了将 PDF 页面转换为不同的图像格式，您需要创建 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法打开 PDF 文件。 在此之后，你需要调用 [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) 方法来进行初始化任务。然后，你可以使用 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 方法遍历所有页面。[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 方法允许你创建特定页面的图像。你还需要传递 ImageFormat 给此方法，以便创建特定类型的图像，即 JPEG、GIF 或 PNG 等。最后，调用 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) 方法。以下代码片段展示了如何将 PDF 页面转换为图像。

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // 创建 PdfConverter 对象
            PdfConverter converter = new PdfConverter();

            // 绑定输入的 pdf 文件
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // 初始化转换过程
            converter.DoConvert();

            // 检查页面是否存在然后逐一转换为图像
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // 关闭 PdfConverter 对象
            converter.Close();
        }
```
在下一个代码片段中，我们将展示如何更改一些参数。使用 [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) 我们设置框架 'CropBox'。此外，我们可以通过指定每英寸点数来更改 [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution)。下一个是 [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - 表单呈现模式。然后我们指示 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage)，它设置转换开始的页码。我们还可以通过设置范围来指定最后一页。

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // 创建 PdfConverter 对象
            PdfConverter converter = new PdfConverter();

            // 绑定输入 pdf 文件
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // 初始化转换过程
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // 检查页面是否存在，然后逐个转换为图像
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // 关闭 PdfConverter 对象
            converter.Close();
        }
```

## 另请参阅

Aspose.PDF for .NET 允许将 PDF 文档转换为多种格式，也可以从其他格式转换为 PDF。此外，您可以使用 Aspose.PDF 转换应用程序在线检查 Aspose.PDF 转换的质量并查看结果。了解[转换](/pdf/zh/net/converting/)部分以解决您的任务。