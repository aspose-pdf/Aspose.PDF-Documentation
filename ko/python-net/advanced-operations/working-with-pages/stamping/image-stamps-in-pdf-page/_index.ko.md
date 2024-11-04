---
title: PDF에 이미지 스탬프 추가하기 (Python 사용)
linktitle: PDF 파일에 이미지 스탬프
type: docs
weight: 10
url: /python-net/image-stamps-in-pdf-page/
description: Aspose.PDF for Python 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에 이미지 스탬프 추가하기 (Python 사용)",
    "alternativeHeadline": "PDF에 이미지 스탬프 추가하기 (Python 사용)",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다."
}
</script>


## PDF 파일에 이미지 스탬프 추가하기

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스는 높이, 너비, 불투명도 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다.

이미지 스탬프를 추가하려면:

1. 필요한 속성을 사용하여 Document 객체와 ImageStamp 객체를 생성합니다.
1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스의 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드를 호출하여 PDF에 스탬프를 추가합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 이미지 스탬프 생성
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # 특정 페이지에 스탬프 추가
    document.pages[1].add_stamp(image_stamp)

    # 출력 문서 저장
    document.save(output_pdf)
```


## 스탬프 추가 시 이미지 품질 제어

이미지를 스탬프 객체로 추가할 때 이미지의 품질을 제어할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스의 [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 속성이 이 목적에 사용됩니다. 이는 이미지의 품질을 퍼센트로 나타내며 (유효한 값은 0..100)입니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 이미지 스탬프 생성
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # 특정 페이지에 스탬프 추가
    document.pages[1].add_stamp(image_stamp)

    # 출력 문서 저장
    document.save(output_pdf)
```

## 플로팅 박스의 배경으로 이미지 스탬프

Aspose.PDF for Python API를 사용하면 플로팅 박스의 배경으로 이미지 스탬프를 추가할 수 있습니다.
 [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 속성은 [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 클래스의 배경 이미지 스탬프를 설정하는 데 사용할 수 있으며, 아래의 코드 샘플에 나타나 있습니다.

```python

    import aspose.pdf as ap

    # Document 객체를 인스턴스화합니다.
    document = ap.Document()
    # PDF 문서에 페이지를 추가합니다.
    page = document.pages.add()
    # FloatingBox 객체를 생성합니다.
    box = ap.FloatingBox(200.0, 100.0)
    # FloatingBox의 왼쪽 위치를 설정합니다.
    box.left = 40
    # FloatingBox의 위쪽 위치를 설정합니다.
    box.top = 80
    # FloatingBox의 수평 정렬을 설정합니다.
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # FloatingBox의 단락 컬렉션에 텍스트 조각을 추가합니다.
    box.paragraphs.add(ap.text.TextFragment("main text"))
    # FloatingBox에 테두리를 설정합니다.
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # 배경 이미지를 추가합니다.
    box.background_image = img
    # FloatingBox의 배경 색상을 설정합니다.
    box.background_color = ap.Color.yellow
    # 페이지 객체의 단락 컬렉션에 FloatingBox를 추가합니다.
    page.paragraphs.add(box)
    # PDF 문서를 저장합니다.
    document.save(output_pdf)
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