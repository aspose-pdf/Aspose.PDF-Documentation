---
title: 파이썬에서 PDF 텍스트 포맷 지정하기
linktitle: PDF 내 텍스트 서식
type: docs
weight: 70
url: /ko/python-net/text-formatting-inside-pdf/
description: 간격, 테두리, 들여쓰기 및 스타일 지정 옵션을 사용하여 Python에서 PDF 문서 내의 텍스트 서식을 지정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일 내의 텍스트 서식 지정 및 스타일 지정
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 텍스트 서식을 지정하는 방법을 설명합니다.Python에서 간격, 들여쓰기, 테두리, 밑줄, 취소선 효과 및 기타 텍스트 스타일 지정 옵션을 제어하는 방법을 알아봅니다.
---

## 줄 및 문자 간격

### 줄 간격 사용

#### Python에서 사용자 지정 줄 간격으로 텍스트 서식을 지정하는 방법 - 간단한 사례

Aspose.PDF for Python은 줄 간격 조정을 통해 텍스트 레이아웃과 가독성을 제어하는 간단한 접근 방식을 제공합니다.

코드 스니펫은 PDF 문서에서 줄 간격을 제어하는 방법을 보여줍니다.파일에서 텍스트를 읽거나 대체 메시지를 사용하고, 사용자 지정 글꼴 크기 및 줄 간격을 적용하고, 서식이 지정된 텍스트를 PDF의 새 페이지에 추가합니다.

1. 새 PDF 문서 만들기
1. 소스 텍스트를 로드합니다.
1. TextFragment 객체를 초기화하고 로드된 텍스트를 해당 객체에 할당합니다.
1. 텍스트의 글꼴 및 간격 속성을 설정합니다.이러한 값은 텍스트 줄이 얼마나 세게 또는 느슨하게 표시되는지를 결정합니다.
    - 글자 크기: 12포인트
    - 줄 간격: 16포인트
1. 서식이 지정된 텍스트 부분을 페이지의 단락 컬렉션에 삽입합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Python에서 사용자 지정 줄 간격으로 텍스트 서식을 지정하는 방법 - 특정 사례

사용자 정의 TTF (TrueType 글꼴) 를 사용하여 PDF 문서에서 다양한 줄 간격 모드를 적용하는 방법을 확인해 보겠습니다.
파일에서 텍스트를 로드하고, 특정 글꼴을 포함하고, 매번 다른 줄 간격 모드를 사용하여 동일한 텍스트를 PDF 페이지에 두 번 렌더링합니다.

- FONT_SIZE 모드: 줄 간격은 글꼴 크기와 같습니다.
- FULL_SIZE 모드: 줄 간격은 오름차순 및 내림차순을 포함하여 글꼴의 전체 높이를 나타냅니다.

이 예제에서는 선택한 모드에 따라 줄 간격 동작이 어떻게 달라지는지 보여줍니다.

1. 새 PDF 문서 만들기
1. 사용자 정의 글꼴 파일과 텍스트 소스 파일의 경로를 지정합니다.
1. 텍스트 콘텐츠를 로드합니다.
1. 사용자 지정 글꼴을 엽니다.
1. 첫 번째 텍스트 프래그먼트를 만들고 구성합니다 (FONT_SIZE 모드).줄 간격을 'TextFormattingOptions.LinespacingMode.Font_Size'로 설정합니다. 즉, 줄 간격이 글꼴 크기와 같습니다.
1. 두 번째 텍스트 조각을 만들고 구성합니다 (FULL_SIZE 모드).줄 간격을 'TextFormattingOptions.LinespacingMode.Full_Size'로 설정합니다. 이 설정은 글꼴의 전체 높이를 사용합니다.
1. 두 텍스트 조각을 동일한 PDF 페이지에 추가합니다.
1. 완료된 문서를 지정된 출력 위치에 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![사용자 지정 줄 간격으로 텍스트를 표시하는 PDF 문서로서, 줄 사이의 16포인트 간격을 보여 주어 가독성과 텍스트 레이아웃 서식을 개선합니다.](line_spacing.png)

