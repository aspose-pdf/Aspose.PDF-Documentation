---
title: 파이썬에서 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/python-net/add-text-to-pdf-file/
description: Python에서 PDF 문서에 텍스트, HTML 조각, 목록, 링크 및 사용자 지정 글꼴을 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 텍스트, 링크, HTML 및 글꼴 추가
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 텍스트를 추가하고 서식을 지정하는 방법을 설명합니다.Python 워크플로우에서 텍스트 위치 지정, 글꼴 및 스타일 설정 적용, 링크 및 목록 삽입, HTML, LaTeX 및 사용자 지정 글꼴 사용과 같은 핵심 기술을 다룹니다.
---

이 가이드는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 텍스트 내용을 추가하는 방법을 설명합니다.간단한 텍스트 부분을 특정 위치에 배치하는 것부터 스타일 지정 (글꼴, 크기, 색상, 스타일), 오른쪽에서 왼쪽 방향 (RTL) 언어 처리, 하이퍼링크 포함, 단락 레이아웃, 목록 및 투명도 효과 작업에 이르기까지 핵심 텍스트 삽입 기술을 배우게 됩니다.이 문서에서는 HTML 또는 LaTeX 조각, 사용자 지정 글꼴, 줄 간격 및 문자 간격과 같은 텍스트 서식 지정 옵션과 같은 고급 시나리오도 다룹니다.

간단한 주석을 작성하든, 풍부한 타이포그래피 레이아웃을 작성하든, 이 리소스는 Aspose.PDF 를 사용하여 PDF의 텍스트 작업을 위한 기본 구성 요소를 제공합니다.

## 기본 텍스트 삽입

.NET을 통한 파이썬용 Aspose.PDF 파일은 PDF 파일 내의 텍스트를 처리하기 위한 강력하고 유연한 API를 제공합니다.
간단한 정적 레이블, 풍부한 형식의 콘텐츠, 다국어 텍스트 또는 대화형 하이퍼링크 등 필요한 경우 툴킷을 사용하면 간결한 Python 코드로 모든 작업을 수행할 수 있습니다.

### 텍스트 추가 심플 케이스

.NET을 통한 Python용 Aspose.PDF 는 페이지의 특정 위치에 간단한 텍스트 조각을 추가하는 방법을 보여줍니다.새 PDF 문서를 만들고, 페이지를 추가하고, 지정된 좌표에 텍스트를 삽입하고, 결과 파일을 저장하는 방법을 배웁니다.

