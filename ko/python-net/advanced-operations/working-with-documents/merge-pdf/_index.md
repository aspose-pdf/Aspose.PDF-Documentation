---
title: Python을 사용하여 PDF 병합하는 방법
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /ko/python-net/merge-pdf-documents/
keywords: "여러 pdf를 하나의 pdf로 병합 python, 여러 pdf를 하나로 결합 python, 여러 pdf를 하나로 병합 python"
description: 이 페이지는 Python을 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF 병합하는 방법",
    "alternativeHeadline": "Python을 통해 PDF 문서 결합",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 조작",
    "keywords": "pdf, python, pdf 병합, 연결, pdf 결합",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "이 페이지는 .NET을 통해 Python으로 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다."
}
</script>


## Python에서 여러 PDF를 하나의 PDF로 병합 또는 결합하기

PDF 파일을 결합하는 것은 사용자들 사이에서 매우 인기 있는 요청입니다. 이는 여러 PDF 파일을 하나의 문서로 공유하거나 저장하고 싶을 때 유용할 수 있습니다.

PDF 파일을 병합하면 문서를 정리하고, PC의 저장 공간을 확보하며, 여러 PDF 파일을 하나의 문서로 결합하여 다른 사람과 공유할 수 있습니다.

.NET을 통해 Python에서 PDF를 병합하는 것은 3rd party 라이브러리를 사용하지 않고는 간단하지 않습니다.
이 문서는 Aspose.PDF for Python via .NET을 사용하여 여러 PDF 파일을 하나의 PDF 문서로 병합하는 방법을 보여줍니다.

## Python 및 DOM을 사용하여 PDF 파일 병합하기

두 개의 PDF 파일을 연결하려면:

1. 두 개의 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 생성하고, 각각의 객체에 입력 PDF 파일 중 하나를 포함시킵니다.

1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 메서드를 호출하여 다른 PDF 파일을 추가하고자 하는 Document 객체에 추가합니다.
1. 두 번째 Document 객체의 PageCollection 컬렉션을 첫 번째 PageCollection 컬렉션의 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 메서드에 전달합니다.
1. 마지막으로, [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일을 연결하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 첫 번째 문서 열기
    document1 = ap.Document(input_pdf_1)
    # 두 번째 문서 열기
    document2 = ap.Document(input_pdf_2)

    # 두 번째 문서의 페이지를 첫 번째 문서에 추가
    document1.pages.add(document2.pages)

    # 연결된 출력 파일 저장
    document1.save(output_pdf)
```


## 실시간 예제

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)는 프레젠테이션 병합 기능이 어떻게 작동하는지 조사할 수 있는 무료 온라인 웹 애플리케이션입니다.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

<script type="application/ld+json">
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