### 문자 간격 사용

#### TextFragment 클래스를 사용하여 PDF 텍스트의 문자 간격을 제어하는 방법

문자 간격은 텍스트 줄의 개별 문자 간 거리를 결정하므로 텍스트 모양을 미세 조정하거나 특정 타이포그래피 효과를 내는 데 유용합니다.

1. 새 Document 객체를 초기화하고 텍스트를 배치하기 위한 빈 페이지를 추가합니다.
1. 프래그먼트 생성기를 정의합니다.도우미 함수 make_fragment (간격) 을 구현합니다.
    - 샘플 텍스트로 텍스트 프래그먼트를 생성합니다.
    - 글꼴을 설정합니다.
1. 간격 값이 다른 텍스트 조각을 추가합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![동일한 텍스트를 3줄로 표시하는 PDF 문서 샘플 텍스트는 문자 간격이 위에서 아래로 갈수록 점점 좁아지고 있습니다. 첫 줄은 글자 사이의 간격이 넓고, 가운데 줄은 중간 줄의 간격이 적당하며, 맨 아래 줄은 문자 간격이 가장 가까워 PDF 텍스트 형식에서 서로 다른 문자 간격 값의 시각적 효과를 보여줍니다.](character_spacing_simple.png)

#### 텍스트 단락 및 텍스트 빌더를 사용하여 PDF 텍스트의 문자 간격을 제어하는 방법

Aspose.PDF 를 사용하면 텍스트 단락 및 텍스트 빌더를 사용하여 PDF 문서에 텍스트를 추가할 때 사용자 지정 문자 간격을 적용할 수 있습니다.
페이지의 특정 영역을 정의하고, 텍스트 줄 바꿈을 구성하고, 문자 사이의 간격을 조정한 텍스트 조각을 렌더링합니다.

TextParamearage를 사용하면 구조화된 텍스트 블록 또는 여러 열로 구성된 텍스트 블록을 만들 때와 같이 텍스트 배치 및 레이아웃을 정밀하게 제어해야 하는 경우에 적합합니다.

1. 새 PDF 문서 만들기
1. 페이지의 텍스트빌더 인스턴스를 초기화합니다.
1. 텍스트 단락을 만들고 구성합니다.
    - 자동 줄 바꿈 모드를 '텍스트 서식 지정 옵션.워드 랩 모드.by_words'로 설정합니다.
1. 사용자 지정 문자 간격을 사용하여 TextFragment를 생성합니다.
    - 새 TextFragment를 만들고 해당 텍스트를 설정합니다 (예: “문자 간격이 있는 샘플 텍스트”).
    - Arial 및 글꼴 크기 14pt와 같은 글꼴 속성을 지정합니다.
    - 문자 간격 적용 = 2.0, 문자 사이의 간격을 늘립니다.
1. 텍스트 단락에 텍스트 조각을 추가합니다.
1. 페이지에 텍스트 단락을 추가합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

## 목록 생성

PDF 파일로 작업할 때 목록과 같은 구조화된 정보 (글머리 기호, 번호 지정, HTML 또는 LaTeX 형식 지정) 를 표시해야 할 수 있습니다.
.NET을 통한 Python용 Aspose.PDF 는 PDF 문서 내에서 직접 목록을 만들고 형식을 지정할 수 있는 몇 가지 유연한 방법을 제공하므로 레이아웃, 글꼴 및 스타일을 완벽하게 제어할 수 있습니다.

이 문서에서는 일반 텍스트 서식에서 고급 HTML 및 LaTeX 렌더링에 이르기까지 PDF로 목록을 만드는 다양한 방법을 보여줍니다.정밀한 프로그래밍 방식 제어를 선호하든 편리한 마크업 기반 스타일 지정을 선호하든 관계없이 각 방법은 특정 사용 사례에 적합합니다.

이 문서를 마치면 다음과 같은 방법을 알게 될 것입니다.

- 텍스트 단락 및 텍스트 빌더를 사용하여 사용자 지정 글머리 기호 및 번호 목록을 만들 수 있습니다.

