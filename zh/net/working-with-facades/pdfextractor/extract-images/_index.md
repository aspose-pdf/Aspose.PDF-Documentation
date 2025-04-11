---
title: 使用 PdfExtractor 提取图像
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/extract-images/
description: 本节解释如何使用 PdfExtractor 类通过 Aspose.PDF Facades 提取图像。
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "Aspose.PDF 的 PdfExtractor 功能使用户能够高效地从 PDF 文档中提取图像，提供多种选项，例如从整个文档、特定页面或指定范围提取图像。它支持将图像直接保存到文件或内存流中，增强了开发人员处理 PDF 资产的灵活性。这一强大的功能允许对图像提取模式进行精确控制，使处理不同 PDF 内容类型变得更加容易。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 从整个 PDF 提取图像到文件 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类允许您从 PDF 文件中提取图像。首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。之后，调用 [ExtractImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。为了将图像保存到磁盘，您可以调用 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法以文件路径作为参数。以下代码片段演示了如何从整个 PDF 提取图像到文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## 从整个 PDF 提取图像到流 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类允许您将图像从 PDF 文件提取到流中。首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。之后，调用 [ExtractImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。为了将图像保存到流中，您可以调用 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法以 Stream 作为参数。以下代码片段演示了如何从整个 PDF 提取图像到流。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## 从 PDF 的特定页面提取图像 (Facades)

您可以从 PDF 文件的特定页面提取图像。为此，您需要将 [StartPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性设置为您想要提取图像的特定页面。首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。其次，您必须设置 [StartPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性。之后，调用 [ExtractImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。您可以将图像保存到磁盘或流中。您只需调用适当的 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载。以下代码片段演示了如何从 PDF 的特定页面提取图像到流。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## 从 PDF 的一系列页面提取图像 (Facades)

您可以从 PDF 文件的一系列页面提取图像。为此，您需要将 [StartPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性设置为您想要提取图像的页面范围。首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。其次，您必须设置 [StartPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/startpage) 和 [EndPage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/endpage) 属性。之后，调用 [ExtractImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。您可以将图像保存到磁盘或流中。您只需调用适当的 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载。以下代码片段演示了如何从 PDF 的一系列页面提取图像到流。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## 使用图像提取模式提取图像 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类允许您从 PDF 文件中提取图像。Aspose.PDF 支持两种提取模式；第一种是 ActuallyUsedImage，它提取 PDF 文档中实际使用的图像。第二种模式是 [DefinedInResources](https://reference.aspose.com/pdf/zh/net/aspose.pdf/extractimagemode)，它提取 PDF 文档资源中定义的图像（默认提取模式）。首先，您需要创建一个 [PdfExtractor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。之后，使用 [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) 属性指定图像提取模式。然后调用 [ExtractImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 方法，根据您指定的模式将所有图像提取到内存中。一旦图像被提取，您可以借助 [HasNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 和 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法获取这些图像。您需要使用 while 循环遍历所有提取的图像。为了将图像保存到磁盘，您可以调用 [GetNextImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 方法的重载，该方法以文件路径作为参数。

以下代码片段演示了如何使用 ExtractImageMode 选项从 PDF 文件中提取图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

要检查 PDF 是否包含文本或图像，请使用下一个代码片段：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```