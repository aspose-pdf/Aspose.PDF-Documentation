---
title: 파이썬을 사용한 보안 주석
linktitle: 보안 주석
type: docs
weight: 75
url: /ko/python-net/security-annotations/
description: .NET을 통해 Aspose.PDF for Python을 사용하여 교정할 텍스트를 표시하고, 수정 주석을 적용하고, PDF 파일의 이미지 영역을 수정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 보안 주석을 사용하여 Python에서 민감한 PDF 콘텐츠를 수정합니다.
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 보안 주석을 다루는 방법을 설명합니다.수정 주석으로 일치하는 텍스트를 표시하고, 교정을 영구적으로 적용하고, 감지된 이미지 배치 사각형을 기반으로 선택한 이미지 영역을 수정하는 방법을 다룹니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 보안 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 세 가지 일반적인 편집 워크플로를 보여줍니다.

- 텍스트 부분에 수정 주석으로 표시
- 기존 수정 주석을 영구적으로 적용
- 페이지에서 감지된 이미지 영역 수정

## 마크 텍스트 수정

이 워크플로는 문서에서 일치하는 텍스트를 검색하고 일치하는 각 텍스트에 수정 주석을 배치합니다.내용은 아직 제거되지 않고 나중에 교정할 수 있도록 텍스트만 표시합니다.

### PDF를 열고 대상 텍스트를 검색합니다.

만들기 `TextFragmentAbsorber` 검색어를 입력하고 모든 페이지를 스캔하기 전에 일반 텍스트 검색 옵션을 활성화합니다.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### 각 일치에 대한 편집 주석 만들기

일치하는 모든 텍스트 단편에 대해 다음을 생성하십시오. `RedactionAnnotation` 프래그먼트 사각형을 사용하여 시각적 모양을 구성합니다.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### 표시된 PDF 저장

```python
document.save(outfile)
```

### 전체 예제

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## 교정 적용

수정 주석이 추가된 후 이 워크플로는 첫 페이지에 수정 주석을 영구적으로 적용합니다.적용하고 나면 문서 출력에서 원본 콘텐츠가 제거됩니다.

### PDF 로드 및 편집 주석 수집

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### 각 편집 주석 적용

샘플은 각 주석을 다음과 같이 처리할 수 있는지 확인합니다. `RedactionAnnotation` 전화하기 전에 `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### 편집한 PDF 저장

```python
document.save(outfile)
```

### 전체 예제

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## 편집 영역

이 예제에서는 텍스트 대신 감지된 이미지 영역을 교정합니다.페이지에서 이미지 배치를 검색하고 배치 사각형 하나를 선택한 다음 해당 영역에 수정 주석을 추가합니다.

### PDF를 열고 이미지 배치를 감지합니다.

용도 `ImagePlacementAbsorber` 첫 페이지에서 이미지 위치를 찾을 수 있습니다.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### 선택한 이미지 영역에 대한 편집 주석 만들기

샘플은 세 번째로 감지된 이미지 배치를 사용하며 텍스트 표시 예제에서 사용된 것과 동일한 편집 스타일을 적용합니다.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### 주석을 추가하고 PDF를 저장합니다.

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### 전체 예제

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
