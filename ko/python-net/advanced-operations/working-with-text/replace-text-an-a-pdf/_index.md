---
title: Python을 사용한 PDF 텍스트 교체
linktitle: PDF 텍스트 교체
type: docs
weight: 40
url: /ko/python-net/replace-text-in-pdf/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 텍스트를 교체하고 제거하는 다양한 방법에 대해 자세히 알아보세요.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 텍스트를 교체하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에서 다양한 텍스트 조작 기술에 대한 포괄적인 가이드를 제공합니다. 전체 페이지에서 텍스트를 교체하거나 특정 페이지 영역 내에서 교체하고 정규식을 사용하는 등 여러 텍스트 교체 전략을 다룹니다. 또한 PDF 내에서 폰트를 교체하고 사용되지 않는 폰트를 제거하는 방법과 텍스트 교체를 관리하여 페이지 내용을 자동으로 재배치하는 방법을 설명합니다. 추가로 PDF 생성 시 교체 가능한 기호를 렌더링하는 방법, 헤더/푸터 영역에서의 활용을 통해 문서 맞춤화를 향상시키는 내용도 포함됩니다. 마지막으로 PDF 문서에서 모든 텍스트를 제거하는 방법을 자세히 다루어 완전한 텍스트 제거가 필요한 시나리오에 대한 작업을 최적화합니다. 각 섹션은 Python 및 기타 지원 언어의 코드 스니펫을 통해 실제 구현을 보여줍니다.
---

이 예제들은 기존 PDF에서 텍스트를 **수정하거나 제거**하는 방법을 보여줍니다.

## 기존 텍스트 교체

### PDF 문서 모든 페이지의 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾아 교체해보고, 온라인에서 결과를 확인하려면 이 [링크](https://products.aspose.app/pdf/redaction) 를 이용하세요.

{{% /alert %}}

텍스트 교체는 기존 PDF 문서의 내용을 업데이트하거나 수정할 때 흔히 요구되는 작업입니다 — 예를 들어 제품 이름을 바꾸거나 오타를 수정하고, 여러 페이지에 걸쳐 용어를 업데이트하는 경우입니다.

Aspose.PDF for Python via .NET은 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 클래스를 통해 프로그래밍 방식으로 텍스트를 검색하고 교체하는 강력하고 효율적인 방법을 제공합니다.

이 예제는 특정 구문(예: "Black cat")의 모든 발생을 찾아서 전체 PDF 문서에서 새로운 구문(예: "White dog")으로 교체하는 방법을 보여줍니다.

1. 검색 및 교체 구문 지정. 찾고자 하는 텍스트와 교체할 텍스트를 설정합니다.
1. PDF 문서를 로드합니다.
1. 텍스트 흡수기 생성. TextFragmentAbsorber를 검색 구문으로 초기화합니다. 이는 문서에서 해당 구문의 모든 인스턴스를 스캔합니다.
1. 모든 페이지에 흡수기를 적용합니다. 이는 모든 페이지를 순회하며 구문에 일치하는 텍스트 조각을 수집합니다.
1. 찾은 각 조각을 교체합니다. "Black cat"의 모든 인스턴스를 "White dog"로 변경합니다.
1. 업데이트된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 특정 페이지 영역의 텍스트 교체

때때로 전체 문서를 검색하는 대신 PDF 페이지의 특정 영역 내에서만 텍스트를 교체해야 할 수도 있습니다 — 예를 들어, 알려진 위치에 있는 헤더, 푸터 또는 테이블 셀을 업데이트하는 경우입니다.

Aspose.PDF for Python via .NET 라이브러리는 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)를 활용하고 영역 기반 텍스트 검색과 결합하여 이 기능을 구현합니다.

이 예제는 특정 페이지의 정의된 사각형 영역 내에서 대상 구문의 모든 발생을 찾아 교체하는 방법을 보여줍니다.

