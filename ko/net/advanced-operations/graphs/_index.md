---
title: PDF 파일에서 그래프 다루기
linktitle: 그래프 다루기
type: docs
weight: 70
url: /ko/net/graphs/
description: 이 글은 그래프가 무엇인지, 채워진 사각형 객체를 생성하는 방법 및 기타 기능에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에서 그래프 다루기",
    "alternativeHeadline": "PDF에서 그래프 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 내의 그래프",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 그래프가 무엇인지, 채워진 사각형 객체를 생성하는 방법 및 기타 기능에 대해 설명합니다."
}
</script>
## 그래프란 무엇인가

PDF 문서에 그래프를 추가하는 것은 Adobe Acrobat Writer 또는 기타 PDF 처리 응용 프로그램을 사용하는 개발자들에게 매우 일반적인 작업입니다. PDF 응용 프로그램에서 사용할 수 있는 그래프의 유형은 많습니다.
[Aspose.PDF for .NET](/pdf/ko/net/)도 PDF 문서에 그래프를 추가하는 것을 지원합니다. 이를 위해 Graph 클래스가 제공됩니다. Graph는 단락 수준 요소이며 Page 인스턴스의 Paragraphs 컬렉션에 추가할 수 있습니다. Graph 인스턴스는 여러 가지 형태의 모음을 포함합니다.

다음 유형의 형태는 [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 클래스에 의해 지원됩니다:

- [Arc](/pdf/ko/net/add-arc/) - 때로는 인접한 정점의 순서쌍으로 불리기도 하며, 지향성 선이라고도 합니다.
- [Circle](/pdf/ko/net/add-circle/) - 원을 부문으로 나누어 데이터를 표시합니다. 원형 그래프(또는 파이 차트라고도 함)를 사용하여 데이터가 하나의 전체나 하나의 그룹의 부분을 어떻게 나타내는지 보여줍니다.
- [Curve](/pdf/ko/net/add-curve/) - 각 선이 세 개의 다른 선과 평범한 이중 점에서 만나는 사영선의 연결된 합입니다.
- [곡선](/pdf/ko/net/add-curve/) - 각 선이 평범한 이중 점에서 세 다른 선과 만나는 사영선들의 연결된 합집합입니다.
- [선](/pdf/ko/net/add-line) - 선 그래프는 연속 데이터를 표시하는 데 사용되며 시간에 걸쳐 추세를 보일 때 미래 이벤트를 예측하는 데 유용할 수 있습니다.
- [직사각형](/pdf/ko/net/add-rectangle/) - 그래프에서 볼 수 있는 많은 기본 형태 중 하나이며 문제를 해결하는 데 매우 유용할 수 있습니다.
- [타원](/pdf/ko/net/add-ellipse/) - 평면상의 점들의 집합으로, 타원형 곡선을 만듭니다.

위의 세부 정보는 아래 그림에도 나타나 있습니다:

![그래프 내의 도형들](graphs.png)

