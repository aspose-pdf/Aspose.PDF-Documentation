---
title: PDF에서 링크 작업하기
linktitle: 링크
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/links/
description: 이 가이드는 PDF에 내부 페이지 링크를 추가하거나 C# 언어로 PDF에 외부 웹사이트 하이퍼링크를 삽입하는 방법에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Links in PDF programmatically",
    "alternativeHeadline": "Programmatically Add Links to PDF Files in C#",
    "abstract": "C#을 사용하여 PDF 문서 내에서 링크를 프로그래밍 방식으로 관리하는 새로운 기능을 발견하세요. 이 기능을 통해 내부 페이지 링크와 외부 웹사이트 하이퍼링크를 손쉽게 추가하여 PDF의 탐색 및 상호작용을 향상시킬 수 있습니다. PDF 관리 프로세스를 간소화하려는 개발자에게 완벽합니다!",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Working with Links, PDF programmatically, internal page link, external website hyperlink, C# language, PDF document generation, create links in PDF, extract links from PDF, update link destinations, Aspose.PDF for .NET",
    "wordcount": "118",
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
    "url": "/net/links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/links/"
    },
    "dateModified": "2024-11-25",
    "description": "이 가이드는 PDF에 내부 페이지 링크를 추가하거나 C# 언어로 PDF에 외부 웹사이트 하이퍼링크를 삽입하는 방법에 대해 설명합니다."
}
</script>

- [링크 만들기](/pdf/net/create-links/) - C#을 사용하여 PDF 파일에 링크를 만드는 간단한 방법을 배워보세요.
- [링크 업데이트](/pdf/net/update-links/) - PDF에 대상을 설정하고, 링크 목적지를 웹 주소로 설정하고, 링크 대상을 다른 PDF 파일로 설정하고, 링크 텍스트 색상을 업데이트해 보세요.
- [링크 추출하기](/pdf/net/extract-links) - AnnotationSelector 클래스를 사용하여 PDF 파일에서 링크를 추출하세요.

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