---
title: PDF에서 첨부파일 제거
linktitle: 기존 PDF에서 첨부파일 제거
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부파일을 제거할 수 있습니다. C# PDF API를 사용하여 Aspose.PDF 라이브러리로 PDF 파일에서 첨부파일을 제거하세요.
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
    "abstract": "Aspose.PDF는 이제 사용자가 C# PDF API를 사용하여 PDF 문서에서 첨부파일을 쉽게 제거할 수 있는 강력한 기능을 포함하고 있습니다. 이 기능은 사용자가 문서에서 모든 내장 파일을 삭제할 수 있게 하여 PDF 관리를 간소화하고, 더 깔끔하고 효율적인 PDF 경험을 보장합니다.",
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
    "description": "Aspose.PDF는 PDF 문서에서 첨부파일을 제거할 수 있습니다. C# PDF API를 사용하여 Aspose.PDF 라이브러리로 PDF 파일에서 첨부파일을 제거하세요."
}
</script>

Aspose.PDF는 PDF 파일에서 첨부파일을 제거할 수 있습니다. PDF 문서의 첨부파일은 Document 객체의 EmbeddedFiles 컬렉션에 저장됩니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

PDF 파일과 관련된 모든 첨부파일을 삭제하려면:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션의 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection/methods/delete) 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 업데이트된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 첨부파일을 제거하는 방법을 보여줍니다.

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