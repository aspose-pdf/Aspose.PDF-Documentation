---
title: Python을 사용한 PDF 내 텍스트 서식 지정
linktitle: PDF 내 텍스트 서식 지정
type: docs
weight: 70
url: /ko/python-net/text-formatting-inside-pdf/
description: Python에서 Aspose.PDF를 사용하여 PDF 파일 내 텍스트 서식 옵션을 탐색하고 맞춤형 문서 스타일링을 수행하세요.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 텍스트 편집하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET를 사용한 PDF 문서에서 다양한 텍스트 서식 기술에 대한 포괄적인 가이드를 제공합니다. 여기에는 줄 들여쓰기 추가, 텍스트 테두리 만들기, 텍스트 밑줄 설정, 취소선 추가 등 다양한 기능이 포함됩니다.
---

## 줄 및 문자 간격

### 줄 간격 사용

#### Python에서 사용자 정의 줄 간격으로 텍스트 서식 지정하기 - 간단한 사례

Aspose.PDF for Python은 줄 간격 조정을 통해 텍스트 레이아웃과 가독성을 제어하는 간단한 방법을 보여줍니다.

우리의 코드 예제는 PDF 문서에서 줄 간격을 제어하는 방법을 보여줍니다. 파일에서 텍스트를 읽고(또는 대체 메시지를 사용), 사용자 정의 글꼴 크기와 줄 간격을 적용한 뒤, 서식이 적용된 텍스트를 PDF의 새 페이지에 추가합니다.

1. 새 PDF 문서를 생성합니다.
1. 소스 텍스트를 로드합니다.
1. TextFragment 객체를 초기화하고 로드한 텍스트를 할당합니다.
1. 텍스트의 글꼴 및 간격 속성을 설정합니다. 이 값들은 텍스트 라인이 얼마나 촘촘하거나 느슨하게 표시될지를 결정합니다:
- 글꼴 크기: 12포인트
- 줄 간격: 16포인트
1. 서식이 적용된 텍스트 조각을 페이지의 단락 컬렉션에 삽입합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Python에서 사용자 정의 줄 간격으로 텍스트 서식 지정하기 - 구체적 사례

PDF 문서에서 사용자 정의 TrueType 글꼴(TTF)을 사용하여 다양한 줄 간격 모드를 적용하는 방법을 확인해 보겠습니다.
파일에서 텍스트를 로드하고, 특정 글꼴을 포함하며, 같은 텍스트를 PDF 페이지에 두 번 렌더링합니다—각각 다른 줄 간격 모드를 사용합니다:

- FONT_SIZE 모드: 줄 간격이 글꼴 크기와 동일합니다.
- FULL_SIZE 모드: 줄 간격이 글꼴의 전체 높이를 고려하며, 상승부와 하강부를 포함합니다.

예제는 선택된 모드에 따라 줄 간격 동작이 어떻게 달라질 수 있는지 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 사용자 정의 글꼴 파일과 텍스트 소스 파일의 경로를 지정합니다.
1. 텍스트 내용을 로드합니다.
1. 사용자 정의 글꼴을 엽니다.
1. 첫 번째 TextFragment를 생성하고 구성합니다(FONT_SIZE 모드). line_spacing를 'TextFormattingOptions.LineSpacingMode.FONT_SIZE'로 설정하여 줄 간격이 글꼴 크기와 같게 합니다.
1. 두 번째 TextFragment를 생성하고 구성합니다(FULL_SIZE 모드). line_spacing를 'TextFormattingOptions.LineSpacingMode.FULL_SIZE'로 설정하여 글꼴의 전체 높이를 사용합니다.
1. 두 텍스트 조각을 같은 PDF 페이지에 추가합니다.
1. 완성된 문서를 지정된 출력 위치에 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![맞춤형 줄 간격(줄 사이에 16포인트 간격)으로 텍스트가 표시된 PDF 문서, 가독성 및 텍스트 레이아웃 서식을 향상](line_spacing.png)

### 문자 간격 사용

#### TextFragment 클래스를 사용하여 PDF 텍스트의 문자 간격을 제어하는 방법

문자 간격은 텍스트 한 줄의 개별 문자 사이 거리를 결정합니다—텍스트 외관을 미세 조정하거나 특정 타이포그래피 효과를 얻는 데 유용합니다.

