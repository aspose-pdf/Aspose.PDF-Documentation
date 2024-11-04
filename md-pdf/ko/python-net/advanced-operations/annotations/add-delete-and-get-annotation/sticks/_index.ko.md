---
title: PDF 스티커 주석을 파이썬으로 사용하기
linktitle: 스티커 주석
type: docs
weight: 50
url: /python-net/sticky-annotations/
description: 이 주제는 스티커 주석에 관한 것이며, 예시로 텍스트에 워터마크 주석을 보여줍니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 스티커 주석을 파이썬으로 사용하기",
    "alternativeHeadline": "PDF에 스티커 주석 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 스티커 주석, 워터마크 주석",
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
    "url": "/python-net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/sticky-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "이 주제는 스티커 주석에 관한 것이며, 예시로 파이썬 라이브러리를 사용하여 텍스트에 워터마크 주석을 보여줍니다."
}
</script>


## 워터마크 주석 추가

가장 눈에 띄고 시각화 및 전송이 쉬운 것은 워터마크 주석입니다. 이는 PDF 문서에 로고나 원본임을 확인하는 기타 표식을 배치하는 가장 좋은 방법입니다.

워터마크 주석은 인쇄된 페이지의 크기에 관계없이 페이지의 고정된 크기와 위치에 인쇄될 그래픽을 나타내는 데 사용됩니다.

PDF 페이지의 특정 위치에 [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/)을 사용하여 워터마크 텍스트를 추가할 수 있습니다. 워터마크의 불투명도는 [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) 속성을 사용하여 제어할 수 있습니다.

워터마크 주석을 추가하는 다음 코드 스니펫을 확인하십시오.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # 주석 생성
    # 주석을 추가할 페이지 객체 로드
    page = document.pages[1]

    # 주석 생성
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # 페이지의 주석 컬렉션에 주석 추가
    page.annotations.append(wa)

    # 글꼴 설정을 위한 TextState 생성
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # 주석 텍스트의 불투명도 수준 설정
    wa.opacity = 0.5

    # 주석에 텍스트 추가
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```


## 워터마크 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## 워터마크 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>