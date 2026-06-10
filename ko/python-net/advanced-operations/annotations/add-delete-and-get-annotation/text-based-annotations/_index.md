---
title: Python을 사용한 텍스트 기반 주석
linktitle: 텍스트 주석
type: docs
weight: 10
url: /ko/python-net/text-based-annotations/
description: .NET을 통해 Aspose.PDF for Python을 사용하여 PDF 문서에서 자유 텍스트를 추가, 검사 및 삭제하고, 강조 표시, 밑줄을 긋고, 구불구불하게 주석을 제거하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 텍스트 및 텍스트 마크업 PDF 주석으로 작업하세요.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 텍스트 기반 주석을 만들고, 읽고, 제거하는 방법을 설명합니다.병합, 쿼드 포인트, 표시된 텍스트 추출과 같은 고급 언더라인 워크플로를 비롯하여 자유 텍스트 주석과 하이라이트, 밑줄, 물결 모양 및 취소선과 같은 텍스트 마크업 주석을 다룹니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 텍스트 기반 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 몇 가지 텍스트 주석 워크플로를 보여줍니다.

- 자유 텍스트 주석
- 하이라이트 주석
- 밑줄 주석
- 구불구불한 주석
- 스트라이크아웃 주석

## 자유 텍스트 주석

### 자유 텍스트 주석 추가 

자유 텍스트 주석을 사용하면 눈에 보이는 텍스트 주석을 PDF 페이지에 직접 추가할 수 있습니다.이 예제에서는 첫 페이지에 간단한 자유 텍스트 주석을 추가합니다.

#### 원본 PDF 열기

```python
document = ap.Document(infile)
```

#### 자유 텍스트 주석 생성 및 구성

```python
free_text_annotation = ap.annotations.FreeTextAnnotation(
    document.pages[1],
    ap.Rectangle(299, 713, 308, 720, True),
    ap.annotations.DefaultAppearance(),
)
free_text_annotation.title = "Aspose User"
free_text_annotation.color = ap.Color.light_green
```

#### 주석을 추가하고 PDF를 저장합니다.

```python
document.pages[1].annotations.append(free_text_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### 자유 텍스트 주석 받기 

자유 텍스트 주석을 검사하려면 첫 페이지 주석을 다음과 같이 필터링합니다. `FREE_TEXT` 각 주석 사각형을 입력하고 인쇄합니다.

#### 문서 로드 및 자유 텍스트 주석 수집

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]
```

#### 주석 사각형 인쇄

```python
for annotation in free_text_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### 자유 텍스트 주석 삭제 

이 워크플로우는 첫 페이지에서 모든 자유 텍스트 주석을 제거하고 업데이트된 PDF를 저장합니다.

#### 자유 텍스트 주석 찾기 및 삭제

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]

for annotation in free_text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## 텍스트 마크업 주석

### 하이라이트 주석

#### 텍스트 하이라이트 추가

하이라이트 주석은 기본 내용을 변경하지 않고 문서의 일부를 강조합니다.이 예제에서는 첫 페이지에 하이라이트 주석을 추가합니다.

```python
document = ap.Document(infile)

highlight_annotation = ap.annotations.HighlightAnnotation(
    document.pages[1],
    ap.Rectangle(300, 750, 320, 770, True),
)

document.pages[1].annotations.append(highlight_annotation)
document.save(outfile)
```

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

#### 텍스트 하이라이트 가져오기

하이라이트 주석을 검사하려면 페이지 주석을 다음과 같이 필터링하십시오. `HIGHLIGHT` 직사각형을 입력하고 인쇄합니다.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    print(annotation.rect)
```

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

#### 텍스트 하이라이트 삭제

이 워크플로우는 첫 페이지에서 모든 강조 주석을 제거하고 출력 PDF를 저장합니다.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### 밑줄 주석

#### 텍스트 밑줄 주석 추가

밑줄 주석은 텍스트를 눈에 띄는 밑줄로 표시합니다.이 예제에서는 기본 밑줄 주석을 추가하고 메타데이터와 색상을 설정합니다.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline 1"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### 텍스트 추가, 밑줄, 주석 평평하게 하기 

밑줄을 대화형 주석으로 남지 않고 페이지 내용의 일부로 사용하려면 밑줄을 추가한 후 밑줄을 평평하게 할 수 있습니다.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline to Flatten"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
underline_annotation.flatten()

