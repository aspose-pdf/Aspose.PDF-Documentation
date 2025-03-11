---
title: 양식 작업하기
linktitle: 양식 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/working-with-forms/
description: 이 섹션에서는 PDF 문서에서 AcroForms 및 XFA 양식으로 작업하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Forms",
    "alternativeHeadline": "Effortlessly Manage AcroForms and XFA in PDFs",
    "abstract": "Aspose.PDF for .NET의 새로운 기능을 발견하여 PDF 문서 내에서 AcroForms 및 XFA 양식과 원활하게 상호작용할 수 있습니다. 이 강력한 기능은 프로그래밍 방식으로 양식을 매핑하고 작성하는 과정을 단순화하여 C# 개발자의 문서 조작 능력을 향상시킵니다. 오늘 고급 PDF 양식 처리를 시작하세요!",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, XFA Forms, Aspose.PDF, PDF document generation, fill form fields, extract data from form, map PDF fields, programmatically complete PDF, XML presentation forms",
    "wordcount": "153",
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
    "url": "/net/working-with-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "이 섹션에서는 PDF 문서에서 AcroForms 및 XFA 양식으로 작업하는 방법을 설명합니다."
}
</script>

이 섹션에서는 Aspose.PDF를 사용하여 PDF 문서를 프로그래밍 방식으로 작성하는 간단하고 빠른 접근 방식을 설명합니다. 이 섹션에서는 Aspose.PDF for .NET을 사용하여 기존 PDF 내에서 AcroForms와 함께 사용할 수 있는 필드를 발견하고 매핑하는 방법에 대해서도 논의합니다. 또한 XML 기반의 프레젠테이션 양식에 대한 또 다른 기술인 XFA로 작업하는 방법도 배울 수 있습니다.

- [AcroForms](/pdf/ko/net/acroforms/) - .NET 라이브러리를 사용하여 양식을 생성하고, 양식 필드를 채우고, 양식에서 데이터를 추출하고, PDF에서 필드를 추가 및 제거합니다.
- [XFA Forms](/pdf/ko/net/xfa-forms/) - XFA 필드를 채우고, XFA를 변환하고, XFA 필드 속성을 가져옵니다.

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