1. 새 Document 객체를 초기화하고 텍스트를 배치할 빈 페이지를 추가합니다.
1. Fragment Generator를 정의합니다. 도움 함수 make_fragment(spacing)를 구현합니다:
- 샘플 텍스트로 TextFragment를 생성합니다.
- 글꼴을 설정합니다.
1. 서로 다른 간격 값을 가진 텍스트 조각을 추가합니다.
1. Document를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![PDF 문서에 동일한 텍스트 'Sample Text'가 세 줄 표시됩니다. 문자 간격이 위에서 아래로 점점 좁아지는 모습을 보여주며, 첫 번째 줄은 글자 사이 간격이 넓고, 중간 줄은 보통, 마지막 줄은 가장 좁은 문자 간격으로 PDF 텍스트 포맷팅에서 다양한 문자 간격 값의 시각적 효과를 나타냅니다](character_spacing_simple.png)

#### TextParagraph 및 TextBuilder를 사용하여 PDF 텍스트의 문자 간격을 제어하는 방법

Aspose.PDF는 TextParagraph와 TextBuilder를 사용하여 PDF 문서에 텍스트를 추가할 때 사용자 정의 문자 간격을 적용할 수 있습니다.
페이지에 특정 영역을 정의하고, 텍스트 래핑을 설정하며, 문자 간 간격이 조정된 텍스트 조각을 렌더링합니다.

텍스트 배치와 레이아웃에 대한 정밀한 제어가 필요할 때, 특히 구조화된 텍스트 블록이나 다중 열 텍스트 블록을 구축할 경우 TextParagraph를 사용하는 것이 이상적입니다.

1. 새 PDF 문서를 생성합니다.
1. 페이지용 TextBuilder 인스턴스를 초기화합니다.
1. TextParagraph를 생성하고 구성합니다.
- 단어 래핑 모드를 'TextFormattingOptions.WordWrapMode.BY_WORDS'로 설정합니다.
1. 사용자 정의 문자 간격이 적용된 TextFragment를 생성합니다.
- 새로운 TextFragment를 만들고 텍스트를 설정합니다(예: "Sample Text with character spacing").
- Arial과 같은 글꼴 및 글꼴 크기 14pt와 같은 속성을 지정합니다.
- 문자 간격 = 2.0을 적용하여 문자 사이의 간격을 늘립니다.
1. TextFragment를 TextParagraph에 추가합니다.
1. TextParagraph를 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## 목록 만들기

PDF 파일을 작업할 때, 목록과 같이 구조화된 정보를 표시해야 할 수 있습니다—불릿, 번호 매김, 혹은 HTML이나 LaTeX로 포맷된 경우도 포함합니다.
Aspose.PDF for Python via .NET는 PDF 문서 내에서 바로 목록을 만들고 포맷할 수 있는 여러 유연한 방법을 제공하여 레이아웃, 글꼴 및 스타일을 완벽하게 제어할 수 있게 합니다.

이 문서에서는 PDF에서 목록을 만드는 다양한 접근 방식을 보여줍니다. 일반 텍스트 포맷팅부터 고급 HTML 및 LaTeX 렌더링까지. 각 방법은 특정 사용 사례에 맞추어져 있으며, 정밀한 프로그래밍 제어를 원하든 편리한 마크업 기반 스타일링을 원하든 선택할 수 있습니다.

이 문서를 끝까지 읽으면 다음을 할 수 있게 됩니다:

- TextParagraph와 TextBuilder를 사용하여 사용자 정의 불릿 및 번호 매긴 목록을 만들기.

- HTML 조각(HtmlFragment)을 사용하여 PDF에서 '<ul>' 및 '<ol>' 목록을 쉽게 렌더링합니다.

- LaTeX 조각(TeXFragment)을 활용하여 수학적 또는 과학적 목록 포맷팅을 수행합니다.

- 페이지 내에서 텍스트 래핑, 글꼴 스타일, 레이아웃 위치를 제어합니다.

- 수동 목록 구성과 마크업 기반 접근 방식의 차이를 이해합니다.

### 불릿 목록 만들기

