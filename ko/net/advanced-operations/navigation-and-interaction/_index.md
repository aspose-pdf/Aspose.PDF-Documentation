---
title: PDF에서의 탐색 및 상호작용
linktitle: 탐색 및 상호작용
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /ko/net/navigation-and-interaction/
description: 이 섹션에서는 링크, 작업 및 북마크 작업의 기능을 설명합니다.
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
    "url": "/net/navigation-and-interaction/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/navigation-and-interaction/"
    },
    "dateModified": "2024-11-25",
    "description": "이 섹션에서는 링크, 작업 및 북마크 작업의 기능을 설명합니다."
}
</script>

- [링크](/pdf/net/links/) - C#으로 링크를 쉽게 생성, 업데이트 및 추출할 수 있습니다.
- [작업](/pdf/net/actions/) - PDF 파일에 하이퍼링크를 추가하고 가져오는 것이 가능합니다. 또한 이 기사에서는 PDF 파일에서 문서 열기 작업을 제거하는 방법과 문서를 볼 때 PDF 페이지를 지정하는 방법을 배울 수 있습니다.
- [북마크](/pdf/net/bookmarks/) - 대규모 출판물은 일반적으로 북마크 패널에서 쉽게 보고 선택할 수 있는 북마크 프레임워크를 포함하고 있어, 북마크를 클릭하여 해당 페이지나 장으로 이동할 수 있습니다. 북마크 패널은 콘텐츠 인식 요소이며, 열린 PDF 문서에 북마크 구조가 포함되어 있을 때만 사이드바에 표시됩니다.

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