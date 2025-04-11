---
title: 使用 C# 更改 PDF 页面大小
linktitle: 更改 PDF 页面大小
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/change-page-size/
description: 使用 Aspose.PDF for .NET 库更改 PDF 文档的页面大小。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change PDF Page Size with C#",
    "alternativeHeadline": "Effortlessly Resize PDF Pages in C#",
    "abstract": "Aspose.PDF for .NET 中的新功能使开发人员能够轻松地以编程方式更改 PDF 文档的页面大小。只需几行代码，用户就可以修改现有 PDF 的尺寸，增强文档管理能力，并确保与各种布局要求的兼容性。此功能简化了将 PDF 页面调整为所需格式（如 A4）的过程，直接在 .NET 应用程序中进行。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "300",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2024-11-26",
    "description": "使用 Aspose.PDF for .NET 库更改 PDF 文档的页面大小。"
}
</script>

## 更改 PDF 页面大小

Aspose.PDF for .NET 让您可以在 .NET 应用程序中通过简单的代码行更改 PDF 页面大小。 本主题解释了如何更新/更改现有 PDF 文件的页面尺寸（大小）。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

[Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 类包含 SetPageSize(...) 方法，允许您设置页面大小。以下代码片段通过几个简单的步骤更新页面尺寸：

1. 加载源 PDF 文件。
1. 将页面获取到 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 对象中。
1. 获取指定页面。
1. 调用 SetPageSize(..) 方法以更新其尺寸。
1. 调用 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 类的 Save(..) 方法以生成具有更新页面尺寸的 PDF 文件。

{{% alert color="primary" %}}

请注意，高度和宽度属性使用点作为基本单位，其中 1 英寸 = 72 点，1 厘米 = 1/2.54 英寸 = 0.3937 英寸 = 28.3 点。

{{% /alert %}}

以下代码片段演示如何将 PDF 页面尺寸更改为 A4 大小。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.SetPageSize(597.6, 842.4);
        // Save PDF document
        document.Save(dataDir + "UpdateDimensions_out.pdf"); 
    }
}
```

## 获取 PDF 页面大小

您可以使用 Aspose.PDF for .NET 读取现有 PDF 文件的页面大小。以下代码示例演示了如何使用 C# 读取 PDF 页面尺寸。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Adds a blank page to pdf document
        Page page = document.Pages.Count > 0 ? document.Pages[1] : document.Pages.Add();
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
        // Rotate page at 90 degree angle
        page.Rotate = Rotation.on90;
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
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