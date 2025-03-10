---
title: 添加图像和文本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/adding-images-and-text-using-pdffilemend-class/
description: 本节解释如何使用 PdfFileMend 类添加图像和文本。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "使用新的 PdfFileMend 类轻松增强您的 PDF 文档，该类允许您在现有 PDF 中的指定位置添加图像和文本。利用直观的 AddImage 和 AddText 方法无缝集成各种图像格式和格式化文本，确保放置和页面选择的精确性。通过自定义图像叠加和文本换行来简化您的 PDF 操作任务，使您的文档在视觉上引人注目且信息丰富。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类可以帮助您在现有 PDF 文档中指定位置添加图像和文本。它提供了两个方法，分别是 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 和 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)。 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法允许您添加 JPG、GIF、PNG 和 BMP 类型的图像。 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) 方法接受一个类型为 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类的参数，并将其添加到现有 PDF 文件中。图像和文本可以添加到由左下角和右上角坐标指定的矩形区域。在添加图像时，您可以指定图像文件路径或图像文件的流。为了指定需要添加图像或文本的页面编号，这两个方法都提供了页面编号的参数。因此，您不仅可以在指定位置添加图像和文本，还可以在指定页面上添加。

图像是 PDF 文档内容的重要组成部分。在现有 PDF 文件中操作图像是处理 PDF 文件的人员的常见需求。在本文中，我们将探讨如何借助 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 操作现有 PDF 文件中的图像。所有与图像相关的操作都已在本文中整合。

## 实现细节

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 允许您在现有 PDF 文件中添加新图像。您还可以替换或删除现有图像。PDF 文件也可以转换为图像。您可以将每个单独的页面转换为单个图像，或将整个 PDF 文件转换为一张图像。它支持 JPEG、BMP、PNG 和 TIFF 等格式。您还可以从 PDF 文件中提取图像。您可以使用 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 的四个类来实现这些操作，即 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 和 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)。

## 图像操作

在本节中，我们将详细了解这些图像操作。我们还将查看代码片段以展示相关类和方法的使用。首先，让我们看看如何在现有 PDF 文件中添加图像。我们可以使用 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类的 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法来添加新图像。使用此方法，您不仅可以指定要添加图像的页面编号，还可以指定图像的位置。

## 在现有 PDF 文件中添加图像（外观）

您可以使用 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 类的 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 方法。 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 方法需要添加的图像、需要添加图像的页面编号和坐标信息。之后，使用 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) 方法保存更新后的 PDF 文件。

在以下示例中，我们使用 imageStream 向页面添加图像：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![添加图像](/pdf/zh/net/images/add_image1.png)

借助 [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)，我们可以将一张图像叠加在另一张图像上：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![添加图像](/pdf/zh/net/images/add_image2.png)

在 PDF 文件中存储图像有几种方法。我们将在以下示例中演示其中一种：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## 在现有 PDF 文件中添加文本（外观）

我们可以通过几种方式添加文本。考虑第一种。我们获取 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 并将其添加到页面。之后，我们指明左下角的坐标，然后将文本添加到页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

查看效果：

![添加文本](/pdf/zh/net/images/add_text.png)

第二种添加 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 的方法。此外，我们指明一个矩形，以便我们的文本适合其中。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

第三个示例提供了将文本添加到指定页面的能力。在我们的示例中，让我们在文档的第 1 页和第 3 页上添加标题。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```