---
title: 提取图像使用 PdfExtractor
type: docs
weight: 20
url: zh/net/extract-images/
description: 本节说明如何使用 Aspose.PDF Facades 中的 PdfExtractor 类提取图像。
lastmod: "2021-07-15"
---

## 从整个 PDF 中提取图像到文件 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类允许您从 PDF 文件中提取图像。 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入的 PDF 文件。 在那之后，调用 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取出来，你可以使用 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。你需要使用 while 循环遍历所有提取的图像。为了将图像保存到磁盘，你可以调用 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法将文件路径作为参数。以下代码片段向你展示了如何将整个 PDF 中的图像提取到文件中。

```csharp
   public static void ExtractImagesWholePDF()
        {
            // 打开输入 PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // 提取所有图像
            pdfExtractor.ExtractImage();

            // 获取所有提取的图像
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## 从整个 PDF 中提取图像到流 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类允许您将 PDF 文件中的图像提取到流中。 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. 首先，你需要创建一个[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)类的对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)方法绑定输入的PDF文件。 接下来，调用 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取出来，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。为了将图像保存到流中，您可以调用 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法以流作为参数。以下代码片段向您展示如何将整个 PDF 的图像提取到流中。

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // 打开输入 PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // 提取图像
            pdfExtractor.ExtractImage();
            // 获取所有提取的图像
            while (pdfExtractor.HasNextImage())
            {
                // 将图像读入内存流
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // 如果您愿意，可以将其写入磁盘，或者以其他方式使用它。
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## 从PDF特定页面提取图像 (Facades)

您可以从PDF文件的特定页面提取图像。 为了做到这一点，您需要将 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性设置为您想要提取图像的特定页面。 首先，您需要创建一个[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)类的对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)方法绑定输入的PDF文件。 Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * 和 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性。 在那之后，调用 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。图像提取完成后，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。您可以选择将图像保存到磁盘或流中。您只需调用 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的适当重载。以下代码片段展示了如何将 PDF 特定页面的图像提取到流中。

```csharp
public static void ExtractImagesParticularPage()
{
    // 打开输入 PDF
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // 设置 StartPage 和 EndPage 属性到您想要提取图像的页码
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // 提取图像
    pdfExtractor.ExtractImage();
    // 获取提取的图像
    while (pdfExtractor.HasNextImage())
    {
        // 将图像读入内存流
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // 如果需要，可以写入磁盘，或以其他方式使用。
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## 从 PDF 的页面范围中提取图像 (Facades)

您可以从 PDF 文件的页面范围中提取图像。 为了做到这一点，你需要将 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性设置为你想要提取图像的页面范围。 首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入的 PDF 文件。 其次，您必须设置 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性。 之后，调用 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取，你可以借助 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。你需要使用 while 循环遍历所有提取的图像。你可以选择将图像保存到磁盘或流中。你只需调用 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的适当重载。以下代码片段展示了如何从 PDF 的页面范围中提取图像到流中。

```csharp
public static void ExtractImagesRangePages()
{
    // 打开输入 PDF
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // 设置 StartPage 和 EndPage 属性为你想要提取图像的页码
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // 提取图像
    pdfExtractor.ExtractImage();
    // 获取提取的图像
    while (pdfExtractor.HasNextImage())
    {
        // 将图像读入内存流
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // 写入磁盘，如果你愿意，或者以其他方式使用它。
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## 提取图像使用图像提取模式（Facades）

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类允许您从 PDF 文件中提取图像。 Aspose.PDF 支持两种提取模式；第一种是 ActuallyUsedImage，它提取实际用于 PDF 文档中的图像。 第二种模式是 [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode)，用于提取在 PDF 文档资源中定义的图像（默认提取模式）。 First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.  

首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入的 PDF 文件。 在此之后，使用 [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) 属性指定图像提取模式。然后调用 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法，根据您指定的模式将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。为了将图像保存到磁盘，您可以调用 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法将文件路径作为参数。

以下代码片段向您展示了如何使用 ExtractImageMode 选项从 PDF 文件中提取图像。
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // 打开输入 PDF
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // 指定图像提取模式
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // 基于图像提取模式提取图像
    extractor.ExtractImage();

    // 获取所有提取的图像
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

检查 PDF 是否包含文本或图像请使用以下代码片段：

```csharp
public static void CheckIfPdfContainsTextOrImages()
{
    // 实例化一个内存流对象以保存从文档中提取的文本
    MemoryStream ms = new MemoryStream();
    // 实例化 PdfExtractor 对象
    PdfExtractor extractor = new PdfExtractor();

    // 将输入 PDF 文档绑定到提取器
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // 从输入 PDF 文档中提取文本
    extractor.ExtractText();
    // 将提取的文本保存到一个文本文件中
    extractor.GetText(ms);
    // 检查内存流的长度是否大于或等于 1

    bool containsText = ms.Length >= 1;

    // 从输入 PDF 文档中提取图像
    extractor.ExtractImage();

    // 在 while 循环中调用 HasNextImage 方法。当图像提取完毕时，循环将退出
    bool containsImage = extractor.HasNextImage();

    // 现在找出这个 PDF 是仅包含文本、仅包含图像，还是两者都包含

    if (containsText && !containsImage)
        Console.WriteLine("PDF 仅包含文本");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF 仅包含图像");
    else if (containsText && containsImage)
        Console.WriteLine("PDF 包含文本和图像");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF 既不包含文本也不包含图像");
}
```