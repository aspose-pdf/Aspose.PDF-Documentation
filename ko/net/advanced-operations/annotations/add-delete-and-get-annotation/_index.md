---
title: 주석 추가, 삭제 및 가져오기
linktitle: 주석 추가, 삭제 및 가져오기
type: docs
weight: 20
url: /ko/net/add-delete-and-get-annotation/
description: Aspose.PDF for .NET을 사용하면 PDF 파일에서 주석을 추가, 삭제 및 가져올 수 있습니다. 작업을 해결하기 위해 모든 주석 목록을 확인하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "주석 추가, 삭제 및 가져오기",
    "alternativeHeadline": "PDF 파일에서 주석 작업",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 주석 추가, 주석 가져오기, 주석 삭제",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 PDF 파일에서 주석을 추가, 삭제 및 가져올 수 있습니다. 작업을 해결하기 위해 모든 주석 목록을 확인하세요."
}
</script>
**PDF 문서에서의 주석은 무엇입니까?**

이것들은 텍스트의 내용을 확장하고, 수정하고, 다른 사용자를 위한 코멘트를 추가하기 위해 파일에 추가하는 추가 객체입니다. 또한 문서의 텍스트를 더 읽기 쉽게 만들고, 강조하고, 밑줄을 긋거나 완전히 새로운 텍스트를 추가할 수도 있습니다.

Aspose.PDF for .NET 라이브러리에서 사용 가능한 다양한 종류의 주석을 그룹으로 묶었습니다:

- [PDF 텍스트 주석](/pdf/ko/net/text-annotation/)
- [PDF 하이라이트 주석](/pdf/ko/net/highlights-annotation/)
- [PDF 도형 주석](/pdf/ko/net/figures-annotation/)
- [멀티미디어 주석](/pdf/ko/net/multimedia-annotation/)
- [PDF 스티키 주석](/pdf/ko/net/sticky-annotations/)
- [링크 주석](/pdf/ko/net/link-annotations/)
- [추가 주석](/pdf/ko/net/extra-annotations/)

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

