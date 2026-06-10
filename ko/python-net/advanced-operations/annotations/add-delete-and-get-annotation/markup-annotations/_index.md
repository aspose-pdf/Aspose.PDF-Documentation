---
title: Python을 사용한 마크업 주석
linktitle: 마크업 주석
type: docs
weight: 30
url: /ko/python-net/markup-annotations/
description: .NET을 통해 Aspose.PDF for Python을 사용하여 PDF 문서에서 텍스트, 캐럿 및 주석을 추가, 읽고, 삭제하고, 주석을 바꾸는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 마크업 주석 작업을 할 수 있습니다.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 마크업 주석을 만들고, 검사하고, 제거하는 방법을 설명합니다.텍스트 주석, 캐럿 주석, 대체 주석을 다루며, 각 워크플로를 작은 단계와 코드 예제로 나누어 설명합니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 마크업 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 세 가지 일반적인 주석 워크플로를 보여줍니다.

- 노트 스타일 코멘트의 텍스트 주석
- 삽입 마커용 캐럿 주석
- 텍스트 대체 마크업을 위한 주석 교체

## 텍스트 주석

### 텍스트 주석 추가

이 예제에서는 첫 페이지에 텍스트 주석을 만들어 팝업 창에 연결합니다.텍스트 주석은 검토 워크플로의 스티커 노트 스타일 주석에 유용합니다.

#### 원본 PDF 열기

```python
document = ap.Document(infile)
```

#### 텍스트 주석 생성 및 구성

주석 사각형을 정의하고 제목, 제목, 내용, 표시 플래그, 색상 및 아이콘을 설정합니다.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### 팝업 주석 만들기

팝업 창을 만들어 텍스트 주석에 연결합니다.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### 주석을 추가하고 PDF를 저장합니다.

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### 전체 예제

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### 텍스트 주석 가져오기

기존 텍스트 주석을 검사하려면 첫 페이지에서 주석 컬렉션을 필터링하고 유형이 다음과 같은 항목만 유지합니다. `TEXT`.

#### 문서 로드 및 텍스트 주석 수집

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### 주석 사각형 인쇄

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### 전체 예제

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### 텍스트 주석 삭제

이 워크플로우는 첫 페이지에서 모든 텍스트 주석을 제거하고 수정된 PDF를 저장합니다.

#### 제거할 텍스트 주석 찾기

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### 주석을 삭제하고 파일을 저장합니다.

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 전체 예제

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## 캐럿 주석

### 캐럿 주석 추가

캐럿 주석은 리뷰 시나리오에서 삽입점을 표시하는 데 사용됩니다.이 예에서는 팝업 노트가 첨부된 캐럿 주석을 추가합니다.

#### 문서를 열고 대상 페이지 가져오기

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### 캐럿 주석 생성 및 구성

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### 팝업을 첨부하고 문서를 저장합니다.

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### 전체 예제

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### 캐럿 주석 가져오기

캐럿 주석을 검사하려면 페이지 주석을 반복하고 다음을 기준으로 필터링합니다. `CARET` 주석 유형

#### 문서 및 페이지 로드

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### 캐럿 주석 사각형 인쇄

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### 전체 예제

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### 캐럿 주석 삭제

이 워크플로는 먼저 캐럿 주석을 수집하고 하나씩 삭제한 다음 업데이트된 파일을 저장합니다.

#### 문서 로드 및 캐럿 주석 수집

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### 주석을 삭제하고 문서를 저장합니다.

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### 전체 예제

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## 주석 바꾸기

### 대체 주석 추가

대체 주석은 캐럿 주석과 그룹화된 취소선 주석을 결합합니다.이 패턴은 바꿔야 할 텍스트를 표시하고, 줄이 그어진 내용에 대체 메모를 연결합니다.

#### 문서를 열고 페이지를 가져옵니다.

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### 대체 텍스트를 위한 캐럿 주석 만들기

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### 그룹화된 스트라이크아웃 주석 만들기

스트라이크아웃 영역을 정의하고 쿼드 포인트를 할당한 다음 다음을 통해 캐럿 주석에 연결합니다. `in_reply_to` 과 `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### 주석을 모두 추가하고 PDF를 저장합니다.

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### 전체 예제

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### 대체 주석 가져오기

대체 주석을 식별하려면 다른 주석에 대한 회신으로 그룹화된 취소선 주석을 찾으십시오.샘플은 관계 필드를 확인하기 전에 각 취소선 주석을 캐스팅합니다.

#### 문서를 로드하고 주석을 반복합니다.

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### 그룹화된 스트라이크아웃 주석 필터링

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### 전체 예제

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### 교체 주석 삭제

이 워크플로우는 마크업 교체에 사용되는 취소선 주석을 수집하여 페이지에서 제거하고 출력 PDF를 저장합니다.

#### 문서 로드 및 주석 수집, 교체

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### 주석을 삭제하고 문서를 저장합니다.

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### 전체 예제

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
