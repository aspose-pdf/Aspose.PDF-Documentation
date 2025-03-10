---
title: 从 PDF 文件中提取链接
linktitle: 提取链接
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/extract-links/
description: 了解如何使用 Aspose.PDF 在 .NET 中从 PDF 文档中提取超链接，以进行内容管理和链接分析。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Links from the PDF File",
    "alternativeHeadline": "Effortlessly Extract Links from PDF Files",
    "abstract": "使用新的 AnnotationSelector 类无缝提取 PDF 文件中的链接。此功能允许开发人员轻松识别和提取 PDF 文档指定页面中的链接注释，从而增强需要精确链接提取的应用程序的 PDF 操作能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Links, PDF extraction, C# PDF library, AnnotationSelector class, LinkAnnotation objects, PDF document manipulation, Aspose.PDF library, extract links from PDF",
    "wordcount": "303",
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
    "url": "/net/extract-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-links/"
    },
    "dateModified": "2024-11-25",
    "description": "使用 C# 从 PDF 中提取链接。本主题向您解释如何使用 AnnotationSelector 类提取链接。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 从 PDF 文件中提取链接

链接在 PDF 文件中表示为注释，因此要提取链接，请提取所有 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 对象。

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象。
1. 获取您想要提取链接的 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 类从指定页面提取所有 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 对象。
1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 对象传递给 Page 对象的 Accept 方法。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 对象的 Selected 属性将所有选定的链接注释获取到 IList 对象中。

以下代码片段向您展示如何从 PDF 文件中提取链接。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractLinks.pdf"))
    {
        // Extract actions
        var page = document.Pages[1];
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
        page.Accept(selector);
        var list = selector.Selected;
        var annotation = (Aspose.Pdf.Annotations.Annotation)list[0];

        // Save PDF document
        document.Save(dataDir + "ExtractLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ExtractLinks.pdf");

    // Extract actions
    var page = document.Pages[1];
    var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
    page.Accept(selector);
    var list = selector.Selected;
    var annotation = (Aspose.Pdf.Annotations.Annotation)list[0];

    // Save PDF document
    document.Save(dataDir + "ExtractLinks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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