document.save(outfile)
```

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

#### 쿼드 포인트가 있는 텍스트 밑줄 주석 추가

쿼드 포인트를 사용하면 밑줄 주석의 정확한 표시 영역을 정의할 수 있습니다.이는 단순한 직사각형보다 더 많은 제어가 필요할 때 유용합니다.

```python
document = ap.Document(infile)
rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline with Quad Points"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue
underline_annotation.quad_points = [
    ap.Point(rect.llx, rect.lly),
    ap.Point(rect.urx, rect.lly),
    ap.Point(rect.urx, rect.ury),
    ap.Point(rect.llx, rect.ury),
]

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### 텍스트 밑줄 주석 삭제

이 워크플로우는 첫 페이지에서 모든 밑줄 주석을 제거하고 업데이트된 문서를 저장합니다.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### 제목별 텍스트 밑줄 주석 삭제

이 워크플로우는 제목을 확인한 후 밑줄 주석을 선택적으로 삭제하는 방법을 보여줍니다.

```python
document = ap.Document(infile)

underline_annotations = [
    cast(ap.annotations.UnderlineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    if annotation.title.startswith("a"):
        document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### 텍스트 밑줄 주석 가져오기

밑줄 주석을 검사하려면 첫 페이지 주석을 다음과 같이 필터링합니다. `UNDERLINE` 각 사각형을 입력하고 인쇄합니다.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    print(annotation.rect)
```

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

#### 텍스트, 밑줄, 주석, 표시된 텍스트 가져오기

이 워크플로우는 각 밑줄 주석을 다음과 같이 변환합니다. `UnderlineAnnotation` 객체를 생성하고 표시된 텍스트를 추출합니다.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    print(f"Marked text: {ua.get_marked_text()}")
```

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

#### 텍스트, 밑줄, 주석, 표시된 부분 가져오기

표시된 각 프래그먼트가 별도로 필요한 경우 에서 반환한 컬렉션을 반복할 수 있습니다. `get_marked_text_fragments()`.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    for fragment in ua.get_marked_text_fragments():
        print(f"Fragment text: {fragment.text}")
```

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


### 구불구불한 주석

#### 구불구불한 주석 추가

구불구불한 주석은 텍스트의 맞춤법, 문법 또는 주의 영역을 표시하는 데 자주 사용됩니다.이 예제에서는 첫 페이지에 구불구불한 주석을 추가합니다.

```python
document = ap.Document(infile)
page = document.pages[1]

squiggly_annotation = ap.annotations.SquigglyAnnotation(
    page,
    ap.Rectangle(67, 317, 261, 459, True),
)
squiggly_annotation.title = "John Smith"
squiggly_annotation.color = ap.Color.blue

page.annotations.append(squiggly_annotation)
document.save(outfile)
```

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

#### 구불구불한 주석 가져오기

구불구불한 주석을 검사하려면 페이지 주석을 다음과 같이 필터링하십시오. `SQUIGGLY` 직사각형을 입력하고 인쇄합니다.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    print(annotation.rect)
```

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

#### 구불구불한 주석 삭제

이 워크플로우는 첫 페이지에서 구불구불한 주석을 모두 제거하고 결과를 저장합니다.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### 스트라이크아웃 어노테이션

#### 텍스트 취소선 주석 추가

취소선 주석은 제거되거나 줄이 그어진 것으로 처리해야 하는 텍스트를 표시합니다.이 예제에서는 취소선 주석을 추가하고 메타데이터와 색상을 설정합니다.

```python
document = ap.Document(infile)

strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
strikeout_annotation.title = "Aspose User"
strikeout_annotation.subject = "Inserted text 1"
strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
strikeout_annotation.color = ap.Color.blue

document.pages[1].annotations.append(strikeout_annotation)
document.save(outfile)
```

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

#### 텍스트 취소선 주석 가져오기

취소선 주석을 검사하려면 페이지 주석을 다음과 같이 필터링하십시오. `STRIKE_OUT` 직사각형을 입력하고 인쇄합니다.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    print(annotation.rect)
```

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

#### 텍스트 취소선 주석 삭제

이 워크플로우는 첫 페이지에서 취소선 주석을 모두 제거하고 업데이트된 문서를 저장합니다.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
