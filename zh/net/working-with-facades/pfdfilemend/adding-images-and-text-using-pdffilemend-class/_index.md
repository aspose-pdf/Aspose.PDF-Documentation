---
title: 添加图像和文本 
type: docs
weight: 10
url: /zh/net/adding-images-and-text-using-pdffilemend-class/
description: 本节解释如何使用 PdfFileMend 类添加图像和文本。
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类可以帮助您在现有的 PDF 文档中，在指定位置添加图像和文本。 它提供了两个方法，名称为 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 和 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)。 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法允许您添加 JPG、GIF、PNG 和 BMP 类型的图像。 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) 方法接受一个 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类类型的参数，并将其添加到现有的 PDF 文件中。图像和文本可以添加到由左下角和右上角点的坐标指定的矩形区域中。在添加图像时，您可以指定图像文件路径或图像文件的流。为了指定需要添加图像或文本的页码，这两种方法都提供了页码参数。因此，您不仅可以在指定位置添加图像和文本，还可以在指定页面上添加。

图像是 PDF 文档内容的重要组成部分。 操控现有 PDF 文件中的图像是处理 PDF 文件的常见需求。在本文中，我们将探讨如何借助 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 在现有 PDF 文件中操控图像。[Aspose.PDF for .NET](/pdf/zh/net/) 的所有与图像相关的操作都已在本文中整合。

## 实施细节

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 允许您在现有的 PDF 文件中添加新图像。 你还可以替换或删除现有图像。PDF 文件也可以转换为图像。您可以将每个单独的页面转换为单个图像，或者将整个 PDF 文件转换为一个图像。它允许您使用多种格式，例如 JPEG、BMP、PNG 和 TIFF 等。您还可以从 PDF 文件中提取图像。您可以使用 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 的四个类来实现这些操作，即 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 和 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)。

## 图像操作

在本节中，我们将详细了解这些图像操作。 我们还将看到代码片段，以展示相关类和方法的使用。首先，让我们看看如何在现有的 PDF 文件中添加图像。我们可以使用 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类的 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法来添加新图像。使用此方法，您不仅可以指定要添加图像的页码，还可以指定图像的位置。

## 在现有 PDF 文件中添加图像 (Facades)

您可以使用 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类的 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 方法。 The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 方法需要加入的图像、需要添加图像的页码和坐标信息。之后，使用 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) 方法保存更新后的PDF文件。

在下面的示例中，我们使用 imageStream 向页面添加图像：

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // 加载图像到流中
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // 保存输出文件
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/zh/net/images/add_image1.png)

借助于 [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)，我们可以将一个图像叠加在另一个图像上：
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 将图像加载到流中
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 保存输出文件
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/zh/net/images/add_image2.png)

有几种方法可以将图像存储在PDF文件中。我们将在下面的示例中演示其中一种方法：

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 将图像加载到流中
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 保存输出文件
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 将图像加载到流中
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 保存输出文件
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## 在现有 PDF 文件中添加文本（外观）

我们可以通过多种方式添加文本。 考虑第一个。我们获取 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 并将其添加到页面中。之后，我们指明左下角的坐标，然后将文本添加到页面。

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

检查它的外观：

![添加文本](/pdf/zh/net/images/add_text.png)

添加 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 的第二种方式。此外，我们指明一个矩形以适应我们的文本。

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
第三个示例提供了向指定页面添加文本的功能。在我们的示例中，让我们在文档的第 1 页和第 3 页添加一个标题。

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```