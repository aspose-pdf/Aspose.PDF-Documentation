---
title: 파이썬을 사용하여 AcroForms 작업하기
linktitle: AcroForms
type: docs
weight: 10
url: /python-net/acroforms/
description: Aspose.PDF for Python을 사용하여 처음부터 폼을 생성하고, PDF 문서에서 폼 필드를 채우고, 폼에서 데이터를 추출하는 등의 작업을 수행할 수 있습니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 AcroForms 작업하기",
    "alternativeHeadline": "PDF에서 AcroForms 작업을 위한 옵션",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf의 acroforms",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python을 사용하여 처음부터 폼을 생성하고, PDF 문서에서 폼 필드를 채우고, 폼에서 데이터를 추출하는 등의 작업을 수행할 수 있습니다."
}
</script>


## AcroForms의 기초

**AcroForms** - Adobe의 독특한 PDF 폼 기술. AcroForms는 페이지 지향적인 폼입니다. 처음 등장한 것은 1998년입니다. 데이터 형식 또는 FDF와 XML 폼 데이터 형식 또는 xFDF의 형태로 입력을 받습니다. 서드파티 제공자들이 AcroForms를 지원합니다. Adobe가 AcroForms를 도입했을 때, 그들은 이를 "PDF 폼"이라고 불렀습니다. 이 폼은 Adobe Acrobat Pro/Standard의 작성자이며 정적 또는 동적 XFA 폼의 특별한 종류가 아닙니다. AcroForms는 휴대성이 뛰어나고 모든 플랫폼에서 작동합니다.

AcroForms를 사용하여 PDF 폼 문서에 추가 페이지를 추가할 수 있습니다. 템플릿 개념 덕분에 AcroForms를 사용하여 여러 데이터베이스 레코드로 폼을 채우는 것을 지원할 수 있습니다.

PDF 1.7은 데이터와 PDF 폼을 통합하는 두 가지 다른 방법을 지원합니다.

*AcroForms (Acrobat forms로도 알려져 있음)*, PDF 1.2 형식 사양에 도입 및 포함됨.

Java 라이브러리의 기능을 더 자세히 배우려면 다음 기사를 참조하십시오:

- [Create AcroForm](/pdf/python-net/create-form) - Python으로 처음부터 폼 생성.
- [Fill AcroForm](/pdf/python-net/fill-form) - PDF 문서에서 양식 필드를 채웁니다.
- [Extract AcroForm](/pdf/python-net/extract-form) - PDF 문서의 모든 필드 또는 개별 필드에서 값을 가져옵니다.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF 조작 라이브러리 for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>