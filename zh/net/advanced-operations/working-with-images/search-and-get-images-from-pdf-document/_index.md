---
title: 在PDF中获取和搜索图像
linktitle: 搜索和获取图像
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/search-and-get-images-from-pdf-document/
description: 学习如何使用Aspose.PDF在Java中搜索和提取PDF文档中的图像以进行媒体检索。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Search Images in PDF",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Documents",
    "abstract": "发现使用Aspose.PDF库搜索和提取PDF文档中图像的新功能。此功能简化了在多个页面中定位图像的过程，使用户能够轻松检索图像属性，如尺寸和分辨率，使用简单的代码片段。通过利用这一高效的图像处理功能，提升您的PDF文档操作技能。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get images, search images, PDF document, Aspose.PDF library, ImagePlacementAbsorber, ImagePlacements, .NET PDF manipulation, document image extraction, image placement properties, code examples",
    "wordcount": "316",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "本节解释如何使用Aspose.PDF库搜索和获取PDF文档中的图像。"
}
</script>

ImagePlacementAbsorber允许您在PDF文档的所有页面中搜索图像。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

要在整个文档中搜索图像：

1. 调用Pages集合的Accept方法。Accept方法接受一个ImagePlacementAbsorber对象作为参数。这将返回一个ImagePlacement对象的集合。
1. 遍历ImagePlacements对象并获取其属性（图像、尺寸、分辨率等）。

以下代码片段演示了如何在文档中搜索所有图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(abs);

        // Loop through all ImagePlacements, get image and ImagePlacement properties
        foreach (var imagePlacement in abs.ImagePlacements)
        {
            // Get the image using ImagePlacement object
            var image = imagePlacement.Image;

            // Display image placement properties for all placements
            Console.Out.WriteLine("image width: " + imagePlacement.Rectangle.Width);
            Console.Out.WriteLine("image height: " + imagePlacement.Rectangle.Height);
            Console.Out.WriteLine("image LLX: " + imagePlacement.Rectangle.LLX);
            Console.Out.WriteLine("image LLY: " + imagePlacement.Rectangle.LLY);
            Console.Out.WriteLine("image horizontal resolution: " + imagePlacement.Resolution.X);
            Console.Out.WriteLine("image vertical resolution: " + imagePlacement.Resolution.Y);
        }
    }
}

```

要从单个页面获取图像，请使用以下代码：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromAnIndividualPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages[1].Accept(abs);
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