- HTML 프래그먼트 (HTML프래그먼트) 를 사용하여 쉽게 렌더링할 수 있습니다.<ul>'및'<ol>'목록은 PDF로 표시됩니다.

- 수학적 또는 과학적 목록 형식 지정을 위해 LaTeX 프래그먼트 (TexFragment) 를 활용하세요.

- 페이지 내 텍스트 줄 바꿈, 글꼴 스타일 및 레이아웃 위치를 제어할 수 있습니다.

- 수동 목록 구성과 마크업 기반 접근 방식의 차이점을 이해하세요.

### 번호가 매겨진 목록 만들기

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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

### 글머리 기호 목록 만들기

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### 번호가 매겨진 목록 HTML 버전 만들기

HTML 조각을 사용하여 PDF 문서에 번호가 매겨진 (정렬된) 목록을 만듭니다.파이썬 문자열 목록을 HTML 정렬 목록 요소로 변환하고 이를 PDF 페이지에 HTMLFragment로 삽입합니다.

HTML 조각을 사용하면 번호 목록, 굵게, 기울임꼴 등과 같은 HTML 기반 서식 지정 기능을 PDF에 직접 통합할 수 있습니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 목록 항목을 준비합니다.
1. 목록을 HTML 순서가 지정된 목록으로 변환합니다.
    - 번호가 매겨진 목록에 HTML 정렬 목록 태그를 사용합니다.
    - 목록 이해를 사용하여 각 항목을 목록 항목 태그로 래핑합니다.
1. HTML 문자열을 PDF 페이지에 추가할 수 있는 HTMLFragment 객체로 변환합니다.
1. 페이지의 단락 컬렉션에 HTML 프래그먼트를 삽입합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![자동으로 번호가 매겨진 항목 4개를 보여 주는 PDF 문서에 표시된 번호 목록: 1.목록의 첫 번째 항목, 2.줄 바꿈 동작을 설명하는 텍스트가 더 있는 두 번째 항목, 3.세 번째 항목, 그리고 4.네 번째 항목.이 목록은 적절한 숫자 순서, 들여쓰기 및 항목 간 간격을 사용하여 PDF 구조 내에서 HTML 형식의 순서가 지정된 목록을 렌더링하는 방법을 보여줍니다.](numbered_list_html.png)

### 글머리 기호 목록 HTML 버전 만들기

우리 라이브러리는 HTML 조각을 사용하여 PDF 문서에서 글머리 기호 (정렬되지 않은) 목록을 만드는 방법을 보여줍니다.파이썬 문자열 목록을 HTML 정렬되지 않은 목록 요소로 변환하여 PDF 페이지에 HTMLFragment로 삽입합니다.HTML 조각을 사용하면 목록, 굵게, 기울임꼴 등의 HTML 서식 지정 기능을 PDF에서 직접 활용할 수 있습니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 목록 항목을 준비합니다.
1. 목록을 순서가 지정되지 않은 HTML 목록으로 변환합니다.
    - 순서가 지정되지 않은 (글머리 기호) 목록에는 HTML 정렬되지 않은 목록 태그를 사용하십시오.
    - 목록 이해를 사용하여 각 항목을 목록 항목 태그로 래핑합니다.
1. HTML 프래그먼트를 생성합니다.HTML 문자열을 PDF 페이지에 추가할 수 있는 HTMLFragment 객체로 변환합니다.
1. 페이지의 단락 컬렉션에 HTML 프래그먼트를 삽입합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![목록의 첫 번째 항목, 줄 바꿈 동작을 설명하는 텍스트가 더 많은 두 번째 항목, 세 번째 항목, 네 번째 항목 등 네 가지 항목을 보여 주는 글머리 기호 목록이 PDF 문서에 표시됩니다.각 항목 앞에는 표준 글머리 기호가 있으며 적절한 들여쓰기와 간격을 두고 PDF 구조 내에서 HTML 형식의 목록 렌더링을 보여 줍니다.](bullet_list_html.png)

### 글머리 기호 목록 만들기 LaTeX 버전