1. 검색 및 교체 구문 지정.
1. PDF 문서를 로드합니다.
1. 검색을 위한 텍스트 흡수기 생성. 원하는 텍스트를 찾기 위해 TextFragmentAbsorber를 초기화합니다.
1. 검색 영역 제한. 사각형은 페이지의 x 및 y 좌표 범위를 지정합니다.
1. 특정 페이지에 흡수기 적용. 이는 지정된 영역 내에서 검색을 수행하고 일치하는 텍스트 조각을 수집합니다.
1. 찾은 텍스트 교체. 정의된 영역 내의 'doc' 모든 발생을 'DOC'로 변경합니다.
1. 업데이트된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 폰트 크기 변경 없이 텍스트 크기 조정 및 이동

PDF에서 텍스트를 교체할 때, 폰트 크기를 변경하지 않고 새로운 텍스트를 특정 영역에 맞추거나 재배치하고 싶을 때가 있습니다.
Aspose.PDF for Python via .NET은 원래 폰트 크기를 유지하면서 텍스트 레이아웃과 간격을 조정할 수 있는 옵션을 제공합니다.

1. PDF 문서를 로드합니다.
1. 'TextFragmentAbsorber'를 사용하여 페이지의 모든 텍스트 조각을 수집합니다.
1. 수정할 조각을 선택합니다.
1. 텍스트 사각형을 이동하고 크기를 조정합니다.
1. 텍스트 간격 조정. 수정된 사각형에 텍스트가 맞도록 간격 조정을 활성화합니다.
1. 조각 텍스트를 교체합니다.
1. 업데이트된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### PDF에서 단락 크기 조정 및 이동

PDF 작업 시 때때로 페이지 레이아웃과 시각적으로 정렬된 상태로 단락을 교체하거나 확장해야 할 때가 있습니다. Aspose.PDF를 사용하면 단락의 경계 사각형 크기를 조정하고 새로운 텍스트에 맞게 간격을 조절할 수 있으며, 폰트 크기를 변경하지 않고도 가능합니다.

1. PDF 문서를 로드합니다.
1. 'TextFragmentAbsorber'를 사용하여 페이지의 모든 텍스트 조각을 수집합니다.
1. 수정할 조각을 선택합니다.
1. 단락의 크기를 조정하고 이동합니다. 페이지의 미디어 박스를 사용하여 경계를 결정하고 사각형을 조정합니다.
1. 간격을 조정합니다. 이는 폰트 크기를 변경하는 대신 단어/문자 사이의 간격을 수정합니다.
1. 조각 텍스트를 교체합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 텍스트 교체 및 자동으로 폰트 확대하여 대상 영역 채우기

PDF에서 텍스트를 교체하면서 자동으로 폰트 크기를 조정하고 확대하여 특정 사각형 영역을 채웁니다. Aspose.PDF for Python via .NET 라이브러리를 사용하면 코드가 동적으로 폰트 크기와 간격을 조절하여 새로운 텍스트 내용이 정의된 경계 상자에 완벽히 맞도록 합니다 — 수동 폰트 계산이 필요 없습니다.

1. PDF를 로드합니다.
1. 텍스트 조각을 캡처합니다.
1. 특정 조각을 선택합니다.
1. 대상 사각형을 정의합니다.
1. 텍스트 조정 옵션을 활성화합니다.
1. 텍스트를 교체합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### 텍스트 교체 및 사각형에 맞추기

PDF 문서에서 텍스트를 교체하면서, 필요시 자동으로 폰트 크기를 줄여 새로운 내용이 원본 텍스트의 사각형 영역에 맞도록 합니다.

Aspose.PDF for Python via .NET 라이브러리를 사용하여 이 기능은 텍스트 레이아웃과 폰트 크기를 동적으로 조정하며, 문서 구조를 유지하면서 넘침을 방지합니다.

