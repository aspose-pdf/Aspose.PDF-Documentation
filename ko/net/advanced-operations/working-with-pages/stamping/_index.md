---
title: Aspose.PDF를 사용한 C#으로 스탬핑하기
linktitle: 스탬핑
type: docs
weight: 120
url: ko/net/stamping/
description: 이 섹션에서는 PDF 페이지에 이미지 스탬프와 텍스트 스탬프를 추가하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-stamp-in-a-pdf-file/
    - /net/adding-text-stamp-watermark/
    - /net/add-text-and-image-stamp/   
    - /net/add-pdf-page-stamp/
    - /net/extract-image-and-change-position-of-a-stamp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF를 사용한 C#으로 스탬핑하기",
    "alternativeHeadline": "PDF에 이미지 스탬프 추가하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 스탬프, 이미지 스탬프",
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
    "url": "/net/stamping/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/stamping/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 PDF 페이지에 이미지 스탬프와 텍스트 스탬프를 추가하는 방법을 설명합니다."
}
</script>
PDF 문서의 도장은 종이 문서에 고무 도장을 찍는 것과 유사합니다.
PDF 파일의 도장은 PDF 파일의 추가 정보를 제공하는데, 이는 다른 사람이 PDF 파일을 사용하는 것을 보호하고 PDF 파일의 내용의 보안을 확인하는 데 사용됩니다. **Aspose.PDF for .NET**은 PDF 문서에 이미지 또는 텍스트 도장을 추가할 수 있습니다.

다음 섹션에서 C#을 사용하여 도장을 추가하는 방법을 확인하세요:

- [PDF 페이지에 이미지 도장 추가](/pdf/net/image-stamps-in-pdf-page/) - 이미지 도장 추가, 이미지 품질 제어, PDF 파일의 배경으로 이미지 도장 사용.
- [PDF 파일에 텍스트 도장 추가](/pdf/net/text-stamps-in-the-pdf-file/) - 텍스트 도장 추가, TextStamp 객체의 정렬 정의, PDF 파일에 도장으로 텍스트 채우기.

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