LaTeX 조각 (TexFragment) 을 사용하여 PDF에서 글머리 기호 (정렬되지 않은) 목록을 만듭니다.파이썬 문자열 목록을 LaTeX 항목화 환경으로 변환하여 PDF 페이지에 삽입합니다.수학 공식, 기호 또는 구조화된 목록을 정확한 서식으로 렌더링하려는 경우 LaTeX 조각을 사용하는 것이 이상적입니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. LaTeX 항목화 환경에서 글머리 기호가 될 문자열의 Python 목록을 정의합니다.
1. 목록을 LaTeX 항목화 환경으로 변환하십시오.
    - 항목을\ begin {itemize} 및\ end {itemize} 로 래핑합니다.
    - 각 항목에는 목록 이해를 사용하여\ item 접두사가 붙습니다.
1. LaTeX 문자열을 PDF에서 렌더링할 수 있는 TexFragment 객체로 변환합니다.
1. 페이지에 LaTeX 프래그먼트를 추가합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
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

![Latex로 렌더링된 텍스트 서식을 보여 주는 PDF에 표시된 글머리 기호 목록은 쉽게 만들 수 있습니다. 그 다음에는 글머리 기호가 있는 네 개의 항목 (첫 번째 항목, 줄 바꿈 동작을 설명하는 텍스트가 더 많은 두 번째 항목, 세 번째 항목, 네 번째 항목) 이 이어집니다.이 목록은 깔끔한 PDF 문서 레이아웃 내에서 적절한 글머리 기호 서식, 일정한 간격 및 텍스트 줄 바꿈 기능을 갖춘 전문적인 LaTeX 조판을 보여줍니다.](bullet_list_latex.png)

### 번호가 매겨진 목록 LaTeX 버전 만들기

LaTeX 프래그먼트 (TexFragment) 를 사용하여 PDF에서 번호가 매겨진 (정렬된) 목록을 만듭니다.파이썬 문자열 목록을 LaTeX 열거 환경으로 변환하여 PDF 페이지에 삽입합니다.LaTeX 프래그먼트는 PDF에 정확한 서식 지정, 구조화된 목록 또는 수학 표기법을 사용하려는 경우에 이상적입니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. LaTeX 열거 환경에서 번호가 매겨진 항목이 될 문자열의 Python 목록을 정의합니다.
1. 목록을 LaTeX 열거 환경으로 변환합니다.
1. LaTeX 문자열을 PDF에서 렌더링할 수 있는 TexFragment 객체로 변환합니다.
1. 페이지에 LaTeX 프래그먼트를 추가합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
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

![항목 1과 함께 LaTex로 렌더링된 서식을 보여 주는 PDF에 표시된 번호 목록.첫 번째 항목, 2.두 번째 항목에는 줄 바꿈 동작을 설명하는 텍스트가 더 있습니다. 3.세 번째 항목, 그리고 4.네 번째 항목, 앞에 텍스트가 있습니다. 목록은 쉽게 만들 수 있습니다.](numbered_list_latex.png)

## 각주 및 미주

### 각주 추가

각주는 관련 텍스트 옆에 연속적인 위 첨자 번호를 배치하여 문서 본문 내의 메모를 참조하는 데 사용됩니다.이 번호는 일반적으로 같은 페이지 하단에 들여쓰기되어 배치되는 상세 메모에 해당하며, 추가 맥락, 인용 또는 해설을 제공합니다.

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서의 텍스트 단편에 각주를 추가합니다.각주는 주요 내용을 복잡하게 만들지 않으면서 보충 정보, 인용 또는 설명을 제공하는 데 유용합니다.이 방법을 사용하면 각주를 시각적으로나 구조적으로 PDF 레이아웃에 통합할 수 있습니다.

1. 새 문서 만들기.
1. 주요 내용이 포함된 텍스트 조각을 만드세요.
1. 인라인 텍스트 추가.같은 단락에서 이어지는 또 다른 TextFragment를 만드세요.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### PDF에 사용자 지정 스타일을 사용하여 각주 추가