HTML이나 LaTeX 포맷에 의존하지 않고 TextParagraph와 TextBuilder를 사용하여 PDF에서 사용자 정의 불릿 목록을 생성합니다.
각 목록 항목은 불릿 문자(•)가 앞에 붙으며 개별 TextFragment로 추가됩니다.

1. Document 객체를 초기화하고 빈 페이지를 추가합니다.
1. 불릿 포인트로 변환될 문자열의 Python 리스트를 정의합니다.
1. TextBuilder와 TextParagraph를 생성합니다.
1. 'TextBuilder'를 사용하여 구성된 단락을 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 번호 매긴 목록 만들기

HTML이나 LaTeX 포맷에 의존하지 않고 TextParagraph와 TextBuilder를 사용하여 PDF에서 사용자 정의 번호 매긴(ordered) 목록을 생성합니다.
각 목록 항목은 번호(예: 1., 2.)가 앞에 붙으며 개별 TextFragment로 추가됩니다.

1. Document 객체를 초기화하고 빈 페이지를 추가합니다.
1. 번호 매긴 목록 항목으로 변환될 문자열의 Python 리스트를 정의합니다.
1. TextBuilder와 TextParagraph를 생성합니다.
1. 각 항목을 번호와 함께 TextFragment로 추가합니다.
1. TextBuilder를 사용하여 구성된 단락을 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 불릿 목록 HTML 버전 만들기

우리 라이브러리는 HTML 조각을 사용하여 PDF 문서에서 불릿(순서 없는) 목록을 만드는 방법을 보여줍니다. Python 문자열 리스트를 HTML `<ul>` 요소로 변환하고 이를 HtmlFragment로 PDF 페이지에 삽입합니다. HTML 조각을 사용하면 목록, 굵게, 이탤릭과 같은 HTML 포맷팅 기능을 PDF에서 직접 활용할 수 있습니다.

1. 새 PDF 문서를 생성하고 페이지를 추가합니다.
1. 목록 항목을 준비합니다.
1. 목록을 HTML 순서 없는 리스트로 변환합니다.
- 순서 없는(불릿) 목록에는 `<ul>` 태그를 사용합니다.
- 리스트 컴프리헨션을 사용하여 각 항목을 'li' 태그로 감싸세요.
1. HtmlFragment를 생성합니다. HTML 문자열을 PDF 페이지에 추가할 수 있는 HtmlFragment 객체로 변환합니다.
1. HtmlFragment를 페이지의 paragraphs 컬렉션에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF 문서에 표시된 불렛 리스트로, 네 개 항목이 보여집니다: 리스트의 첫 번째 항목, 래핑 동작을 보여주기 위한 더 많은 텍스트가 포함된 두 번째 항목, 세 번째 항목, 네 번째 항목. 각 항목은 표준 불렛 포인트가 앞에 붙으며, 적절한 들여쓰기와 간격을 갖춘 PDF 구조 내에서 HTML 형식 리스트 렌더링을 보여줍니다.](bullet_list_html.png)

### 번호 매기기 리스트 HTML 버전 만들기

HTML 조각을 사용하여 PDF 문서에 번호 매기기(ordered) 리스트를 생성합니다. 파이썬 문자열 리스트를 HTML `<ol>` 요소로 변환하고 이를 HtmlFragment로 PDF 페이지에 삽입합니다.

HTML 조각을 사용하면 번호 매기기 리스트, 굵게, 기울임 등과 같은 HTML 기반 서식 기능을 PDF에 직접 포함시킬 수 있습니다.

1. 새로운 PDF 문서를 만들고 페이지를 추가합니다.
1. 리스트 항목을 준비합니다.
1. 리스트를 HTML ordered list로 변환합니다.
- 번호 매기기 리스트에는 `<ol>` 태그를 사용합니다.
- 리스트 컴프리헨션을 사용하여 각 항목을 'li' 태그로 감쌉니다.
1. HTML 문자열을 PDF 페이지에 추가할 수 있는 HtmlFragment 객체로 변환합니다.
1. HtmlFragment를 페이지의 paragraphs 컬렉션에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF 문서에 표시된 번호 매기기 리스트로, 네 개의 자동 번호가 매겨진 항목이 보여집니다: 1. 리스트의 첫 번째 항목, 2. 래핑 동작을 보여주기 위한 더 많은 텍스트가 포함된 두 번째 항목, 3. 세 번째 항목, 4. 네 번째 항목. 이 리스트는 PDF 구조 내에서 적절한 숫자 순서, 들여쓰기 및 항목 간 간격을 갖춘 HTML 형식 ordered list 렌더링을 보여줍니다.](numbered_list_html.png)

