---
title: C#를 사용한 PDF에서 텍스트 작업
linktitle: 텍스트 작업
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/working-with-text/
description: 이 섹션에서는 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF와 C#을 사용하여 텍스트를 추가, 교체, 회전 및 검색하는 방법을 배우십시오.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "Aspose.PDF for .NET를 사용하여 PDF에서 강력한 텍스트 조작 기능을 발견하십시오. 이 기능은 사용자가 PDF 문서 내에서 텍스트를 원활하게 추가, 교체, 회전 및 형식화할 수 있도록 하여 문서의 상호작용성과 사용자 정의를 향상시킵니다. C# 개발자를 위해 맞춤화된 효율적인 검색 기능과 유연한 텍스트 처리 기술로 애플리케이션을 강화하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2024-11-26",
    "description": "이 섹션에서는 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF와 C#을 사용하여 텍스트를 추가, 교체, 회전 및 검색하는 방법을 배우십시오."
}
</script>

우리는 모두 때때로 PDF 파일에 텍스트를 추가해야 했습니다. 예를 들어, 주요 텍스트 아래에 번역을 추가하거나, 이미지 옆에 캡션을 배치하거나, 단순히 신청서를 작성할 때 유용합니다. 모든 텍스트 요소를 원하는 스타일로 형식화할 수 있다면 더욱 도움이 됩니다. PDF 파일에서 가장 인기 있는 텍스트 조작은 PDF에 텍스트 추가, PDF 파일 내 텍스트 형식화, 문서 내 텍스트 교체 및 회전입니다. **Aspose.PDF for .NET**는 PDF 콘텐츠와 상호작용하는 데 필요한 모든 것을 갖춘 최고의 솔루션입니다.

다음 작업을 수행할 수 있습니다:

- [PDF 파일에 텍스트 추가](/pdf/ko/net/add-text-to-pdf-file/) - PDF에 텍스트를 추가하고, 스트림 및 파일에서 글꼴을 사용하고, HTML 문자열을 추가하고, 하이퍼링크를 추가하는 등의 작업을 수행합니다.
- [PDF 툴팁](/pdf/ko/net/pdf-tooltip/) - C#을 사용하여 검색된 텍스트에 보이지 않는 버튼을 추가하여 툴팁을 추가할 수 있습니다.
- [PDF 내 텍스트 형식화](/pdf/ko/net/text-formatting-inside-pdf/) - 텍스트를 형식화할 때 문서에 추가할 수 있는 많은 기능이 있습니다. Aspose.PDF 라이브러리를 사용하여 줄 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가, 줄 바꿈 추가 등을 할 수 있습니다.
- [FloatingBox 사용하기](/pdf/ko/net/floating-box/) - Floating Box 도구는 PDF 페이지에 텍스트 및 기타 콘텐츠를 배치하기 위한 특별한 도구입니다.
- [PDF에서 텍스트 교체](/pdf/ko/net/replace-text-in-pdf/) - PDF 문서의 모든 페이지에서 텍스트를 교체합니다. 먼저 TextFragmentAbsorber를 사용해야 합니다.
- [PDF 내 텍스트 회전](/pdf/ko/net/rotate-text-inside-pdf/) - TextFragment 클래스의 회전 속성을 사용하여 PDF 내 텍스트를 회전합니다.
- [PDF 문서의 페이지에서 텍스트 검색 및 가져오기](/pdf/ko/net/search-and-get-text-from-pdf/) - 페이지에서 텍스트를 검색하고 가져오기 위해 TextFragmentAbsorber 클래스를 사용할 수 있습니다.
- [줄 바꿈 결정하기](/pdf/ko/net/determine-line-break/) - 이 주제에서는 다중 줄 텍스트 조각의 줄 바꿈을 추적하는 방법을 설명합니다.

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