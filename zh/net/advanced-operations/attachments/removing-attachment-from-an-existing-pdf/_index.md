---
title: 从PDF中删除附件
linktitle: 从现有PDF中删除附件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF可以从您的PDF文档中删除附件。使用C# PDF API通过Aspose.PDF库删除PDF文件中的附件。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Removing attachment from PDF",
    "alternativeHeadline": "Remove Attachments Efficiently from PDF Files",
    "abstract": "Aspose.PDF现在包含一个强大的功能，允许用户使用C# PDF API轻松地从他们的PDF文档中删除附件。此功能通过使用户能够删除文档中的任何嵌入文件，从而简化了PDF管理，确保了更清晰和更流畅的PDF体验。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Removing attachment from PDF, Aspose.PDF, delete attachments, PDF API, C# PDF library, EmbeddedFiles collection, document.Save method, PDF manipulation, attachments management, Aspose.PDF for .NET",
    "wordcount": "229",
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
    "url": "/net/removing-attachment-from-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/removing-attachment-from-an-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF可以从您的PDF文档中删除附件。使用C# PDF API通过Aspose.PDF库删除PDF文件中的附件。"
}
</script>

Aspose.PDF可以从PDF文件中删除附件。PDF文档的附件保存在Document对象的EmbeddedFiles集合中。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

要删除与PDF文件关联的所有附件：

1. 调用[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection)集合的[Delete](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection/methods/delete)方法。
1. 使用[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)对象的[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)方法保存更新后的文件。

以下代码片段演示了如何从PDF文档中删除附件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"))
    {
        // Delete all attachments
        document.EmbeddedFiles.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAttachments_out.pdf");
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