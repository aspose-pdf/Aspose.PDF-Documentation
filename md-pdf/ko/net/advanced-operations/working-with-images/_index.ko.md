---
title: PDF에서 C#을 사용하여 이미지 다루기
linktitle: 이미지 다루기
type: docs
weight: 40
url: /net/working-with-images/
description: 이 섹션은 C# 라이브러리를 사용하여 PDF 파일에서 이미지를 다루는 기능에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/manipulate-images/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 C#을 사용하여 이미지 다루기",
    "alternativeHeadline": "PDF에서 .NET을 사용하여 이미지 다루는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 내 이미지",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/working-with-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션은 C# 라이브러리를 사용하여 PDF 파일에서 이미지를 다루는 기능에 대해 설명합니다."
}
</script>

PDF 형식에서 이미지는 상당히 복잡한 주제일 수 있습니다. 사용자가 PDF 문서 작업을 할 때 이미지와 관련된 다양한 조작을 기다리고 있습니다. 우리는 파일에서 이미지를 추가하거나 제거할 수 있다는 것에 익숙하지만, Aspose.PDF 라이브러리를 사용하면 이미지 크기를 설정하고, 이미지를 교체하고, 이미지를 추출하고, PDF 문서에서 이미지를 검색하고 가져오는 등의 작업도 할 수 있습니다.

**PDF에 이미지를 추가하는 방법은?** Aspose.PDF를 사용하여 PDF에서 이미지에 대해 가장 자주 묻는 질문에 대한 답변을 받을 수 있습니다.

**Aspose.PDF for .NET**은 디지털 문서 작업에 있어서 똑똑하고 효율적인 도구로, 기존 PDF에 어떤 그래픽 객체도 빠르게 가져오고 배치할 수 있게 해줍니다.
저희 C# 라이브러리는 보고서에 차트를 삽입하거나 프로젝트에 배치도를 덮어쓰거나 이력서에 사진을 포함시키는 등의 작업이 필요한 경우에도 유용합니다. PDF 문서에서 이미지를 삽입하고 편집하는 고급 방법을 찾고 있다면, 귀하의 작업을 해결하기 위해 다음 글을 배우시는 것을 적극 추천합니다.

다음과 같은 작업을 수행할 수 있습니다:
- [기존 PDF 파일에 이미지 추가](/pdf/net/add-image-to-existing-pdf-file/) - PDF 문서에 단일 이미지의 이미지와 참조를 추가한 후 품질을 제어합니다.
- [PDF 파일에서 이미지 삭제](/pdf/net/delete-images-from-pdf-file/) - PDF 파일에서 이미지를 삭제하는 코드 스니펫을 확인하세요.
- [PDF 파일에서 이미지 추출](/pdf/net/extract-images-from-pdf-file/) - 이미지 컬렉션을 사용하여 PDF 파일에서 이미지를 추출하세요.
- [임베디드 이미지의 해상도 및 크기 가져오기](/pdf/net/get-resolution-and-dimensions-of-embedded-images/) - Aspose.PDF 네임스페이스의 연산자 클래스를 사용하여 해상도 및 크기 정보를 얻을 수 있습니다.
- [이미지 배치 작업](/pdf/net/working-with-image-placement/) - PDF 문서에서 이미지의 해상도와 위치를 얻을 수 있습니다.
- [PDF 문서에서 이미지 검색 및 가져오기](/pdf/net/search-and-get-images-from-pdf-document/) - C#을 사용하여 개별 페이지에서 이미지를 얻고 모든 페이지의 이미지 중에서 검색할 수 있습니다.
- [PDF 문서에서 이미지 검색 및 가져오기](/pdf/net/search-and-get-images-from-pdf-document/) - 개별 페이지에서 이미지를 가져올 수 있으며 C#을 사용하여 모든 페이지의 이미지 중에서 검색할 수 있습니다.
- [기존 PDF 파일에서 이미지 교체](/pdf/net/replace-image-in-existing-pdf-file/) - 코드 스니펫을 확인하세요. PDF 파일에서 이미지를 교체하는 방법을 보여줍니다.
- [이미지 크기 설정](/pdf/net/set-image-size/) - C# 라이브러리를 사용하여 이미지의 크기를 설정할 수 있습니다.
- [기본 글꼴 이름 설정](/pdf/net/set-default-font-name/) - 변환 과정에 대한 기본 글꼴 이름 설정.
- [PDF 문서에서 썸네일 이미지 생성](/pdf/net/generate-thumbnail-images-from-pdf-documents/) - 다음 글은 먼저 Acrobat SDK를 사용한 후 Aspose.PDF를 사용하여 PDF 문서에서 썸네일 이미지를 생성하는 방법을 보여줍니다.
- DICOM 이미지 지원 - Aspose.PDF for .NET은 특수 의료 그래픽 표준 이미지를 지원합니다.
- DICOM 이미지 지원 - Aspose.PDF for .NET은 특수한 의료 그래픽 표준 이미지를 지원합니다.

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

