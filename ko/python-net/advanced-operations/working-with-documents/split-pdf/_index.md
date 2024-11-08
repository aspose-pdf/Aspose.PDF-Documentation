---
title: 파이썬에서 프로그래밍 방식으로 PDF 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/python-net/split-pdf-document/
keywords: 여러 파일로 PDF 분할, 개별 PDF로 PDF 분할, 파이썬 PDF 분할
description: 이 주제는 파이썬 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "프로그래밍 방식으로 PDF 분할",
    "alternativeHeadline": "파이썬으로 PDF 분할하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 분할",
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
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "이 주제는 파이썬 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다."
}
</script>


PDF 페이지를 분할하는 것은 큰 파일을 개별 페이지나 페이지 그룹으로 분할하려는 사람들에게 유용한 기능이 될 수 있습니다.

## 라이브 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있도록 도와주는 무료 온라인 웹 애플리케이션입니다.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

이 주제는 Python 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. Python을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션을 통해 PDF 문서의 페이지를 반복합니다.
1. 각 반복마다 새로운 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 빈 문서에 추가합니다.

1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 새 PDF를 저장합니다.

## PDF를 여러 파일로 분할하거나 Python에서 개별 PDF로 분할

다음 Python 코드 조각은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    page_count = 1

    # 모든 페이지를 순회합니다
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

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
    "applicationCategory": "PDF Manipulation Library for Python",
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