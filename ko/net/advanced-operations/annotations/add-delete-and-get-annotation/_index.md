---
title: 주석 추가, 삭제 및 가져오기
linktitle: 주석 추가, 삭제 및 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/add-delete-and-get-annotation/
description: Aspose.PDF for .NET을 사용하여 PDF 파일에서 주석을 추가, 삭제 및 가져올 수 있습니다. 작업을 해결하기 위해 모든 주석 목록을 확인하십시오.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add, Delete and Get Annotation",
    "alternativeHeadline": "Manage PDF Annotations with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET의 새로운 주석 추가, 삭제 및 가져오기 기능으로 PDF 조작 능력을 향상시키십시오. 이 강력한 기능은 사용자가 PDF 파일 내에서 주석을 원활하게 관리할 수 있도록 하여 편집을 간소화하고 콘텐츠 상호작용을 개선합니다. 특정 문서 요구 사항을 충족하기 위해 다양한 유형의 주석을 사용하는 방법을 알아보십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add annotation, delete annotation, get annotation, Aspose.PDF for .NET, PDF document generation, PDF annotations, multimedia annotation, PDF text annotation, highlights annotation, PDF manipulation library",
    "wordcount": "174",
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
    "url": "/net/add-delete-and-get-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-delete-and-get-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET을 사용하여 PDF 파일에서 주석을 추가, 삭제 및 가져올 수 있습니다. 작업을 해결하기 위해 모든 주석 목록을 확인하십시오."
}
</script>

**PDF 문서에서 주석이란 무엇인가요?**

주석은 파일에 추가하여 텍스트의 내용을 확장하고, 편집하고, 다른 사용자에게 댓글을 달기 위해 추가하는 추가 객체입니다. 문서의 텍스트를 더 읽기 쉽게 만들고, 강조 표시하고, 밑줄을 긋거나 완전히 새로운 텍스트를 추가하는 것도 가능합니다.

우리는 Aspose.PDF for .NET 라이브러리에서 사용할 수 있는 다양한 종류의 주석을 그룹으로 통합했습니다:

- [PDF 텍스트 주석](/pdf/net/text-annotation/)
- [PDF 하이라이트 주석](/pdf/net/highlights-annotation/)
- [PDF 도형 주석](/pdf/net/figures-annotation/)
- [멀티미디어 주석](/pdf/net/multimedia-annotation/)
- [PDF 스티키 주석](/pdf/net/sticky-annotations/)
- [링크 주석](/pdf/net/link-annotations/)
- [추가 주석](/pdf/net/extra-annotations/)

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