1. 첫 페이지에서 모든 텍스트 조각을 추출하기 위해 TextFragmentAbsorber 객체를 생성합니다.
1. 특정 텍스트 조각에 접근합니다.
1. 교체 영역을 설정합니다.
1. 텍스트 조정 옵션을 구성합니다. 두 가지 주요 교체 옵션을 설정합니다:
- 폰트 크기 조정 - 'SHRINK_TO_FIT'은 새로운 텍스트가 너무 길 경우 자동으로 폰트 크기를 줄입니다.
- 간격 조정 - 'ADJUST_SPACE_WIDTH'는 간격을 비례적으로 유지합니다.
1. 텍스트를 교체합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 자리 표시자 텍스트를 자동으로 교체하고 PDF 레이아웃 재배치

PDF(예: 템플릿이나 양식) 내부의 자리 표시자 텍스트를 이름이나 회사 정보와 같은 실제 데이터로 교체합니다.
새 텍스트에 맞게 페이지 레이아웃을 자동으로 조정하고 사용자 지정 서식(폰트, 색상, 크기)을 적용합니다.

1. PDF를 가져와 로드합니다.
1. 자리 표시자를 위한 Text Absorber를 생성합니다.
1. 모든 페이지에 Absorber를 적용합니다.
1. 찾아낸 텍스트 조각들을 순회합니다.
1. 사용자 지정 텍스트 서식을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### 정규 표현식을 기반으로 텍스트 교체

PDF 문서를 작업할 때 특정 구문이 아니라 패턴에 따라 텍스트를 교체해야 할 수 있습니다 — 예를 들어 전화번호, 코드, 날짜 형식 등.

Aspose.PDF for Python via .NET을 사용하면 TextFragmentAbsorber 클래스를 통해 정규 표현식(레귤러 익스프레션)을 사용하여 이러한 교체를 수행할 수 있습니다.

