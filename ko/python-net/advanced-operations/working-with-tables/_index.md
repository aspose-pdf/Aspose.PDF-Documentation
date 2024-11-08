---
title: Python을 사용하여 PDF에서 테이블 작업하기
linktitle: 테이블 작업하기
type: docs
weight: 50
url: /ko/python-net/working-with-tables/
description: 이 섹션은 Python 라이브러리를 사용하여 테이블을 추가하고 추출하는 방법, 테이블을 조작하는 방법을 설명합니다.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF에서 테이블 작업하기",
    "alternativeHeadline": "테이블 작업하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, tables in pdf",
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
    "url": "/python-net/working-with-tables/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-tables/"
    },
    "dateModified": "2023-09-04",
    "description": "이 기사는 Python 라이브러리를 사용하여 테이블을 추가하고 추출하는 방법, 테이블을 조작하고 통합하는 방법을 설명합니다."
}
</script>


**Aspose.PDF for Python via .NET**은 PDF 파일에서 테이블을 고급으로 다룰 수 있게 해줍니다. 이 완벽한 도구는 PDF의 단순성을 극복하여 테이블을 추출하는 데 도움을 줍니다. Python 라이브러리 리소스를 사용하여 기존 PDF 문서에 테이블을 쉽게 생성하거나 추가할 수 있으며, 테이블이 현재 페이지에서 나뉠지 여부를 결정하고, 테이블을 추출하며, 기존 PDF에서 테이블을 제거할 수 있습니다.

다음 작업을 수행할 수 있습니다:

- [기존 PDF 문서에 테이블 생성 또는 추가](/pdf/ko/python-net/add-table-in-existing-pdf-document/) - 테두리, 여백, 패딩을 고려하여 열이나 행을 병합하여 PDF 파일에 테이블을 생성합니다.
- [기존 PDF 문서에서 테이블 추출](/pdf/ko/python-net/extract-table-from-existing-pdf-document/) - PDF 파일에서 테이블을 추출할 수 있습니다.
- [기존 PDF에서 테이블 조작](/pdf/ko/python-net/manipulate-tables-in-existing-pdf/) - TableAbsorber를 사용하여 PDF에서 테이블을 조작합니다.

- [기존 PDF에서 테이블 제거](/pdf/ko/python-net/remove-tables-from-existing-pdf/) - PDF 문서에서 하나 또는 여러 개의 테이블을 제거합니다.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET 라이브러리",
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
    "applicationCategory": "Python용 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>