1. 새 PDF 문서를 초기화하고 빈 페이지를 추가합니다.
1. 메인 텍스트 프래그먼트 만들기.
1. 각주 작성 및 스타일 지정 (글꼴, 크기, 색상, 스타일).
1. 각주와 함께 스타일이 지정된 텍스트 부분을 페이지에 삽입합니다.
1. 각주 없이 다른 텍스트 조각을 추가합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

### PDF에 사용자 지정 기호가 있는 각주 추가

.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 텍스트 조각에 각주를 추가하고 각주 표시자 기호를 사용자 지정할 수 있습니다.

1. PDF 문서 및 페이지 작성
1. 사용자 지정 각주 기호로 첫 번째 텍스트 조각을 추가합니다.
1. 각주 없이 단락을 이어주는 다른 텍스트 조각을 추가합니다.
1. 기본 각주와 함께 두 번째 텍스트 조각을 추가합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

### PDF에 사용자 지정 선 스타일로 각주 추가

Python 라이브러리를 사용하여 PDF 문서에서 각주 줄의 시각적 모양을 사용자 지정합니다.각주 줄을 사용자 정의하면 시각적 명확성이 향상되고 보고서, 학술 논문 및 주석이 달린 출판물과 같은 문서의 스타일 일관성이 향상됩니다.

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 각주 커넥터의 사용자 지정 선 스타일 (색상, 너비 및 대시 패턴) 을 정의합니다.
1. 각주와 함께 여러 텍스트 조각을 추가합니다.
1. 최종 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

### PDF에 이미지 및 표가 있는 각주 추가

.NET을 통해 Python용 Aspose.PDF 를 사용하여 이미지, 스타일이 지정된 텍스트 및 표를 포함하여 PDF 문서의 각주를 풍부하게 만드는 방법은 무엇입니까?

1. 새 PDF 문서를 만들고 페이지를 추가합니다.
1. 각주가 첨부된 텍스트 조각을 추가합니다.
1. 각주 안에 이미지, 스타일이 적용된 텍스트, 표를 삽입합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

Endnote는 독자를 문서 끝에 있는 지정된 섹션으로 안내하는 인용 유형입니다. 이 섹션에서는 인용문, 의역된 아이디어 또는 요약된 내용에 대한 전체 참조를 찾을 수 있습니다.미주를 사용할 때는 참조 자료 바로 뒤에 위 첨자 번호를 붙여 논문 끝에 있는 해당 메모로 안내합니다.

이 코드 스니펫은 PDF 문서의 텍스트 부분에 미주를 추가하는 방법을 보여줍니다.참조된 텍스트 근처에 나타나는 각주와 달리 미주는 일반적으로 문서나 섹션의 끝에 위치합니다.또한 이 방법은 긴 문서를 시뮬레이션하여 확장 콘텐츠에서 미주가 어떻게 작동하는지 보여줍니다.

1. PDF 문서 및 페이지 작성
1. Endnote에 텍스트 조각을 추가하세요.
1. 외부 텍스트 내용을 로드합니다.
1. 긴 문서를 시뮬레이션하세요.로드된 텍스트를 여러 번 추가하여 더 긴 문서를 시뮬레이션할 수 있습니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### PDF에 사용자 지정 마커 텍스트가 있는 미주 추가

사용자 지정 마커 기호 (예: “***”) 를 사용하여 PDF 문서의 텍스트 부분에 미주를 추가합니다.미주는 일반적으로 문서 또는 섹션의 끝에 위치하며 추가 컨텍스트, 인용 또는 설명을 제공하는 데 유용합니다.

1. PDF 문서 및 페이지 작성
1. 스타일이 적용된 텍스트 부분을 미주에 추가하세요.
1. 엔드노트 마커 텍스트를 사용자 지정합니다.
1. .txt 파일에서 외부 콘텐츠를 로드합니다.
1. 긴 형식의 콘텐츠를 시뮬레이션하여 미주 배치를 설명합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## 레이아웃 및 페이지 제어

### 표를 PDF의 새 페이지에서 강제로 시작하도록 설정

