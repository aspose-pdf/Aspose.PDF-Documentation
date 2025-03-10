---
title: 将页眉和页脚添加到PDF
linktitle: 将页眉和页脚添加到PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET允许您使用TextStamp类向PDF文件添加页眉和页脚。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET介绍了一项强大的功能，允许用户通过添加可自定义的页眉和页脚来丰富他们的PDF文档。使用TextStamp和ImageStamp类，开发人员可以轻松集成文本和图像，调整其位置和外观以适应各种文档格式和样式。这增强了文档的专业性和可读性，使其非常适合报告、发票和其他正式通信。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET允许您使用TextStamp类向PDF文件添加页眉和页脚。"
}
</script>

**Aspose.PDF for .NET**允许您在现有的PDF文件中添加页眉和页脚。您可以向PDF文档添加图像或文本。此外，尝试使用C#在一个PDF文件中添加不同的页眉。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

## 在PDF文件的页眉中添加文本

您可以使用[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp)类在PDF文件的页眉中添加文本。TextStamp类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加文本，您需要使用所需的属性创建一个Document对象和一个TextStamp对象。之后，您可以调用Page的AddStamp方法将文本添加到PDF的页眉中。

您需要以适当的方式设置TopMargin属性，以便将文本调整到PDF的页眉区域。您还需要将HorizontalAlignment设置为Center，将VerticalAlignment设置为Top。

以下代码片段演示了如何使用C#在PDF文件的页眉中添加文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## 在PDF文件的页脚中添加文本

您可以使用TextStamp类在PDF文件的页脚中添加文本。TextStamp类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚中添加文本，您需要使用所需的属性创建一个Document对象和一个TextStamp对象。之后，您可以调用Page的AddStamp方法将文本添加到PDF的页脚中。

{{% alert color="primary" %}}

您需要以适当的方式设置Bottom Margin属性，以便将文本调整到PDF的页脚区域。您还需要将HorizontalAlignment设置为Center，将VerticalAlignment设置为Bottom。

{{% /alert %}}

以下代码片段演示了如何使用C#在PDF文件的页脚中添加文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## 在PDF文件的页眉中添加图像

您可以使用[ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp)类在PDF文件的页眉中添加图像。Image Stamp类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加图像，您需要使用所需的属性创建一个Document对象和一个Image Stamp对象。之后，您可以调用[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)方法将图像添加到PDF的页眉中。

{{% alert color="primary" %}}

您需要以适当的方式设置TopMargin属性，以便将图像调整到PDF的页眉区域。您还需要将HorizontalAlignment设置为Center，将VerticalAlignment设置为Top。

{{% /alert %}}

以下代码片段演示了如何使用C#在PDF文件的页眉中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## 在PDF文件的页脚中添加图像

您可以使用Image Stamp类在PDF文件的页脚中添加图像。Image Stamp类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚中添加图像，您需要使用所需的属性创建一个Document对象和一个Image Stamp对象。之后，您可以调用Page的AddStamp方法将图像添加到PDF的页脚中。

{{% alert color="primary" %}}

您需要以适当的方式设置[BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin)属性，以便将图像调整到PDF的页脚区域。您还需要将[HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment)设置为`Center`，将[VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment)设置为`Bottom`。

{{% /alert %}}

以下代码片段演示了如何使用C#在PDF文件的页脚中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## 在一个PDF文件中添加不同的页眉

我们知道可以通过使用TopMargin或Bottom Margin属性在文档的页眉/页脚部分添加TextStamp，但有时我们可能需要在单个PDF文档中添加多个页眉/页脚。**Aspose.PDF for .NET**解释了如何做到这一点。

为了实现这一要求，我们将创建单独的TextStamp对象（对象的数量取决于所需的页眉/页脚数量），并将它们添加到PDF文档中。我们还可以为每个印章对象指定不同的格式信息。在以下示例中，我们创建了Document对象和三个TextStamp对象，然后使用Page的[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)方法将文本添加到PDF的页眉部分。以下代码片段演示了如何使用Aspose.PDF for .NET在PDF文件的页脚中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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