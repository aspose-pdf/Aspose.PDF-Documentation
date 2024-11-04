---
title: PDF에서 첨부 파일 다루기
linktitle: 첨부 파일 다루기
type: docs
weight: 130
url: /net/attachments/
description: C# PDF API를 사용하여 애플리케이션 내에서 PDF 파일의 첨부 파일에 접근하고 추가 및 제거하는 방법을 안내합니다. C# 코드 샘플이 포함된 완벽한 가이드입니다.
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
    "headline": "PDF에서 첨부 파일 다루기",
    "alternativeHeadline": "PDF 파일의 첨부 파일",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF의 첨부 파일",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2022-02-04",
    "description": "C# PDF API를 사용하여 애플리케이션 내에서 PDF 파일의 첨부 파일에 접근하고 추가 및 제거하는 방법을 안내합니다. C# 코드 샘플이 포함된 완벽한 가이드입니다."
}
</script>
이 섹션에서는 Aspose.PDF for .NET을 사용하여 PDF에서 첨부 파일을 다루는 방법을 설명합니다.
첨부 파일은 부모 문서에 첨부된 추가 파일로, pdf, word, image 또는 기타 파일 유형일 수 있습니다.
PDF에 첨부 파일을 추가하고, 첨부 파일 정보를 가져오고, 파일로 저장하고, C#을 사용하여 프로그래밍 방식으로 PDF에서 첨부 파일을 삭제하는 방법을 배우게 됩니다.

- [PDF 문서에 첨부 파일 추가](/pdf/net/add-attachment-to-pdf-document/)
- [첨부 파일 추출 및 저장](/pdf/net/extract-and-save-an-attachment/)
- [기존 PDF에서 첨부 파일 제거](/pdf/net/removing-attachment-from-an-existing-pdf/)
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
To provide a thorough translation, please include the document content that you need translated into Korean.
