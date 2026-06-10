---
title: Python을 사용한 대화형 주석
linktitle: 인터랙티브 어노테이션
type: docs
weight: 60
url: /ko/python-net/interactive-annotations/
description: 링크 주석을 추가, 읽기 및 삭제하는 방법과 .NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 탐색 및 인쇄 버튼을 만드는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 대화형 PDF 주석과 버튼으로 작업하세요.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 파일에서 대화형 주석을 사용하는 방법을 설명합니다.링크 주석 추가, 기존 링크 영역 읽기, 링크 주석 삭제, 페이지 탐색 버튼 만들기, PDF 문서에 인쇄 버튼 추가에 대해 설명합니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 대화형 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 몇 가지 일반적인 워크플로를 보여줍니다.

- 기존 텍스트에 링크 주석 추가
- 페이지에서 링크 주석 사각형 가져오기
- 링크 주석 삭제
- 네비게이션 버튼 생성
- 인쇄 버튼 만들기

## 링크 주석

### 링크 주석 추가

이 예제에서는 첫 페이지에서 텍스트 부분을 검색합니다. `"file"` 일치하는 텍스트 영역 위에 클릭 가능한 링크 주석을 배치합니다.사용자가 주석을 클릭하면 PDF에서 지정된 웹 주소를 엽니다.

#### 문서 불러오기 및 대상 텍스트 찾기

만들기 `Document` 목적 및 사용 `TextFragmentAbsorber` 대화식으로 전환될 텍스트를 검색합니다.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### 링크 주석 만들기

빌드하기 `LinkAnnotation` 일치하는 텍스트 조각의 사각형을 사용하고 여기에 URI 작업을 할당합니다.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### 주석을 추가하고 PDF를 저장합니다.

페이지에 주석을 추가하고 업데이트된 파일을 저장합니다.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### 전체 예제

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### 링크 주석 가져오기

기존 대화형 링크를 검사하려면 첫 페이지에서 주석 컬렉션을 필터링하고 유형이 다음과 같은 항목만 유지합니다. `LINK`.그런 다음 샘플은 일치하는 각 주석의 사각형을 인쇄합니다.

#### PDF 로드 및 링크 주석 수집

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 주석 사각형 읽기

필터링된 주석을 반복하여 각 링크 영역의 좌표를 인쇄합니다.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### 전체 예제

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### 링크 주석 삭제

이 워크플로우는 첫 페이지에서 모든 링크 주석을 제거하고 정리된 PDF를 새 파일로 저장합니다.

#### 제거할 링크 주석 찾기

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 각 링크 주석 삭제

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### 업데이트된 문서 저장

```python
document.save(outfile)
```

#### 전체 예제

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## 위젯 어노테이션

### 네비게이션 버튼 추가

탐색 단추는 여러 페이지로 구성된 PDF에서 독자가 뷰어 인터페이스를 사용하지 않고 페이지 사이를 이동할 수 있도록 하려는 경우에 유용합니다.이 샘플은 다음을 추가합니다. `Previous Page` 과 `Next Page` 각 페이지에 버튼을 누릅니다.

#### 버튼 설정 정의

버튼 캡션, 위치 및 사전 정의된 동작을 간단한 구성 목록에 저장합니다.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### PDF를 로드하고 여러 페이지가 존재하는지 확인합니다.

샘플은 소스 문서를 열고 한 페이지를 더 추가하므로 탐색 작업에 사용할 페이지가 두 개 이상 있습니다.

```python
document = ap.Document(infile)
document.pages.add()
```

#### 각 페이지에 버튼 만들기

모든 페이지에 대해 만들기 `ButtonField`텍스트와 색상을 설정하고 사전 정의된 탐색 동작을 지정한 다음 양식에 추가합니다.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### 결과 저장

```python
document.save(outfile)
```

#### 전체 예제

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### 인쇄 버튼 추가

이 예제에서는 한 페이지짜리 PDF를 새로 만들고 페이지 상단에 인쇄 버튼을 배치합니다.버튼을 클릭하면 호환되는 PDF 뷰어에서 사전 정의된 인쇄 작업이 트리거됩니다.

#### 새 PDF 작성 및 페이지 추가

```python
document = ap.Document()
page = document.pages.add()
```

#### 버튼 생성 및 구성

버튼 사각형을 정의하고 생성하십시오. `ButtonField`캡션을 설정하고 인쇄 작업을 첨부합니다.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### 테두리 및 배경 스타일 설정

샘플은 단색 테두리를 정의하고 사용자 지정 색상을 적용하여 문서에 버튼이 표시되도록 합니다.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### 버튼을 추가하고 PDF를 저장합니다.

```python
document.form.add(print_button)
document.save(outfile)
```

#### 전체 예제

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
