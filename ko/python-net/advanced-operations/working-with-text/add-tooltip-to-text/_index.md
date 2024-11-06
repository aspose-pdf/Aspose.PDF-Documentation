---
title: PDF Tooltip using Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: ko/python-net/pdf-tooltip/
description: Python과 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 배우세요.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using Python",
    "alternativeHeadline": "Add PDF Tooltip to the Text",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf tooltip",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Python과 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 배우세요."
}
</script>


## 검색된 텍스트에 보이지 않는 버튼으로 툴팁 추가하기

이 코드는 Aspose.PDF를 사용하여 PDF 문서의 특정 텍스트 조각에 툴팁을 추가하는 방법을 보여줍니다. 마우스 커서가 해당 텍스트 위로 이동하면 툴팁이 표시됩니다.

다음 코드 스니펫은 이 기능을 구현하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("마우스 커서를 여기에 이동하여 툴팁을 표시")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "마우스 커서를 여기에 이동하여 매우 긴 툴팁을 표시"
        )
    )
    document.save(output_pdf)

    # 텍스트가 있는 문서 열기
    document = ap.Document(output_pdf)
    # 정규 표현식과 일치하는 모든 구문을 찾기 위해 TextAbsorber 객체 생성
    absorber = ap.text.TextFragmentAbsorber(
        "마우스 커서를 여기에 이동하여 툴팁을 표시"
    )
    # 문서 페이지에 흡수기 적용
    document.pages.accept(absorber)
    # 추출된 텍스트 조각 가져오기
    text_fragments = absorber.text_fragments

    # 조각들을 순회하기
    for fragment in text_fragments:
        # 텍스트 조각 위치에 보이지 않는 버튼 생성
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # alternate_name 값이 뷰어 애플리케이션에 의해 툴팁으로 표시됨
        field.alternate_name = "텍스트에 대한 툴팁."
        # 문서에 버튼 필드 추가
        document.form.add(field)

    # 다음은 매우 긴 툴팁의 예제
    absorber = ap.text.TextFragmentAbsorber(
        "마우스 커서를 여기에 이동하여 매우 긴 툴팁을 표시"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # 매우 긴 텍스트 설정
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # 문서 저장
    document.save(output_pdf)
```


## 마우스를 올리면 나타나는 숨겨진 텍스트 블록 만들기

이 Python 코드 스니펫은 특정 영역에 마우스 커서를 올리면 나타나는 PDF 문서에 떠있는 텍스트를 추가하는 방법을 보여줍니다.

먼저, 새로운 PDF 문서를 생성하고 "마우스 커서를 여기로 이동하여 떠있는 텍스트 표시"라는 텍스트를 포함하는 단락을 추가합니다. 그런 다음 문서를 저장합니다.

다음으로, 저장된 문서를 다시 열고, 이전에 추가된 텍스트 조각을 찾기 위해 TextAbsorber 객체를 생성합니다. 이 텍스트 조각은 떠있는 텍스트 필드의 위치와 특성을 정의하는 데 사용됩니다.

떠있는 텍스트 필드를 나타내기 위해 TextBoxField 객체가 생성되며, 위치, 값, 읽기 전용 상태, 가시성 등의 속성이 적절하게 설정됩니다. 또한 필드에 고유한 이름과 외관 특성이 할당됩니다.

떠있는 텍스트 필드는 문서의 폼에 추가되고, 원본 텍스트 조각의 위치에 보이지 않는 버튼 필드가 생성됩니다.
 HideAction 이벤트는 버튼 필드에 할당되어 있으며, 마우스 커서가 그 주변에 들어올 때 부동 텍스트 필드가 나타나고 커서가 나갈 때 사라지도록 지정합니다.

마지막으로, 버튼 필드를 문서의 양식에 추가하고 수정된 문서를 저장합니다.

이 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 문서에서 상호작용하는 부동 텍스트 요소를 생성하는 방법을 제공합니다.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("여기에 마우스 커서를 이동하여 부동 텍스트 표시")
    )
    document.save(output_pdf)

    # 텍스트가 포함된 문서 열기
    document = ap.Document(output_pdf)
    # 정규 표현식과 일치하는 모든 구문을 찾기 위한 TextAbsorber 객체 생성
    absorber = ap.text.TextFragmentAbsorber(
        "여기에 마우스 커서를 이동하여 부동 텍스트 표시"
    )
    # 문서 페이지에 흡수기 적용
    document.pages.accept(absorber)
    # 첫 번째 추출된 텍스트 조각 얻기
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # 페이지의 지정된 사각형에 부동 텍스트를 위한 숨겨진 텍스트 필드 생성
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # 필드 값으로 표시될 텍스트 설정
    floating_field.value = '이것은 "부동 텍스트 필드"입니다.'
    # 이 시나리오에서는 필드를 '읽기 전용'으로 만드는 것이 좋습니다.
    floating_field.read_only = True
    # 문서 열 때 필드를 보이지 않게 하기 위한 'hidden' 플래그 설정
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # 고유한 필드 이름 설정은 필수는 아니지만 허용됨
    floating_field.partial_name = "FloatingField_1"

    # 필드 모양의 특성을 설정하는 것은 필수는 아니지만 더 좋게 만듭니다.
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # 문서에 텍스트 필드 추가
    document.form.add(floating_field)
    # 텍스트 조각 위치에 보이지 않는 버튼 생성
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # 지정된 필드(주석)에 대한 새 숨김 동작 및 보이지 않음 플래그 생성.
    # (위에서 지정한 경우 필드 이름으로 부동 필드를 참조할 수도 있습니다.)
    # 보이지 않는 버튼 필드에 마우스 입력/출력 시 동작 추가

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # 문서에 버튼 필드 추가
    document.form.add(button_field)

    # 문서 저장
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
                "contactType": "판매",
                "areaServed": "미국",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "영국",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
                "areaServed": "호주",
                "availableLanguage": "영어"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>