---
title: 파이썬에서 PDF 머리말과 꼬리말 추가하기
linktitle: PDF에 머리말 및 꼬리말 추가
type: docs
weight: 50
url: /ko/python-net/add-headers-and-footers-of-pdf-file/
description: 텍스트, 이미지 및 구조화된 콘텐츠를 사용하여 Python에서 PDF 파일에 머리말과 꼬리말을 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 머리말과 꼬리말 추가
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 머리말과 꼬리말을 추가하는 방법을 보여줍니다.텍스트, 페이지 번호 지정, HTML, 이미지, 표, LaTex 기반 머리글 및 바닥글 내용을 다룹니다.
---

이 페이지에서는**Python용 Aspose.pdf를.NET**로 PDF 페이지 전체에 일관된 머리말과 꼬리말 내용을 추가할 수 있습니다.

머리말과 꼬리말은 다음과 같이 작성할 수 있습니다. [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), 및 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 오브젝트를 통해 적용 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 각 페이지에.

## 머리말과 꼬리말을 텍스트 조각으로 추가

PDF의 모든 페이지에 간단한 텍스트 머리말과 꼬리말을 추가합니다.그러면 생성됩니다. [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 오브젝트, 인서트 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 요소, 세트 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 올바른 위치를 지정하기 위해 문서의 각 페이지에 첨부합니다.그 결과 모든 페이지에 일관된 머리말과 꼬리말 텍스트가 표시되는 PDF가 만들어집니다.

다음 코드 스니펫은 Python을 사용하여 PDF에서 머리말과 꼬리말을 텍스트 조각으로 추가하는 방법을 보여줍니다.

1. 머리말과 꼬리말에 사용할 텍스트 조각을 만듭니다.
1. HeaderFooter 객체를 만들고 여기에 텍스트 조각을 추가합니다.
1. 머리말과 꼬리말의 배치를 제어하는 여백 설정을 정의합니다.
1. 입력 파일에서 PDF 문서를 로드합니다.
1. 문서의 모든 페이지를 반복합니다.
1. 각 페이지에 머리말과 꼬리말을 지정합니다.
1. 수정한 PDF를 출력 파일에 저장합니다.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
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

이 방법은 각 페이지의 상단과 하단에 일관된 제목, 페이지 표시기 또는 법적 고지 사항을 추가하는 데 유용합니다.이미지 또는 페이지 번호와 같은 동적 콘텐츠를 포함하도록 확장할 수도 있습니다.

## 페이지 번호 지정을 위한 머리말과 꼬리말 추가

Python용 Aspose.PDF 를 사용하여 PDF 문서의 머리글과 바닥글에 자동 페이지 번호 매기기를 추가합니다.스크립트는 내장 변수 $p (현재 페이지 번호) 및 $P (총 페이지 수) 를 사용하여 모든 페이지에 페이지 번호를 동적으로 삽입합니다.머리글에는 'Page X from Y' 형식이 표시되고 바닥글에는 'Page X/ Y' 형식이 표시됩니다. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 각 페이지에 적절한 배치를 보장합니다.

1. “$P from $P 페이지”를 사용하여 헤더의 텍스트 조각을 만들어 현재 페이지와 전체 페이지를 표시합니다.
1. HeaderFooter 객체를 만들고 여기에 머리글 텍스트를 추가합니다.
1. 대체 번호 매기기 스타일로 “페이지 $p/ $P”를 사용하여 바닥글에 사용할 텍스트 조각을 만드세요.
1. Footer 객체를 만들고 바닥글 텍스트를 추가합니다.
1. 여백 설정 (왼쪽 = 50, 상단 = 20) 을 정의하고 머리말과 꼬리말 모두에 적용합니다.
1. 입력 파일에서 PDF 문서를 엽니다.
1. 모든 페이지를 반복하고 각 페이지에 머리말과 꼬리말을 할당합니다.
1. 업데이트된 PDF를 출력 경로에 저장합니다.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
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

## 머리말과 꼬리말을 HTML 조각으로 추가

파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 모든 페이지에 HTML 형식의 머리말과 꼬리말을 적용합니다.를 사용하여 [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), 스크립트를 사용하면 굵게 및 기울임꼴과 같은 리치 텍스트 스타일을 머리말과 꼬리말에 표시할 수 있습니다. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 적절한 배치를 위해 적용되며 문서의 각 페이지에는 동일한 형식의 요소가 첨부됩니다.

다음 코드 스니펫은 Python을 사용하여 PDF에 머리글과 바닥글을 HTML 조각으로 추가하는 방법을 보여줍니다.

1. HTMLFragment를 사용하여 HTML 헤더 스니펫 만들기 (예: ') 스타일이 적용된 텍스트 포함<strong>'는 굵게 표시한다는 뜻입니다.
1. HeaderFooter 객체를 만들고 여기에 HTML 헤더를 추가합니다.
1. '를 사용하여 HTML 바닥글 스니펫 만들기<i>'(기울임꼴 스타일링의 경우).
1. Footer 객체를 만들고 여기에 바닥글 HTML을 추가합니다.
1. 여백을 설정하고 (왼쪽 = 50, 위쪽 = 20) 머리말과 꼬리말에 모두 할당합니다.
1. 'AP.Document () '를 사용하여 PDF 문서를 로드합니다.
1. 모든 페이지를 반복하고 각 페이지에 머리말과 꼬리말을 할당합니다.
1. 수정한 PDF를 지정된 출력 경로에 저장합니다.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
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

HTMLFragment를 사용하면 인라인 스타일 또는 HTML 마크업으로 풍부한 서식을 지정할 수 있으므로 일반 텍스트에 비해 디자인 유연성이 향상됩니다.

## 머리말과 꼬리말을 이미지로 추가

Python용 Aspose.PDF 를 사용하여 PDF 문서의 각 페이지에 이미지 기반 머리글과 바닥글을 추가합니다.모든 페이지의 머리말과 꼬리말 모두에 동일한 이미지 파일이 사용됩니다. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 이미지의 위치를 지정하면 이미지가 머리말/꼬리말 영역에 맞게 자동으로 조정됩니다.

다음 코드 스니펫은 Python을 사용하여 PDF에 머리말과 꼬리말을 이미지로 추가하는 방법을 보여줍니다.

1. 이미지를 'ap.Image' 객체에 로드하고 헤더로 사용할 준비를 합니다.
1. HeaderFooter 객체를 만들고 여기에 헤더 이미지를 첨부합니다.
1. 동일한 이미지를 다시 로드하여 바닥글로 사용합니다.
1. Footer 객체를 만들고 여기에 Footer 이미지를 추가합니다.
1. 'AP.Document () '를 사용하여 입력된 PDF 문서를 로드합니다.
1. 문서의 모든 페이지를 반복합니다.
1. 머리말과 꼬리말을 모두 배치하려면 여백 (왼쪽 = 50) 을 적용합니다.
1. PDF의 각 페이지에 머리말과 꼬리말을 지정합니다.
1. 업데이트된 PDF를 지정된 출력 파일에 저장합니다.

이 기법은 머리말/꼬리말 영역에 로고나 워터마크가 있는 문서를 브랜딩하는 데 적합합니다.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
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

## 머리말과 꼬리말을 표로 추가

Python용 Aspose.PDF 를 사용하여 PDF 문서의 모든 페이지에 구조화된 표 기반 머리말과 꼬리말을 추가할 수 있습니다. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 개체는 복잡한 머리말과 꼬리말에 대해 더 나은 레이아웃 제어, 정렬 및 일관된 서식을 제공합니다.Arial 12pt 글꼴을 사용하여 머리글 텍스트는 가운데에, 바닥글 텍스트는 왼쪽으로 정렬됩니다.열 너비는 적절한 배치를 위해 페이지 크기를 기반으로 동적으로 계산됩니다.

이 코드 스니펫은.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 각 페이지에 머리글과 바닥글 (표 사용) 을 추가합니다.

1. 를 사용하여 텍스트 스타일 정의 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 머리글 및 바닥글 (글꼴, 크기, 정렬) 용
1. 작성 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 머리글 및 바닥글에 대한 개체
1. 헤더 작성 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 단일 행과 헤더 텍스트를 포함하는 셀이 있습니다.
1. 바닥글 만들기 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 단일 행과 바닥글 텍스트를 포함하는 셀이 있습니다.
1. 해당 테이블에 테이블 추가 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 사물.
1. 바닥글 설정 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 적절한 수평 위치 지정을 위해.
1. 를 여십시오 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 적절한 방법을 사용합니다.
1. 모든 페이지를 반복하고 각 페이지에 표 기반 머리말과 꼬리말을 할당합니다.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 출력 파일에.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
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

## 머리말과 꼬리말을 LaTeX로 추가

Python용 Aspose.PDF 를 사용하여 라텍스 형식의 내용이 포함된 머리말과 꼬리말을 PDF 문서의 모든 페이지에 추가합니다.LaTeX를 사용하면 수학 기호, 날짜, 저작권 표시 및 기타 고급 서식을 렌더링할 수 있습니다.머리글에는 동적 날짜가 포함되고 바닥글에는 현재 페이지 번호 및 총 페이지 수와 함께 저작권 기호가 표시됩니다.

다음 코드 스니펫은 사용 방법을 보여줍니다. [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) .NET을 통해 파이썬용 Aspose.PDF 를 사용하는 PDF의 머리말과 꼬리말에.

1. 를 여십시오 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 적절한 방법을 사용합니다.
1. 동적 바닥글에 사용할 총 페이지 수를 결정합니다.
1. 문서의 모든 페이지를 반복합니다.
1. 만들기 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 헤더의 객체입니다.
1. 만들기 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) LaTeX 명령을 포함하는 헤더 텍스트의 경우 (예: `\\today\\`).
1. 만들기 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 바닥글의 객체.
1. 만들기 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) LaTeX 기호 및 페이지 번호 매기기를 포함한 바닥글 텍스트에 사용됩니다.
1. 추가 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 해당 머리말/꼬리말 개체에.
1. 머리말과 꼬리말을 현재 페이지에 바인딩합니다.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 출력 파일에.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF에 페이지 번호 추가](/pdf/ko/python-net/add-page-number/)
- [파이썬으로 PDF 페이지에 스탬프 찍기](/pdf/ko/python-net/stamping/)
- [파이썬으로 PDF 문서 포맷 지정하기](/pdf/ko/python-net/formatting-pdf-document/)