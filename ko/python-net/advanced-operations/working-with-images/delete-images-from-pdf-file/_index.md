---
title: 파이썬을 사용하여 PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: /ko/python-net/delete-images-from-pdf-file/
description: 이 섹션에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF 파일에서 이미지 삭제",
    "alternativeHeadline": "PDF에서 이미지 제거 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, delete, remove image from pdf",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "이 섹션에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다."
}
</script>


PDF에서 모든 이미지 또는 특정 이미지를 제거해야 하는 여러 가지 이유가 있습니다.

때때로 PDF 파일에는 개인 정보를 보호하거나 특정 정보에 대한 무단 액세스를 방지하기 위해 제거해야 하는 중요한 이미지가 포함될 수 있습니다.

원하지 않거나 중복된 이미지를 제거하면 파일 크기를 줄일 수 있어 PDF를 공유하거나 저장하기가 더 쉬워집니다.

필요한 경우 문서에서 모든 이미지를 제거하여 페이지 수를 줄일 수 있습니다.
또한 문서에서 이미지를 삭제하면 PDF 압축 또는 텍스트 정보 추출 준비에 도움이 됩니다.

**Aspose.PDF for Python via .NET**은 이 작업을 수행하는 데 도움을 줄 것입니다.

## PDF 파일에서 이미지 삭제

PDF 파일에서 이미지를 삭제하려면:

1. 기존 PDF 문서를 엽니다.
1. 특정 이미지를 삭제합니다.
1. 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    # 특정 이미지 삭제
    document.pages[2].resources.images.delete(1)

    # 업데이트된 PDF 파일 저장
    document.save(output_pdf)
```


## 입력 PDF에서 모든 이미지 삭제하기

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    # 모든 페이지에서 모든 이미지 삭제
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # 업데이트된 PDF 파일 저장
    document.save(output_file)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>