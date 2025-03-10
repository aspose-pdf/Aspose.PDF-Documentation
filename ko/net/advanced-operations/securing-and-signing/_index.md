---
title: C#에서 PDF 보안 및 서명
linktitle: PDF에서 보안 및 서명
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /ko/net/securing-and-signing/
description: 이 섹션에서는 C#을 사용하여 서명 및 PDF 문서 보안 기능에 대해 설명합니다.
lastmod: "2024-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "C#을 사용하여 PDF 문서를 보안하고 디지털 서명하는 고급 기능을 발견하십시오. 이 기능은 사용자가 다양한 알고리즘과 다이제스트 옵션으로 강력한 디지털 서명을 적용할 수 있게 하여 문서의 무결성과 진위를 보장합니다. .NET 애플리케이션에 원활하게 통합할 수 있도록 설계된 Aspose.PDF의 포괄적인 서명 기능으로 PDF 보안을 강화하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "302",
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
    "url": "/net/securing-and-signing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/securing-and-signing/"
    },
    "dateModified": "2024-02-07",
    "description": "이 섹션에서는 C#을 사용하여 서명 및 PDF 문서 보안 기능에 대해 설명합니다."
}
</script>

이 섹션에서는 C#을 사용하여 PDF 문서를 안전하게 디지털 서명하는 방법에 대해 설명합니다. 전자 서명과 디지털 서명이라는 용어는 서로 바꿔 사용할 수 있지만 본질적으로 두 가지는 다릅니다. 더 일반적으로, 디지털 서명은 [인증 기관](https://en.wikipedia.org/wiki/Certificate_authority)에서 승인한 도장을 동반하며 서명된 문서를 변조로부터 보호하는 데 사용됩니다. 반면에 전자 서명은 문서에 서명할 의도를 나타내는 데 자주 사용됩니다.

Aspose.PDF는 디지털 서명을 지원합니다:
- RSA 서명 알고리즘과 SHA-1 다이제스트를 사용하는 PKCS1.
- RSA 서명 알고리즘과 SHA-1 다이제스트를 사용하는 PKCS7.
- DSA, RSA 및 ECDSA 서명 알고리즘을 사용하는 PKCS7 분리형. 지원되는 다이제스트 알고리즘은 서명 알고리즘에 따라 다릅니다.
- 타임스탬프 서명.

PKCS7 분리형에 대한 다이제스트 알고리즘:
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

SHA-1 다이제스트 알고리즘을 사용하는 디지털 서명은 보안상의 이유로 피하는 것이 좋습니다.

- [PDF 파일 디지털 서명하기](/pdf/net/digitally-sign-pdf-file/)
- [권한 설정, PDF 파일 암호화 및 복호화](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [이미지 및 서명 정보 추출하기](/pdf/net/extract-image-and-signature-information/)
- [스마트 카드에서 PDF 문서 서명하기](/pdf/net/sign-pdf-document-from-smart-card/)

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