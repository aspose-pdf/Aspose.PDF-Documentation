---
title: PDF에서 첨부파일 작업하기
linktitle: 첨부파일 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 190
url: /ko/net/attachments/
description: C# PDF API를 사용하여 애플리케이션 내에서 PDF 파일의 첨부파일에 접근하고, 추가하고, 제거하는 방법을 설명합니다. C# 코드 샘플이 포함된 완벽한 가이드입니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-attachments/
    - /net/working-with-attachments-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments in PDF",
    "alternativeHeadline": "Effortlessly Manage PDF Attachments with C#",
    "abstract": "강력한 C# PDF API를 사용하여 PDF 파일의 첨부파일을 효율적으로 관리하는 방법을 알아보세요. 이 기능은 개발자가 PDF에 첨부된 다양한 파일 유형에 접근하고, 추가하고, 제거할 수 있도록 하며, 애플리케이션에 원활하게 통합할 수 있는 자세한 C# 코드 샘플이 포함되어 있습니다. 이 포괄적인 가이드를 활용하여 PDF 조작 기능을 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF API, attachments in PDF, add attachments, remove attachments, extract attachments, Aspose.PDF for .NET, manipulate PDF documents, save attachment to file, delete attachment from PDF",
    "wordcount": "181",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "C# PDF API를 사용하여 애플리케이션 내에서 PDF 파일의 첨부파일에 접근하고, 추가하고, 제거하는 방법을 설명합니다. C# 코드 샘플이 포함된 완벽한 가이드입니다."
}
</script>

이 섹션에서는 Aspose.PDF for .NET을 사용하여 PDF에서 첨부파일 작업하는 방법을 설명합니다.
첨부파일은 부모 문서에 첨부된 추가 파일로, pdf, word, 이미지 또는 기타 파일 유형이 될 수 있습니다.
PDF에 첨부파일을 추가하고, 첨부파일 정보를 가져오고, 파일로 저장하고, C#을 사용하여 프로그래밍 방식으로 PDF에서 첨부파일을 삭제하는 방법을 배우게 됩니다.

- [PDF 문서에 첨부파일 추가하기](/pdf/net/add-attachment-to-pdf-document/)
- [첨부파일 추출 및 저장하기](/pdf/net/extract-and-save-an-attachment/)
- [기존 PDF에서 첨부파일 제거하기](/pdf/net/removing-attachment-from-an-existing-pdf/)
- [포트폴리오](/pdf/net/portfolio/)

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