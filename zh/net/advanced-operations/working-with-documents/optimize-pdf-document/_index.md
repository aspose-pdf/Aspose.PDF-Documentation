---
title: 在 C# 中优化、压缩或减少 PDF 大小
linktitle: 优化 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/optimize-pdf/
description: 使用 C# 优化 PDF 文件，缩小所有图像，减少 PDF 大小，取消嵌入字体，删除未使用的对象。
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "C# 中的新 PDF 优化功能允许开发人员通过采用多种策略显著减少 PDF 文件大小，例如压缩图像、取消嵌入字体和删除未使用的对象。此增强功能提高了网络发布、电子邮件共享和存储的效率，为管理大型 PDF 文档提供了有效的解决方案。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "1983",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2025-04-01",
    "description": "使用 C# 优化 PDF 文件，缩小所有图像，减少 PDF 大小，取消嵌入字体，删除未使用的对象。"
}
</script>

PDF 文档有时可能包含额外的数据。减少 PDF 文件的大小将帮助您优化网络传输和存储。这在网页发布、社交网络共享、通过电子邮件发送或存档存储时尤其方便。我们可以使用几种技术来优化 PDF：

- 为在线浏览优化页面内容。
- 缩小或压缩所有图像。
- 启用重用页面内容。
- 合并重复的流。
- 取消嵌入字体。
- 删除未使用的对象。
- 删除扁平化表单字段。
- 删除或扁平化注释。

{{% alert color="primary" %}}

优化方法的详细说明可以在优化方法概述页面中找到。

{{% /alert %}}

## 为网络优化 PDF 文档

优化，或称为网络线性化，指的是使 PDF 文件适合使用网页浏览器在线浏览的过程。要为网页显示优化文件：

1. 在 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象中打开输入文档。
1. 使用 [Optimize](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/optimize) 方法。
1. 使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save) 方法保存优化后的文档。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下代码片段演示了如何为网络优化 PDF 文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## 减少 PDF 大小

[OptimizeResources()](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/optimizeresources) 方法允许您通过剔除不必要的信息来减少文档大小。默认情况下，此方法的工作方式如下：

- 文档页面上未使用的资源被删除。
- 相同的资源合并为一个对象。
- 未使用的对象被删除。

下面的代码片段是一个示例。不过，请注意，此方法不能保证文档缩小。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## 优化策略管理

我们还可以自定义优化策略。目前，[OptimizeResources()](https://reference.aspose.com/pdf/zh/net/aspose.pdf.document/optimizeresources/methods/1) 方法使用 5 种技术。这些技术可以通过带有 [OptimizationOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf.optimization/optimizationoptions) 参数的 OptimizeResources() 方法应用。

### 缩小或压缩所有图像

我们有两种处理图像的方法：降低图像质量和/或更改其分辨率。在任何情况下，都应应用 [ImageCompressionOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf.optimization/imagecompressionoptions)。在以下示例中，我们通过将 [ImageQuality](https://reference.aspose.com/pdf/zh/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) 降低到 50 来缩小图像。

`ImageQuality` 的工作方式类似于 JPEG 质量，其中值 0 是最低的，值 100 是最高的。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

另一种方法是以较低的分辨率调整图像大小。在这种情况下，我们应将 ResizeImages 设置为 true，并将 MaxResolution 设置为适当的值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        // If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        // Specifies maximum resolution of images. If image has higher resolition it will be scaled
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

另一个重要问题是执行时间。但我们也可以管理此设置。目前，我们可以使用两种算法 - 标准和快速。要控制执行时间，我们应设置 [Version](https://reference.aspose.com/pdf/zh/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) 属性。以下代码片段演示了快速算法：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        // Version of compression algorithm. Possible values are:
        // 1. standard compression
        // 2. fast (improved compression which is faster then standard but may be applicable not for all images)
        // 3. mixed (standard compression is applied to images which can not be compressed by faster algorithm, 
        // this may give best compression but more slow then "fast" algorithm. Version "Fast" is not applicable for 
        // resizing images (standard method will be used). Default is "Standard"
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### 删除未使用的对象

PDF 文档有时包含未从文档中的任何其他对象引用的 PDF 对象。例如，当页面从文档页面树中删除但页面对象本身未被删除时，可能会发生这种情况。删除这些对象不会使文档无效，而是缩小了文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 删除未使用的流

有时文档包含未使用的资源流。这些流不是“未使用的对象”，因为它们是从页面资源字典中引用的。因此，它们不会通过“删除未使用的对象”方法被删除。但是这些流从未与页面内容一起使用。当图像从页面中删除但未从页面资源中删除时，可能会发生这种情况。此外，当页面从文档中提取并且文档页面具有“公共”资源，即相同的 Resources 对象时，这种情况也经常发生。页面内容会被分析以确定资源流是否被使用。未使用的流会被删除。这有时会减少文档大小。使用此技术的方式类似于前一步：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 链接重复流

某些文档可能包含多个相同的资源流（例如图像）。例如，当文档与自身连接时，可能会发生这种情况。输出文档包含相同资源流的两个独立副本。我们分析所有资源流并进行比较。如果流重复，则将它们合并，即只保留一个副本。引用会相应更改，并删除对象的副本。在某些情况下，这有助于减少文档大小。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

此外，我们可以使用 [AllowReusePageContent](https://reference.aspose.com/pdf/zh/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) 设置。如果将此属性设置为 true，则在为相同页面优化文档时，页面内容将被重用。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### 取消嵌入字体

如果文档使用嵌入字体，则意味着所有字体数据都存储在文档中。优点是，无论用户的计算机上是否安装字体，文档都可以查看。但是嵌入字体会使文档变大。取消嵌入字体方法会删除所有嵌入字体。因此，文档大小减少，但如果未安装正确的字体，文档本身可能会变得不可读。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

优化资源将这些方法应用于文档。如果应用了这些方法中的任何一种，文档大小很可能会减少。如果没有应用任何这些方法，文档大小将不会改变，这是显而易见的。

## 降低 PDF 文档大小的其他方法

### 删除或扁平化注释

当注释不必要时，可以删除它们。当需要注释但不需要额外编辑时，可以将其扁平化。这两种技术都会减少文件大小。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 删除表单字段

如果 PDF 文档包含 AcroForms，我们可以尝试通过扁平化表单字段来减少文件大小。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### 将 PDF 从 RGB 颜色空间转换为灰度

PDF 文件包含文本、图像、附件、注释、图形和其他对象。您可能会遇到将 PDF 从 RGB 颜色空间转换为灰度的要求，以便在打印这些 PDF 文件时更快。此外，当文件转换为灰度时，文档大小也会减少，但这也可能导致文档质量下降。此功能目前由 Adobe Acrobat 的预检功能支持，但在谈到办公自动化时，Aspose.PDF 是提供此类文档操作的终极解决方案。为了实现此要求，可以使用以下代码片段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### FlateDecode 压缩

{{% alert color="primary" %}}

此功能由版本 18.12 或更高版本支持。

{{% /alert %}}

Aspose.PDF for .NET 提供对 PDF 优化功能的 FlateDecode 压缩支持。以下代码片段显示如何在优化中使用该选项以 **FlateDecode** 压缩存储图像：

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### 在 XImageCollection 中存储图像

Aspose.PDF for .NET 提供将新图像存储到 **XImageCollection** 中并使用 FlateDecode 压缩的能力。要启用此选项，您可以使用 **ImageFilterType.Flate** 标志。以下代码片段显示如何使用此功能：

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
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