이 예제는 텍스트 패턴(예: ####-#### 형식, 1234-5678과 같은)을 찾고 이를 형식화된 문자열 'ABC1-2XZY'로 교체하는 방법을 보여줍니다. 또한 교체된 텍스트의 폰트, 색상 및 크기를 사용자 지정하는 방법도 설명합니다.

다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

1. PDF 문서를 로드합니다.
1. 정규식 기반 텍스트 Absorber를 생성합니다. 정규식 패턴으로 TextFragmentAbsorber를 초기화합니다.
1. 정규식 모드를 활성화합니다. 'True' 매개변수가 정규식 검색 모드를 활성화합니다.
1. 페이지에 Absorber를 적용합니다. 이는 정의된 정규식 패턴에 일치하는 모든 텍스트 조각을 페이지에서 스캔합니다.
1. 각 일치를 새로운 텍스트로 교체하고 사용자 지정 스타일을 적용합니다.
1. 수정된 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## 폰트 교체 또는 사용되지 않은 폰트 제거

### 기존 PDF 파일의 글꼴 교체

때때로 PDF 전체에서 글꼴을 표준화하거나 업데이트해야 할 때가 있습니다 — 예를 들어, 오래되었거나 독점적인 글꼴을 보다 접근하기 쉬운 글꼴로 교체하는 경우입니다. .NET을 통해 Python용 Aspose.PDF 라이브러리를 사용하면 글꼴을 프로그래matically 감지하고 교체할 수 있어 일관된 타이포그래피와 문서 호환성을 보장합니다.

이 예제는 PDF 문서 전체에서 특정 글꼴(예: 'Arial-BoldMT')의 모든 인스턴스를 다른 글꼴(예: 'Verdana')로 교체하는 방법을 보여줍니다.

다음 코드 스니펫은 PDF 문서 내부의 글꼴을 교체하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. TextFragmentAbsorber를 초기화합니다.
1. Absorber를 사용하여 문서의 모든 페이지에서 텍스트 조각을 추출합니다.
1. 글꼴을 식별하고 교체합니다. 스크립트는 조각의 현재 글꼴이 'Arial-BoldMT'인지 확인합니다. true인 경우 FontRepository.find_font() 메서드를 사용하여 'Verdana' 글꼴로 교체합니다.
1. 수정된 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 사용되지 않는 글꼴 제거

시간이 지나면서 PDF 문서는 파일 크기를 늘리고 처리 속도를 늦추는 사용되지 않거나 포함된 글꼴이 누적될 수 있습니다. 이러한 사용되지 않는 글꼴은 텍스트 편집이나 교체 후에도 남아 있는 경우가 많으며, 특히 큰 규모이거나 복잡한 PDF를 다룰 때 더욱 그렇습니다.

.NET을 통해 Python용 Aspose.PDF 라이브러리는 TextEditOptions 클래스를 사용하여 이러한 중복 글꼴을 제거하는 효율적인 방법을 제공합니다. 이는 문서를 최적화할 뿐만 아니라 눈에 보이는 텍스트에 실제 적용된 글꼴만 사용하도록 보장합니다.

'remove_unused_fonts()' 메서드는 중복된 글꼴 데이터를 제거하여 PDF 파일을 최적화하는 간단하지만 강력한 방법입니다.

이 예제는 다음을 수행하는 방법을 보여줍니다:

- PDF에서 사용되지 않은 글꼴을 스캔합니다.
- 안전하게 제거합니다.
- 활성 텍스트 조각에 일관된 글꼴(예: Times New Roman)을 재할당합니다.

1. PDF 문서를 엽니다.
1. 텍스트 편집 옵션을 구성합니다. 이는 엔진에게 현재 눈에 보이는 텍스트에서 사용되지 않은 포함된 글꼴을 제거하도록 지시합니다.
1. 옵션과 함께 텍스트 Absorber를 생성합니다. TextFragmentAbsorber는 문서에서 텍스트 조각을 추출하여 편집합니다.
1. 표준 글꼴을 재할당합니다. Absorber가 모든 조각을 수집한 후, 이를 순회하며 일관된 글꼴을 적용합니다.
1. 정리된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## 모든 텍스트 제거

### PDF에서 텍스트 제거

이미지, 도형 및 레이아웃 구조를 유지하면서 PDF 파일의 모든 텍스트 내용을 제거합니다.
TextFragmentAbsorber를 사용하여 코드는 전체 문서를 효율적으로 스캔하고 각 페이지에서 발견된 모든 텍스트 조각을 삭제합니다.

1. PDF 문서를 로드합니다.
1. PDF의 텍스트 조각을 감지하고 처리하기 위해 TextFragmentAbsorber 객체를 생성합니다.
1. 모든 텍스트 내용을 제거합니다. 'absorber.remove_all_text()' 메서드는 로드된 문서에서 모든 텍스트 요소를 제거하고 비텍스트 구성 요소는 그대로 둡니다.
1. 업데이트된 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 특정 페이지에서 모든 텍스트 제거

Aspose.PDF의 TextFragmentAbsorber 클래스를 사용하여 PDF 문서의 한 페이지에서 모든 텍스트를 제거합니다.
전체 문서 제거와 달리 이 메서드는 페이지 수준 텍스트 정리를 수행하여 선택한 페이지의 텍스트만 삭제하고 다른 모든 페이지는 그대로 둡니다.

1. PDF 파일을 로드합니다.
1. TextFragmentAbsorber 인스턴스를 생성합니다.
1. 첫 번째 페이지에서 모든 텍스트를 제거합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### PDF 페이지의 특정 영역에서 모든 텍스트 제거

Aspose.PDF의 TextFragmentAbsorber를 사용하여 페이지의 특정 사각형 영역에서 모든 텍스트를 제거합니다.
전체 페이지를 지우는 대신, 이 메서드는 대상 텍스트 제거를 수행하여 페이지의 어느 부분이 영향을 받는지 정확히 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 생성합니다.
1. 대상 영역(사각형)을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지를 보존합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### PDF 문서에서 모든 숨겨진 텍스트 제거

Aspose.PDF의 TextFragmentAbsorber를 사용하여 페이지의 특정 사각형 영역에서 모든 텍스트를 제거합니다.
전체 페이지를 지우는 대신, 이 메서드는 대상 텍스트 제거를 수행하여 페이지의 어느 부분이 영향을 받는지 정확히 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 생성합니다.
1. 대상 영역(사각형)을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지 부분을 보존합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