### 불렛 리스트 LaTeX 버전 만들기

PDF에서 LaTeX 조각(TeXFragment)을 사용하여 불릿(순서 없는) 리스트를 생성합니다. 파이썬 문자열 리스트를 LaTeX itemize 환경으로 변환하고 이를 PDF 페이지에 삽입합니다. 수학 공식, 기호 또는 정밀한 서식이 필요한 구조화된 리스트를 렌더링하고 싶을 때 LaTeX 조각을 사용하는 것이 이상적입니다.

1. 새로운 PDF 문서를 만들고 페이지를 추가합니다.
1. LaTeX itemize 환경에서 불릿 포인트가 될 파이썬 문자열 리스트를 정의합니다.
1. 리스트를 LaTeX itemize 환경으로 변환합니다:
- 항목들을 \begin{itemize}와 \end{itemize}로 감쌉니다.
- 리스트 컴프리헨션을 사용하여 각 항목 앞에 \item을 붙입니다.
1. LaTeX 문자열을 PDF에 렌더링할 수 있는 TeXFragment 객체로 변환합니다.
1. LaTeX 조각을 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![PDF에 표시된 불릿 리스트로, LaTeX 렌더링된 서식과 텍스트 'Lists are easy to create:'가 있으며 네 개의 불릿 항목이 뒤따릅니다: 첫 번째 항목, 래핑 동작을 보여주기 위한 더 많은 텍스트가 포함된 두 번째 항목, 세 번째 항목, 네 번째 항목. 이 리스트는 깔끔한 PDF 문서 레이아웃 내에서 적절한 불릿 서식, 일관된 간격 및 텍스트 래핑 기능을 갖춘 전문적인 LaTeX 조판을 보여줍니다.](bullet_list_latex.png)

### 번호 매기기 리스트 LaTeX 버전 만들기

PDF에서 LaTeX 조각(TeXFragment)을 사용하여 번호 매기기(ordered) 리스트를 생성합니다. 파이썬 문자열 리스트를 LaTeX enumerate 환경으로 변환하고 이를 PDF 페이지에 삽입합니다. 정밀한 서식, 구조화된 리스트 또는 수학 기호를 PDF에 포함하고자 할 때 LaTeX 조각을 사용하는 것이 이상적입니다.

1. 새로운 PDF 문서를 만들고 페이지를 추가합니다.
1. LaTeX enumerate 환경에서 번호가 매겨질 항목이 될 파이썬 문자열 리스트를 정의합니다.
1. 리스트를 LaTeX enumerate 환경으로 변환합니다.
1. LaTeX 문자열을 PDF에 렌더링할 수 있는 TeXFragment 객체로 변환합니다.
1. LaTeX 조각을 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![PDF에 표시된 번호 매기기 리스트로, LaTeX 렌더링된 서식과 항목 1. 첫 번째 항목, 2. 래핑 동작을 보여주기 위한 더 많은 텍스트가 포함된 두 번째 항목, 3. 세 번째 항목, 4. 네 번째 항목이 'Lists are easy to create' 텍스트 앞에 나타납니다.](numbered_list_latex.png)

## 각주와 미주

### 각주 추가

각주는 문서 본문 내에서 관련 텍스트 옆에 연속된 위첨자 번호를 배치하여 주석을 참조하는 데 사용됩니다. 이러한 번호는 일반적으로 들여쓰기된 상세 주석에 대응하며, 동일 페이지 하단에 위치하여 추가적인 맥락, 인용 또는 설명을 제공합니다.

PDF 문서에서 텍스트 조각에 각주를 추가하려면 .NET을 통한 Python용 Aspose.PDF를 사용합니다. 각주는 주요 내용에 혼란을 주지 않으면서 보조 정보, 인용 또는 설명을 제공하는 데 유용합니다. 이 방법은 각주가 PDF 레이아웃에 시각적 및 구조적으로 통합되도록 보장합니다.

