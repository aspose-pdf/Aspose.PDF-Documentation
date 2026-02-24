---
title: PDF 페이지에서 텍스트 검색 및 가져오기
linktitle: 검색 및 텍스트 가져오기
type: docs
weight: 60
url: /ko/python-net/search-and-get-text-from-pdf/
description: Aspose.PDF를 사용하여 Python에서 PDF 문서의 텍스트를 검색하고 추출하는 방법을 배웁니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 페이지에서 텍스트를 검색하고 가져오는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서 내 텍스트 추출 및 조작 기능을 심도 있게 탐구합니다. 여기서는 전체 문서 또는 특정 페이지에서 지정된 구문이나 정규식 패턴을 검색할 수 있는 TextFragmentAbsorber 클래스를 소개합니다. 이 페이지에서는 일치하는 텍스트 조각에서 텍스트 내용 검색, 위치(좌표 및 들여쓰기 값 포함) 확인, 글꼴 이름, 크기, 임베드 상태, 색상과 같은 글꼴 속성 추출 등 다양한 실용 시나리오를 설명합니다. 상세한 코드 예제가 과정을 단계별로 시연하여 개발자가 텍스트 검색 기능을 애플리케이션에 쉽게 통합할 수 있도록 돕습니다.
---

## PDF에서 텍스트 검색

TextAbsorber 클래스를 사용하여 PDF 문서에서 지정된 사각형 영역의 텍스트를 검색하고 추출합니다. 순수 텍스트 포맷 모드를 사용하여 깨끗하고 포맷되지 않은 텍스트를 출력하므로 헤더, 푸터 또는 표 영역과 같은 구조화된 영역에서 콘텐츠를 추출하기에 이상적입니다. TextExtractionOptions와 TextSearchOptions를 사각형 제약 조건과 결합함으로써 이 예제는 문서에서 텍스트가 추출되는 위치와 방식을 세밀하게 제어할 수 있도록 합니다.

1. 'ap.Document'를 사용하여 PDF 파일을 로드합니다.
1. 텍스트 추출 옵션을 설정합니다.
1. 사각형 제약 조건으로 검색 영역을 정의합니다.
1. TextAbsorber를 생성하고 구성합니다.
1. 문서의 모든 페이지를 처리합니다.
1. 추출된 텍스트를 가져와 표시합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 특정 PDF 페이지에서 텍스트 검색

Aspose.PDF의 TextAbsorber를 사용하여 PDF의 특정 페이지와 영역에서 텍스트를 검색하고 추출합니다. 문서의 2페이지를 대상으로 하며, 정의된 사각형 영역 내에 있는 텍스트만 추출합니다.
TextExtractionOptions(포맷 제어)와 TextSearchOptions(영역 제한)를 결합함으로써 정확하고 페이지별 텍스트 추출을 효율적으로 수행할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 텍스트 추출 옵션을 설정합니다.
1. 페이지의 특정 사각형 영역으로 텍스트 추출을 제한합니다.
1. TextAbsorber를 생성하고 구성합니다.
1. 특정 페이지를 처리합니다.
1. 추출된 텍스트를 가져와 표시합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## PDF에서 상세 텍스트 조각 속성 분석 및 추출

원시 텍스트를 추출하는 TextAbsorber와 달리, TextFragmentAbsorber는 각 텍스트 조각에 대한 위치, 글꼴 속성, 색상 및 임베드 세부 정보와 같은 상세하고 저수준의 정보를 제공합니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 초기화합니다.
1. 문서의 모든 페이지를 처리합니다.
1. 추출된 텍스트 조각을 반복합니다.
1. 기본 텍스트 정보를 출력합니다.
1. 글꼴 및 서식 세부 정보를 출력합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## 단일 PDF 페이지에서 특정 텍스트 구문 검색

TextFragmentAbsorber를 사용하여 PDF 문서의 페이지 내에서 특정 텍스트 구문을 검색합니다. 전체 문서를 검색하는 것과 달리, 이 방법은 검색을 단일 페이지로 제한하므로 헤더, 푸터 또는 특정 콘텐츠 섹션과 같은 목표 영역에서 텍스트의 존재와 위치를 확인하는 데 더 효율적입니다.

1. PDF 문서를 로드합니다.
1. 검색 구문으로 TextFragmentAbsorber를 초기화합니다.
1. 특정 페이지에 Absorber를 적용합니다.
1. 찾은 조각을 반복합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 누적 결과와 함께 순차적인 페이지별 텍스트 검색

Aspose.PDF의 TextFragmentAbsorber를 사용하여 PDF 문서의 여러 페이지에 걸쳐 텍스트를 점진적으로 검색합니다.
단일 페이지 또는 문서 전체 검색과 달리, 이 방법은 페이지를 순차적으로 처리하고 결과를 점진적으로 수집하며 페이지별 컨텍스트와 함께 텍스트 조각을 분석할 수 있습니다. 이 방식은 대형 문서나 단계적 처리 워크플로에 이상적입니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 초기화하고 검색 구문을 설정합니다.
1. 첫 페이지를 처리합니다. 페이지 1만 검색하며 텍스트, 페이지 번호 및 위치를 출력합니다. 명확성을 위해 페이지별 격리된 결과를 제공합니다.
1. 다음 페이지를 순차적으로 처리합니다. 페이지 2로 이동하고 선택적으로 문서의 나머지 부분을 계속 진행합니다. 'absorber.visit()'는 방문한 모든 페이지의 결과가 누적되도록 보장합니다. 누적된 검색 결과를 출력하며, 텍스트와 위치를 모두 보여줍니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## 사각형 영역 내 특정 구문 검색

