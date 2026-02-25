---
title: Python을 사용한 텍스트 생성을 위한 FloatingBox 사용
linktitle: FloatingBox 사용
type: docs
weight: 30
url: /ko/python-net/floating-box/
description: 이 페이지는 떠다니는 상자 안의 텍스트를 포맷하는 방법을 설명합니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 텍스트 생성용 FloatingBox 도구
Abstract: 이 문서는 Python용 Aspose.PDF의 FloatingBox 도구 사용에 대한 포괄적인 가이드를 제공하며, 이를 통해 개발자는 PDF 페이지에서 이동 가능한 스타일이 적용된 컨테이너에 텍스트 및 기타 콘텐츠를 배치할 수 있습니다. 기본 및 고급 사용법을 모두 다루며, FloatingBox 생성, 테두리 및 배경색 적용, 다중 열 레이아웃 제어, 단락 위치 관리, 상자를 수직 및 수평으로 정렬하는 방법을 보여줍니다. 또한 텍스트 클리핑, 페이지 간 반복 콘텐츠, 절대 위치 지정, 향상된 레이아웃 제어와 같은 주요 기능을 강조하여 PDF 콘텐츠를 정밀하게 맞춤 설정할 수 있게 합니다. 실용적인 코드 예제를 통해 독자는 FloatingBox 컨테이너의 전체 기능을 활용하여 시각적으로 매력적이고 구조가 잘 잡힌 PDF를 만드는 방법을 배웁니다.
---

## FloatingBox 도구 사용 기본

The [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 도구는 PDF 페이지에 텍스트 및 기타 콘텐츠를 배치하기 위한 특수 컨테이너입니다. 주요 기능은 내용이 상자 경계를 초과할 때 텍스트가 잘려 나가는 것입니다. Aspose.PDF for Python을 사용하여 `FloatingBox`를 [`문서`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)에 생성하고 추가합니다. `FloatingBox`는 이동 가능한 텍스트 컨테이너 역할을 하며, 일반 텍스트 단락에 비해 레이아웃 위치 지정, 테두리 및 스타일링을 보다 세밀하게 제어할 수 있습니다.

1. 새 [`문서`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 생성합니다.
1. 문서에 [`페이지`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가합니다.
1. [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/)를 생성합니다.
1. [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/)와 [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/)를 사용하여 상자 테두리를 설정합니다.
1. [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 속성을 사용하여 상자 반복을 제어합니다.
1. [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)를 사용하여 텍스트 내용을 추가합니다.
1. `FloatingBox`를 [`페이지`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 추가합니다.
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)를 사용하여 최종 PDF 문서를 저장합니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

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

위 예시에서는 너비 400 pt, 높이 30 pt인 FloatingBox를 생성하고 있습니다.
또한 이 예시에서는 주어진 크기에 맞지 않을 정도로 의도적으로 더 많은 텍스트를 생성했습니다.
그 결과 텍스트가 잘려 나갔습니다.

![Image 1](image01.png)

속성 [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 의 `False` 값은 텍스트를 한 페이지로 제한합니다.

이 속성을 `True` 로 설정하면 텍스트가 같은 위치에서 다음 페이지로 흐르게 됩니다.

![Image 2](image02.png)

## FloatingBox의 고급 기능

### 다중 열 지원

#### 다중 열 레이아웃 (간단한 경우)

`FloatingBox`는 다중 열 레이아웃을 지원합니다. 이러한 레이아웃을 만들려면 [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) 속성값을 정의해야 합니다.

* `column_widths`는 pt 단위의 너비를 열거한 문자열입니다.
* `column_spacing`는 열 사이 간격의 너비를 나타내는 문자열입니다.
* `column_count`는 열의 개수입니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
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

위 예시에서 추가 라이브러리 LoremNET을 사용하여 20개의 단락을 만들었습니다. 이 단락들은 세 개의 열로 나뉘어 텍스트가 다 떨어질 때까지 다음 페이지들을 채웠습니다.

#### 강제 열 시작이 있는 다중 열 레이아웃

이전 예시와 동일하게 다음 예시를 수행합니다. 차이점은 3개의 단락을 만들었다는 것입니다. `FloatingBox`가 각 단락을 새로운 열에 표시하도록 강제할 수 있습니다. 이를 위해 텍스트를 `FloatingBox` 객체에 추가할 때 `is_first_paragraph_in_column`을 설정해야 합니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

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

### 배경 지원

Aspose.PDF for Python via .NET를 사용하여 PDF 문서의 FloatingBox에 배경색을 적용합니다.
`FloatingBox`는 텍스트 또는 기타 요소를 담는 컨테이너이며, [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/)를 배경색으로 지정하면 콘텐츠가 시각적으로 돋보이게 할 수 있습니다 — 헤더, 강조 표시, 스타일 섹션 등에 유용합니다.

이 코드 조각은 샘플 콘텐츠로 간단한 연녹색 텍스트 상자를 만드는 방법을 보여줍니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

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

### 위치 지정 지원

생성된 페이지에서 FloatingBox의 위치는 `positioning_mode`, `left`, `top` 속성에 따라 결정됩니다.
`positioning_mode` 값이

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (기본값)

위치는 이전에 배치된 요소에 의해 결정되며, 요소를 추가하면 이후 요소의 위치에 영향을 줍니다. [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 또는 [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 값이 0이 아니면 그 값도 고려하지만, 전체 로직은 직관적이지 않을 수 있습니다.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

위치는 `Left`와 `Top` 값으로 지정됩니다; 이전 요소에 의존하지 않으며 이후 요소의 위치에도 영향을 주지 않습니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

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

### PDF에서 수직 및 수평 정렬로 플로팅 박스 맞추기

`FloatingBox` 요소를 PDF 페이지 내에서 서로 다른 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) 및 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 옵션을 사용하여 Aspose.PDF for Python via .NET에서 정렬합니다. 레이아웃 위치(위, 가운데, 아래, 왼쪽, 오른쪽)를 제어하는 방법을 보여주어 플로팅 컨테이너의 정확한 시각적 정렬을 달성합니다. 각 플로팅 박스는 페이지 레이아웃, 헤더/푸터 배치 또는 측면 주석을 위한 정렬 유연성을 보여주기 위해 서로 다른 위치에 할당됩니다.

1. 새 PDF 문서를 생성합니다.
1. 문서에 페이지를 추가합니다.
1. 첫 번째 FloatingBox를 생성합니다 (오른쪽 아래 정렬).
1. 두 번째 FloatingBox를 생성합니다 (오른쪽 중앙 정렬).
1. 세 번째 FloatingBox를 생성합니다 (오른쪽 위 정렬).
1. 문서를 저장합니다.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
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
