---
title: 파이썬을 사용한 추가 주석
linktitle: 추가 주석
type: docs
weight: 60
url: /python-net/extra-annotations/
description: 이 섹션은 PDF 문서에서 추가 유형의 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용한 추가 주석",
    "alternativeHeadline": "PDF에 추가 주석을 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 링크 주석, 캐럿 주석",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "이 섹션은 파이썬으로 PDF 문서에서 추가 유형의 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다."
}
</script>


## 기존 PDF 파일에 Caret 주석 추가하는 방법 (Python 사용)

Caret 주석은 텍스트 편집을 나타내는 기호입니다. Caret 주석은 마크업 주석이기도 하므로, Caret 클래스는 Markup 클래스에서 파생되며 Caret 주석의 속성을 가져오거나 설정하는 함수와 Caret 주석의 모양 흐름을 재설정하는 기능을 제공합니다. Caret 주석은 종종 텍스트의 변경, 추가 또는 수정을 제안하는 데 사용됩니다.

Caret 주석을 만드는 단계:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새로운 [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) 생성 및 Caret 매개변수 설정 (새로운 Rectangle, 제목, 주제, 플래그, 색상). 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다.
1. 페이지에 주석을 추가할 수 있을 때.

다음 코드 스니펫은 PDF 파일에 Caret 주석을 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### 캐럿 주석 가져오기

PDF 문서에서 캐럿 주석을 가져오려면 다음 코드 스니펫을 사용해 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### 캐럿 주석 삭제

다음 코드 스니펫은 Python을 사용하여 PDF 파일에서 캐럿 주석을 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # PDF 파일 로드
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## 링크 주석 추가

[링크](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)는 클릭 시 URL을 열거나 동일한 문서 내 또는 외부 문서 내 특정 위치로 이동하는 주석입니다.

Link Annotations는 페이지 어디에나 배치할 수 있는 직사각형 영역입니다. 각 링크에는 해당 링크 영역을 클릭할 때 수행되는 PDF 작업이 연결되어 있습니다.

다음 코드 스니펫은 전화번호 예제를 사용하여 PDF 파일에 링크 주석을 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # 전화번호를 찾기 위해 TextFragmentAbsorber 객체 생성
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # 1페이지에 대해서만 absorber를 수락
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # 링크 주석을 만들고 전화번호를 호출하는 작업을 설정
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # 페이지에 주석 추가
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### 링크 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)을 가져오십시오.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### 링크 주석 삭제

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 1페이지의 모든 링크 주석을 찾아 제거해야 합니다. 그런 다음 주석이 제거된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Aspose.PDF for Python을 사용하여 특정 페이지 영역을 수정 주석으로 수정

Aspose.PDF for Python via .NET은 기존 PDF 파일에 주석을 추가하고 조작하는 기능을 지원합니다. PDF 문서의 수정 주석은 문서에서 기밀 정보를 영구적으로 제거하거나 숨기는 목적을 가지고 있습니다. 정보 편집 과정은 텍스트, 이미지 또는 그래픽과 같은 특정 콘텐츠를 덮거나 음영 처리하여 다른 사람들이 볼 수 없고 액세스할 수 없도록 하는 것을 포함합니다. 이를 통해 민감한 정보가 문서 내에서 숨겨지고 보호되도록 보장합니다. 이러한 요구를 충족시키기 위해 [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/)이라는 클래스가 제공되며, 특정 페이지 영역을 수정하거나 기존의 수정 주석을 조작하여 수정할 수 있습니다 (즉, 주석을 평평하게 하고 그 아래의 텍스트를 제거합니다).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```


### Get Redaction Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```    

### Delete Redaction Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

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