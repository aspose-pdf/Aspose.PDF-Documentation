---
title: 使用 C# 将图像添加到 PDF
linktitle: 添加图像
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/add-image-to-existing-pdf-file/
description: 本节描述了如何使用 C# 库将图像添加到现有 PDF 文件中。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "Aspose.PDF 库中的新功能允许用户无缝地使用 C# 将图像添加到现有 PDF 文件中。此功能通过直接在文档中启用图像的精确定位和缩放，简化了 PDF 操作，确保高质量的集成和对视觉元素的控制。支持多种图像格式和配置，此工具增强了 PDF 内容管理的灵活性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "1747",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2025-04-08",
    "description": "本节描述了如何使用 C# 库将图像添加到现有 PDF 文件中。"
}
</script>

## 在现有 PDF 文件中添加图像

每个 PDF 页面包含资源和内容属性。资源可以是图像和表单，而内容由一组 PDF 操作符表示。每个操作符都有其名称和参数。此示例使用操作符将图像添加到 PDF 文件中。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

要将图像添加到现有 PDF 文件中：

- 创建一个 Document 对象并打开输入 PDF 文档。
- 获取要添加图像的页面。
- 将图像添加到页面的资源集合中。
- 使用操作符将图像放置在页面上：
- 使用 GSave 操作符保存当前图形状态。
- 使用 ConcatenateMatrix 操作符指定图像放置的位置。
- 使用 Do 操作符在页面上绘制图像。
- 最后，使用 GRestore 操作符保存更新后的图形状态。
- 保存文件。
以下代码片段演示了如何在 PDF 文档中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

默认情况下，JPEG 质量设置为 100%。要应用更好的压缩和质量，请使用以下重载：

{{% /alert %}}

- 在 XImageCollection 类中添加了 Replace 方法重载：public void Replace(int index, Stream stream, int quality)
- 在 XImageCollection 类中添加了 Add 方法重载：public void Add(Stam stream, int quality)

## 在现有 PDF 文件中添加图像（外观）

还有一种替代的、更简单的方法可以将图像添加到 PDF 文件中。您可以使用 [PdfFileMend](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilemend) 类的 [AddImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法。[AddImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法需要添加的图像、需要添加图像的页面编号和坐标信息。之后，使用 Close 方法保存更新后的 PDF 文件。以下代码片段演示了如何在现有 PDF 文件中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

有时，在将图像插入 PDF 之前，需要裁剪图像。您可以使用 `AddImage()` 方法来支持添加裁剪后的图像：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## 在页面上放置图像并保持（控制）纵横比

如果我们不知道图像的尺寸，就有可能在页面上得到失真的图像。以下示例展示了避免这种情况的一种方法。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

有时，添加到 PDF 的大图像在缩放时会遇到问题。以下代码片段根据 PDF 页面尺寸缩放图像，确保图像适合并看起来更好。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var pdfImageSection = document.Pages.Add();
        using (var stream = new FileStream(file, FileMode.Open))
        {
            // Open bitmap
            using (var img = new Bitmap(stream))
            {
                // Scale image according to page dimensions
                using (var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height))
                {
                    using (var ms = new MemoryStream())
                    {
                        scaledImg.Save(ms, ImageFormat.Jpeg);
                        ms.Seek(0, SeekOrigin.Begin);
                        var image = new Aspose.Pdf.Image
                        {
                            ImageStream = ms
                        };

                        // Add the image to the page
                        pdfImageSection.Paragraphs.Add(image);

                        // Save PDF document
                        document.Save("AddImageAccordingToPage.pdf");
                    }
                }
            }
        }
    }
}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using (var graphics = Graphics.FromImage(newImage))
    {
        graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    }
    return newImage;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    
    // Add page
    var pdfImageSection = document.Pages.Add();
    using var stream = new FileStream(file, FileMode.Open);
    // Open bitmap
    using var img = new Bitmap(stream);
    // Scale image according to page dimensions
    using var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height);
    using var ms = new MemoryStream();
    scaledImg.Save(ms, ImageFormat.Jpeg);
    ms.Seek(0, SeekOrigin.Begin);
    var image = new Aspose.Pdf.Image
    {
        ImageStream = ms
    };

    // Add the image to the page
    pdfImageSection.Paragraphs.Add(image);

    // Save PDF document
    document.Save("AddImageAccordingToPage.pdf");

}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using var graphics = Graphics.FromImage(newImage);
    graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    return newImage;
}
```
{{< /tab >}}
{{< /tabs >}}

## 确定 PDF 中的图像是彩色还是黑白

可以对图像应用不同类型的压缩以减少其大小。应用于图像的压缩类型取决于源图像的 ColorSpace，即如果图像是彩色（RGB），则应用 JPEG2000 压缩，如果是黑白，则应应用 JBIG2/JBIG2000 压缩。因此，识别每种图像类型并使用适当的压缩类型将产生最佳/优化的输出。

PDF 文件可能包含文本、图像、图形、附件、注释等元素，如果源 PDF 文件包含图像，我们可以确定图像的颜色空间并应用适当的压缩以减少 PDF 文件大小。以下代码片段展示了识别 PDF 中图像是彩色还是黑白的步骤。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## 控制图像质量

可以控制添加到 PDF 文件中的图像的质量。使用 [XImageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/ximagecollection) 类中的重载 [Replace](https://reference.aspose.com/pdf/zh/net/aspose.pdf.ximagecollection/replace/methods/1) 方法。

以下代码片段演示了如何将文档中的所有图像转换为使用 80% 质量进行压缩的 JPEG。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## 支持对图像应用裁剪蒙版

在基础位图图像上放置矢量形状作为蒙版，仅暴露与矢量形状对齐的基础设计部分。形状外部的所有区域将被隐藏。

代码片段加载一个 PDF，打开两个图像文件，并将这些图像作为模板蒙版应用于 PDF 第一页的前两个图像。

可以通过 'XImage.AddStencilMask(Stream maskStream)' 方法添加模板蒙版：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>