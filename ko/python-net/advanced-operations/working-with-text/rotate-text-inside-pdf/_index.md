---
title: Python을 사용하여 PDF 내부 텍스트 회전
linktitle: PDF 내부 텍스트 회전
type: docs
weight: 50
url: /ko/python-net/rotate-text-inside-pdf/
description: Python에서 Aspose.PDF for Python을 사용하여 PDF 문서 내부 텍스트를 회전시켜 유연한 문서 형식을 만드는 방법을 살펴보세요.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 텍스트 회전하는 방법
Abstract: 이 기사는 Aspose.PDF 라이브러리 for Python via .NET을 사용하여 PDF 문서 내부 텍스트를 회전시키는 방법에 대한 상세 가이드를 제공합니다. 다양한 각도의 텍스트 회전을 달성하기 위해 `TextFragment` 클래스의 `Rotation` 속성을 활용하는 방법을 설명하며, 이는 여러 문서 생성 시나리오에 유용합니다. 지정된 회전 각도로 텍스트 프래그먼트를 생성하고 `TextBuilder`를 사용하여 PDF 페이지에 추가하는 방법을 시연합니다. 회전된 텍스트 프래그먼트를 `TextParagraph`에 첨부한 후 해당 단락을 PDF 페이지에 추가하는 방법을 보여줍니다. 페이지의 단락 컬렉션에 회전된 텍스트 프래그먼트를 직접 추가하는 방법을 제시합니다. 여러 텍스트 프래그먼트를 포함하는 전체 단락을 회전시키는 방법을 설명합니다.
---

Aspose.PDF for Python via .NET을 사용하여 PDF 문서에서 텍스트 프래그먼트를 회전시킵니다. 'TextFragment', 'TextState', 'TextBuilder' 클래스를 결합하여 개별 텍스트 요소의 위치와 회전을 정밀하게 제어하는 방법을 보여줍니다. 각 텍스트 프래그먼트의 회전 각도를 조정함으로써 대각선 헤더, 수직 레이블 또는 회전된 주석과 같은 시각적으로 동적인 레이아웃을 만들 수 있습니다.

## PDF에서 TextBuilder를 사용하여 텍스트 프래그먼트 회전

rotated_fragments.pdf라는 PDF 파일을 생성하며, 가로로 정렬된 세 개의 텍스트 프래그먼트를 포함합니다:

- 첫 번째 텍스트는 회전되지 않음
- 두 번째는 45° 회전
- 세 번째는 90° 회전

1. 새 PDF 문서를 생성합니다.
1. 회전된 텍스트를 포함할 새 페이지를 삽입합니다.
1. 첫 번째 텍스트 프래그먼트 생성 - 회전 없음.
1. 두 번째 텍스트 프래그먼트 생성 - 45° 회전.
1. 세 번째 텍스트 프래그먼트 생성 - 90° 회전.
1. TextBuilder를 사용하여 텍스트 프래그먼트를 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF에서 단락 내부 개별 텍스트 프래그먼트 회전

단락 내에서 개별 텍스트 프래그먼트를 회전시킵니다. 각기 다른 회전 각도를 가진 여러 프래그먼트 (TextFragment)를 포함하는 다중 행 단락 (TextParagraph)을 만드는 방법을 보여줍니다. 이 기술은 가로 및 대각선 방향의 텍스트를 결합한 시각적으로 풍부한 문서를 만드는 데 유용합니다 — 예를 들어 스타일이 적용된 헤더, 다이어그램 또는 주석이 달린 레이블 등.

rotated_paragraph_fragments.pdf라는 PDF를 생성하며, 각기 다른 각도로 회전된 세 줄의 텍스트가 포함된 단락을 포함합니다:

- 첫 번째 줄은 45° 회전
- 두 번째 줄은 가로(0°) 유지
- 세 번째 줄은 -45° 회전

1. 새 PDF 문서를 생성합니다.
1. 회전된 텍스트가 표시될 빈 페이지를 추가합니다.
1. TextParagraph를 생성합니다.
1. 첫 번째 텍스트 프래그먼트를 생성하고 구성합니다 - 45° 회전.
1. 두 번째 텍스트 프래그먼트를 생성합니다 - 회전 없음.
1. 세 번째 텍스트 프래그먼트를 생성합니다 - 45° 회전.
1. 텍스트 프래그먼트를 단락에 추가합니다.
1. TextBuilder를 사용하여 페이지에 단락을 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## PDF에서 페이지 단락을 사용하여 텍스트 회전

Aspose.PDF for Python via .NET을 사용하여 PDF 내 텍스트를 회전시키는 간소화된 방법.
TextBuilder나 TextParagraph와 같은 하위 수준 접근 방식과 달리, 이 방법은 회전된 텍스트 프래그먼트를 페이지의 단락 컬렉션(page.paragraphs)에 직접 추가합니다. 기본적인 텍스트 회전만 필요하고 정밀한 위치 지정이나 단락 구조가 필요 없는 경우에 이상적입니다. 이 접근 방식은 레이아웃 생성을 간소화하고 페이지에 텍스트 배치를 자동으로 처리하면서도 개별 텍스트 회전 제어를 가능하게 합니다.

'simple_rotated_text.pdf'라는 파일을 생성하며, 내용은 다음과 같습니다:

- 메인 가로 텍스트 프래그먼트 0° 회전
- 315° 회전 프래그먼트
- 270° 회전 프래그먼트

1. 새 PDF 문서를 초기화합니다.
1. 회전된 텍스트가 배치될 페이지를 생성합니다.
1. 첫 번째 텍스트 조각 만들기 - 회전 없음.
1. 두 번째 텍스트 조각 만들기 - 315° 회전.
1. 세 번째 텍스트 조각 만들기 - 270° 회전.
1. 텍스트 조각을 페이지 단락에 직접 추가하기.
1. PDF 문서 저장하기.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF에서 전체 단락 회전하기

우리 라이브러리는 PDF에서 고급 단락 수준 텍스트 회전을 보여줍니다. 조각 수준 회전(각 텍스트 조각을 개별적으로 회전하는)과 달리, 이 방법은 전체 단락을 다양한 각도에서 통합된 블록으로 회전시킵니다.
각 단락은 여러 스타일링된 텍스트 조각을 포함하며, 전체 단락이 특정 각도로 회전합니다 — 복잡하고 일관된 레이아웃 변환을 가능하게 합니다.
전체 텍스트 섹션을 다양한 방향으로 배치해야 하는 예술적인 레이아웃, 워터마크, 디자인 중심 PDF에 이상적입니다.

'rotated_paragraphs.pdf'를 생성합니다. 여기에는 네 개의 완전히 스타일링되고 회전된 단락이 포함됩니다:

- 각각 고유한 각도(45°, 135°, 225°, 315°)로 회전
- 각 단락은 색상 배경, 밑줄, 일관된 스타일링이 적용된 세 줄의 텍스트를 포함

1. 새 PDF 문서 만들기.
1. 회전된 단락을 담을 빈 페이지 추가하기.
1. 여러 단락을 만들기 위해 반복하기.
1. 단락을 만들고 위치 지정하기.
1. 서식이 포함된 텍스트 조각 만들기.
1. 텍스트 서식 적용하기.
1. 텍스트 조각을 단락에 추가하기.
1. TextBuilder를 사용해 단락을 페이지에 추가하기.
1. 네 가지 회전 모두에 대해 반복하기.
1. PDF 문서 저장하기.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
