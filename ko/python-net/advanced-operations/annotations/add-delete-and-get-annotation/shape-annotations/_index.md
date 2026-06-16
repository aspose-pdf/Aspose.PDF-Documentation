---
title: 파이썬을 통한 셰이프 주석
linktitle: 셰이프 주석
type: docs
weight: 20
url: /ko/python-net/shape-annotations/
description: .NET을 통해 Aspose.PDF for Python을 사용하여 PDF 문서에서 선, 사각형, 원, 다각형 및 폴리라인 주석을 추가, 검사 및 삭제하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 기하학적 PDF 주석으로 작업하세요.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 모양 주석을 만들고 읽고 제거하는 방법을 설명합니다.선, 사각형, 원, 다각형 및 폴리라인 주석을 다루며, 각 워크플로는 작은 단계와 전체 코드 예제로 나뉩니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 모양 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 여러 지오메트리 기반 주석 워크플로를 보여줍니다.

- 라인 주석
- 정사각형 주석
- 서클 주석
- 폴리곤 주석
- 폴리라인 주석

## 라인 어노테이션 

### 라인 주석 추가 

이 예제에서는 첫 페이지에 선 주석을 추가하고 화살표 스타일, 선 너비 및 팝업 창을 구성합니다.

#### 원본 PDF 열기

```python
document = ap.Document(infile)
```

#### 라인 주석 생성 및 구성

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### 팝업을 첨부하고 PDF를 저장합니다.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### 줄 주석 가져오기 

라인 주석을 검사하려면 첫 페이지에서 주석 컬렉션을 필터링하고 각 결과를 다음과 같이 캐스팅합니다. `LineAnnotation` 그래서 시작점과 끝점을 읽을 수 있습니다.

#### PDF 로드 및 라인 주석 수집

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### 선 좌표 인쇄

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### 전체 예제

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### 라인 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 줄 주석을 제거하고 업데이트된 PDF를 저장합니다.

#### 제거할 라인 주석 찾기

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### 주석을 삭제하고 PDF를 저장합니다.

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## 정사각형 및 원형 주석

### 정사각형 주석 추가 

정사각형 주석은 문서의 사각형 영역을 표시하는 데 유용합니다.이 예제에서는 테두리, 채우기 및 투명도 설정을 사용하여 정사각형 주석을 만듭니다.

#### PDF를 열고 사각형 주석을 작성합니다.

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### 주석을 추가하고 PDF를 저장합니다.

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### 정사각형 주석 가져오기 

사각형 주석을 검사하려면 첫 페이지 주석을 다음과 같이 필터링합니다. `SQUARE` 각 사각형을 입력하고 인쇄합니다.

#### 문서를 로드하고 사각형 주석을 수집하세요.

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### 주석 사각형 인쇄

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### 정사각형 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 사각형 주석을 제거하고 문서를 저장합니다.

#### 정사각형 주석 찾기 및 삭제

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### 원 주석 추가 

원 주석은 PDF의 둥근 영역을 표시합니다.이 예제에서는 채우기 색상, 불투명도 및 팝업 주석이 포함된 원 주석을 추가합니다.

#### PDF를 열고 원 주석을 작성합니다.

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### 팝업을 첨부하고 PDF를 저장합니다.

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### 원 주석 가져오기 

원 주석을 검사하려면 페이지 주석을 다음과 같이 필터링하십시오. `CIRCLE` 직사각형을 입력하고 인쇄합니다.

#### 문서를 로드하고 서클 주석을 수집하세요.

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### 주석 사각형 인쇄

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### 서클 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 원 주석을 제거하고 출력 PDF를 저장합니다.

#### 원 주석 찾기 및 삭제

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## 폴리곤 및 폴리라인 주석

### 폴리곤 주석 추가 

다각형 주석은 닫힌 다중점 모양을 정의합니다.이 예제에서는 사각형과 포인트 목록을 사용하여 폴리곤 주석을 만듭니다.

#### PDF를 열고 다각형 주석을 생성합니다.

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
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
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### 주석을 추가하고 PDF를 저장합니다.

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
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
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### 폴리곤 주석 가져오기 

폴리곤 주석을 검사하려면 첫 페이지 주석을 다음과 같이 필터링합니다. `POLYGON` 각 주석 사각형을 입력하고 인쇄합니다.

#### 문서를 로드하고 폴리곤 주석을 수집합니다.

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### 주석 사각형 인쇄

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### 폴리곤 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 다각형 주석을 제거하고 업데이트된 PDF를 저장합니다.

#### 폴리곤 주석 찾기 및 삭제

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### 폴리라인 주석 추가 

폴리라인 주석은 여러 점을 통과하는 열린 경로를 정의합니다.이 예제에서는 팝업 노트가 있는 폴리라인 주석을 만듭니다.

#### PDF를 열고 폴리라인 주석을 작성합니다.

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
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
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### 팝업을 첨부하고 PDF를 저장합니다.

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
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
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### 폴리라인 주석 가져오기 

폴리라인 주석을 검사하려면 페이지 주석을 다음과 같이 필터링하십시오. `POLY_LINE` 직사각형을 입력하고 인쇄합니다.

#### 문서 로드 및 폴리라인 주석 수집

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### 주석 사각형 인쇄

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### 폴리라인 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 폴리라인 주석을 제거하고 출력 PDF를 저장합니다.

#### 폴리라인 주석 찾기 및 삭제

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
