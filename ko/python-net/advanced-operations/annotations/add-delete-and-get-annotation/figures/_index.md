---
title: Python을 사용하여 도형 주석 추가
linktitle: 도형 주석
type: docs
weight: 30
url: /ko/python-net/figures-annotation/
description: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 도형 주석을 조작하는 방법 가이드
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF 문서에서 사각형, 원형, 다각형 및 폴리라인 주석을 추가, 검색 및 삭제하는 포괄적인 가이드를 제공합니다. 사각형 및 원형 주석은 각각 사각형 및 타원형 모양으로 PDF 페이지의 특정 영역을 시각적으로 강조합니다. 이 문서에는 PDF 파일을 로드하고 제목, 색상, 불투명도와 같은 주석 속성을 구성한 후 PDF 페이지에 추가하는 단계별 지침과 Python 코드 스니펫이 포함되어 있습니다. 또한, 유형별로 주석을 검색하고 사각형 크기를 출력하며 PDF 문서에서 삭제하는 방법도 상세히 설명합니다. 다각형 및 폴리라인 주석도 다루며, 다각형은 연결된 정점들의 시리즈로 폐쇄된 형태를 정의하고, 폴리라인은 정점을 열린 형태로 연결합니다. 문서에는 이러한 주석을 PDF에 추가하는 과정과 접근 및 제거 방법을 보여주는 코드 예제가 제공됩니다.

---

## 사각형 및 원형 주석 추가

PDF 문서에서 사각형 주석은 사각형 모양으로 표현되는 특정 유형의 주석을 의미합니다. 사각형 주석은 문서 내의 특정 영역이나 섹션을 강조하거나 주의를 끌기 위해 사용됩니다.

[사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) 및 [원형](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) 주석은 각각 페이지에 사각형 또는 타원을 표시합니다.

사각형 또는 원형 주석 생성 단계:

1. PDF 파일을 로드합니다 - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새 [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation)을 생성하고 매개변수(새 Rectangle, 제목, 색상, interior_color, 불투명도)를 설정합니다.
1. 그런 다음 페이지에 사각형 주석을 추가합니다.

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

다음 코드 스니펫은 PDF 페이지에 원형 주석을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
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

예제로, PDF 문서에 사각형 및 원형 주석을 추가한 결과는 다음과 같습니다:

![원형 및 사각형 주석 데모](circle_demo.png)

### 원형 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 원형 주석을 가져와 보세요.

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


### 원형 주석 삭제

다음 코드 스니펫은 PDF 파일에서 원형 주석을 삭제하는 방법을 보여줍니다.

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

다음 코드 스니펫은 PDF 파일에서 사각형 주석을 삭제하는 방법을 보여줍니다.

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

Polyline 도구를 사용하면 문서에서 임의 개수의 변을 갖는 형태와 윤곽선을 만들 수 있습니다.

[다각형 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/)은 페이지에 다각형을 나타냅니다. 직선으로 연결된任意 개수의 정점을 가질 수 있습니다.

[폴리라인 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/)도 다각형과 유사하지만, 첫 번째와 마지막 정점이 암시적으로 연결되지 않는 것이 차이점입니다.

다각형 주석을 생성하는 단계:

1. PDF 파일을 로드합니다 - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새 [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation)을 생성하고 Polygon 매개변수(새 Rectangle, 새 Points, 제목, 색상, interior_color 및 불투명도)를 설정합니다.
1. 그런 다음 페이지에 주석을 추가합니다.

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

다음 코드 스니펫은 PDF 파일에 폴리라인 주석을 추가하는 방법을 보여줍니다:

1. PDF 파일을 로드합니다 - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새 [폴리라인 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/)을 생성하고 Polygon 매개변수(새 Rectangle, 새 Points, 제목, 색상, interior_color 및 불투명도)를 설정합니다.
1. 그런 다음 페이지에 주석을 추가합니다.

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

### 다각형 및 폴리라인 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 다각형 주석을 가져와 보세요.

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

다음 코드 스니펫을 사용하여 PDF 문서에서 폴리라인 주석을 가져와 보세요.

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

### 다각형 및 폴리라인 주석 삭제

다음 코드 스니펫은 PDF 파일에서 다각형 주석을 삭제하는 방법을 보여줍니다.

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