1. 새 문서를 생성합니다.
1. 주요 콘텐츠를 포함한 TextFragment를 생성합니다.
1. 인라인 텍스트를 추가합니다. 같은 문단에서 이어지는 또 다른 TextFragment를 생성합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### PDF에 사용자 정의 스타일 각주 추가

1. 새 PDF 문서를 초기화하고 빈 페이지를 추가합니다.
1. 메인 텍스트 조각을 생성합니다.
1. 각주를 생성하고 스타일을 지정합니다(글꼴, 크기, 색상, 스타일).
1. 스타일이 적용된 텍스트 조각과 각주를 페이지에 삽입합니다.
1. 각주가 없는 다른 텍스트 조각을 추가합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### PDF에서 사용자 정의 기호로 각주 추가

Aspose.PDF for Python via .NET를 사용하여 PDF 문서의 텍스트 조각에 각주를 추가하고, 각주 표시 기호를 사용자 정의할 수 있습니다.

1. PDF 문서와 페이지를 생성합니다.
1. 사용자 정의 각주 기호가 있는 첫 번째 텍스트 조각을 추가합니다.
1. 각주 없이 단락을 이어가는 또 다른 텍스트 조각을 추가합니다.
1. 기본 각주가 있는 두 번째 텍스트 조각을 추가합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### PDF에서 사용자 정의 선 스타일로 각주 추가

Python 라이브러리를 사용하여 PDF 문서의 각주 선 시각적 모양을 맞춤 설정합니다. 각주 선을 커스터마이즈하면 시각적 명료성이 향상되고 보고서, 학술 논문, 주석이 달린 출판물 등 문서의 스타일 일관성을 유지할 수 있습니다.

1. 새 PDF 문서를 생성하고 페이지를 추가합니다.
1. 각주 연결선에 대한 사용자 정의 선 스타일(색상, 두께, 점선 패턴)을 정의합니다.
1. 각주가 포함된 여러 텍스트 조각을 추가합니다.
1. 최종 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### PDF에 이미지와 표가 포함된 각주 추가

Aspose.PDF for Python via .NET를 사용하여 이미지, 스타일 텍스트 및 표를 삽입함으로써 PDF 문서의 각주를 풍부하게 만드는 방법은?

1. 새 PDF 문서를 생성하고 페이지를 추가합니다.
1. 첨부된 각주가 있는 텍스트 조각을 추가합니다.
1. 각주 안에 이미지, 스타일 텍스트 및 표를 삽입합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### PDF 문서에 미주 추가

미주는 인용의 한 형태로, 독자를 문서 끝에 지정된 섹션으로 안내하여 인용문, 패러프레이즈된 아이디어 또는 요약된 내용에 대한 전체 참고 정보를 찾을 수 있게 합니다. 미주를 사용할 때는 참고된 자료 바로 뒤에 위첨자 번호를 배치하여 독자가 논문 끝에 있는 해당 메모로 이동하도록 합니다.

이 코드 스니펫은 PDF 문서의 텍스트 조각에 미주를 추가하는 방법을 보여줍니다. 참조된 텍스트 근처에 나타나는 각주와 달리, 미주는 일반적으로 문서나 섹션의 끝에 배치됩니다. 이 메서드는 또한 긴 문서를 시뮬레이션하여 확장된 내용에서 미주가 어떻게 동작하는지 보여줍니다.

1. PDF 문서와 페이지를 생성합니다.
1. 미주가 포함된 텍스트 조각을 추가합니다.
1. 외부 텍스트 콘텐츠를 로드합니다.
1. 긴 문서를 시뮬레이션합니다. 로드한 텍스트를 여러 번 추가하여 더 긴 문서를 흉내냅니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### PDF에 사용자 정의 마커 텍스트가 있는 미주 추가

PDF 문서의 텍스트 조각에 사용자 정의 마커 기호(예: "***")를 사용하여 미주를 추가합니다. 미주는 일반적으로 문서나 섹션의 끝에 배치되며 추가적인 맥락, 인용 또는 주석을 제공하는 데 유용합니다.

