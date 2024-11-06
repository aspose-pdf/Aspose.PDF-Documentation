---
title: Python으로 PDF 페이지 크기 변경
linktitle: PDF 페이지 크기 변경
type: docs
weight: 60
url: ko/python-net/change-page-size/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기 변경.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python으로 PDF 페이지 크기 변경",
    "alternativeHeadline": "Python으로 PDF 페이지 크기 조정",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 크기 변경, pdf 크기 조정",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기 변경."
}
</script>


## PDF 페이지 크기 변경

Aspose.PDF for Python via .NET을 사용하면 Python 애플리케이션에서 간단한 코드 라인으로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제는 기존 PDF 파일의 페이지 치수(크기)를 업데이트/변경하는 방법을 설명합니다.

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스에는 페이지 크기를 설정할 수 있는 [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드가 포함되어 있습니다. 아래 코드 스니펫은 몇 가지 간단한 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
2. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 객체에 페이지를 가져옵니다.
3. 주어진 페이지를 가져옵니다.
4. set_page_size() 메서드를 호출하여 치수를 업데이트합니다.
5. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 업데이트된 페이지 치수로 PDF 파일을 생성합니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 특정 페이지 가져오기
    page = document.pages[1]

    # 페이지 크기를 A4(11.7 x 8.3 인치)로 설정하고 Aspose.Pdf에서는 1인치 = 72포인트
    # 따라서 A4 치수는 포인트로 (842.4, 597.6)이 됩니다
    page.set_page_size(597.6, 842.4)

    # 업데이트된 문서 저장
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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