1. 새 만들기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적.
1. 용도 `document.pages.add()` 새 블랭크 생성하기 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 만들기 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 텍스트 내용과 함께.
1. 를 사용하여 텍스트 위치를 설정합니다. [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) 수업.지정한 경우 `Position`텍스트는 문서에서 왼쪽에서 오른쪽으로 위치하며 아래쪽으로 이동합니다.
1. 텍스트 모양을 사용자 지정합니다.를 통해 글꼴 크기, 색상, 글꼴 스타일 등을 설정할 수 있습니다. [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. 추가 `TextFragment` 를 사용하여 페이지의 단락 컬렉션에 `page.paragraphs.add(text_fragment)`.
1. 문서를 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

이 코드 예제는 텍스트 프래그먼트를 사용합니다.텍스트 단락을 사용하여 PDF 페이지에 텍스트를 추가할 수도 있습니다.
더**[텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)**는 단일 텍스트입니다.개별적으로 배치하고, 스타일을 지정하고, 배치할 수 있는 하나의 텍스트 문자열을 나타냅니다.작고 간단한 텍스트 내용을 추가해야 하는 경우에 적합합니다.

더**[텍스트 단락](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)**는 텍스트 조각 그룹입니다.여러 텍스트 줄을 추가할 수 있습니다.텍스트 단락은 하나 이상의 TextFragment 개체의 컨테이너 또는 컬렉션입니다.예를 들어 여러 줄, 단어 또는 서식이 지정된 요소로 구성된 텍스트 블록을 만드는 등 여러 조각을 그룹화해야 하는 경우에 적합합니다.
또한 TextParage는 페이지의 텍스트 정렬, 줄 간격 및 자동 레이아웃을 관리합니다.빨간색 선은 TextParage에서만 사용할 수 있습니다.

텍스트 작업에 대한 자세한 내용은 을 참조하십시오. [PDF 내 텍스트 서식](/pdf/ko/python-net/text-formatting-inside-pdf/) 과 [PDF에서 텍스트 검색 및 가져오기](/pdf/ko/python-net/search-and-get-text-from-pdf/).

### 텍스트 단락을 사용하여 텍스트 추가

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 사용하여 텍스트 단락을 추가할 수 있습니다. [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) 과 [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 포장 옵션 포함.

1. 새 만들기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 그리고 공백 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 를 사용하여 `document.pages.add()`.
1. 파일에서 텍스트를 읽거나 기본 텍스트를 사용합니다.
1. 만들기 [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) 레이아웃 및 줄 바꿈 제어를 사용하여 단락 수준 콘텐츠를 추가할 수 있습니다.
1. 만들기 [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 랩 모드를 설정합니다 (예제에서는 사용). `DISCRETIONARY_HYPHENATION`).
1. 만들기 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)스타일을 적용하고 단락에 단편을 추가합니다.
1. 를 사용하여 페이지에 단락을 추가합니다. `TextBuilder`.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![텍스트 단락을 사용하여 텍스트 추가](text_paragraph.png)

### 들여쓰기가 있는 단락을 PDF에 추가

다음 코드 스니펫은 새 PDF 문서를 만들고 들여쓰기 스타일이 다른 두 단락의 텍스트를 추가하는 방법을 보여줍니다.

- 첫 번째 단락은 첫 줄 들여쓰기를 보여줍니다 (첫 줄만 들여쓰기).

- 두 번째 단락은 다음 줄 들여쓰기를 보여줍니다 (첫 번째 줄 이후의 모든 줄은 들여쓰기).

Aspose.PDF 의 '텍스트 단락', '텍스트빌더', '텍스트프래그먼트' 클래스를 사용하여 레이아웃과 서식을 정밀하게 제어합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 TextFragment, TextParrame 및 TextBuilder 클래스를 사용하여 PDF 문서에 여러 줄 텍스트를 삽입할 수 있습니다.

1. 새 문서 만들기
1. 줄 바꿈 문자를 포함하는 TextFragment를 정의합니다.
1. 텍스트 스타일을 설정합니다.
1. 단락에 단편을 추가합니다.
1. 단락을 배치합니다.
1. 페이지에 단락을 렌더링합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### PDF에서 줄 바꿈 및 로그 알림 확인

여러 텍스트 조각을 포함하는 PDF 문서를 만들고 Aspose.PDF 알림 로깅을 활성화하여 렌더링 중에 줄 바꿈 및 텍스트 줄 바꿈과 같은 레이아웃 이벤트를 모니터링하는 방법을 보여줍니다.

1. 새 PDF 문서 만들기
1. 알림 로깅을 활성화합니다.
1. 문서.pages.add () 를 사용하여 첫 번째 페이지를 만드십시오.
1. 여러 텍스트 조각을 추가합니다.
1. page.pagphs.add (텍스트) 를 사용하여 각 텍스트 조각을 렌더링합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### PDF에서 동적으로 텍스트 너비 측정

.NET을 통해 Python용 Aspose.PDF 파일을 사용하여 특정 글꼴의 문자 및 문자열 너비를 동적으로 측정합니다.'Font.Measure_String () '과 'TextState.Measure_String () '메서드를 사용하여 측정된 문자열 너비가 일관되고 정확한지 확인합니다.

1. 저장소에서 아리알 글꼴 객체를 검색하려면 'FontRepository.find_Font () '을 사용하십시오.
1. TextState 객체를 생성하여 글꼴 속성을 관리합니다.
1. 개별 문자를 측정합니다.
1. 'A'와 'z' 사이의 모든 문자에 대해 두 방법의 결과를 비교합니다.
1. 두 측정 방법 모두 동일한 결과를 산출하는지 확인하십시오.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### 하이퍼링크가 있는 텍스트 추가

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF의 텍스트에 클릭 가능한 하이퍼링크를 추가할 수 있습니다.라이브러리는 단일 TextFragment 내에 여러 텍스트 세그먼트를 추가하고 특정 세그먼트에 하이퍼링크를 적용하고 텍스트 세그먼트를 개별적으로 스타일 (예: 색상, 기울임꼴 글꼴) 하는 방법을 보여줍니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. 텍스트 조각 만들기.
1. 여러 개의 텍스트세그먼트 객체를 추가합니다.각 세그먼트에는 고유한 내용과 스타일이 있을 수 있습니다.일반 텍스트 또는 하이퍼링크 텍스트를 예로 들 수 있습니다.
1. 세그먼트에 하이퍼링크를 적용합니다.원하는 URL을 사용하여 웹 하이퍼링크 객체를 만듭니다.
1. 세그먼트에 스타일을 지정합니다.text_state를 사용하여 색상, 글꼴 스타일, 크기 등을 사용자 지정합니다.
1. 'page.clarphs.add () '를 사용하여 페이지에 프래그먼트를 추가합니다.
1. PDF를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![[샘플 텍스트 조각] 과 [텍스트 세그먼트 1], [Link to Aspose] (링크) 라는 파란색 하이퍼링크된 텍스트가 포함된 혼합 내용을 보여 주는 텍스트 단편이 PDF에 표시됩니다. https://products.aspose.com/pdf) 를 사용하고 일반 검은색 텍스트 서식의 하이퍼링크 없이 TextSegment로 끝남](hyperlink_text.png)

### PDF 문서에 오른쪽에서 왼쪽 (RTL) 텍스트 추가

RTL (오른쪽에서 왼쪽으로) 은 텍스트 작성 방향을 나타내는 속성으로, 텍스트는 오른쪽에서 왼쪽으로 쓰여집니다.
.NET을 통한 Python용 Aspose.PDF. 에서는 아랍어나 히브리어와 같은 오른쪽에서 왼쪽 방향 (RTL) 텍스트를 PDF 문서에 추가하는 방법을 보여줍니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. RTL 콘텐츠로 텍스트 프래그먼트를 생성합니다.아랍어, 히브리어 또는 기타 RTL 언어 텍스트를 프래그먼트 콘텐츠로 삽입합니다.
글꼴 및 스타일을 설정합니다.RTL 스크립트를 지원하는 글꼴을 선택합니다 (예: Tahoma, Arial 유니코드 MS).필요에 따라 글꼴_크기 및 전경_색상을 설정합니다.
1. '텍스트_조각.수평_정렬'을 사용하여 가로 정렬을 오른쪽으로 설정합니다.
1. 페이지에 텍스트 조각을 추가합니다.
1. PDF 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![오른쪽에서 왼쪽 텍스트](rtl_text.png)

## 텍스트 스타일링

### 글꼴 스타일링으로 텍스트 추가

이것은 텍스트 스타일 지정, 글꼴 사용자 지정 및 혼합 형식 텍스트 (아래 첨자 텍스트 세그먼트 사용) 를 보여주는 고급 예제입니다.Aspose.PDF 글꼴군, 크기, 색상, 굵게, 기울임꼴, 밑줄과 같은 글꼴 속성을 텍스트 부분에 적용하는 방법을 설명합니다.
또한 이 코드 스니펫은 단일 프래그먼트 내에서 여러 텍스트 세그먼트를 사용하여 복잡한 텍스트 표현식 (예: 수식이나 과학 표기법에 자주 필요한 아래 첨자 또는 위 첨자 문자 포함) 을 만드는 방법을 보여줍니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. 단순한 스타일 텍스트를 위한 TextFragment를 만드세요.
1. 텍스트 내용을 정의합니다.
1. 위치 (x, y) 좌표를 사용하여 위치를 설정합니다.
1. 글꼴, 글꼴_크기, 전경_색상, 글꼴_스타일, 밑줄과 같은 '텍스트_상태 속성'을 통해 스타일을 적용합니다.
1. 여러 TextSegment 객체로 복잡한 표현식을 만듭니다.각 TextSegment는 고유한 스타일을 가질 수 있는 텍스트의 일부를 나타냅니다.이를 통해 수학 공식 또는 화학 공식과 같은 표현식을 작성할 수 있습니다.
1. 여러 개의 텍스트스테이트 객체를 정의합니다.하나는 기본 텍스트 (텍스트_상태_문자) 용입니다.다른 하나는 아래 첨자 또는 위 첨자 텍스트 (text_state_index) 용입니다.
1. 텍스트 세그먼트를 결합합니다.'segments.append () '를 사용하여 각 세그먼트를 '텍스트 프래그먼트'에 추가합니다.
1. 페이지에 두 텍스트 개체를 모두 추가합니다.'page.단락s.add () '를 사용하여 문서에 배치하십시오.
1. 최종 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Hello, Aspose! 라는 텍스트가 포함된 파란색 기울임꼴 Arial 글꼴로 표시된 텍스트 조각그 뒤에는 S = 아래 첨자 2n +, 아래 첨자 2n+1+, 아래 첨자 2n+2를 나타내는 수학 공식이 나옵니다 (주 텍스트는 파란색, 빨간색 아래 첨자 서식은 빨간색](styled_text.png)

## 텍스트 추가 (투명)

Python용 Aspose.PDF 를 사용하여 PDF 문서에 반투명 모양과 텍스트를 추가합니다.
부분적으로 불투명도가 있는 색상이 지정된 사각형을 만들고 투명한 전경색으로 TextFragment를 오버레이합니다.

1. Document 객체를 초기화하고 도면 내용을 위한 빈 페이지를 추가합니다.
1. 'ap.Drawing.Graph'를 사용하여 도형을 그릴 수 있는 캔버스를 만드세요.
1. 반투명으로 채워진 사각형을 추가합니다.
1. 캔버스 위치 이동을 방지합니다.
1. 페이지에 캔버스를 추가합니다.페이지 단락 컬렉션에 그래픽 도형을 삽입합니다.
1. 투명한 텍스트 조각을 만드세요.
1. 페이지 단락 컬렉션에 텍스트 조각을 삽입합니다.
1. PDF 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### PDF에 보이지 않는 텍스트 추가

이 예제에서는 보이는 텍스트와 보이지 않는 텍스트를 모두 포함하는 PDF 문서를 만드는 방법을 보여줍니다.보이지 않는 텍스트는 문서 구조의 일부로 남아 있지만 보이지 않게 숨겨지므로 레이아웃에 영향을 주지 않고 메타데이터, 접근성 태그 또는 검색 가능한 콘텐츠를 포함하는 데 유용합니다.

1. PDF 문서 및 페이지 작성
1. 반복되는 가시적 내용이 포함된 텍스트 조각을 만드세요.
1. 두 번째 텍스트 조각을 추가하고 보이지 않는 것으로 표시합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### PDF에 테두리 스타일이 적용된 텍스트 추가

Aspose.PDF 라이브러리는 테두리가 보이는 스타일이 지정된 텍스트 부분을 포함하는 PDF 문서를 만드는 방법을 보여줍니다.이 방법은 텍스트 사각형 주위에 배경색과 전경색, 글꼴 설정, 획 (테두리) 을 적용하여 시각적 강조를 향상시킵니다.

1. PDF 문서 및 페이지 만들기.
1. 텍스트 조각 만들기 및 배치메시지와 함께 텍스트 조각을 추가하고 위치를 설정합니다.
1. 텍스트 스타일 적용.글꼴을 타임즈 뉴 로먼, 크기 12로 설정합니다.밝은 회색 배경과 빨간색 전경색 (텍스트) 색상을 적용합니다.
1. 테두리 스타일을 설정합니다.
1. 페이지에 텍스트 추가.TextBuilder를 사용하여 스타일이 지정된 텍스트를 페이지에 추가합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

취소선 (취소선) 서식을 PDF 문서의 텍스트 부분에 추가합니다.취소선 텍스트는 주석이 달린 문서에서 삭제, 수정 또는 강조를 나타내는 데 유용합니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. 텍스트 조각 만들기 및 스타일 지정
1. 색상 및 스트라이크아웃 서식을 적용합니다.배경을 밝은 회색으로, 텍스트 색상을 빨간색으로 설정하고 취소선을 활성화합니다.
1. 텍스트를 배치합니다.
1. 'TextBuilder'를 사용하여 스타일이 지정된 텍스트를 페이지에 추가합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

### PDF의 텍스트에 축 그라데이션 적용

.NET을 통한 Python용 Aspose.PDF 는 PDF 문서의 텍스트에 선형 그래디언트 효과를 적용하는 방법을 보여줍니다.축 방향 그라디언트는 텍스트 전체에서 빨간색에서 파란색으로 부드럽게 전환되어 시각적으로 눈에 띄는 제목을 만듭니다.이 기법은 PDF 문서 레이아웃의 양식화된 제목, 브랜딩 또는 장식 요소에 적합합니다.

1. 새 문서를 초기화하고 빈 페이지를 추가합니다.
1. 텍스트 조각 만들기 및 스타일 지정제목 추가, 위치, 글꼴, 크기 설정
1. '그라디언트 축 쉐이딩'을 사용하여 축 그라데이션 쉐이딩을 적용합니다.빨간색에서 파란색으로의 그라디언트 축 쉐이딩을 사용하여 전경색을 설정합니다.
1. 밑줄 스타일 추가
1. 스타일이 지정된 텍스트 부분을 페이지에 삽입합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

### PDF의 텍스트에 방사형 그레이디언트 적용

방사형 그래디언트는 텍스트 중앙에서 바깥쪽으로 퍼지는 원형 색상 전환을 만들어 제목, 머리글 또는 장식 요소에 시각적으로 동적인 스타일 지정 옵션을 제공합니다.

1. 새 문서를 초기화하고 빈 페이지를 추가합니다.
1. 텍스트 조각 만들기 및 스타일 지정제목 추가, 위치, 글꼴, 크기 설정
1. '그라디언트 래디얼 쉐이딩'으로 레이디얼 그레이디언트를 적용합니다.빨간색에서 파란색으로의 그라디언트 래디얼쉐이딩을 사용하여 전경색을 설정합니다.
1. 밑줄 스타일 추가
1. 스타일이 지정된 텍스트 부분을 페이지에 삽입합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

![방사형 그라데이션 쉐이딩 적용](gradient_radial_shading.png)

## HTML 및 라텍스 프래그먼트

### PDF 문서에 HTML 텍스트 추가

.NET 라이브러리를 통한 파이썬용 Aspose.PDF 라이브러리를 사용하면 HTMLFragment 클래스를 사용하여 HTML 형식의 콘텐츠를 PDF 문서에 삽입할 수 있습니다.HTML 태그를 사용하면 스타일이 지정되거나 구조화된 텍스트 또는 수식과 유사한 텍스트를 PDF에서 직접 렌더링할 수 있습니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. HTMLFragment 클래스의 인스턴스를 만들고 HTML 문자열을 매개 변수로 전달합니다.
1. HTML 내용을 삽입하려면 'page.clarphs.add () '를 사용하여 페이지에 프래그먼트를 추가합니다.
1. PDF를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![PDF 문서에 HTML 텍스트 추가](html_fragment.png)

### 다양한 서식의 스타일이 적용된 HTML 부분을 PDF 문서에 추가

HTML 태그를 사용하여 HTML 조각을 정의하고 텍스트 스타일을 직접 설정할 수 있습니다.스타일이 적용된 HTML 콘텐츠를 PDF 문서에 포함합니다.이 코드 스니펫은 새 PDF 파일을 만들고, 페이지를 추가하고, 다양한 서식 요소 (제목, 단락, 링크, 인라인 스타일) 가 포함된 HTML 부분을 삽입하고, 결과를 지정된 경로에 저장합니다.

1. PDF를 나타내는 새 문서 객체를 초기화합니다.
1. HTML 내용을 배치할 문서에 빈 페이지를 추가합니다.
1. HTML 콘텐츠를 준비합니다.HTML 문자열에는 h1 제목, 굵게, 기울임꼴, 밑줄이 그어진 텍스트가 있는 녹색 단락, 글꼴 크기가 커진 웹 사이트로 연결되는 하이퍼링크가 포함됩니다.
1. HTML 프래그먼트를 생성합니다.HTML 문자열을 HTMLFragment 객체로 래핑합니다.
1. 페이지에 HTML을 삽입합니다.페이지의 단락 컬렉션에 HTML 부분을 추가하여 HTML을 기본 PDF 내용으로 렌더링합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![PDF 문서에 HTML 콘텐츠 추가](html_content.png)

### 텍스트 상태가 오버라이드된 HTML 프래그먼트 추가

이전 예제에서 살펴본 것처럼 HTML 코드에서 직접 스타일을 설정할 수 있습니다.여기에는 장점도 있지만 몇 가지 단점도 있습니다.고객의 HTML로 작업하면서 출력의 모양을 통일하려고 한다고 가정해 보겠습니다.
이 경우 다음 예와 같이 자체 TextState를 사용하여 고객의 스타일을 재정의할 수 있습니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. HTML 콘텐츠를 준비합니다.HTML 문자열에는 Verdana 글꼴이 있는 h1 제목, 굵게, 기울임꼴, 밑줄이 그어진 텍스트가 있는 녹색 단락, 글꼴 크기가 더 큰 웹 사이트로 연결되는 하이퍼링크가 포함됩니다.
1. HTML 프래그먼트를 생성합니다.HTML 문자열을 HTMLFragment 객체로 래핑합니다.
1. 텍스트 서식을 재정의합니다.TextState 객체를 만들고 글꼴, 글꼴 크기 및 텍스트 색상을 설정합니다.
1. 페이지의 단락 컬렉션에 HTML 부분을 추가합니다.
1. 문서를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![HTML 프래그먼트 오버라이드 텍스트 상태 추가](html_override.png)

### PDF 문서에 라텍스 텍스트 추가

.NET을 통해 파이썬용 Aspose.PDF 의 TextFragment 클래스를 사용하여 라텍스 형식의 수학 표현식을 PDF 문서에 추가합니다.
LaTeX는 과학 및 수학 문서 작성에 널리 사용되는 강력한 조판 시스템입니다.TexFragment를 사용하면 PDF 페이지 내에서 LaTeX 수학 표기법과 기호를 직접 렌더링할 수 있습니다.

1. '문서 () '를 사용하여 새 문서와 페이지를 만들고, 'document.pages.add () '를 사용하여 빈 페이지를 추가합니다.
1. TexFragment 클래스를 사용하여 LaTeX 구문을 직접 렌더링할 수 있습니다.
1. 'page.clarphs.add () '를 사용하여 PDF 레이아웃에 LaTeX 콘텐츠를 추가합니다.
1. PDF를 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![LaTeX 수식을 나타내는 복잡한 수학 표현식으로 (a+b) 에는 중괄호 표기법, 전체 표현식 (a+b) · (c+d) 에는 밑중괄호 표기법을 사용하며 텍스트의 예시로 레이블이 지정되어 42와 같음을 나타내는 PDF에 표시된 복잡한 수학 표현식입니다.이 공식은 LaTeX 렌더링의 전형적인 전형적인 적절한 간격과 대괄호 스타일을 사용한 고급 수학 조판을 보여줍니다.](latex_fragment.png)

## 사용자 지정 글꼴

### 파일에서 사용자 지정 글꼴 사용

이 예제에서는.NET을 통해 파이썬용 Aspose.PDF 사용자 지정 OpenType 글꼴을 사용하여 PDF 파일에 텍스트를 추가할 수 있습니다.새 PDF 문서를 만들고, 페이지에 텍스트를 정확하게 배치하고, 글꼴 유형, 크기, 색상, 기울임꼴 스타일과 같은 사용자 지정 서식을 적용하는 방법을 보여줍니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. PDF에 추가할 텍스트 내용을 정의합니다.
1. 텍스트의 위치를 설정합니다.
1. 페이지에 텍스트 조각을 추가합니다.
1. PDF 문서를 저장합니다.

이 기능은 OTF뿐만 아니라 TTF 글꼴에서도 작동합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Hello, Aspose! 를 보여주는 PDF 문서에 표시된 텍스트 조각파란색 기울임꼴 BriosoPro 글꼴로 렌더링되어 PDF 텍스트 서식 내에서 사용자 지정 OpenType 글꼴 통합 및 스타일링 기능을 보여줍니다.](custom_font.png)

### 스트림에서 사용자 지정 글꼴 사용

이 코드 스니펫은 .NET을 통해 Python용 Aspose.PDF 및 사용자 지정 임베디드 OpenType (OTF) 글꼴을 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.글꼴 파일을 스트림으로 열고, PDF에 포함하여 여러 시스템에서 글꼴을 사용할 수 있도록 하고, 글꼴 크기, 색상, 기울임꼴 스타일과 같은 텍스트 서식을 적용하는 방법을 보여줍니다.이 방법은 글꼴이 설치되어 있지 않은 장치에서 공유하거나 볼 때에도 타이포그래피가 보존되는 시각적으로 일관된 PDF를 만드는 데 적합합니다.

1. 글꼴 파일을 바이너리 스트림으로 로드합니다.
1. '글꼴 저장소.open_Font'를 사용하여 글꼴을 열고 포함합니다.
1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 다음을 사용하여 스타일이 지정된 텍스트 부분 추가
    - 사용자 정의 글꼴이 내장되어 있습니다.
    - 이탤릭 스타일과 블루 컬러.
    - 특정 글꼴 크기 및 위치
1. 최종 문서를 지정된 출력 경로에 저장합니다.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

글꼴을 포함하면 플랫폼 전반에서 일관된 렌더링이 보장되므로 이 접근 방식은 브랜딩, 디자인 충실도 및 다국어 지원에 이상적입니다.

## 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [파이썬에서 PDF 텍스트 포맷 지정하기](/pdf/ko/python-net/text-formatting-inside-pdf/)
- [파이썬을 통해 PDF의 텍스트 바꾸기](/pdf/ko/python-net/replace-text-in-pdf/)
- [파이썬에서 PDF 텍스트 검색 및 추출](/pdf/ko/python-net/search-and-get-text-from-pdf/)