1. PDF 문서와 페이지를 생성합니다.
1. 미주가 포함된 스타일 텍스트 조각을 추가합니다.
1. 미주 마커 텍스트를 사용자 정의합니다.
1. .txt 파일에서 외부 콘텐츠를 로드합니다.
1. 미주 배치를 보여주기 위해 장문 콘텐츠를 시뮬레이션합니다.
1. PDF 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## 레이아웃 및 페이지 제어

### PDF에서 표를 새 페이지에서 시작하도록 강제

Aspose.PDF for Python via .NET를 사용하여 PDF 문서에서 특정 콘텐츠를 새 페이지에서 시작하도록 추가합니다.
'is_in_new_page' 속성을 설정하면 페이지 레이아웃과 구조를 정밀하게 제어할 수 있어, 표, 보고서, 요약 등 특정 섹션이 항상 새 페이지에서 시작하도록 보장합니다 — 문서 형식화, 인쇄 준비 보고서 또는 체계적인 출력 생성에 이상적입니다.

1. 표를 만들고 구성합니다.
1. 표에 데이터를 추가합니다.
1. 표를 새 페이지에 강제합니다. 이렇게 하면 현재 페이지에 내용이 있더라도 표가 새 페이지 상단에서 시작하도록 보장합니다.
1. 표를 페이지에 추가합니다. 'page.paragraphs.add()'를 사용하여 PDF 레이아웃에 표를 포함합니다.
1. 문서를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### PDF에서 인라인 단락 속성 사용

우리 라이브러리는 PDF 내에서 텍스트와 이미지 사이의 인라인 흐름을 제어하기 위해 'is_in_line_paragraph' 속성을 사용할 수 있게 합니다.
보통 새 요소(텍스트 조각이나 이미지 등)를 추가하면 각각 새 줄이나 새 단락에서 시작합니다.
'is_in_line_paragraph = True'로 설정하면 요소가 같은 줄이나 같은 단락에 나타나도록 할 수 있어 부드러운 인라인 레이아웃을 만들 수 있습니다 — 로고, 아이콘, 기호 등을 문장 내에 삽입하는 등 텍스트와 이미지를 인라인으로 결합하는 데 적합합니다.

첫 번째 텍스트 조각, 이미지, 두 번째 텍스트 조각이 같은 줄에 나타나 연속적인 인라인 단락을 형성합니다.
세 번째 텍스트 조각은 새 단락을 시작하며 기본 줄바꿈 동작을 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 첫 번째 텍스트 조각을 추가합니다.
1. 인라인 이미지를 삽입합니다.
1. 추가 인라인 텍스트를 삽입합니다.
1. 새 단락을 추가합니다.
1. PDF를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### 다중 열 PDF 만들기

Aspose.PDF for Python via .NET를 사용하여 PDF에서 신문 스타일의 다중 열 레이아웃을 만듭니다.
FloatingBox 내에서 텍스트, HTML 서식 및 그래픽을 결합하는 방법을 보여주며, 다중 열 잡지나 뉴스레터 디자인과 유사한 고급 레이아웃 제어를 가능하게 합니다.

1. PDF 문서를 초기화합니다.
1. 상단에 가로 구분선 라인을 추가합니다.
1. 스타일이 적용된 HTML 헤딩을 추가합니다.
1. 레이아웃 제어를 위해 FloatingBox를 생성합니다.
1. 다중 열 레이아웃을 구성합니다.
1. 저자 정보를 추가합니다.
1. 또 다른 내부 가로선을 그립니다.
1. 기사 텍스트를 추가합니다.
1. 최종 PDF를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### PDF에서 텍스트 정렬을 위한 사용자 지정 탭 정지점

사용자 지정 탭 정지점을 사용하여 PDF에서 표와 같은 텍스트 레이아웃을 만들며, 표 구조에 의존하지 않습니다.
탭 정지점 위치, 정렬 및 리더 스타일을 정의함으로써 열 사이에 텍스트를 정확하게 정렬할 수 있습니다. 이는 청구서, 보고서 또는 구조화된 텍스트 데이터에 유용합니다.

1. 새 PDF 문서를 생성합니다.
1. 사용자 지정 탭 정지점을 정의합니다.
1. 텍스트에서 #$TAB 자리 표시자를 사용합니다.
1. PDF에 텍스트를 추가합니다.
1. PDF를 저장합니다.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
