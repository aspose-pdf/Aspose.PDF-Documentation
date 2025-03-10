---
title: PDF 파일에서 그래프 작업하기
linktitle: 그래프 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/working-with-graphs/
description: 이 문서에서는 그래프가 무엇인지, 채워진 사각형 객체를 만드는 방법, 그리고 기타 기능에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Aspose.PDF for .NET을 사용하여 PDF 문서 내에서 그래프를 생성하고 조작하는 강력한 새로운 기능을 발견하세요. 이 기능은 개발자가 아크, 원, 선 및 사각형을 포함한 다양한 그래프 모양을 생성할 수 있게 하여 애플리케이션의 데이터 시각적 표현을 향상시킵니다. PDF 생성 프로세스를 최적화하고 동적 데이터 시각화를 쉽게 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 그래프가 무엇인지, 채워진 사각형 객체를 만드는 방법, 그리고 기타 기능에 대해 설명합니다."
}
</script>

## 그래프란 무엇인가

PDF 문서에 그래프를 추가하는 것은 Adobe Acrobat Writer 또는 기타 PDF 처리 애플리케이션을 사용할 때 개발자에게 매우 일반적인 작업입니다. PDF 애플리케이션에서 사용할 수 있는 그래프의 종류는 다양합니다.
[Aspose.PDF for .NET](/pdf/net/) 또한 PDF 문서에 그래프를 추가하는 것을 지원합니다. 이를 위해 그래프 클래스가 제공됩니다. 그래프는 단락 수준 요소이며 페이지 인스턴스의 단락 컬렉션에 추가할 수 있습니다. 그래프 인스턴스는 도형 컬렉션을 포함합니다.

다음과 같은 도형 유형이 [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 클래스에서 지원됩니다:

- [아크](/pdf/net/add-arc/) - 때때로 플래그라고도 하며, 인접한 정점의 순서 쌍이지만 때때로 방향선이라고도 합니다.
- [원](/pdf/net/add-circle/) - 부문으로 나누어진 원을 사용하여 데이터를 표시합니다. 우리는 데이터가 하나의 전체 또는 하나의 그룹의 일부를 나타내는 방식을 보여주기 위해 원 그래프(파이 차트라고도 함)를 사용합니다.
- [곡선](/pdf/net/add-curve/) - 각 선이 세 개의 다른 선과 일반적인 이중 점에서 만나는 연결된 투영선의 집합입니다.
- [선](/pdf/net/add-line) - 선 그래프는 연속 데이터를 표시하는 데 사용되며, 시간이 지남에 따라 추세를 보여줄 때 미래의 사건을 예측하는 데 유용할 수 있습니다.
- [사각형](/pdf/net/add-rectangle/) - 그래프에서 볼 수 있는 많은 기본 도형 중 하나로, 문제를 해결하는 데 매우 유용할 수 있습니다.
- [타원](/pdf/net/add-ellipse/) - 평면의 점 집합으로, 타원형 곡선을 생성합니다.

위의 세부 사항은 아래 그림에서도 나타납니다:

![그래프의 그림](graphs.png)


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