---
title: 파이썬을 사용하여 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 110
url: /ko/python-net/rotate-pages/
description: 이 주제는 파이썬을 사용하여 기존 PDF 파일에서 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF 페이지 회전",
    "alternativeHeadline": "파이썬으로 PDF 페이지 회전하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 페이지 회전",
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
    "url": "/python-net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "이 주제는 파이썬을 사용하여 기존 PDF 파일에서 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다."
}
</script>


이 주제는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 업데이트하거나 변경하는 방법을 설명합니다.

## 페이지 방향 변경

.NET을 통한 Aspose.PDF for Python은 가로 모드에서 세로 모드로 또는 그 반대로 페이지 방향을 변경하는 등의 훌륭한 기능을 지원합니다. 페이지 방향을 변경하려면 다음 코드 스니펫을 사용하여 페이지의 MediaBox를 설정하십시오. 'rotate' 메서드를 사용하여 회전 각도를 설정함으로써 페이지 방향을 변경할 수도 있습니다.

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    for page in doc.pages:
        r = page.media_box
        newHeight = r.width
        newWidth = r.height
        newLLX = r.llx
        # 페이지 크기 변경을 보상하기 위해 페이지를 위로 이동해야 합니다
        # (페이지의 하단 모서리는 0,0이며 정보는 일반적으로 페이지 상단에서 배치됩니다. 
        #  따라서 우리는 이전 높이와 새로운 높이의 차이만큼 하단 모서리를 위로 이동합니다.)
        newLLY = r.lly + (r.height - newHeight)
        page.media_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)
        # 때로는 CropBox를 설정해야 할 수도 있습니다 (원본 파일에서 설정된 경우)
        page.crop_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)

        # 페이지의 회전 각도 설정
        page.rotate = ap.Rotation.ON90

    # 출력 파일 저장
    doc.save(output_pdf)
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
    "applicationCategory": "Python을 위한 PDF 조작 라이브러리",
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