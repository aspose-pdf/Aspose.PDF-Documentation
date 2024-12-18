---
title: 파이썬을 사용하여 PDF에서 텍스트 작업하기
linktitle: 텍스트 작업하기
type: docs
weight: 30
url: /ko/python-net/working-with-text/
description: 이 섹션에서는 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF for Python을 사용하여 텍스트 추가, 교체, 회전, 검색하는 방법을 배웁니다.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF에서 텍스트 작업하기",
    "alternativeHeadline": "PDF 파일에서 텍스트 추가, 회전, 검색 및 삭제",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 텍스트 추가, 텍스트 검색, 텍스트 삭제, pdf에서 텍스트 조작",
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
    "url": "/python-net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-text/"
    },
    "dateModified": "2024-01-04",
    "description": "이 섹션에서는 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF for Python을 사용하여 텍스트 추가, 교체, 회전, 검색하는 방법을 배웁니다."
}
</script>


우리는 모두 때때로 PDF 파일에 텍스트를 추가해야 했습니다. 예를 들어, 주요 텍스트 아래에 번역을 추가하거나, 이미지 옆에 캡션을 배치하거나, 단지 신청서를 작성할 때 그렇습니다. 모든 텍스트 요소를 원하는 스타일로 형식화할 수 있다면 더욱 유용합니다. PDF 파일에서 가장 인기 있는 텍스트 조작은 다음과 같습니다: PDF에 텍스트 추가, PDF 파일 내 텍스트 형식화, 문서 내 텍스트 교체 및 회전. **Aspose.PDF for Python via .NET**은 PDF 콘텐츠와 상호 작용하는 데 필요한 모든 것을 갖춘 최고의 솔루션입니다.

다음 작업을 수행할 수 있습니다:

- [PDF 파일에 텍스트 추가하기](/pdf/ko/python-net/add-text-to-pdf-file/) - PDF에 텍스트를 추가하고 스트림 및 파일에서 폰트를 사용하고, HTML 문자열을 추가하고, 하이퍼링크를 추가하는 등의 작업을 수행합니다.
- [PDF 툴팁](/pdf/ko/python-net/pdf-tooltip/) - Python을 사용하여 보이지 않는 버튼을 추가하여 검색된 텍스트에 툴팁을 추가할 수 있습니다.
- [PDF 내 텍스트 형식화](/pdf/ko/python-net/text-formatting-inside-pdf/) - 문서 내 텍스트를 형식화할 때 문서에 추가할 수 있는 많은 기능이 있습니다.
 줄 들여쓰기 추가, 텍스트 테두리 추가, 텍스트 밑줄 추가, Aspose.PDF 라이브러리를 사용하여 줄 바꿈 추가.
- [PDF에서 텍스트 교체하기](/pdf/ko/python-net/replace-text-in-pdf/) - PDF 문서의 모든 페이지에서 텍스트를 교체합니다. 먼저 TextFragmentAbsorber를 사용해야 합니다.
- [PDF 내부 텍스트 회전](/pdf/ko/python-net/rotate-text-inside-pdf/) - TextFragment 클래스의 회전 속성을 사용하여 PDF 내부의 텍스트를 회전합니다.
- [PDF 문서 페이지에서 텍스트 검색 및 가져오기](/pdf/ko/python-net/search-and-get-text-from-pdf/) - 페이지에서 텍스트를 검색하고 가져오려면 TextFragmentAbsorber 클래스를 사용할 수 있습니다.
- [줄 바꿈 결정하기](/pdf/ko/python-net/determine-line-break/) - 이 주제는 다중 줄 텍스트 조각의 줄 바꿈을 추적하는 방법을 설명합니다.

```json
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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