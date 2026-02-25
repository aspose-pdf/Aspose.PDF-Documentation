---
title: Python을 사용하여 PDF에 머리글 및 바닥글 추가
linktitle: PDF에 머리글 및 바닥글 추가
type: docs
weight: 50
url: /ko/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET은 TextStamp 클래스를 사용하여 PDF 파일에 머리글 및 바닥글을 추가할 수 있도록 합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 머리글 및 바닥글 추가하는 방법
Abstract: 이 문서는 **Aspose.PDF for Python via .NET**를 사용하여 PDF 파일에 머리글 및 바닥글을 추가하는 포괄적인 가이드를 제공하며, 텍스트 또는 이미지를 포함할 수 있습니다. 먼저 `TextStamp` 클래스를 사용하여 PDF 문서의 머리글에 텍스트를 삽입하는 방법을 자세히 설명합니다. 글꼴 크기, 스타일, 색상과 같은 주요 속성을 조정할 수 있으며, 머리글에 텍스트를 추가하는 방법은 Python 코드 조각으로 시연됩니다. 이 문서는 동일한 절차를 따라 바닥글에 텍스트를 추가하는 방법도 설명합니다. 이미지를 추가하기 위해서는 `ImageStamp` 클래스를 사용하며, 머리글과 바닥글 모두에 대한 과정이 Python 코드 예제로 지원됩니다. 또한, 하나의 PDF 파일에 여러 개의 머리글을 추가하는 방법에 대해 논의합니다. 여기에는 서로 다른 형식을 가진 여러 `TextStamp` 객체를 생성하고 이를 서로 다른 페이지에 적용하는 것이 포함됩니다. 설명은 이 기능을 보여주는 상세한 코드 조각으로 보완됩니다.
---

