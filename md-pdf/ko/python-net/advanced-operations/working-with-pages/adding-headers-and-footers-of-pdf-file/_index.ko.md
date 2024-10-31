---
title: 파이썬을 사용하여 PDF에 헤더 및 푸터 추가
linktitle: PDF에 헤더 및 푸터 추가
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET을 사용하면 TextStamp 클래스를 사용하여 PDF 파일에 헤더 및 푸터를 추가할 수 있습니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF에 헤더 및 푸터 추가",
    "alternativeHeadline": "PDF 파일에 헤더 및 푸터 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 헤더 추가, pdf에 푸터 추가",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NET을 사용하면 TextStamp 클래스를 사용하여 PDF 파일에 헤더 및 푸터를 추가할 수 있습니다."
}
</script>


**Aspose.PDF for Python via .NET**은 기존 PDF 파일에 헤더와 푸터를 추가할 수 있게 해줍니다. PDF 문서에 이미지나 텍스트를 추가할 수 있습니다. 또한, 하나의 PDF 파일에 서로 다른 헤더를 추가하는 것도 Python으로 시도해 보세요.

## PDF 파일 헤더에 텍스트 추가

[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스를 사용하여 PDF 파일의 헤더에 텍스트를 추가할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 텍스트를 추가하기 위해서는, 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그런 다음, 'add_stamp' 메서드를 호출하여 PDF 헤더에 텍스트를 추가할 수 있습니다.

PDF의 헤더 영역에 텍스트가 적절히 조정되도록 [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 속성을 설정해야 합니다. 또한 'horizontal_alignment'를 Center로, 'vertical_alignment'를 Top으로 설정해야 합니다.

다음 코드 스니펫은 Python으로 PDF 파일의 헤더에 텍스트를 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 헤더 생성
    textStamp = ap.TextStamp("Header Text")
    # 스탬프의 속성 설정
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # 모든 페이지에 헤더 추가
    for page in document.pages:
        page.add_stamp(textStamp)

    # 업데이트된 문서 저장
    document.save(output_pdf)
```

## PDF 파일의 바닥글에 텍스트 추가

[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스를 사용하여 PDF 파일의 바닥글에 텍스트를 추가할 수 있습니다.
 TextStamp 클래스는 폰트 크기, 폰트 스타일, 폰트 색상 등 텍스트 기반의 스탬프를 생성하는 데 필요한 속성을 제공합니다. 하단에 텍스트를 추가하려면, Document 객체와 필수 속성을 사용하여 TextStamp 객체를 생성해야 합니다. 그런 다음, PDF의 하단에 텍스트를 추가하기 위해 Page의 'add_stamp' 메서드를 호출할 수 있습니다.

다음 코드 스니펫은 Python으로 PDF 파일의 하단에 텍스트를 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # 하단부 생성
    textStamp = ap.TextStamp("Footer Text")
    # 스탬프의 속성 설정
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # 모든 페이지에 하단부 추가
    for page in document.pages:
        page.add_stamp(textStamp)

    # 업데이트된 PDF 파일 저장
    document.save(output_pdf)
```

## PDF 파일의 헤더에 이미지 추가

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스를 사용하여 PDF 파일의 헤더에 이미지를 추가할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 이미지를 추가하려면 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그런 다음, 'add_stamp' 메서드를 호출하여 PDF의 헤더에 이미지를 추가할 수 있습니다.

다음 코드 스니펫은 Python을 사용하여 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다:

```python 

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 헤더 생성
    image_stamp = ap.ImageStamp(input_image)
    # 스탬프의 속성 설정
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # 모든 페이지에 헤더 추가
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 업데이트된 문서 저장
    document.save(output_pdf)
```

## PDF 파일의 바닥글에 이미지 추가

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스를 사용하여 PDF 파일의 바닥글에 이미지를 추가할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 이미지를 추가하려면, Document 객체와 필요한 속성을 사용하여 Image Stamp 객체를 생성해야 합니다. 그 후, PDF의 바닥글에 이미지를 추가하기 위해 Page의 'add_stamp' 메소드를 호출할 수 있습니다.

다음 코드 스니펫은 Python으로 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # 바닥글 생성
    image_stamp = ap.ImageStamp(input_image)
    # 스탬프의 속성 설정
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # 모든 페이지에 바닥글 추가
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 업데이트된 PDF 파일 저장
    document.save(output_pdf)
```

## 하나의 PDF 파일에 다른 헤더 추가하기

우리는 [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 또는 [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 속성을 사용하여 문서의 헤더/푸터 섹션에 TextStamp를 추가할 수 있다는 것을 알고 있지만, 때로는 단일 PDF 문서에 여러 헤더/푸터를 추가해야 할 수도 있습니다. **Aspose.PDF for Python via .NET**은 이를 수행하는 방법을 설명합니다.

이 요구 사항을 달성하기 위해, 우리는 개별 TextStamp 객체를 생성하고(필요한 헤더/푸터의 수에 따라 객체의 수가 달라짐) 이를 PDF 문서에 추가할 것입니다.
 개별 스탬프 객체에 대해 다른 서식 정보를 지정할 수도 있습니다. 다음 예제에서는 Document 객체와 세 개의 TextStamp 객체를 생성한 다음 페이지의 'add_stamp' 메서드를 사용하여 PDF의 헤더 섹션에 텍스트를 추가했습니다. 다음 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 세 개의 스탬프 생성
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # 스탬프 정렬 설정 (페이지 상단에 스탬프를 배치하고 수평으로 가운데 정렬)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 글꼴 스타일을 굵게 지정
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # 텍스트 전경색 정보를 빨간색으로 설정
    stamp1.text_state.foreground_color = ap.Color.red
    # 글꼴 크기를 14로 지정
    stamp1.text_state.font_size = 14

    # 이제 두 번째 스탬프 객체의 수직 정렬을 상단으로 설정해야 합니다
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # 스탬프의 수평 정렬 정보를 가운데 정렬로 설정
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 스탬프 객체의 확대 비율 설정
    stamp2.zoom = 10

    # 세 번째 스탬프 객체의 서식 설정
    # 스탬프 객체의 수직 정렬 정보를 상단으로 지정
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # 스탬프 객체의 수평 정렬 정보를 가운데 정렬로 설정
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 스탬프 객체의 회전 각도 설정
    stamp3.rotate_angle = 35
    # 스탬프의 배경색을 분홍색으로 설정
    stamp3.text_state.background_color = ap.Color.pink
    # 스탬프의 글꼴 정보를 Verdana로 변경
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # 첫 번째 스탬프가 첫 페이지에 추가됩니다;
    document.pages[1].add_stamp(stamp1)
    # 두 번째 스탬프가 두 번째 페이지에 추가됩니다;
    document.pages[2].add_stamp(stamp2)
    # 세 번째 스탬프가 세 번째 페이지에 추가됩니다.
    document.pages[3].add_stamp(stamp3)

    # 업데이트된 문서 저장
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