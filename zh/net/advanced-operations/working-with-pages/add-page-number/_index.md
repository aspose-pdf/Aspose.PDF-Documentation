---
title: 将页码添加到PDF
linktitle: 添加页码
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /zh/net/add-page-number/
description: Aspose.PDF for .NET允许您使用PageNumber Stamp类将页码印章添加到PDF文件中。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Page Number to PDF",
    "alternativeHeadline": "Add Dynamic Page Numbering to PDF",
    "abstract": "Aspose.PDF for .NET引入了一种强大的页码印章功能，使页码无缝集成到PDF文档中。此功能通过允许用户自定义格式、对齐和样式来增强文档的导航和组织，从而提高可读性和专业呈现。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Page Number, PDF Stamp, Aspose.PDF for .NET, PageNumberStamp class, Document object, PageNumberStamp properties, Bates numbering, PDF document generation, Page number stamp, C# PDF manipulation",
    "wordcount": "559",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET允许您使用PageNumber Stamp类将页码印章添加到PDF文件中。"
}
</script>

所有文档必须包含页码。页码使读者更容易定位文档的不同部分。
**Aspose.PDF for .NET**允许您使用PageNumberStamp添加页码。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

您可以使用[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)类在PDF文件中添加页码印章。[PageNumber Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)类提供了创建基于页码的印章所需的属性，如格式、边距、对齐、起始编号等。为了添加页码印章，您需要使用所需属性创建一个[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)对象和一个[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)对象。之后，您可以调用[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)的[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)方法将印章添加到PDF中。您还可以设置页码印章的字体属性。以下代码片段向您展示如何在PDF文件中添加页码。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageNumberStamp.pdf"))
    {
        // Create page number stamp
        var pageNumberStamp = new Aspose.Pdf.PageNumberStamp();
        // Whether the stamp is background
        pageNumberStamp.Background = false;
        pageNumberStamp.Format = "Page # of " + document.Pages.Count;
        pageNumberStamp.BottomMargin = 10;
        pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
        pageNumberStamp.StartingNumber = 1;
        // Set text properties
        pageNumberStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        pageNumberStamp.TextState.FontSize = 14.0F;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        pageNumberStamp.TextState.ForegroundColor = Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(pageNumberStamp);
        // Save PDF document
        document.Save(dataDir + "PageNumberStamp_out.pdf");  
    }
}
```

## 实时示例

[添加PDF页码](https://products.aspose.app/pdf/page-number)是一个在线免费Web应用程序，允许您调查添加页码功能的工作原理。

[![如何使用C#在pdf中添加页码](page_number.png)](https://products.aspose.app/pdf/page-number)

## 添加/删除Bates编号

**Bates编号**（也称为Bates印章）用于法律、医疗和商业领域，在图像和文档上放置识别号码和/或日期/时间标记，例如，在准备审判的发现阶段或识别商业收据时。此过程提供了识别、保护和图像或文档的自动连续编号。

Aspose.PDF目前对Bates编号的支持有限。此功能将根据客户的请求进行更新。

### 如何删除Bates编号

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveBatesNumbering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveBatesNumberingInput.pdf"))
    {
        foreach (var page in document.Pages)
        {
            // Remove bates numbering
            var artifacts = page.Artifacts.Where(ar => ar.CustomSubtype == "BatesN");
            foreach (var artifact in artifacts)
            {
                page.Artifacts.Delete(artifact);   
            }
        }
        // Save PDF document
        document.Save(dataDir + "RemoveBatesNumbering_out.pdf");
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