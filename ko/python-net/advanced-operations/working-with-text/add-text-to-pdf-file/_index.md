---
title: PDF에 텍스트 추가하기
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/python-net/add-text-to-pdf-file/
description: 이 문서에서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하고, HTML 조각을 삽입하거나, 사용자 정의 OTF 글꼴을 사용하는 방법을 배울 수 있습니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF에 텍스트 추가
Abstract: 이 문서는 Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 조작하는 포괄적인 가이드를 제공합니다. 텍스트 추가 및 서식 지정 기술을 다루며, 글꼴 크기, 유형, 색상 및 위치와 같은 텍스트 속성 설정을 포함합니다.
---

이 가이드는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 텍스트 내용을 추가하는 방법을 설명합니다. 간단한 텍스트 조각을 특정 위치에 배치하는 것부터 글꼴, 크기, 색상, 스타일을 적용하고, 오른쪽에서 왼쪽(RTL) 언어 처리, 하이퍼링크 삽입, 단락 레이아웃, 리스트 및 투명도 효과 작업까지 핵심 텍스트 삽입 기술을 배웁니다. 또한 HTML 또는 LaTeX 조각, 사용자 정의 글꼴, 줄 간격 및 문자 간격과 같은 텍스트 서식 옵션과 같은 고급 시나리오도 다룹니다.

간단한 주석을 만들든 풍부한 타이포그래피 레이아웃을 구축하든, 이 자료는 Aspose.PDF를 사용하여 PDF에서 텍스트 작업을 위한 기본 빌딩 블록을 제공합니다.

## 기본 텍스트 삽입

Aspose.PDF for Python via .NET은 PDF 파일 내 텍스트를 처리하기 위한 강력하고 유연한 API를 제공합니다.
간단한 정적 레이블이든, 풍부하게 서식이 적용된 콘텐츠이든, 다국어 텍스트이든, 인터랙티브 하이퍼링크이든, 이 툴킷을 사용하면 간결한 Python 코드로 모두 구현할 수 있습니다.

### 텍스트 추가 간단 사례

Aspose.PDF for Python via .NET은 페이지의 특정 위치에 간단한 텍스트 조각을 추가하는 방법을 보여줍니다. 새 PDF 문서를 만들고, 페이지를 추가하고, 지정된 좌표에 텍스트를 삽입하고, 결과 파일을 저장하는 방법을 배웁니다.

1. 새 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 생성합니다.
1. `document.pages.add()`를 사용하여 새 빈 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 만듭니다.
1. 텍스트 내용을 포함하는 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)을 생성합니다.
1. [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) 클래스를 사용하여 텍스트 위치를 설정합니다. `Position`을 지정하면 텍스트가 문서에서 왼쪽에서 오른쪽으로 배치되고 아래쪽으로 이동합니다.
1. 텍스트 모양을 사용자 정의합니다. [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)를 통해 글꼴 크기, 색상, 스타일 등을 설정할 수 있습니다.
1. `page.paragraphs.add(text_fragment)`를 사용하여 `TextFragment`를 페이지의 단락 컬렉션에 추가합니다.
1. 문서를 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

