---
title: PDF에서 C#을 사용한 텍스트 작업
linktitle: 텍스트 작업
type: docs
weight: 30
url: /ko/net/working-with-text/
description: 이 섹션은 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF와 C#을 사용하여 텍스트를 추가, 교체, 회전, 검색하는 방법을 배우십시오.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 C#을 사용한 텍스트 작업",
    "alternativeHeadline": "PDF 파일에서 텍스트 추가, 회전, 검색 및 삭제",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 텍스트 추가, 텍스트 검색, 텍스트 삭제, pdf에서 텍스트 조작",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션은 텍스트 처리의 다양한 기술을 설명합니다. Aspose.PDF와 C#을 사용하여 텍스트를 추가, 교체, 회전, 검색하는 방법을 배우십시오."
}
</script>
우리 모두 가끔 PDF 파일에 텍스트를 추가해야 할 때가 있습니다. 예를 들어, 주요 텍스트 아래에 번역을 추가하거나 이미지 옆에 캡션을 배치하거나 신청서를 작성해야 할 때입니다. 모든 텍스트 요소를 원하는 스타일로 포맷할 수 있다면 더욱 유용합니다. PDF 파일에서 가장 인기 있는 텍스트 조작에는 PDF에 텍스트 추가, PDF 파일 내부의 텍스트 포맷, 문서에서 텍스트 교체 및 회전 등이 있습니다. **Aspose.PDF for .NET**은 PDF 콘텐츠와 상호 작용할 수 있는 모든 것을 갖춘 최상의 솔루션입니다.

다음 작업을 수행할 수 있습니다:

- [PDF 파일에 텍스트 추가](/pdf/ko/net/add-text-to-pdf-file/) - PDF에 텍스트 추가, 스트림과 파일에서 글꼴 사용, HTML 문자열 추가, 하이퍼링크 추가 등.
- [PDF 도구팁](/pdf/ko/net/pdf-tooltip/) - C#을 사용하여 보이지 않는 버튼을 추가함으로써 검색된 텍스트에 도구팁을 추가할 수 있습니다.
- [PDF 내부의 텍스트 포맷팅](/pdf/ko/net/text-formatting-inside-pdf/) - 텍스트를 포맷할 때 문서에 추가할 수 있는 많은 기능들이 있습니다.
- [PDF 내에서 텍스트 서식 지정](/pdf/ko/net/text-formatting-inside-pdf/) - 텍스트 서식을 지정할 때 문서에 추가할 수 있는 여러 기능이 있습니다.
- [PDF에서 텍스트 교체](/pdf/ko/net/replace-text-in-pdf/) - PDF 문서의 모든 페이지에서 텍스트를 교체하려면 TextFragmentAbsorber를 사용해야 합니다.
- [PDF 내에서 텍스트 회전](/pdf/ko/net/rotate-text-inside-pdf/) - TextFragment 클래스의 회전 속성을 사용하여 PDF 내에서 텍스트를 회전시킵니다.
- [PDF 문서의 페이지에서 텍스트 검색 및 가져오기](/pdf/ko/net/search-and-get-text-from-pages-of-pdf/) - 페이지에서 텍스트를 검색하고 가져오기 위해 TextFragmentAbsorber 클래스를 사용할 수 있습니다.
- [줄 바꿈 결정](/pdf/ko/net/determine-line-break/) - 이 주제는 여러 줄의 텍스트 조각의 줄 바꿈을 추적하는 방법을 설명합니다.

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


