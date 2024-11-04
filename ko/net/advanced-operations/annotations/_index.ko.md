---
title: 주석 작업하기
linktitle: PDF의 주석
type: docs
weight: 100
url: /net/annotations/
description: 이 섹션에서는 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 모든 종류의 주석을 사용하는 방법을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 주석",
    "alternativeHeadline": "PDF에서 주석 작업하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 주석",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 모든 종류의 주석을 사용하는 방법을 보여줍니다."
}
</script>

PDF 페이지 내용은 편집하기 어렵지만, PDF 사양은 페이지 내용을 변경하지 않고 PDF 페이지에 추가할 수 있는 객체의 전체 세트를 정의합니다.

이러한 객체들을 주석이라고 하며, 페이지 내용을 표시하는 것부터 양식과 같은 대화형 기능을 구현하는 것에 이르기까지 그 목적이 다양합니다.

PDF 뷰어는 일반적으로 텍스트 하이라이트, 메모, 선 또는 도형과 같은 다양한 주석 유형의 생성 및 편집을 허용합니다. 생성할 수 있는 주석 유형에 관계없이 PDF 사양을 준수하는 PDF 뷰어는 모든 주석 유형에 대한 렌더링도 지원해야 합니다.

주석은 PDF 파일의 중요한 부분입니다. Aspose.PDF for .NET을 사용하면 새 주석을 추가하고, 기존 주석을 편집하고, 주석을 삭제하는 등의 작업을 할 수 있습니다. 이 섹션에서는 다음 주제를 다룹니다:

다음을 수행할 수 있습니다:

- [주석 개요](/pdf/net/overview-of-annotations/) - PDF 사양에서 정의하는 주석 유형과 Aspose.PDF가 지원하는 내용을 학습합니다.
- [주석 추가, 삭제 및 가져오기](/pdf/net/add-delete-and-get-annotation/) - 이 섹션에서는 허용된 모든 유형의 주석을 사용하는 방법을 설명합니다.
- [주석 추가, 삭제 및 가져오기](/pdf/net/add-delete-and-get-annotation/) - 이 섹션에서는 허용된 모든 유형의 주석을 다루는 방법을 설명합니다.
- [XFDF 형식으로 주석 가져오기 및 내보내기](/pdf/net/import-export-xfdf/) - Aspose.PDF 라이브러리는 XFDF 파일로 주석 데이터를 가져오고 내보내는 메소드를 제공합니다.

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

