---
title: PDF에 텍스트 스탬프 추가하기 (Python 사용)
linktitle: PDF 파일에 텍스트 스탬프
type: docs
weight: 20
url: /ko/python-net/text-stamps-in-the-pdf-file/
description: Aspose.PDF for Python 라이브러리의 TextStamp 클래스를 사용하여 PDF 문서에 텍스트 스탬프를 추가합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에 텍스트 스탬프 추가하기 (Python)",
    "alternativeHeadline": "PDF에 텍스트 스탬프 추가하기 (Python)",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python 라이브러리의 TextStamp 클래스를 사용하여 PDF 문서에 텍스트 스탬프를 추가합니다."
}
</script>


## Python으로 텍스트 스탬프 추가하기

PDF 파일에 텍스트 스탬프를 추가하려면 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스를 사용할 수 있습니다. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 텍스트 스탬프를 추가하려면 Document 객체와 필요한 속성을 사용하는 TextStamp 객체를 생성해야 합니다. 그 후, [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드를 호출하여 PDF에 스탬프를 추가할 수 있습니다. 다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 텍스트 스탬프 생성
    text_stamp = ap.TextStamp("Sample Stamp")
    # 스탬프가 배경인지 설정
    text_stamp.background = True
    # 원점 설정
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # 스탬프 회전
    text_stamp.rotate = ap.Rotation.ON90
    # 텍스트 속성 설정
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # 특정 페이지에 스탬프 추가
    document.pages[1].add_stamp(text_stamp)

    # 출력 문서 저장
    document.save(output_pdf)
```


## TextStamp 객체에 대한 정렬 정의

PDF 문서에 워터마크를 추가하는 것은 자주 요구되는 기능 중 하나이며 Aspose.PDF for Python은 이미지뿐만 아니라 텍스트 워터마크를 추가할 수 있는 완전한 기능을 제공합니다. 우리는 PDF 파일에 텍스트 스탬프를 추가하는 기능을 제공하는 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/)라는 클래스를 가지고 있습니다. 최근에는 TextStamp 객체를 사용할 때 텍스트의 정렬을 지정할 수 있는 기능을 지원해야 할 필요가 있었습니다. 따라서 이 요구를 충족시키기 위해 [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 속성을 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스에 도입했습니다. 이 속성을 사용하여 [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 텍스트 정렬을 지정할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서를 로드하고 TextStamp를 추가하는 방법을 예시로 보여줍니다.

```python

    import aspose.pdf as ap

    # 입력 파일로 Document 객체 인스턴스화
    doc = ap.Document(input_pdf)
    # 예제 문자열로 FormattedText 객체 인스턴스화
    text = ap.facades.FormattedText("This")
    # FormattedText에 새 텍스트 줄 추가
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # FormattedText를 사용하여 TextStamp 객체 생성
    stamp = ap.TextStamp(text)
    # 텍스트 스탬프의 수평 정렬을 가운데 정렬로 지정
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 텍스트 스탬프의 수직 정렬을 가운데 정렬로 지정
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # TextStamp의 텍스트 수평 정렬을 가운데 정렬로 지정
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # 스탬프 객체의 상단 여백 설정
    stamp.top_margin = 20
    # 문서의 첫 번째 페이지에 스탬프 객체 추가
    doc.pages[1].add_stamp(stamp)

    # 업데이트된 문서 저장
    doc.save(output_pdf)
```


## PDF 파일에 도장으로 채우기 및 윤곽선 텍스트 추가

텍스트 추가 및 편집 시나리오에 대한 렌더링 모드를 설정하는 기능을 구현했습니다. 윤곽선 텍스트를 렌더링하려면 고급 속성을 전달하기 위해 TextState 객체를 생성하세요. 윤곽선의 색상을 설정하세요. 그런 다음 텍스트 렌더링 모드를 설정합니다. 다음 단계는 TextState를 바인딩하고 도장을 추가하는 것입니다.

다음 코드 스니펫은 채우기 및 윤곽선 텍스트 추가를 시연합니다:

```python

    import aspose.pdf as ap

    # 고급 속성을 전달하기 위해 TextState 객체 생성
    ts = ap.text.TextState()
    # 윤곽선의 색상 설정
    ts.stroking_color = ap.Color.gray
    # 텍스트 렌더링 모드 설정
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # 입력 PDF 문서 로드
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # TextState 바인딩
    stamp.bind_text_state(ts)
    # X,Y 원점 설정
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # 도장 추가
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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