PDF에서 특정 구문을 검색하되, 단일 페이지의 특정 사각형 영역으로 검색을 제한합니다.
구문 검색과 공간 제한을 결합하면 전체 페이지나 문서를 스캔하지 않고도 지정된 영역에서 콘텐츠를 정확히 찾을 수 있습니다. 이는 양식, 머리글, 바닥글 또는 내용이 예측 가능한 위치에 나타나는 구조화된 보고서에 특히 유용합니다.

1. PDF 문서를 로드합니다.
1. 구문과 사각형 제한을 사용하여 TextFragmentAbsorber를 초기화합니다.
1. 페이지 2에 Absorber를 적용합니다. 처리를 페이지 2로 제한하여 불필요한 연산을 줄이고, 검색이 페이지별로 이루어지도록 보장합니다.
1. 찾은 조각을 순회하며 출력합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 정규 표현식을 사용한 PDF 텍스트 패턴 검색

정규 표현식을 사용하여 PDF에서 텍스트 패턴을 검색합니다. TextFragmentAbsorber에서 regex 모드를 활성화하면 숫자, 날짜, 가격, 좌표 또는 사용자 정의 텍스트 형식과 같은 복잡한 패턴을 찾을 수 있습니다. 이 함수는 검색을 특정 페이지로 제한하여 구조화된 데이터의 목표 추출을 효율적으로 수행합니다.

1. PDF 문서를 로드합니다.
1. 정규식 패턴으로 TextFragmentAbsorber를 초기화합니다.
1. 페이지 2에 Absorber를 적용합니다. 효율성과 정밀성을 위해 검색을 페이지 2로 제한합니다. 이 페이지의 텍스트만 분석됩니다.
1. 찾은 조각을 순회합니다. 일치하는 텍스트 조각과 좌표를 출력합니다. 추출된 패턴에 대한 정확한 위치 정보를 제공합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## TextFragmentAbsorber를 사용하여 PDF에서 텍스트 매치를 하이퍼링크로 변환하기

PDF에서 특정 텍스트 구문을 검색하고 클릭 가능한 하이퍼링크로 변환합니다. 정규식 패턴을 사용한 TextFragmentAbsorber를 활용하여 대상 단어를 찾아 시각적 스타일(색상 및 밑줄)과 인터랙티브 링크를 적용합니다.

1. PDF 문서를 로드합니다.
1. 정규식 패턴으로 TextFragmentAbsorber를 초기화합니다.
1. 페이지 1에 Absorber를 적용합니다.
1. 매치된 부분에 스타일을 적용하고 하이퍼링크를 추가합니다.
1. 수정된 PDF를 저장합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## TextFragmentAbsorber를 사용한 PDF 스타일 텍스트 검색 및 식별

PDF에서 내용이 아니라 서식 속성을 기준으로 텍스트 조각을 검색합니다. TextFragmentAbsorber를 사용하여 볼드 텍스트와 같은 특정 스타일의 텍스트를 식별합니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 초기화합니다.
1. 페이지 1에 Absorber를 적용합니다.
1. 서식을 기반으로 텍스트 조각을 검사합니다. 볼드 서식 여부를 확인합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

텍스트 서식 속성을 분석하여 PDF 문서에서 숨겨진 또는 보이지 않는 텍스트를 감지합니다:

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 초기화합니다.
1. 페이지 1에 Absorber를 적용합니다.
1. 서식을 기반으로 텍스트 조각을 검사합니다. 숨겨진 텍스트는 'fragment.text_state.invisible'를 확인합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## PDF 페이지에서 시각적 텍스트 강조

이 함수는 텍스트 인식과 렌더링을 하나의 워크플로우로 결합합니다. 텍스트를 추출할 뿐만 아니라 각 페이지의 PNG 이미지에 색상 코드가 적용된 사각형으로 조각, 구간 및 문자를 강조 표시하여 시각화합니다.

우리 예제는 다음과 같이 PDF에서 고급 텍스트 시각화를 수행합니다:

- 정규 표현식을 사용하여 모든 보이는 텍스트 조각을 검색합니다
- 각 PDF 페이지를 고해상도 PNG 이미지로 렌더링합니다
- 텍스트 조각, 텍스트 구간 및 개별 문자 주위에 색상 사각형을 그립니다

1. 출력 이미지 해상도를 설정합니다. 각 PDF 페이지는 150 DPI PNG 이미지로 변환됩니다.
1. PDF를 열고 Text Absorber를 초기화합니다.
1. 각 페이지를 처리합니다. 모든 페이지에 absorber를 적용하고 감지된 모든 텍스트 조각 및 그 기하학적 위치를 수집합니다.
1. 페이지를 PNG 스트림으로 변환합니다.
1. 그리기를 위한 Graphics 객체를 준비합니다.
1. 좌표 변환을 적용합니다. PDF 좌표를 이미지 픽셀로 변환합니다.
1. 텍스트 요소에 대한 사각형을 그립니다.
1. 결과를 저장합니다.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
