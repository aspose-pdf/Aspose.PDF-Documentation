---
title: 파이썬에서 PDF 레이아웃에 플로팅 박스 사용하기
linktitle: 플로팅 박스 사용
type: docs
weight: 30
url: /ko/python-net/floating-box/
description: Python으로 PDF 문서에서 FloatingBox를 사용하여 텍스트 레이아웃, 여러 열 콘텐츠 및 정확한 위치 지정을 수행하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 스타일이 지정된 플로팅박스 컨테이너를 만들고 배치합니다.
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일에서 FloatingBox를 사용하는 방법을 설명합니다.스타일이 지정된 플로팅 컨테이너에 텍스트 및 기타 콘텐츠를 배치하고, 레이아웃, 테두리, 정렬 및 클리핑을 제어하고, Python으로 보다 구조화된 PDF 페이지 디자인을 만드는 방법을 알아보세요.
---

## 기본 플로팅 박스 사용법

더 [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 클래스는 PDF 페이지에 텍스트 및 기타 내용을 배치하기 위한 컨테이너입니다.일반 텍스트 단락보다 레이아웃, 테두리 및 스타일을 더 강력하게 제어할 수 있습니다.내용이 상자 크기를 초과할 경우 상자 설정에 따라 클리핑 동작이 제어됩니다.

.NET을 통한 Python용 Aspose.PDF 기능을 사용하여 구조화된 텍스트 컨테이너, 다중 열 레이아웃 및 PDF 문서의 정확한 위치 지정이 필요한 경우 이 페이지를 사용하십시오.

1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 추가 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 문서에.
1. 만들기 [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. 를 사용하여 상자 테두리 설정 [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) 과 [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. 를 사용한 컨트롤 박스 반복 [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 재산.
1. 를 사용하여 텍스트 콘텐츠 추가 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. 추가 `FloatingBox` 에 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 를 사용하여 최종 PDF 문서 저장 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```

위의 예에서는 `FloatingBox` 너비 400피트, 높이 30피트로 생성됩니다.
텍스트가 의도적으로 사용 가능한 높이를 초과하여 텍스트의 일부가 잘립니다.

![이미지 1](image01.png)

더 [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 가치가 다음과 같은 재산 `False` 텍스트 렌더링을 단일 페이지로 제한합니다.

이 속성을 다음과 같이 설정하는 경우 `True`텍스트가 같은 위치에 있는 다음 페이지로 리플로우됩니다.

![이미지 2](image02.png)

## 고급 플로팅 박스 기능

### 다중 컬럼 지원

#### 다중 열 레이아웃 (간단한 경우)

`FloatingBox` 다중 열 레이아웃을 지원합니다.이러한 레이아웃을 생성하려면 의 값을 정의해야 합니다. [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) 속성.

* `column_widths` 각 열 너비를 포인트 단위로 정의하는 문자열입니다.
* `column_spacing` 열 사이의 간격 너비를 정의하는 문자열입니다.
* `column_count` 는 열 개수입니다.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

이 예제에서는 샘플 단락을 생성하여 세 열에 배치합니다.콘텐츠는 모든 단락이 렌더링될 때까지 추가 페이지에 계속 표시됩니다.

#### 강제 열 시작 기능이 있는 다중 열 레이아웃

이 예제에서는 동일한 다중 열 설정을 사용하지만 추가된 각 단락이 새 열에서 시작되도록 합니다.이렇게 하려면 다음을 설정하십시오. `is_first_paragraph_in_column = True` 각각에 `TextFragment` 추가하기 전에 `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### 백그라운드 지원

에 배경색 적용 `FloatingBox` .NET을 통해 파이썬용 Aspose.PDF 를 사용하는 PDF 문서에서
a를 할당하여 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 에 `background_color`머리글, 콜아웃 또는 스타일이 지정된 섹션의 내용을 강조 표시할 수 있습니다.

이 코드 스니펫은 샘플 콘텐츠가 포함된 간단한 연한 녹색 텍스트 상자를 만드는 방법을 보여줍니다.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### 포지셔닝 지원

a의 위치 `FloatingBox` 이 페이지는 다음에 의해 제어됩니다. `positioning_mode`, `left`, 및 `top`.
언제 `positioning_mode` 는 다음과 같습니다.

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (기본값)

위치는 이전에 추가한 요소에 따라 달라집니다.새 단락을 추가하면 후속 요소의 흐름에 영향을 줍니다.만약 [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 또는 [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 0이 아닌 값도 적용됩니다.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

위치는 다음과 같이 고정됩니다. `left` 과 `top`; 이전 요소에 의존하지 않으며 이후 요소의 흐름에 영향을 주지 않습니다.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### PDF에서 플로팅 박스를 세로 및 가로 정렬로 정렬

정렬 `FloatingBox` PDF 페이지의 요소 사용 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) 과 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) .NET을 통해 파이썬용 Aspose.PDF 에서이렇게 하면 페이지 레이아웃, 머리글/바닥글 블록 또는 사이드 노트의 상단, 중앙 또는 하단에 플로팅 컨테이너를 배치할 수 있습니다.

1. 새 PDF 문서 만들기
1. 문서에 페이지를 추가합니다.
1. 첫 번째 추가 `FloatingBox` 오른쪽 하단 정렬 포함.
1. 두 번째 추가 `FloatingBox` 중앙 오른쪽 정렬 포함.
1. 세 번째 추가 `FloatingBox` 오른쪽 상단 정렬 포함.
1. 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```

## 관련 텍스트 주제

* [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
* [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
* [파이썬에서 PDF 텍스트 포맷 지정하기](/pdf/ko/python-net/text-formatting-inside-pdf/)
* [Python에서 PDF 텍스트에 툴팁 추가](/pdf/ko/python-net/pdf-tooltip/)
