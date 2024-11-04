---
title: C#를 사용하여 PDF 페이지 크기 변경
linktitle: PDF 페이지 크기 변경
type: docs
weight: 40
url: /net/change-page-size/
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기를 변경합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 PDF 페이지 크기 변경",
    "alternativeHeadline": ".NET으로 PDF 페이지 크기 조정",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 크기 변경, pdf 크기 조정",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기를 변경합니다."
}
</script>

## PDF 페이지 크기 변경

Aspose.PDF for .NET을 사용하면 .NET 애플리케이션에서 간단한 코드 줄로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제는 기존 PDF 파일의 페이지 치수(크기)를 업데이트/변경하는 방법을 설명합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스에는 페이지 크기를 설정할 수 있는 SetPageSize(...) 메소드가 포함되어 있습니다. 아래의 코드 스니펫은 몇 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 객체로 페이지를 가져옵니다.
1. 주어진 페이지를 가져옵니다.
1. SetPageSize(..) 메소드를 호출하여 치수를 업데이트합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 Save(..) 메소드를 호출하여 업데이트된 페이지 치수로 PDF 파일을 생성합니다.

{{% alert color="primary" %}}

높이와 너비 속성은 기본 단위로 포인트를 사용하는데, 1인치 = 72포인트이고 1cm = 1/2.54인치 = 0.3937인치 = 28.3포인트입니다.
높이와 너비 속성은 기본 단위로 포인트를 사용하며, 1 인치 = 72 포인트, 1 cm = 1/2.54 인치 = 0.3937 인치 = 28.3 포인트입니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 페이지 크기를 A4 크기로 변경하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## PDF 페이지 크기 가져오기

기존 PDF 파일의 PDF 페이지 크기를 읽을 수 있습니다. 다음 코드 샘플은 C#을 사용하여 PDF 페이지 크기를 읽는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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