이 코드 예제는 TextFragment를 사용합니다. 하지만 TextParagraph를 사용하여 PDF 페이지에 텍스트를 추가할 수도 있습니다. 차이점을 살펴보겠습니다.
**[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** 은 단일 텍스트 조각입니다. TextFragment는 텍스트의 단일 단위를 나타내며, 기본적으로 배치, 스타일링 및 위치 지정이 가능한 하나의 문자열입니다. 간단하고 적은 양의 텍스트를 추가해야 할 때 이상적입니다.

**[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** 은 TextFragment들의 그룹입니다. 여러 텍스트 라인을 추가할 수 있습니다. TextParagraph는 하나 이상의 TextFragment 객체를 포함하는 컨테이너 또는 컬렉션입니다. 여러 조각을 함께 묶어야 할 때—예를 들어 여러 줄, 단어 또는 서식이 적용된 요소들로 구성된 텍스트 블록을 만들 때—이상적입니다.
TextParagraph는 텍스트 정렬, 줄 간격 및 페이지의 자동 레이아웃도 관리합니다. 빨간 선의 사용은 TextParagraph에서만 가능합니다.

텍스트 작업에 대한 자세한 내용은 [PDF 내부 텍스트 서식](/pdf/python-net/text-formatting-inside-pdf/) 및 [Python을 사용한 PDF에서 텍스트 추출](/pdf/python-net/extract-text-from-pdf/) 문서 섹션을 확인하십시오.

### TextParagraph를 사용한 텍스트 추가

Aspose.PDF for Python via .NET은 [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/)와 [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)를 사용하여 줄 바꿈 옵션과 함께 텍스트 단락을 추가할 수 있습니다.

1. `document.pages.add()`를 사용하여 새 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)과 빈 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 생성합니다.
1. 파일에서 텍스트를 읽거나 기본 텍스트를 사용합니다.
1. 레이아웃 및 줄 바꿈 제어가 가능한 단락 수준의 콘텐츠를 추가하기 위해 [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/)를 생성합니다.
1. [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)를 생성하고 래핑 모드를 설정합니다(예제에서는 `DISCRETIONARY_HYPHENATION`을 사용합니다).
1. [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)를 생성하고 스타일을 적용한 뒤, 해당 조각을 단락에 추가합니다.
1. `TextBuilder`를 사용하여 단락을 페이지에 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![TextParagraph를 사용한 텍스트 추가](text_paragraph.png)

### PDF에서 들여쓰기가 있는 단락 추가

다음 코드 스니펫은 새 PDF 문서를 만들고 서로 다른 들여쓰기 스타일을 가진 두 개의 텍스트 단락을 추가하는 방법을 보여줍니다:

- 첫 번째 단락은 첫 줄 들여쓰기를 보여줍니다(첫 줄만 들여쓰기).

- 두 번째 단락은 이후 줄 들여쓰기를 보여줍니다(첫 줄 이후 모든 줄이 들여쓰기).

이 예제는 Aspose.PDF의 'TextParagraph', 'TextBuilder', 'TextFragment' 클래스를 사용하여 레이아웃과 서식을 정밀하게 제어합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### PDF에 새 텍스트 줄 추가

Aspose.PDF for Python via .NET을 사용하면 TextFragment, TextParagraph, TextBuilder 클래스를 이용해 PDF 문서에 여러 줄 텍스트를 삽입할 수 있습니다.

1. 새 문서를 생성합니다.
1. 새 줄 문자를 포함하는 TextFragment를 정의합니다.
1. 텍스트 스타일을 설정합니다.
1. 프래그먼트를 단락에 추가합니다.
1. 단락의 위치를 지정합니다.
1. 페이지에 단락을 렌더링합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### PDF에서 줄 바꿈 및 로그 알림 결정

PDF 문서에 여러 텍스트 프래그먼트를 포함하고 Aspose.PDF 알림 로깅을 활성화하여 렌더링 중에 줄 바꿈 및 텍스트 래핑과 같은 레이아웃 이벤트를 모니터링하는 방법을 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 알림 로깅을 활성화합니다.
1. document.pages.add()를 사용하여 첫 페이지를 생성합니다.
1. 여러 텍스트 프래그먼트를 추가합니다.
1. page.paragraphs.add(text)를 사용하여 각 텍스트 프래그먼트를 렌더링합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### PDF에서 텍스트 너비를 동적으로 측정

Aspose.PDF for Python via .NET를 사용하여 특정 글꼴에서 문자와 문자열의 너비를 동적으로 측정합니다. 'Font.measure_string()' 및 'TextState.measure_string()' 메서드를 사용하여 측정된 문자열 너비가 일관되고 정확함을 확인합니다.

1. 'FontRepository.find_font()'를 사용하여 저장소에서 Arial 글꼴 객체를 가져옵니다.
1. 글꼴 속성을 관리하기 위해 TextState 객체를 생성합니다.
1. 개별 문자를 측정합니다.
1. 'A'와 'z' 사이의 모든 문자에 대해 두 방법의 결과를 비교합니다.
1. 두 측정 방법이 동일한 결과를 제공하는지 확인합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### 하이퍼링크가 포함된 텍스트 추가

Aspose.PDF for Python via .NET를 사용하여 PDF 텍스트에 클릭 가능한 하이퍼링크를 추가합니다. 이 라이브러리는 단일 TextFragment 내에 여러 텍스트 세그먼트를 추가하고 특정 세그먼트에 하이퍼링크를 적용하며, 텍스트 세그먼트를 개별적으로 스타일링(예: 색상, 이탤릭체)하는 방법을 보여줍니다.

1. 'Document()'를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. TextFragment를 생성합니다.
1. 여러 TextSegment 객체를 추가합니다. 각 세그먼트는 고유한 내용과 스타일을 가질 수 있습니다. 예를 들어 일반 텍스트나 하이퍼링크 텍스트가 있습니다.
1. 세그먼트에 하이퍼링크를 적용합니다. 원하는 URL로 WebHyperlink 객체를 생성합니다.
1. 세그먼트를 스타일링합니다. text_state를 사용하여 색상, 글꼴 스타일, 크기 등을 사용자 지정합니다.
1. 'page.paragraphs.add()'를 사용하여 프래그먼트를 페이지에 추가합니다.
1. PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![PDF에 표시된 텍스트 프래그먼트로, Sample Text Fragment 다음에 Text Segment 1이 표시되고, 그 뒤에 파란색 하이퍼링크 텍스트 'Link to Aspose' (링크: https://products.aspose.com/pdf) 가 있으며, 마지막으로 일반 검은색 텍스트 형식의 하이퍼링크 없이 TextSegment 로 끝납니다](hyperlink_text.png)

### PDF 문서에 오른쪽-왼쪽(RTL) 텍스트 추가

RTL(오른쪽에서 왼쪽) 은 텍스트 쓰기 방향을 나타내는 속성으로, 텍스트가 오른쪽에서 왼쪽으로 작성됩니다.
Aspose.PDF for Python via .NET는 아랍어 또는 히브리어와 같은 오른쪽-왼쪽(RTL) 텍스트를 PDF 문서에 추가하는 방법을 보여줍니다.

1. 'Document()'를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. RTL 내용을 가진 TextFragment를 생성합니다. 아랍어, 히브리어 또는 기타 RTL 언어 텍스트를 프래그먼트 내용으로 삽입합니다.
글꼴 및 스타일을 설정합니다. RTL 스크립트를 지원하는 글꼴(예: Tahoma, Arial Unicode MS)을 선택합니다. 필요에 따라 font_size와 foreground_color를 설정합니다.
1. 'text_fragment.horizontal_alignment'를 사용하여 수평 정렬을 오른쪽으로 설정합니다.
1. 텍스트 프래그먼트를 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![오른쪽-왼쪽 텍스트](rtl_text.png)

## 텍스트 스타일링

### 글꼴 스타일링이 포함된 텍스트 추가

이 예시는 텍스트 스타일링, 글꼴 사용자 정의 및 혼합 형식 텍스트(서브스크립트 텍스트 세그먼트 사용)를 보여주는 보다 고급 예제입니다. Aspose.PDF는 글꼴 패밀리, 크기, 색상, 굵게, 이탤릭, 밑줄과 같은 글꼴 속성을 텍스트 프래그먼트에 적용하는 방법을 설명합니다.
또한 이 코드 스니펫은 단일 프래그먼트 내에서 여러 텍스트 세그먼트를 사용하여 복잡한 텍스트 표현을 만드는 방법을 보여줍니다—예를 들어, 수식이나 과학적 표기에서 자주 필요한 아래첨자 또는 위첨자 문자를 포함하는 경우 등.

1. 'Document()'를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. 간단한 스타일 텍스트를 위한 TextFragment를 생성합니다.
1. 텍스트 내용을 정의합니다.
1. Position(x, y) 좌표를 사용하여 위치를 설정합니다.
1. 'text_state property'를 통해 스타일을 적용합니다 - font, font_size, foreground_color, font_style, underline.
1. 여러 TextSegment 개체를 사용하여 복합 식을 생성합니다. 각 TextSegment는 자체 스타일을 가질 수 있는 텍스트 부분을 나타냅니다. 이를 통해 수학식이나 화학식과 같은 식을 만들 수 있습니다.
1. 여러 TextState 개체를 정의합니다. 하나는 메인 텍스트(text_state_letters)를 위해, 다른 하나는 아래첨자 또는 위첨자 텍스트(text_state_index)를 위해 사용합니다.
1. 텍스트 세그먼트를 결합합니다. 각 세그먼트를 'TextFragment'에 'segments.append()'로 추가합니다.
1. 두 텍스트 객체를 페이지에 추가합니다. 'page.paragraphs.add()'를 사용하여 문서에 배치합니다.
1. 최종 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![텍스트 조각이 파란색 이탤릭 Arial 폰트로 표시되고 'Hello, Aspose!' 텍스트와 뒤이어 파란색 메인 텍스트와 빨간색 아래첨자 서식이 적용된 수학식 S = a₂n + a₂n+1 + a₂n+2 를 포함하고 있습니다](styled_text.png)

## 텍스트 투명 추가

Aspose.PDF for Python을 사용하여 PDF 문서에 반투명 도형과 텍스트를 추가합니다.
색상이 지정된 사각형을 부분 투명도로 생성하고 투명한 전경 색상의 TextFragment를 겹쳐 놓습니다.

1. Document 객체를 초기화하고 그리기 콘텐츠를 위해 빈 페이지를 추가합니다.
1. 'ap.drawing.Graph'를 사용하여 도형을 그릴 수 있는 캔버스를 만듭니다.
1. 반투명 채우기가 적용된 사각형을 추가합니다.
1. 캔버스 위치 이동을 방지합니다.
1. 캔버스를 페이지에 추가합니다. 그래픽 도형을 페이지 단락 컬렉션에 삽입합니다.
1. 투명 텍스트 조각을 생성합니다.
1. 텍스트 조각을 페이지 단락 컬렉션에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### PDF에 보이지 않는 텍스트 추가

이 예제는 보이는 텍스트와 보이지 않는 텍스트를 모두 포함하는 PDF 문서를 만드는 방법을 보여줍니다. 보이지 않는 텍스트는 문서 구조의 일부로 남아 있지만 화면에 표시되지 않아 메타데이터, 접근성 태그, 레이아웃에 영향을 주지 않는 검색 가능한 콘텐츠를 삽입하는 데 유용합니다.

1. PDF 문서와 페이지를 생성합니다.
1. 반복되는 가시 텍스트가 포함된 텍스트 조각을 만듭니다.
1. 두 번째 텍스트 조각을 추가하고 이를 보이지 않도록 표시합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### PDF에서 테두리 스타일이 적용된 텍스트 추가

Aspose.PDF 라이브러리를 사용하면 보이는 테두리가 있는 스타일링된 텍스트 조각을 포함한 PDF 문서를 만드는 방법을 보여줍니다. 이 방법은 배경 및 전경 색, 폰트 설정, 텍스트 사각형 주변에 스트로크(테두리)를 적용하여 시각적 강조 효과를 높입니다.

1. PDF 문서와 페이지를 생성합니다.
1. 텍스트 조각을 만들고 위치를 지정합니다. 메시지가 포함된 텍스트 조각을 추가하고 위치를 설정합니다.
1. 텍스트 스타일을 적용합니다. 폰트를 Times New Roman, 크기 12로 설정하고, 밝은 회색 배경과 빨간색 전경(텍스트) 색을 적용합니다.
1. 테두리 스타일을 구성합니다.
1. 페이지에 텍스트를 추가합니다. TextBuilder를 사용하여 스타일링된 텍스트를 페이지에 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### PDF에 취소선 텍스트 추가

PDF 문서의 텍스트 조각에 취소선(선 위에 그어진) 서식을 추가합니다. 취소선 �스트는 삭제, 수정 또는 강조를 나타내는 주석 문서에 유용합니다.

1. 'Document()'와 'document.pages.add()'를 사용하여 새 문서와 페이지를 만들고 빈 페이지를 추가합니다.
1. 텍스트 조각을 만들고 스타일을 지정합니다.
1. 색상 및 취소선 서식을 적용합니다. 배경을 밝은 회색으로, 텍스트 색을 빨간색으로 설정하고 취소선을 활성화합니다.
1. 텍스트 위치를 지정합니다.
1. 'TextBuilder'를 사용하여 스타일링된 텍스트를 페이지에 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## 고급 색상 효과

### PDF에서 텍스트에 축 방향 그라디언트 적용

Aspose.PDF for Python via .NET은 PDF 문서의 텍스트에 선형 그라디언트 효과를 적용하는 방법을 보여줍니다. 축 방향 그라디언트는 텍스트 전체에 걸쳐 빨간색에서 파란색으로 부드럽게 전환되어 시각적으로 눈에 띄는 헤딩을 만듭니다. 이 기법은 스타일화된 제목, 브랜딩, 또는 PDF 레이아웃에서 장식 요소에 이상적입니다.

1. 새 문서를 초기화하고 빈 페이지를 추가합니다.
1. 텍스트 조각을 만들고 스타일을 지정합니다. 제목을 추가하고 위치, 폰트, 크기를 설정합니다.
1. 'GradientAxialShading'을 사용하여 축 방향 그라디언트 색조를 적용합니다. 빨간색에서 파란색으로 전환되는 GradientAxialShading으로 전경 색을 설정합니다.
1. 밑줄 스타일을 추가합니다.
1. 스타일링된 텍스트 조각을 페이지에 삽입합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### PDF에서 텍스트에 방사형 그라디언트 적용

방사형 그라디언트는 텍스트 중심에서 바깥쪽으로 퍼지는 원형 색상 전환을 만들어 제목, 헤더 또는 장식 요소에 시각적으로 역동적인 스타일 옵션을 제공합니다.

1. 새 문서를 초기화하고 빈 페이지를 추가합니다.
1. 텍스트 조각을 생성하고 스타일을 적용합니다. 제목을 추가하고 위치, 글꼴 및 크기를 설정합니다.
1. 'GradientRadialShading'을 사용하여 방사형 그라디언트를 적용합니다. GradientRadialShading을 사용해 전경 색상을 빨간색에서 파란색으로 설정합니다.
1. 밑줄 스타일을 추가합니다.
1. 스타일이 적용된 텍스트 조각을 페이지에 삽입합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![방사형 그라디언트 셰이딩 적용](gradient_radial_shading.png)

## HTML 및 LaTeX 조각

### PDF 문서에 HTML 텍스트 추가

Aspose.PDF for Python via .NET 라이브러리를 사용하면 HtmlFragment 클래스를 통해 HTML 형식의 콘텐츠를 PDF 문서에 삽입할 수 있습니다. HTML 태그를 사용하면 스타일이 적용된 구조화된 텍스트나 수식과 같은 텍스트를 PDF에 직접 렌더링할 수 있습니다.

1. 'Document()'를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. HtmlFragment 클래스의 인스턴스를 생성하고 HTML 문자열을 매개변수로 전달합니다.
1. 'page.paragraphs.add()'를 사용하여 페이지에 조각을 추가하고 HTML 콘텐츠를 삽입합니다.
1. PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![PDF 문서에 HTML 텍스트 추가](html_fragment.png)

### 다양한 서식이 적용된 스타일 HTML 조각을 PDF 문서에 추가

HTML 조각을 정의하고 HTML 태그를 사용하여 텍스트 스타일을 직접 설정할 수 있습니다. 스타일이 적용된 HTML 콘텐츠를 PDF 문서에 삽입합니다. 이 코드 조각은 새로운 PDF 파일을 생성하고, 페이지를 추가한 뒤, 다양한 서식 요소(헤딩, 단락, 링크 및 인라인 스타일)가 포함된 HTML 조각을 삽입하고, 지정된 경로에 결과를 저장합니다.

1. PDF를 나타내는 새 Document 객체를 초기화합니다.
1. HTML 콘텐츠가 배치될 빈 페이지를 문서에 추가합니다.
1. HTML 콘텐츠를 준비합니다. HTML 문자열에는 h1 제목, 녹색 단락(굵게, 이탤릭 및 밑줄이 적용된 텍스트)과 글꼴 크기가 확대된 웹사이트 하이퍼링크가 포함되어 있습니다.
1. HTML 조각을 생성합니다. HTML 문자열을 HtmlFragment 객체에 래핑합니다.
1. HTML을 페이지에 삽입합니다. HTML 조각을 페이지의 단락 컬렉션에 추가하여 HTML을 기본 PDF 콘텐츠로 렌더링합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF 문서에 HTML 콘텐츠 추가](html_content.png)

### 텍스트 상태를 재정의한 HTML 조각 추가

이전 예제에서 보듯이, HTML 코드에 직접 스타일을 설정할 수 있습니다. 이는 장점이 있지만 단점도 있습니다. 고객의 HTML을 사용하고 출력물의 외관을 통일하려고 한다고 가정해 보겠습니다.
이 경우, 아래 예시와 같이 자체 TextState를 사용하여 고객의 스타일을 재정의할 수 있습니다.

1. 'Document()'를 사용해 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. HTML 콘텐츠를 준비합니다. HTML 문자열에는 Verdana 글꼴을 적용한 h1 제목, 녹색 단락(굵게, 이탤릭 및 밑줄이 적용된 텍스트)과 글꼴 크기가 큰 웹사이트 하이퍼링크가 포함되어 있습니다.
1. HTML 조각을 생성합니다. HTML 문자열을 HtmlFragment 객체에 래핑합니다.
1. 텍스트 서식을 재정의합니다. TextState 객체를 생성하고 글꼴, 글꼴 크기 및 텍스트 색상을 설정합니다.
1. HTML 조각을 페이지의 단락 컬렉션에 추가합니다.
1. 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![HTML 조각 텍스트 상태 재정의 추가](html_override.png)

### PDF 문서에 LaTeX 텍스트 추가

Aspose.PDF for Python via .NET의 TeXFragment 클래스를 사용하여 PDF 문서에 LaTeX 형식의 수학식을 추가합니다.
LaTeX는 과학 및 수학 문서를 작성할 때 널리 사용되는 강력한 조판 시스템입니다. TeXFragment를 사용하면 PDF 페이지 내에서 LaTeX 수학 표기법과 기호를 직접 렌더링할 수 있습니다.

1. 'Document()'를 사용해 새 문서와 페이지를 만들고, 'document.pages.add()'로 빈 페이지를 추가합니다.
1. TeXFragment 클래스를 사용하여 LaTeX 구문을 직접 렌더링합니다.
1. 'page.paragraphs.add()'를 사용해 LaTeX 콘텐츠를 PDF 레이아웃에 추가합니다.
1. PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![PDF에 표시된 복잡한 수학식으로, (a+b)⁶ 위에 overbrace 표기, 전체 식 (a+b)⁶·(c+d)⁷ 아래에 underbrace 표기, 'example of text' 라벨이 붙고 =42 로 표시됩니다. 이 수식은 LaTeX 렌더링의 전형적인 적절한 간격 및 괄호 스타일을 갖춘 고급 수학 조판을 보여줍니다](latex_fragment.png)

## 사용자 정의 폰트

### 파일에서 사용자 정의 폰트 사용

이 예제는 Aspose.PDF for Python via .NET에서 사용자 정의 OpenType 폰트를 사용하여 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다. 새 PDF 문서를 만들고, 페이지에 텍스트를 정확하게 배치하며, 글꼴 종류, 크기, 색상 및 이탤릭 스타일과 같은 사용자 정의 서식을 적용하는 방법을 설명합니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. PDF에 추가하려는 텍스트 내용을 정의합니다.
1. 텍스트 위치를 설정합니다.
1. TextFragment를 페이지에 추가합니다.
1. PDF 문서를 저장합니다.

이 기능은 OTF뿐만 아니라 TTF 글꼴에서도 작동합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![PDF 문서에 표시된 텍스트 조각으로, Hello, Aspose!가 파란색 이탤릭 BriosoPro 폰트로 렌더링되어 PDF 텍스트 서식 내에서 사용자 정의 OpenType 글꼴 통합 및 스타일링 기능을 보여줍니다](custom_font.png)

### 스트림에서 사용자 정의 폰트 사용

이 코드 스니펫은 Aspose.PDF for Python via .NET을 사용하여 사용자 정의 임베디드 OpenType (OTF) 글꼴로 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다. 글꼴 파일을 스트림으로 열어 PDF에 임베드함으로써 다양한 시스템에서 글꼴 가용성을 보장하고, 글꼴 크기, 색상, 이탤릭 스타일과 같은 텍스트 서식을 적용하는 방법을 설명합니다. 이 접근 방식은 설치된 글꼴이 없는 장치에서도 공유하거나 볼 때도 타이포그래피를 유지하여 시각적으로 일관된 PDF를 만드는 데 이상적입니다.

1. 글꼴 파일을 바이너리 스트림으로 로드합니다.
1. 'FontRepository.open_font'를 사용하여 글꼴을 열고 임베드합니다.
1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 다음을 사용하여 스타일이 적용된 텍스트 조각을 추가합니다:
- 임베디드 사용자 정의 글꼴.
- 이탤릭 스타일 및 파란색 색상.
- 지정된 글꼴 크기와 위치.
1. 최종 문서를 지정된 출력 경로에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

글꼴을 임베드하면 플랫폼 전반에 걸쳐 일관된 렌더링을 보장하므로 이 접근 방식은 브랜딩, 디자인 정확성 및 다국어 지원에 이상적입니다.

