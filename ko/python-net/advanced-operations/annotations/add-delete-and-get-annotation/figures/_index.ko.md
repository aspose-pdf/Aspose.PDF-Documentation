---
title: 파이썬을 사용하여 도형 주석 추가하기
linktitle: 도형 주석
type: docs
weight: 30
url: /python-net/figures-annotation/
description: 이 문서에서는 Aspose.PDF for Python을 통해 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 도형 주석 추가하기",
    "alternativeHeadline": "PDF에 도형 주석 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, figures annotations, polygon annotation, line annotation, square annotation, circle annotation",
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
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "이 문서에서는 Aspose.PDF for Python을 사용하여 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다."
}
</script>


## 사각형 및 원 주석 추가

PDF 문서에서 사각형 주석은 사각형 모양으로 나타나는 특정 유형의 주석을 의미합니다. 사각형 주석은 문서 내의 특정 영역이나 섹션을 강조하거나 주의를 끌기 위해 사용됩니다.

[사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) 및 [원](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) 주석은 각각 페이지에 사각형 또는 타원을 표시합니다.

사각형 또는 원 주석을 만드는 단계:

1. PDF 파일을 로드합니다 - 새로운 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. 새로운 [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation)을 생성하고 매개변수(새로운 Rectangle, 제목, 색상, 내부 색상, 불투명도)를 설정합니다.
3. 그런 다음 페이지에 사각형 주석을 추가해야 합니다.

다음 코드 스니펫은 PDF 페이지에 사각형 주석을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

다음 코드 조각은 PDF 페이지에 원형 주석을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```


예를 들어, PDF 문서에 사각형 및 원 주석을 추가한 결과는 다음과 같습니다:

![원 및 사각형 주석 데모](circle_demo.png)

### 원 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 원 주석을 가져와 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### 사각형 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 사각형 주석을 가져와 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```



### 원 주석 삭제하기

PDF 파일에서 원 주석을 삭제하는 방법을 보여주는 다음 코드 조각입니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### 사각형 주석 삭제

PDF 파일에서 사각형 주석을 삭제하는 방법을 보여주는 다음 코드 조각입니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## 다각형 및 폴리라인 주석 추가

폴리라인 도구를 사용하면 문서에서 임의의 개수의 변을 가진 도형 및 윤곽선을 생성할 수 있습니다.

[Polygon Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/)는 페이지에 다각형을 나타냅니다. 이들은 직선으로 연결된 임의의 수의 꼭지점을 가질 수 있습니다.

[Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/)도 다각형과 유사하지만, 첫 번째와 마지막 꼭지점이 암묵적으로 연결되지 않는다는 점이 다릅니다.

다각형 주석을 생성하는 단계:

1. PDF 파일 로드 - 새 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새 [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) 생성 및 다각형 매개변수 설정 (새 Rectangle, 새 Points, 제목, 색상, 내부 색상 및 불투명도).
1. 이후 페이지에 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 다각형 주석을 추가하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```


다음 코드 스니펫은 PDF 파일에 Polyline 주석을 추가하는 방법을 보여줍니다:

1. PDF 파일을 로드합니다 - 새로운 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새로운 [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/)을 생성하고 다각형 매개변수(새 Rectangle, 새 Points, 제목, 색상, 내부 색상 및 불투명도)를 설정합니다.
1. 그 후 페이지에 주석을 추가할 수 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```


### 폴리곤 및 폴리라인 주석 가져오기

PDF 문서에서 폴리곤 주석을 가져오기 위해 다음 코드 조각을 사용해 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

PDF 문서에서 폴리라인 주석을 가져오기 위해 다음 코드 조각을 사용해 보세요.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### 폴리곤 및 폴리라인 주석 삭제

다음 코드 조각은 PDF 파일에서 폴리곤 주석을 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


다음 코드 스니펫은 PDF 파일에서 폴리라인 주석을 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
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