.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 새 페이지에서 시작할 특정 콘텐츠를 추가합니다.
'is_in_new_page' 속성을 설정하면 페이지 레이아웃과 구조를 정밀하게 제어할 수 있어 특정 섹션 (예: 표, 보고서 또는 요약) 이 항상 새 페이지에서 시작되도록 할 수 있습니다. 이는 문서 서식 지정, 인쇄 가능한 보고서 또는 체계적인 출력 생성에 적합합니다.

1. 테이블 생성 및 구성
1. 테이블에 데이터를 추가합니다.
1. 테이블에 새 페이지를 강제 적용합니다.이렇게 하면 현재 페이지에 기존 콘텐츠가 있더라도 테이블이 새 페이지의 맨 위에서 시작되도록 할 수 있습니다.
1. 페이지에 테이블을 추가합니다.'page.clarphs.add () '를 사용하여 PDF 레이아웃에 테이블을 포함시키십시오.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

라이브러리에서는 'is_in_line_parph' 속성을 사용하여 PDF 내 텍스트와 이미지 간의 인라인 흐름을 제어할 수 있습니다.
일반적으로 새 요소 (예: 텍스트 조각이나 이미지) 를 추가하면 각 요소가 새 줄이나 새 단락에서 시작됩니다.
'is_in_line_paragraph = True'를 설정하면 요소가 같은 줄 또는 같은 단락 내에 나타나도록 하여 매끄러운 인라인 레이아웃을 만들 수 있습니다. 문장 내에 로고, 아이콘 또는 기호를 추가하는 것과 같이 텍스트와 이미지를 인라인으로 결합하는 데 적합합니다.

첫 번째 텍스트 부분, 이미지 및 두 번째 텍스트 부분이 같은 줄에 나타나며 연속적인 인라인 단락을 형성합니다.
세 번째 텍스트 단편은 새 단락을 시작하여 기본 줄 바꿈 동작을 보여줍니다.

1. 새 PDF 문서 만들기
1. 첫 번째 텍스트 조각을 추가합니다.
1. 인라인 이미지를 삽입합니다.
1. 인라인 텍스트를 더 추가하세요.
1. 새 단락을 추가합니다.
1. PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

### 여러 열로 구성된 PDF 만들기

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF로 여러 열로 구성된 신문 스타일의 레이아웃을 만들 수 있습니다.
FloatingBox 내에서 텍스트, HTML 서식 및 그래픽을 결합하는 방법을 보여 주므로 여러 열로 구성된 잡지 또는 뉴스레터 디자인과 유사한 고급 레이아웃 제어가 가능합니다.

1. PDF 문서를 초기화합니다.
1. 상단에 수평 구분선을 추가합니다.
1. 스타일이 지정된 HTML 제목을 추가합니다.
1. 레이아웃 제어를 위한 플로팅박스를 생성합니다.
1. 다중 열 레이아웃을 구성합니다.
1. 작성자 정보 추가.
1. 또 다른 내부 수평선을 그립니다.
1. 기사 텍스트를 추가합니다.
1. 최종 PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### PDF의 텍스트 정렬을 위한 사용자 지정 탭 중지

사용자 지정 탭 간격을 사용하여 테이블 구조에 의존하지 않고 PDF에서 표와 같은 텍스트 레이아웃을 만들 수 있습니다.
탭 정지 위치, 정렬 및 지시선 스타일을 정의하여 열 전체에 텍스트를 정확하게 정렬할 수 있습니다.이는 청구서, 보고서 또는 구조화된 텍스트 데이터에 유용합니다.

1. 새 PDF 문서 만들기
1. 사용자 지정 탭 정지를 정의합니다.
1. 텍스트에 #$TAB 플레이스홀더를 사용하세요.
1. PDF에 텍스트를 추가합니다.
1. PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
- [Python을 사용하여 PDF 내에서 텍스트 회전하기](/pdf/ko/python-net/rotate-text-inside-pdf/)
- [파이썬을 통해 PDF의 텍스트 바꾸기](/pdf/ko/python-net/replace-text-in-pdf/)