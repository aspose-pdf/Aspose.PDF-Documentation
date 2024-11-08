---
title: C#을 사용하여 PDF 문서 작업하기
linktitle: 문서 작업하기
type: docs
weight: 10
url: /ko/net/working-with-documents/
description: 이 글은 Aspose.PDF 라이브러리로 문서를 조작할 수 있는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-document/
    - /net/working-with-document-facades/
    - /net/create-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용하여 PDF 문서 작업하기",
    "alternativeHeadline": "PDF 문서 조작하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 문서",
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF 라이브러리로 문서를 조작할 수 있는 방법을 설명합니다."
}
</script>

PDF는 Portable Document Format의 약자로, 소프트웨어, 하드웨어 또는 운영 체제에 관계없이 전자적 형태로 문서를 표시하는 데 사용됩니다.

PDF는 현재 국제 표준화 기구(ISO)에 의해 유지되는 개방형 표준입니다.

원래의 목표는 문서의 내용과 레이아웃을 보존하고 보호하는 것이었습니다 - 어떤 플랫폼이나 컴퓨터 프로그램에서 보더라도 말이죠. 이것이 PDF가 편집하기 어렵고 때로는 정보를 추출하는 것도 도전이 되는 이유입니다.

하지만 **Aspose.PDF for .NET**은 PDF 문서 작업 시 발생하는 대부분의 작업을 처리할 수 있게 도와줍니다.

다음과 같은 작업이 가능합니다:

- [PDF 문서 형식](/pdf/ko/net/formatting-pdf-document/) - 문서 생성, 문서 속성 가져오기 및 설정, 글꼴 임베딩 및 PDF 파일과 관련된 기타 작업.
- [PDF 문서 조작](/pdf/ko/net/manipulate-pdf-document/) - PDF 문서를 PDF A 표준에 대해 검증, 목차 작업, PDF 만료 날짜 설정 등.
- [PDF 최적화](/pdf/ko/net/optimize-pdf/) - 페이지 콘텐츠 최적화, 파일 크기 최적화, 사용되지 않는 객체 제거, 모든 이미지 압축을 통한 문서 최적화 성공.

type: docs
changefreq: "monthly"
- [PDF 최적화](/pdf/ko/net/optimize-pdf/) - 페이지 내용 최적화, 파일 크기 최적화, 사용하지 않는 객체 제거, 모든 이미지 압축을 통한 문서 최적화.
- [PDF 병합](/pdf/ko/net/merge-pdf-documents/) - C#을 사용하여 여러 PDF 파일을 단일 PDF 문서로 병합합니다.
- [PDF 분할](/pdf/ko/net/split-document/) - .NET 응용 프로그램에서 PDF 페이지를 개별 PDF 파일로 분할합니다.
- [폴더의 PDF 파일 연결](/pdf/ko/net/concatenating-all-pdf-files-in-particular-folder/) - PdfFileEditor 클래스를 사용하여 특정 폴더의 모든 PDF 파일을 연결합니다.
- [MemoryStreams를 사용하여 여러 PDF 파일 연결](/pdf/ko/net/concatenate-pdf-documents/) - C#을 사용하여 MemoryStreams를 사용하여 여러 PDF 파일을 연결하는 방법을 배웁니다.
- [제목 작업](/pdf/ko/net/working-with-headings/) - C#을 사용하여 PDF 문서의 제목에 번호 매기기를 생성할 수 있습니다.

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