이 페이지는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 머리글 및 바닥글을 추가하는 간결한 개요를 제공하며, 텍스트, HTML, LaTeX, 이미지 및 표 기반 접근 방식과 동적 페이지 번호 매기기 및 페이지당 다중 머리글을 포함합니다; [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체를 생성하고 스타일링하는 방법([`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 등 사용)과, 정확한 배치를 위한 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 및 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 조정 방법을 설명하고, 실용적인 Python 코드 예제로 결과를 페이지에 첨부합니다.

**Aspose.PDF for Python via .NET**은 기존 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)에 머리글 및 바닥글을 추가할 수 있게 합니다. PDF 문서에 이미지나 텍스트를 추가할 수 있습니다. 또한 Python을 사용하여 하나의 PDF 파일에 다른 머리글을 추가해 보세요.

## 텍스트 조각으로 머리글 및 바닥글 추가

PDF의 모든 페이지에 간단한 텍스트 머리글 및 바닥글을 추가합니다. [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체를 생성하고, 그 안에 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 요소를 삽입하고, 적절한 위치 지정을 위해 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/)를 설정한 후, 문서의 각 페이지에 첨부합니다. 결과적으로 모든 페이지에 일관된 머리글 및 바닥글 텍스트가 표시되는 PDF가 생성됩니다.

다음 코드 조각은 Python을 사용하여 PDF에 텍스트 조각 형태의 머리글 및 바닥글을 추가하는 방법을 보여줍니다:

1. 머리글과 바닥글을 위한 텍스트 조각을 생성합니다.
1. HeaderFooter 객체를 생성하고 텍스트 조각을 추가합니다.
1. 머리글 및 바닥글 위치를 제어하기 위해 여백 설정을 정의합니다.
1. 입력 파일에서 PDF 문서를 로드합니다.
1. 문서의 모든 페이지를 순회합니다.
1. 각 페이지에 머리글과 바닥글을 할당합니다.
1. 수정된 PDF를 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

이 방법은 각 페이지 상단 및 하단에 일관된 제목, 페이지 표시기 또는 법적 고지를 추가할 때 유용합니다. 또한 이미지를 포함하거나 페이지 번호와 같은 동적 콘텐츠를 추가하도록 확장할 수 있습니다.

## 페이지 번호 매기를 위한 머리글 및 바닥글 추가

Aspose.PDF for Python을 사용하여 PDF 문서의 머리글 및 바닥글에 자동 페이지 번호 매기기를 추가합니다. 내장 변수 $p(현재 페이지 번호)와 $P(전체 페이지 수)를 사용하여 스크립트가 모든 페이지에 동적으로 페이지 번호를 삽입합니다. 머리글은 'Page X from Y' 형식으로 표시되고, 바닥글은 'Page X / Y' 형식으로 표시됩니다. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/)는 각 페이지에 적절한 배치를 보장합니다.

1. 현재 페이지와 전체 페이지를 표시하기 위해 "Page $p from $P"를 사용하여 머리글용 TextFragment를 생성합니다.
1. HeaderFooter 객체를 생성하고 머리글 텍스트를 추가합니다.
1. 대체 번호 매기기 스타일인 "Page $p / $P"를 사용하여 바닥글용 TextFragment를 생성합니다.
1. Footer 객체를 생성하고 바닥글 텍스트를 추가합니다.
1. 여백 설정(왼쪽 = 50, 위 = 20)을 정의하고 머리글과 바닥글 모두에 적용합니다.
1. 입력 파일에서 PDF 문서를 엽니다.
1. 모든 페이지를 순환하며 각 페이지에 머리글과 바닥글을 할당합니다.
1. 업데이트된 PDF를 출력 경로에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## HTML 조각으로 머리글 및 바닥글 추가

Aspose.PDF for Python을 사용하여 PDF 문서의 모든 페이지에 HTML 형식의 머리글 및 바닥글을 적용합니다. [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)을 사용함으로써 스크립트는 머리글과 바닥글에 굵게 및 기울임과 같은 풍부한 텍스트 스타일을 표시할 수 있게 합니다. 적절한 배치를 위해 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/)를 적용하고, 동일한 형식화된 요소들을 문서의 각 페이지에 첨부합니다.

다음 코드 조각은 Python을 사용하여 PDF에 HTML 조각 형태의 머리글 및 바닥글을 추가하는 방법을 보여줍니다:

1. HtmlFragment를 사용하여 HTML 머리글 조각을 생성합니다—예를 들어 굵게 표시를 위한 '<strong>'와 같은 스타일 텍스트를 포함합니다.
1. HeaderFooter 객체를 생성하고 HTML 머리글을 추가합니다.
1. '<i>'를 사용하여 이탤릭 스타일링을 적용한 HTML 바닥글 조각을 생성합니다.
1. Footer 객체를 생성하고 바닥글 HTML을 추가합니다.
1. 여백을 설정합니다(왼쪽 = 50, 위 = 20) 및 이를 머리글과 바닥글 모두에 할당합니다.
1. 'ap.Document()'를 사용하여 PDF 문서를 로드합니다.
1. 모든 페이지를 순환하며 각각에 머리글과 바닥글을 할당합니다.
1. 수정된 PDF를 지정된 출력 경로에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

HtmlFragment를 사용하면 인라인 스타일이나 HTML 마크업을 통한 풍부한 형식이 가능해져 일반 텍스트에 비해 디자인 유연성을 더 크게 제공합니다.

## 이미지를 사용한 머리글 및 바닥글 추가

Aspose.PDF for Python을 사용하여 PDF 문서의 각 페이지에 이미지 기반 머리글 및 바닥글을 추가합니다. 동일한 이미지 파일이 모든 페이지의 머리글과 바닥글에 사용됩니다. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/)는 이미지를 위치시키며, 이미지는 머리글/바닥글 영역에 맞게 자동으로 조정됩니다.

다음 코드 스니펫은 Python을 사용하여 PDF에 헤더와 푸터를 이미지로 추가하는 방법을 보여줍니다:

1. 이미지를 'ap.Image' 객체에 로드하고 헤더로 사용할 수 있도록 준비합니다.
1. HeaderFooter 객체를 생성하고 헤더 이미지를 연결합니다.
1. 같은 이미지를 다시 로드하여 푸터로 사용합니다.
1. Footer 객체를 생성하고 푸터 이미지를 추가합니다.
1. 'ap.Document()'를 사용하여 입력 PDF 문서를 로드합니다.
1. 문서의 모든 페이지를 반복합니다.
1. 여백을 적용하여(왼쪽 = 50) 헤더와 푸터를 배치합니다.
1. PDF의 각 페이지에 헤더와 푸터를 할당합니다.
1. 업데이트된 PDF를 지정된 출력 파일에 저장합니다.

이 기법은 헤더/푸터 영역에 로고나 워터마크를 넣어 문서에 브랜드를 부여하는 데 이상적입니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 헤더와 푸터를 테이블로 추가

Aspose.PDF for Python을 사용하여 PDF 문서의 모든 페이지에 구조화된 테이블 기반 헤더와 푸터를 추가합니다. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 객체는 복잡한 헤더와 푸터에 대해 더 나은 레이아웃 제어, 정렬 및 일관된 서식을 제공합니다. 헤더 텍스트는 가운데 정렬되고 푸터 텍스트는 왼쪽 정렬되며, 둘 다 Arial 12pt 글꼴을 사용합니다. 열 너비는 페이지 크기에 따라 동적으로 계산되어 적절한 배치를 보장합니다.

이 코드 스니펫은 Aspose.PDF for Python을 .NET을 통해 사용하여 PDF 문서의 각 페이지에 테이블을 사용한 헤더와 푸터를 추가합니다.

1. 헤더와 푸터에 대해 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 를 사용하여 텍스트 스타일(글꼴, 크기, 정렬)을 정의합니다.
1. 헤더와 푸터용 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체를 생성합니다.
1. 단일 행과 헤더 텍스트를 포함하는 셀을 가진 헤더 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 을 구성합니다.
1. 단일 행과 푸터 텍스트를 포함하는 셀을 가진 푸터 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 을 구성합니다.
1. 해당하는 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체에 테이블을 추가합니다.
1. 적절한 수평 위치 지정을 위해 푸터 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 를 설정합니다.
1. 적절한 방법을 사용하여 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 을 엽니다.
1. 모든 페이지를 반복하고 테이블 기반 헤더와 푸터를 각 페이지에 할당합니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 을 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 헤더와 푸터를 LaTeX로 추가

Aspose.PDF for Python을 사용하여 PDF 문서의 모든 페이지에 LaTeX 형식 콘텐츠를 포함한 헤더와 푸터를 추가합니다. LaTeX는 수학 기호, 날짜, 저작권 표시 및 기타 고급 서식을 렌더링할 수 있습니다. 헤더에는 동적 날짜가 포함되고, 푸터에는 현재 페이지 번호와 전체 페이지 수와 함께 저작권 기호가 표시됩니다.

다음 코드 스니펫은 Aspose.PDF for Python을 .NET을 통해 사용하여 PDF의 헤더와 푸터에 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 를 사용하는 방법을 보여줍니다.

1. 적절한 방법을 사용하여 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 을 엽니다.
1. 동적 푸터에 사용할 전체 페이지 수를 결정합니다.
1. 문서의 모든 페이지를 반복합니다.
1. 헤더용 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체를 생성합니다.
1. LaTeX 명령(예: `\\today\\`)을 포함한 헤더 텍스트용 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 을 생성합니다.
1. 푸터용 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 객체를 생성합니다.
1. LaTeX 기호와 페이지 번호를 포함한 푸터 텍스트용 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 을 생성합니다.
1. 해당 헤더/푸터 객체에 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 을 추가합니다.
1. 현재 페이지에 헤더와 푸터를 바인딩합니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 을 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
