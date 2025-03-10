---
title: 使用 C# 旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/rotate-pages/
description: 本主题描述了如何使用 C# 程序化地旋转现有 PDF 文件中的页面方向。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate PDF Pages Using C#",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with C#",
    "abstract": "Aspose.PDF for .NET 中的新功能允许开发人员以编程方式更改现有 PDF 文件中页面的方向。用户可以轻松在横向和纵向模式之间切换，确保内容在新布局中适当适应，从而增强文档的可用性和展示效果。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "236",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "本主题描述了如何使用 C# 程序化地旋转现有 PDF 文件中的页面方向。"
}
</script>

本主题描述了如何使用 C# 程序化地更新或更改现有 PDF 文件中页面的方向。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 更改页面方向

从 Aspose.PDF for .NET 9.6.0 版本开始，我们添加了很棒的新功能，例如将页面方向从横向更改为纵向，反之亦然。要更改页面方向，请使用以下代码片段设置页面的 MediaBox。您还可以通过使用 Rotate() 方法设置旋转角度来更改页面方向。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePageOrientation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        foreach (Page page in document.Pages)
        {
            Aspose.Pdf.Rectangle r = page.MediaBox;
            double newHeight = r.Width;
            double newWidth = r.Height;
            double newLLX = r.LLX;
            //  We must to move page upper in order to compensate changing page size
            // (lower edge of the page is 0,0 and information is usually placed from the
            //  Top of the page. That's why we move lover edge upper on difference between
            //  Old and new height.
            double newLLY = r.LLY + (r.Height - newHeight);
            page.MediaBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Sometimes we also need to set CropBox (if it was set in original file)
            page.CropBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Setting Rotation angle of page
            page.Rotate = Rotation.on90;
        }
        // Save PDF document
        document.Save(dataDir + "ChangeOrientation_out.pdf");
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