---
title: C#에서 PDF 페이지 작업하기
linktitle: 페이지 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/working-with-pages/
description: 이 섹션에서는 페이지 추가, 머리글 및 바닥글 추가, 워터마크 추가 방법을 알 수 있습니다. Aspose.PDF for .NET이 이 주제에 대한 모든 세부 정보를 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "Aspose.PDF for .NET의 고급 기능을 통해 PDF 페이지를 관리하는 방법을 알아보세요. 페이지 추가, 이동 및 삭제를 정밀하게 수행할 수 있습니다. 이 기능을 통해 사용자는 머리글, 바닥글, 워터마크 및 사용자 정의 페이지 크기를 통합하여 PDF 문서를 향상시킬 수 있습니다. 직관적인 C# 코드를 통해 문서 워크플로를 최적화하고 원활한 PDF 조작 및 사용자 정의 기능을 활용하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "이 섹션에서는 페이지 추가, 머리글 및 바닥글 추가, 워터마크 추가 방법을 알 수 있습니다. Aspose.PDF for .NET이 이 주제에 대한 모든 세부 정보를 설명합니다."
}
</script>

**Aspose.PDF for .NET**을 사용하면 PDF 문서의 원하는 위치에 페이지를 삽입하거나 PDF 파일의 끝에 페이지를 추가할 수 있습니다. 이 섹션에서는 Acrobat Reader 없이 PDF에 페이지를 추가하는 방법을 보여줍니다.
PDF 파일의 머리글과 바닥글에 텍스트나 이미지를 추가할 수 있으며, Aspose의 C# 라이브러리를 사용하여 문서에서 다양한 머리글을 선택할 수 있습니다.
또한, C#을 사용하여 PDF 문서의 페이지를 프로그래밍 방식으로 자르는 방법을 시도해 보세요.

이 섹션에서는 Artifact 클래스를 사용하여 PDF 파일에 워터마크를 추가하는 방법을 배웁니다. 이 작업을 위한 프로그래밍 샘플을 확인할 수 있습니다.
PageNumberStamp 클래스를 사용하여 페이지 번호를 추가합니다. 문서에 스탬프를 추가하려면 ImageStamp 및 TextStamp 클래스를 사용하세요. **Aspose.PDF for .NET**을 사용하여 PDF 파일에 배경 이미지를 생성하기 위해 워터마크를 추가하세요.

다음 작업을 수행할 수 있습니다:

- [페이지 추가하기](/pdf/net/add-pages/) - 원하는 위치에 페이지를 추가하거나 PDF 파일의 끝에 페이지를 추가하고 문서에서 페이지를 삭제합니다.
- [페이지 이동하기](/pdf/net/move-pages/) - 한 문서에서 다른 문서로 페이지를 이동합니다.
- [페이지 삭제하기](/pdf/net/delete-pages/) - PageCollection 컬렉션을 사용하여 PDF 파일에서 페이지를 삭제합니다.
- [페이지 크기 변경하기](/pdf/net/change-page-size/) - Aspose.PDF 라이브러리를 사용하여 코드 스니펫으로 PDF 페이지 크기를 변경할 수 있습니다.
- [페이지 회전하기](/pdf/net/rotate-pages/) - 기존 PDF 파일의 페이지 방향을 변경할 수 있습니다.
- [페이지 분할하기](/pdf/net/split-document/) - PDF 파일을 하나 또는 여러 개의 PDF로 분할할 수 있습니다.
- [머리글 및/또는 바닥글 추가하기](/pdf/net/add-headers-and-footers-of-pdf-file/) - PDF 파일의 머리글과 바닥글에 텍스트나 이미지를 추가합니다.
- [페이지 자르기](/pdf/net/crop-pages/) - 다양한 페이지 속성을 사용하여 PDF 문서의 페이지를 프로그래밍 방식으로 자를 수 있습니다.
- [워터마크 추가하기](/pdf/net/add-watermarks/) - Artifact 클래스를 사용하여 PDF 파일에 워터마크를 추가합니다.
- [PDF 파일에 페이지 번호 추가하기](/pdf/net/add-page-number/) - PageNumberStamp 클래스가 PDF 파일에 페이지 번호를 추가하는 데 도움이 됩니다.
- [배경 추가하기](/pdf/net/add-backgrounds/) - 배경 이미지를 사용하여 워터마크를 추가할 수 있습니다.
- [스탬핑](/pdf/net/stamping/) - ImageStamp 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가하고 TextStamp 클래스를 사용하여 텍스트를 추가할 수 있습니다.

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