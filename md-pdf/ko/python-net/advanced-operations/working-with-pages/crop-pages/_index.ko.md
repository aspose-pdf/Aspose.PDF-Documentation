---
title: PDF 페이지 자르기 프로그래밍 방식으로 Python
linktitle: 페이지 자르기
type: docs
weight: 70
url: /python-net/crop-pages/
description: Aspose.PDF for Python via .NET을 사용하여 너비, 높이, 블리드박스, 크롭박스 및 트림박스와 같은 페이지 속성을 가져올 수 있습니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 페이지 자르기 프로그래밍 방식으로 Python",
    "alternativeHeadline": "Python에서 PDF 페이지 자르는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, crop pdf pages",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NET을 사용하여 너비, 높이, 블리드박스, 크롭박스 및 트림박스와 같은 페이지 속성을 가져올 수 있습니다."
}
</script>


## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드 박스, 크롭 박스, 트림 박스와 같은 여러 속성이 있습니다. Aspose.PDF for Python을 사용하면 이러한 속성에 접근할 수 있습니다.

- **media_box**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 PostScript 또는 PDF로 문서를 인쇄할 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 미디어의 물리적 크기를 결정합니다.
- **bleed_box**: 문서에 블리드가 있는 경우, PDF에도 블리드 박스가 있습니다. 블리드는 페이지 가장자리를 넘어서 확장되는 색상(또는 예술 작품)의 양을 의미합니다. 이는 문서가 인쇄되고 크기에 맞게 잘릴 때("트림") 잉크가 페이지의 가장자리까지 가도록 보장하기 위해 사용됩니다. 페이지가 잘못 트림되어 트림 마크에서 약간 벗어나 잘리더라도 페이지에 흰색 가장자리가 나타나지 않습니다.
- **trim_box**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **art_box**: 아트 박스는 문서의 페이지 실제 내용 주위에 그려진 박스입니다.
 이 페이지 상자는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **crop_box**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기 모드에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.

아래 코드 조각은 페이지를 크롭하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 새 Box 사각형 생성
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

이 예제에서는 샘플 파일을 사용했습니다 [여기](crop_page.pdf). 처음에 우리의 페이지는 그림 1과 같이 보입니다.
![그림 1. 크롭된 페이지](crop_page.png)

변경 후, 페이지는 그림 2와 같이 보일 것입니다.
![Figure 2. Cropped Page](crop_page2.png)

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
    "applicationCategory": "파이썬용 PDF 조작 라이브러리",
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