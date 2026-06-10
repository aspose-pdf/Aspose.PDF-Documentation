---
title: 파이썬을 사용한 워터마크 주석
linktitle: 워터마크 주석
type: docs
weight: 70
url: /ko/python-net/watermark-annotations/
description: .NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 워터마크 주석을 추가, 검사 및 삭제하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 워터마크 주석 작업을 할 수 있습니다.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 워터마크 주석을 만들고, 읽고, 제거하는 방법을 설명합니다.사용자 지정 텍스트 상태 및 불투명도를 사용하여 텍스트 워터마크 주석 추가, 기존 워터마크 주석 검사, PDF 페이지에서 워터마크 주석 삭제에 대해 설명합니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 워터마크 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 세 가지 일반적인 워크플로를 보여줍니다.

- 워터마크 주석 추가
- 워터마크 주석 사각형 가져오기
- 워터마크 주석 삭제

## 워터마크 주석 추가

이 예제에서는 PDF 문서의 첫 페이지에 워터마크 주석을 추가합니다.워터마크는 텍스트 상태를 사용하여 글꼴 설정을 제어하고 반투명 모양에 사용자 정의 불투명도를 적용합니다.

### PDF를 열고 대상 페이지 가져오기

```python
document = ap.Document(infile)
page = document.pages[1]
```

### 워터마크 주석 만들기

주석 사각형을 정의하고 페이지 주석 컬렉션에 추가합니다.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### 텍스트 모양 구성

만들기 `TextState` 텍스트 색상, 글꼴 크기 및 글꼴 모음을 제어하는 개체입니다.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### 불투명도 및 워터마크 텍스트 설정

샘플은 50% 의 불투명도를 사용하며 워터마크 주석에 세 줄의 텍스트를 씁니다.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### PDF 저장하기

```python
document.save(outfile)
```

### 전체 예제

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## 워터마크 주석 가져오기

기존 워터마크 주석을 검사하려면 첫 페이지 주석을 다음과 같이 필터링합니다. `WATERMARK` 직사각형을 입력하고 인쇄합니다.

### 문서 로드 및 워터마크 주석 수집

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 주석 사각형 인쇄

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### 전체 예제

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## 워터마크 주석 삭제

이 워크플로우는 첫 페이지에서 모든 워터마크 주석을 제거하고 업데이트된 PDF를 저장합니다.

### 제거할 워터마크 주석 찾기

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 주석을 삭제하고 PDF를 저장합니다.

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### 전체 예제

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
