---
title: 파이썬을 사용한 PDF 하이라이트 주석
linktitle: 하이라이트 주석
type: docs
weight: 20
url: /python-net/highlights-annotation/
description: 마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 지그재그 밑줄로 표시됩니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용한 PDF 하이라이트 주석",
    "alternativeHeadline": "PDF에 하이라이트 주석 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 하이라이트 주석, 텍스트 마크업 주석",
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
    "url": "/python-net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/highlights-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 지그재그 밑줄로 표시됩니다."
}
</script>


PDF의 텍스트 마크업 주석은 문서의 텍스트를 강조 표시, 밑줄, 생략 또는 노트 추가하는 데 사용됩니다. 이러한 주석은 텍스트의 특정 부분을 강조하거나 주의를 끌기 위한 것입니다. 이러한 주석을 통해 사용자는 PDF 파일의 내용을 시각적으로 표시하거나 수정할 수 있습니다.

강조 주석은 텍스트의 중요성이나 관련성을 나타내기 위해 보통 노란색 배경으로 텍스트를 표시하는 데 사용됩니다.

밑줄 주석은 선택된 텍스트 아래에 선을 그어 중요성, 강조 또는 제안된 수정을 나타냅니다.

취소선 주석은 특정 텍스트의 취소선 또는 취소선을 포함하여 삭제되었거나 교체되었거나 더 이상 유효하지 않음을 표시합니다.

물결선은 철자 오류, 잠재적 문제 또는 제안된 변경 사항과 같은 다른 유형의 강조를 나타내기 위해 텍스트에 밑줄을 긋는 데 사용됩니다.

## 텍스트 마크업 주석 추가

PDF 문서에 텍스트 마크업 주석을 추가하려면 다음 작업을 수행해야 합니다:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체.
1. 주석 생성:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) 및 매개변수 설정 (제목, 색상).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) 및 매개변수 설정 (제목, 색상).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) 및 매개변수 설정 (제목, 색상).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) 및 매개변수 설정 (제목, 색상).
1. 그런 다음 모든 주석을 페이지에 추가해야 합니다.

### 하이라이트 주석 추가

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    # 원형 주석 생성
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```


### 취소선 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "삽입된 텍스트 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### 물결선 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### 밑줄 주석 추가

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "삽입된 밑줄 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```


## 텍스트 마크업 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 텍스트 마크업 주석을 가져오세요.

### 하이라이트 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### 취소선 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

### 물결선 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```


### 밑줄 주석 가져오기

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## 텍스트 마크업 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 마크업 주석을 삭제하는 방법을 보여줍니다.

### 형광펜 주석 삭제

```python

    import aspose.pdf as ap

    # PDF 파일 불러오기
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### 취소선 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


### 물결표 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 밑줄 주석 삭제

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
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